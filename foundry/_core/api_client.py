#  Copyright 2024 Palantir Technologies, Inc.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.


import json
import re
import sys
from dataclasses import dataclass
from inspect import isclass
from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import Tuple
from typing import Type
from typing import Union
from urllib.parse import quote

from pydantic import BaseModel
from pydantic import TypeAdapter
from requests import Response

from foundry._core.auth_utils import Auth
from foundry._core.palantir_session import PalantirSession
from foundry._core.resource_iterator import ResourceIterator
from foundry._errors.palantir_rpc_exception import PalantirRPCException
from foundry._errors.sdk_internal_error import SDKInternalError
from foundry._versions import __version__

QueryParameters = Dict[str, Union[Any, List[Any]]]


_TYPE_ADAPTERS: Dict[Any, Any] = {}


@dataclass(frozen=True)
class RequestInfo:
    method: str
    resource_path: str
    response_type: Any
    query_params: QueryParameters
    path_params: Dict[str, Any]
    header_params: Dict[str, Any]
    body: Any
    body_type: Any
    request_timeout: Optional[int]

    def update(
        self,
        query_params: Optional[Dict[str, Any]] = None,
        header_params: Optional[Dict[str, Any]] = None,
    ):
        return RequestInfo(
            method=self.method,
            resource_path=self.resource_path,
            response_type=self.response_type,
            query_params={**self.query_params, **(query_params or {})},
            path_params=self.path_params,
            header_params={**self.header_params, **(header_params or {})},
            body=self.body,
            body_type=self.body_type,
            request_timeout=self.request_timeout,
        )


class _BaseModelTypeAdapter:
    def __init__(self, _type: Type[BaseModel]) -> None:
        self._type = _type

    def validate_python(self, data: Any):
        return self._type.model_validate(data)

    def dump_json(self, data: Any, **kwargs: Dict[str, Any]):
        # .encode() to match the behaviour of TypeAdapter.dump_json which returns bytes.
        return self._type.model_dump_json(data, **kwargs).encode()  # type: ignore


class ApiClient:
    def __init__(self, auth: Auth, hostname: str):
        self.session = PalantirSession(auth=auth, hostname=hostname)

        self.default_headers = {
            "User-Agent": f"python-foundry-platform-sdk/{__version__} python/{sys.version_info.major}.{sys.version_info.minor}",
        }

    def iterate_api(self, request_info: RequestInfo) -> ResourceIterator[Any]:
        def fetch_page(
            page_size: Optional[int],
            next_page_token: Optional[str],
        ) -> Tuple[Optional[str], List[Any]]:
            result = self.call_api(
                request_info.update(
                    # pageSize will already be present in the query params dictionary
                    query_params={"pageToken": next_page_token},
                ),
            )

            return result.next_page_token, result.data or []

        return ResourceIterator(paged_func=fetch_page)

    def call_api(self, request_info: RequestInfo) -> Any:
        """Makes the HTTP request (synchronous)"""
        headers = request_info.header_params or {}
        headers.update(self.default_headers)

        # The body could be a pydantic model
        # We need to serialize these to dictionaries to be passed to the
        # the API endpoint
        body = self._serialize(request_info.body, request_info.body_type)
        path = self._create_path(request_info)

        url = f"https://{self.session.hostname}/api{path}"

        res = self.session.request(
            method=request_info.method,
            url=url,
            headers=headers,
            params=self._process_query_parameters(request_info.query_params),
            data=body,
            stream=False,
            timeout=request_info.request_timeout,
        )

        if not 200 <= res.status_code <= 299:
            try:
                raise PalantirRPCException(res.json())
            except json.JSONDecodeError:
                raise SDKInternalError("Unable to decode JSON error response: " + res.text)

        return self._deserialize(res, request_info.response_type)

    def _process_query_parameters(self, query_params: QueryParameters):
        result: List[Tuple[str, Any]] = []

        for key, value in query_params.items():
            if not isinstance(value, list):
                result.append((key, value))
                continue

            # Explode list query parameters
            for inner_value in value:
                result.append((key, inner_value))

        return result

    def _create_path(self, request_info: RequestInfo) -> str:
        resource_path = request_info.resource_path
        path_params = request_info.path_params

        for k, v in path_params.items():
            # the "safe" option defaults to "/"
            # this does not work with the backend which expects "/" characters to be encoded
            resource_path = resource_path.replace(f"{{{k}}}", quote(v, safe=""))

        return resource_path

    def _serialize(self, value: Any, value_type: Any) -> Optional[bytes]:
        if value_type is bytes:
            return value
        elif value_type is None:
            return None

        json_bytes: bytes
        if value_type is Any:
            json_bytes = json.dumps(value).encode()
        else:
            type_adapter = self._get_type_adapter(value_type)

            # Use "exclude_unset" to remove optional inputs that weren't explicitely set
            # Use "by_alias" to use the expected field name rather than the class property name
            json_bytes = type_adapter.dump_json(value, exclude_unset=True, by_alias=True)

        return json_bytes

    def _deserialize(self, res: Response, response_type: Any) -> Any:
        if response_type is bytes:
            return res.content
        elif response_type is None:
            return None

        content_type = res.headers.get("content-type")
        if content_type is not None:
            match = re.search(r"charset=([a-zA-Z\-\d]+)[\s;]?", content_type)
        else:
            match = None

        encoding = match.group(1) if match else "utf-8"
        response_text = res.content.decode(encoding)

        data = json.loads(response_text)

        if response_type is Any:
            return data

        type_adapter = self._get_type_adapter(response_type)
        return type_adapter.validate_python(data)

    @staticmethod
    def _get_type_adapter(_type: Any):
        if _type not in _TYPE_ADAPTERS:
            if isclass(_type) and issubclass(_type, BaseModel):
                _TYPE_ADAPTERS[_type] = _BaseModelTypeAdapter(_type)  # type: ignore
            else:
                # Create an instance of a type adapter. This has a non-trivial overhead according
                # to the documentation so we do this once the first time we encounter this type
                _TYPE_ADAPTERS[_type] = TypeAdapter(_type)

        return _TYPE_ADAPTERS[_type]
