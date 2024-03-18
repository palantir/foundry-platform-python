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


import datetime
import json
import os
import re
import sys
import tempfile
from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import Tuple
from typing import TypeVar

from pydantic import BaseModel
from pydantic import TypeAdapter

from foundry._core.auth_utils import Auth
from foundry._core.palantir_session import PalantirSession
from foundry._versions import __version__
from foundry._errors.palantir_rpc_exception import PalantirRPCException
from foundry._errors.sdk_internal_error import SDKInternalError


class ApiClient:
    def __init__(self, auth: Auth, hostname: str):
        self.session = PalantirSession(auth=auth, hostname=hostname)

        self.default_headers = {
            "User-Agent": f"python-foundry-platform-sdk/{__version__} python/{sys.version_info.major}.{sys.version_info.minor}",
        }

    def call_api(
        self,
        method,
        resource_path,
        response_types_map: Dict[int, Any],
        query_params,
        header_params,
        body,
        request_timeout: Optional[int] = None,
    ) -> Any:
        """Makes the HTTP request (synchronous)
        :param method: Method to call.
        :param resource_path: Path to method endpoint.
        :param query_params: Query parameters in the url.
        :param header_params: Header parameters to be
            placed in the request header.
        :param body: Request body.
        """
        # header parameters
        headers = header_params or {}
        headers.update(self.default_headers)

        url = f"https://{self.session.hostname}/api{resource_path}"

        res = self.session.request(
            method=method,
            url=url,
            headers=headers,
            params=self._process_query_parameters(query_params),
            json=body,
            stream=False,
            timeout=request_timeout,
        )

        response_type = response_types_map.get(res.status_code, None)

        if not 200 <= res.status_code <= 299:
            try:
                raise PalantirRPCException(res.json())
            except json.JSONDecodeError:
                raise SDKInternalError("Unable to decode JSON error response: " + res.text)

        if response_type is bytes:
            return_data = res.content
        elif response_type is None:
            return_data = None
        else:
            match = None
            content_type = res.headers.get("content-type")
            if content_type is not None:
                match = re.search(r"charset=([a-zA-Z\-\d]+)[\s;]?", content_type)
            encoding = match.group(1) if match else "utf-8"

            response_text = res.content.decode(encoding)
            return_data = self._deserialize(response_text, response_type)

        return return_data

    def _process_query_parameters(self, query_params: Dict[str, Any]):
        result: List[Tuple[str, Any]] = []

        for key, value in query_params.items():
            if not isinstance(value, list):
                result.append((key, value))
                continue

            # Explode list query parameters
            for inner_value in value:
                result.append((key, inner_value))

        return result

    def _deserialize(self, response_text, response_type):
        # fetch data from response object
        try:
            data = json.loads(response_text)
        except ValueError:
            data = response_text

        if response_type is object:
            return data

        if hasattr(response_type, "from_dict"):
            return response_type.from_dict(data, allow_extra=True)

        if not hasattr(response_type, "type_adapter"):
            # Create an instance of a type adapter. This has a non-trivial overhead according
            # to the documentation so we do this once the first time we encounter this type
            object.__setattr__(response_type, "type_adapter", TypeAdapter(response_type))

        return response_type.type_adapter.validate_python(data)
