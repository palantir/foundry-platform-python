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


from __future__ import annotations

from typing import Any
from typing import Dict
from typing import Optional

import pydantic
from typing_extensions import Annotated

from foundry._core import ApiClient
from foundry._core import Auth
from foundry._core import RequestInfo
from foundry._errors import handle_unexpected
from foundry.v2.core.models._preview_mode import PreviewMode
from foundry.v2.functions.models._value_type import ValueType
from foundry.v2.functions.models._value_type_rid import ValueTypeRid
from foundry.v2.functions.version_id import VersionIdClient


class ValueTypeClient:
    def __init__(self, auth: Auth, hostname: str) -> None:
        self._api_client = ApiClient(auth=auth, hostname=hostname)

        self.VersionId = VersionIdClient(auth=auth, hostname=hostname)

    @pydantic.validate_call
    @handle_unexpected
    def get(
        self,
        value_type_rid: ValueTypeRid,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ValueType:
        """
        Gets a specific value type with the given RID. The latest version is returned.

        :param value_type_rid: valueTypeRid
        :type value_type_rid: ValueTypeRid
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ValueType
        """

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/functions/valueTypes/{valueTypeRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "valueTypeRid": value_type_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ValueType,
                request_timeout=request_timeout,
            ),
        )
