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

from typing import cast

from pydantic import BaseModel
from pydantic import Field

from foundry.v2.models._abort_on_failure import AbortOnFailure
from foundry.v2.models._branch_name import BranchName
from foundry.v2.models._build_dict import BuildDict
from foundry.v2.models._build_rid import BuildRid
from foundry.v2.models._build_status import BuildStatus
from foundry.v2.models._created_by import CreatedBy
from foundry.v2.models._created_time import CreatedTime
from foundry.v2.models._fallback_branches import FallbackBranches
from foundry.v2.models._retry_backoff_duration import RetryBackoffDuration
from foundry.v2.models._retry_count import RetryCount


class Build(BaseModel):
    """Build"""

    rid: BuildRid
    """The RID of a build"""

    branch_name: BranchName = Field(alias="branchName")
    """The branch that the build is running on."""

    created_time: CreatedTime = Field(alias="createdTime")
    """The timestamp that the build was created."""

    created_by: CreatedBy = Field(alias="createdBy")
    """The user who created the build."""

    fallback_branches: FallbackBranches = Field(alias="fallbackBranches")

    retry_count: RetryCount = Field(alias="retryCount")

    retry_backoff_duration: RetryBackoffDuration = Field(alias="retryBackoffDuration")

    abort_on_failure: AbortOnFailure = Field(alias="abortOnFailure")

    status: BuildStatus

    model_config = {"extra": "allow"}

    def to_dict(self) -> BuildDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(BuildDict, self.model_dump(by_alias=True, exclude_unset=True))
