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

from foundry.v2.core.models._created_by import CreatedBy
from foundry.v2.core.models._created_time import CreatedTime
from foundry.v2.orchestration.models._schedule_rid import ScheduleRid
from foundry.v2.orchestration.models._schedule_run_result_dict import ScheduleRunResultDict  # NOQA
from foundry.v2.orchestration.models._schedule_run_rid import ScheduleRunRid
from foundry.v2.orchestration.models._schedule_version_rid import ScheduleVersionRid


class ScheduleRunDict(TypedDict):
    """ScheduleRun"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    rid: ScheduleRunRid
    """The RID of a schedule run"""

    scheduleRid: ScheduleRid

    scheduleVersionRid: ScheduleVersionRid

    createdTime: CreatedTime
    """The time at which the schedule run was created."""

    createdBy: NotRequired[CreatedBy]
    """
    The Foundry user who manually invoked this schedule run. Automatic trigger runs have this field set to
    empty.
    """

    result: NotRequired[ScheduleRunResultDict]
    """
    The result of triggering the schedule. If empty, it means the service
    is still working on triggering the schedule.
    """
