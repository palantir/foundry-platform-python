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
from foundry.v2.admin.host import HostClient
from foundry.v2.admin.models._enrollment import Enrollment
from foundry.v2.core.models._enrollment_rid import EnrollmentRid
from foundry.v2.core.models._preview_mode import PreviewMode


class EnrollmentClient:
    def __init__(self, auth: Auth, hostname: str) -> None:
        self._api_client = ApiClient(auth=auth, hostname=hostname)

        self.Host = HostClient(auth=auth, hostname=hostname)

    @pydantic.validate_call
    @handle_unexpected
    def get(
        self,
        enrollment_rid: EnrollmentRid,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> Enrollment:
        """
        Get the Enrollment with the specified rid.
        :param enrollment_rid: enrollmentRid
        :type enrollment_rid: EnrollmentRid
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: Enrollment
        """

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/admin/enrollments/{enrollmentRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "enrollmentRid": enrollment_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=Enrollment,
                request_timeout=request_timeout,
            ),
        )

    @pydantic.validate_call
    @handle_unexpected
    def get_current(
        self,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> Enrollment:
        """
        Returns the Enrollment associated with the current User's primary organization.

        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: Enrollment
        """

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/admin/enrollments/getCurrent",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=Enrollment,
                request_timeout=request_timeout,
            ),
        )
