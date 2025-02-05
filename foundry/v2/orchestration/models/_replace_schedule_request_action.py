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

from typing import Optional
from typing import cast

import pydantic

from foundry.v2.datasets.models._branch_name import BranchName
from foundry.v2.orchestration.models._abort_on_failure import AbortOnFailure
from foundry.v2.orchestration.models._fallback_branches import FallbackBranches
from foundry.v2.orchestration.models._force_build import ForceBuild
from foundry.v2.orchestration.models._notifications_enabled import NotificationsEnabled
from foundry.v2.orchestration.models._replace_schedule_request_action_dict import (
    ReplaceScheduleRequestActionDict,
)  # NOQA
from foundry.v2.orchestration.models._replace_schedule_request_build_target import (
    ReplaceScheduleRequestBuildTarget,
)  # NOQA
from foundry.v2.orchestration.models._retry_backoff_duration import RetryBackoffDuration
from foundry.v2.orchestration.models._retry_count import RetryCount


class ReplaceScheduleRequestAction(pydantic.BaseModel):
    """ReplaceScheduleRequestAction"""

    abort_on_failure: Optional[AbortOnFailure] = pydantic.Field(alias=str("abortOnFailure"), default=None)  # type: ignore[literal-required]

    force_build: Optional[ForceBuild] = pydantic.Field(alias=str("forceBuild"), default=None)  # type: ignore[literal-required]

    retry_backoff_duration: Optional[RetryBackoffDuration] = pydantic.Field(alias=str("retryBackoffDuration"), default=None)  # type: ignore[literal-required]

    retry_count: Optional[RetryCount] = pydantic.Field(alias=str("retryCount"), default=None)  # type: ignore[literal-required]

    fallback_branches: Optional[FallbackBranches] = pydantic.Field(alias=str("fallbackBranches"), default=None)  # type: ignore[literal-required]

    branch_name: Optional[BranchName] = pydantic.Field(alias=str("branchName"), default=None)  # type: ignore[literal-required]

    """The target branch the schedule should run on."""

    notifications_enabled: Optional[NotificationsEnabled] = pydantic.Field(alias=str("notificationsEnabled"), default=None)  # type: ignore[literal-required]

    target: ReplaceScheduleRequestBuildTarget

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> ReplaceScheduleRequestActionDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(
            ReplaceScheduleRequestActionDict, self.model_dump(by_alias=True, exclude_none=True)
        )
