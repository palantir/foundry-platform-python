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

from foundry.v2.datasets.models._branch_name import BranchName
from foundry.v2.orchestration.models._abort_on_failure import AbortOnFailure
from foundry.v2.orchestration.models._action_dict import ActionDict
from foundry.v2.orchestration.models._build_target import BuildTarget
from foundry.v2.orchestration.models._fallback_branches import FallbackBranches
from foundry.v2.orchestration.models._force_build import ForceBuild
from foundry.v2.orchestration.models._notifications_enabled import NotificationsEnabled
from foundry.v2.orchestration.models._retry_backoff_duration import RetryBackoffDuration
from foundry.v2.orchestration.models._retry_count import RetryCount


class Action(BaseModel):
    """Action"""

    target: BuildTarget

    branch_name: BranchName = Field(alias="branchName")
    """The target branch the schedule should run on."""

    fallback_branches: FallbackBranches = Field(alias="fallbackBranches")

    force_build: ForceBuild = Field(alias="forceBuild")

    retry_count: Optional[RetryCount] = Field(alias="retryCount", default=None)

    retry_backoff_duration: Optional[RetryBackoffDuration] = Field(
        alias="retryBackoffDuration", default=None
    )

    abort_on_failure: AbortOnFailure = Field(alias="abortOnFailure")

    notifications_enabled: NotificationsEnabled = Field(alias="notificationsEnabled")

    model_config = {"extra": "allow"}

    def to_dict(self) -> ActionDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(ActionDict, self.model_dump(by_alias=True, exclude_unset=True))
