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
from typing_extensions import TypedDict

from foundry._core import ApiClient
from foundry._core import Auth
from foundry._core import RequestInfo
from foundry._errors import handle_unexpected
from foundry.v2.core.models._preview_mode import PreviewMode
from foundry.v2.datasets.models._branch_name import BranchName
from foundry.v2.orchestration.models._abort_on_failure import AbortOnFailure
from foundry.v2.orchestration.models._build import Build
from foundry.v2.orchestration.models._build_rid import BuildRid
from foundry.v2.orchestration.models._build_target_dict import BuildTargetDict
from foundry.v2.orchestration.models._fallback_branches import FallbackBranches
from foundry.v2.orchestration.models._force_build import ForceBuild
from foundry.v2.orchestration.models._notifications_enabled import NotificationsEnabled
from foundry.v2.orchestration.models._retry_backoff_duration_dict import (
    RetryBackoffDurationDict,
)  # NOQA
from foundry.v2.orchestration.models._retry_count import RetryCount


class BuildClient:
    def __init__(self, auth: Auth, hostname: str) -> None:
        self._api_client = ApiClient(auth=auth, hostname=hostname)

    @validate_call
    @handle_unexpected
    def create(
        self,
        *,
        fallback_branches: FallbackBranches,
        target: BuildTargetDict,
        abort_on_failure: Optional[AbortOnFailure] = None,
        branch_name: Optional[BranchName] = None,
        force_build: Optional[ForceBuild] = None,
        notifications_enabled: Optional[NotificationsEnabled] = None,
        preview: Optional[PreviewMode] = None,
        retry_backoff_duration: Optional[RetryBackoffDurationDict] = None,
        retry_count: Optional[RetryCount] = None,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> Build:
        """

        :param fallback_branches:
        :type fallback_branches: FallbackBranches
        :param target: The targets of the schedule.
        :type target: BuildTargetDict
        :param abort_on_failure:
        :type abort_on_failure: Optional[AbortOnFailure]
        :param branch_name: The target branch the build should run on.
        :type branch_name: Optional[BranchName]
        :param force_build:
        :type force_build: Optional[ForceBuild]
        :param notifications_enabled:
        :type notifications_enabled: Optional[NotificationsEnabled]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param retry_backoff_duration:
        :type retry_backoff_duration: Optional[RetryBackoffDurationDict]
        :param retry_count: The number of retry attempts for failed jobs.
        :type retry_count: Optional[RetryCount]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: Build
        """

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/orchestration/builds/create",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "target": target,
                    "branchName": branch_name,
                    "fallbackBranches": fallback_branches,
                    "forceBuild": force_build,
                    "retryCount": retry_count,
                    "retryBackoffDuration": retry_backoff_duration,
                    "abortOnFailure": abort_on_failure,
                    "notificationsEnabled": notifications_enabled,
                },
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "target": BuildTargetDict,
                        "branchName": Optional[BranchName],
                        "fallbackBranches": FallbackBranches,
                        "forceBuild": Optional[ForceBuild],
                        "retryCount": Optional[RetryCount],
                        "retryBackoffDuration": Optional[RetryBackoffDurationDict],
                        "abortOnFailure": Optional[AbortOnFailure],
                        "notificationsEnabled": Optional[NotificationsEnabled],
                    },
                ),
                response_type=Build,
                request_timeout=request_timeout,
            ),
        )

    @validate_call
    @handle_unexpected
    def get(
        self,
        build_rid: BuildRid,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> Build:
        """
        Get the Build with the specified rid.
        :param build_rid: buildRid
        :type build_rid: BuildRid
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: Build
        """

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/orchestration/builds/{buildRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "buildRid": build_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=Build,
                request_timeout=request_timeout,
            ),
        )
