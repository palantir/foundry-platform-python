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

from pydantic import StrictStr
from typing_extensions import NotRequired
from typing_extensions import TypedDict

from foundry.v2.models._action_dict import ActionDict
from foundry.v2.models._created_by import CreatedBy
from foundry.v2.models._created_time import CreatedTime
from foundry.v2.models._schedule_paused import SchedulePaused
from foundry.v2.models._schedule_rid import ScheduleRid
from foundry.v2.models._schedule_version_rid import ScheduleVersionRid
from foundry.v2.models._scope_mode_dict import ScopeModeDict
from foundry.v2.models._trigger_dict import TriggerDict
from foundry.v2.models._updated_by import UpdatedBy
from foundry.v2.models._updated_time import UpdatedTime


class ScheduleDict(TypedDict):
    """Schedule"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    rid: ScheduleRid

    displayName: NotRequired[StrictStr]

    description: NotRequired[StrictStr]

    currentVersionRid: ScheduleVersionRid
    """The RID of the current schedule version"""

    createdTime: CreatedTime

    createdBy: CreatedBy

    updatedTime: UpdatedTime

    updatedBy: UpdatedBy

    paused: SchedulePaused

    trigger: NotRequired[TriggerDict]
    """
    The schedule trigger. If the requesting user does not have
    permission to see the trigger, this will be empty.
    """

    action: ActionDict

    scopeMode: ScopeModeDict
