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

from typing_extensions import NotRequired
from typing_extensions import TypedDict

from foundry.v2.datasets.models._branch_name import BranchName
from foundry.v2.orchestration.models._abort_on_failure import AbortOnFailure
from foundry.v2.orchestration.models._fallback_branches import FallbackBranches
from foundry.v2.orchestration.models._force_build import ForceBuild
from foundry.v2.orchestration.models._notifications_enabled import NotificationsEnabled
from foundry.v2.orchestration.models._replace_schedule_request_action_build_target_dict import (
    ReplaceScheduleRequestActionBuildTargetDict,
)  # NOQA
from foundry.v2.orchestration.models._retry_backoff_duration_dict import (
    RetryBackoffDurationDict,
)  # NOQA
from foundry.v2.orchestration.models._retry_count import RetryCount


class ReplaceScheduleRequestActionDict(TypedDict):
    """ReplaceScheduleRequestAction"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    abortOnFailure: NotRequired[AbortOnFailure]

    forceBuild: NotRequired[ForceBuild]

    retryBackoffDuration: NotRequired[RetryBackoffDurationDict]

    retryCount: NotRequired[RetryCount]

    fallbackBranches: NotRequired[FallbackBranches]

    branchName: NotRequired[BranchName]
    """The target branch the schedule should run on."""

    notificationsEnabled: NotRequired[NotificationsEnabled]

    target: ReplaceScheduleRequestActionBuildTargetDict
