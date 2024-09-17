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

from typing_extensions import TypedDict

from foundry.v2.models._abort_on_failure import AbortOnFailure
from foundry.v2.models._branch_name import BranchName
from foundry.v2.models._build_rid import BuildRid
from foundry.v2.models._build_status import BuildStatus
from foundry.v2.models._created_by import CreatedBy
from foundry.v2.models._created_time import CreatedTime
from foundry.v2.models._fallback_branches import FallbackBranches
from foundry.v2.models._retry_backoff_duration_dict import RetryBackoffDurationDict
from foundry.v2.models._retry_count import RetryCount


class BuildDict(TypedDict):
    """Build"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    rid: BuildRid
    """The RID of a build"""

    branchName: BranchName
    """The branch that the build is running on."""

    createdTime: CreatedTime
    """The timestamp that the build was created."""

    createdBy: CreatedBy
    """The user who created the build."""

    fallbackBranches: FallbackBranches

    retryCount: RetryCount

    retryBackoffDuration: RetryBackoffDurationDict

    abortOnFailure: AbortOnFailure

    status: BuildStatus
