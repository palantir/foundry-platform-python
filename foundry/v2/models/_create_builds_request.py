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

from pydantic import BaseModel
from pydantic import Field

from foundry.v2.models._abort_on_failure import AbortOnFailure
from foundry.v2.models._branch_name import BranchName
from foundry.v2.models._build_target import BuildTarget
from foundry.v2.models._create_builds_request_dict import CreateBuildsRequestDict
from foundry.v2.models._fallback_branches import FallbackBranches
from foundry.v2.models._force_build import ForceBuild
from foundry.v2.models._notifications_enabled import NotificationsEnabled
from foundry.v2.models._retry_backoff_duration import RetryBackoffDuration
from foundry.v2.models._retry_count import RetryCount


class CreateBuildsRequest(BaseModel):
    """CreateBuildsRequest"""

    target: BuildTarget
    """The targets of the schedule."""

    branch_name: Optional[BranchName] = Field(alias="branchName", default=None)
    """The target branch the build should run on."""

    fallback_branches: FallbackBranches = Field(alias="fallbackBranches")

    force_build: Optional[ForceBuild] = Field(alias="forceBuild", default=None)

    retry_count: Optional[RetryCount] = Field(alias="retryCount", default=None)
    """The number of retry attempts for failed jobs."""

    retry_backoff_duration: Optional[RetryBackoffDuration] = Field(
        alias="retryBackoffDuration", default=None
    )

    abort_on_failure: Optional[AbortOnFailure] = Field(alias="abortOnFailure", default=None)

    notifications_enabled: Optional[NotificationsEnabled] = Field(
        alias="notificationsEnabled", default=None
    )

    model_config = {"extra": "allow"}

    def to_dict(self) -> CreateBuildsRequestDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(CreateBuildsRequestDict, self.model_dump(by_alias=True, exclude_unset=True))
