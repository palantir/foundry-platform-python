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

from foundry.v2.core.models._created_by import CreatedBy
from foundry.v2.core.models._created_time import CreatedTime
from foundry.v2.orchestration.models._schedule_rid import ScheduleRid
from foundry.v2.orchestration.models._schedule_run_dict import ScheduleRunDict
from foundry.v2.orchestration.models._schedule_run_result import ScheduleRunResult
from foundry.v2.orchestration.models._schedule_run_rid import ScheduleRunRid
from foundry.v2.orchestration.models._schedule_version_rid import ScheduleVersionRid


class ScheduleRun(BaseModel):
    """ScheduleRun"""

    rid: ScheduleRunRid
    """The RID of a schedule run"""

    schedule_rid: ScheduleRid = Field(alias="scheduleRid")

    schedule_version_rid: ScheduleVersionRid = Field(alias="scheduleVersionRid")

    created_time: CreatedTime = Field(alias="createdTime")
    """The time at which the schedule run was created."""

    created_by: Optional[CreatedBy] = Field(alias="createdBy", default=None)
    """
    The Foundry user who manually invoked this schedule run. Automatic trigger runs have this field set to
    empty.
    """

    result: Optional[ScheduleRunResult] = None
    """
    The result of triggering the schedule. If empty, it means the service
    is still working on triggering the schedule.
    """

    model_config = {"extra": "allow"}

    def to_dict(self) -> ScheduleRunDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(ScheduleRunDict, self.model_dump(by_alias=True, exclude_unset=True))
