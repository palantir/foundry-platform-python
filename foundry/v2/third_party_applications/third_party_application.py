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

from pydantic import Field
from pydantic import StrictInt
from pydantic import validate_call
from typing_extensions import Annotated

from foundry._core import ApiClient
from foundry._core import Auth
from foundry._core import RequestInfo
from foundry._errors import handle_unexpected
from foundry.v2.core.models._preview_mode import PreviewMode
from foundry.v2.third_party_applications.models._third_party_application import (
    ThirdPartyApplication,
)  # NOQA
from foundry.v2.third_party_applications.models._third_party_application_rid import (
    ThirdPartyApplicationRid,
)  # NOQA
from foundry.v2.third_party_applications.website import WebsiteClient


class ThirdPartyApplicationClient:
    def __init__(self, auth: Auth, hostname: str) -> None:
        self._api_client = ApiClient(auth=auth, hostname=hostname)

        self.Website = WebsiteClient(auth=auth, hostname=hostname)

    @validate_call
    @handle_unexpected
    def get(
        self,
        third_party_application_rid: ThirdPartyApplicationRid,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> ThirdPartyApplication:
        """
        Get the ThirdPartyApplication with the specified rid.
        :param third_party_application_rid: thirdPartyApplicationRid
        :type third_party_application_rid: ThirdPartyApplicationRid
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ThirdPartyApplication
        """

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/thirdPartyApplications/{thirdPartyApplicationRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "thirdPartyApplicationRid": third_party_application_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ThirdPartyApplication,
                request_timeout=request_timeout,
            ),
        )
