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
from typing import cast
from urllib.parse import quote

import pydantic
import requests
import requests.adapters
from typing_extensions import deprecated

from foundry._core.auth_utils import Auth
from foundry._core.binary_stream import BinaryStream
from foundry._core.config import Config
from foundry._core.resource_iterator import ResourceIterator
from foundry._core.utils import remove_prefixes
from foundry._errors.palantir_rpc_exception import PalantirRPCException
from foundry._errors.sdk_internal_error import SDKInternalError
from foundry._versions import __version__

_GLOBAL_ADAPTER = requests.adapters.HTTPAdapter()


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
    stream: bool = False
    chunk_size: Optional[int] = None

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
            stream=self.stream,
        )

    @classmethod
    def with_defaults(
        cls,
        method: str,
        resource_path: str,
        response_type: Any = None,
        query_params: QueryParameters = {},
        path_params: Dict[str, Any] = {},
        header_params: Dict[str, Any] = {},
        body: Any = None,
        body_type: Any = None,
        request_timeout: Optional[int] = None,
        stream: bool = False,
        chunk_size: Optional[int] = None,
    ):
        return cls(
            method=method,
            resource_path=resource_path,
            response_type=response_type,
            query_params=query_params,
            path_params=path_params,
            header_params=header_params,
            body=body,
            body_type=body_type,
            request_timeout=request_timeout,
            stream=stream,
            chunk_size=chunk_size,
        )


class _BaseModelTypeAdapter:
    def __init__(self, _type: Type[pydantic.BaseModel]) -> None:
        self._type = _type

    def validate_python(self, data: Any):
        return self._type.model_validate(data)

    def dump_json(self, data: Any, **kwargs: Dict[str, Any]):
        # .encode() to match the behaviour of pydantic.TypeAdapter.dump_json which returns bytes.
        return self._type.model_dump_json(data, **kwargs).encode()  # type: ignore


class ApiClient:
    """
    The API client.

    :param auth: Your auth configuration.
    :param hostname: Your Foundry hostname (for example, "myfoundry.palantirfoundry.com").
    :param config: Optionally specify the configuration for the HTTP session.
    """

    def __init__(
        self,
        auth: Auth,
        hostname: str,
        config: Optional[Config] = None,
    ):
        self._config = config = config or Config()
        self._auth = auth
        self._hostname = remove_prefixes(hostname, ["https://", "http://"])

        self._session = requests.Session()
        self._session.mount("http://", _GLOBAL_ADAPTER)
        self._session.mount("https://", _GLOBAL_ADAPTER)

        self._session.headers["User-Agent"] = (
            f"python-foundry-platform-sdk/{__version__} python/{sys.version_info.major}.{sys.version_info.minor}"
        )
        if config.default_headers:
            self._session.headers.update(config.default_headers)

        if config.proxies:
            # Need to cast here since Dict[Literal[...], str] is not assignable to to Dict[str, str]
            self._session.proxies.update(cast(Dict[str, str], config.proxies))

        self._session.verify = config.verify

        if config.default_params:
            self._session.params.update(config.default_params)  # type: ignore

    @property
    @deprecated(
        "Accessing the session directly is deprecated. Please configure the session using the new Config class."
    )
    def session(self):
        # DEPRECATED: This ensures that users who were previously accessing the PalantirSession
        # will have code that continues to work (now we just return the ApiClient)
        return self

    @property
    def hostname(self) -> str:
        return self._hostname

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
        res = self._session.request(
            method=request_info.method,
            url=self._create_url(request_info),
            params=self._process_query_parameters(request_info.query_params),
            data=self._serialize(request_info.body, request_info.body_type),
            headers={
                "Authorization": "Bearer " + self._auth.get_token().access_token,
                **request_info.header_params,
            },
            stream=request_info.stream,
            timeout=(
                request_info.request_timeout
                if request_info.request_timeout is not None
                else self._config.timeout
            ),
        )

        if res.status_code == 401:
            res.raise_for_status()

        if not 200 <= res.status_code <= 299:
            try:
                raise PalantirRPCException(res.json())
            except json.JSONDecodeError:
                raise SDKInternalError("Unable to decode JSON error response: " + res.text)

        return self._deserialize(res, request_info)

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

    def _create_url(self, request_info: RequestInfo) -> str:
        resource_path = request_info.resource_path
        path_params = request_info.path_params

        for k, v in path_params.items():
            # the "safe" option defaults to "/"
            # this does not work with the backend which expects "/" characters to be encoded
            resource_path = resource_path.replace(f"{{{k}}}", quote(v, safe=""))

        return f"{self._config.scheme}://{self._hostname}/api{resource_path}"

    def _serialize(self, value: Any, value_type: Any) -> Optional[bytes]:
        """
        Serialize the data passed in to JSON bytes.
        """
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

    def _deserialize(self, res: requests.Response, request_info: RequestInfo) -> Any:
        if request_info.response_type is bytes:
            if request_info.stream:
                return BinaryStream(res.iter_content(chunk_size=request_info.chunk_size))
            else:
                return res.content
        elif request_info.response_type is None:
            return None

        content_type = res.headers.get("content-type")
        if content_type is not None:
            match = re.search(r"charset=([a-zA-Z\-\d]+)[\s;]?", content_type)
        else:
            match = None

        encoding = match.group(1) if match else "utf-8"
        response_text = res.content.decode(encoding)

        data = json.loads(response_text)

        if request_info.response_type is Any:
            return data

        type_adapter = self._get_type_adapter(request_info.response_type)
        return type_adapter.validate_python(data)

    @staticmethod
    def _get_type_adapter(_type: Any):
        if _type not in _TYPE_ADAPTERS:
            if isclass(_type) and issubclass(_type, pydantic.BaseModel):
                _TYPE_ADAPTERS[_type] = _BaseModelTypeAdapter(_type)  # type: ignore
            else:
                # Create an instance of a type adapter. This has a non-trivial overhead according
                # to the documentation so we do this once the first time we encounter this type
                _TYPE_ADAPTERS[_type] = pydantic.TypeAdapter(_type)

        return _TYPE_ADAPTERS[_type]
