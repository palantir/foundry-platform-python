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

from foundry.v2.core.models._created_by import CreatedBy
from foundry.v2.core.models._created_time import CreatedTime
from foundry.v2.core.models._updated_by import UpdatedBy
from foundry.v2.core.models._updated_time import UpdatedTime
from foundry.v2.orchestration.models._action import Action
from foundry.v2.orchestration.models._schedule_dict import ScheduleDict
from foundry.v2.orchestration.models._schedule_paused import SchedulePaused
from foundry.v2.orchestration.models._schedule_rid import ScheduleRid
from foundry.v2.orchestration.models._schedule_version_rid import ScheduleVersionRid
from foundry.v2.orchestration.models._scope_mode import ScopeMode
from foundry.v2.orchestration.models._trigger import Trigger


class Schedule(pydantic.BaseModel):
    """Schedule"""

    rid: ScheduleRid

    display_name: Optional[pydantic.StrictStr] = pydantic.Field(alias="displayName", default=None)

    description: Optional[pydantic.StrictStr] = None

    current_version_rid: ScheduleVersionRid = pydantic.Field(alias="currentVersionRid")
    """The RID of the current schedule version"""

    created_time: CreatedTime = pydantic.Field(alias="createdTime")

    created_by: CreatedBy = pydantic.Field(alias="createdBy")

    updated_time: UpdatedTime = pydantic.Field(alias="updatedTime")

    updated_by: UpdatedBy = pydantic.Field(alias="updatedBy")

    paused: SchedulePaused

    trigger: Optional[Trigger] = None
    """
    The schedule trigger. If the requesting user does not have
    permission to see the trigger, this will be empty.
    """

    action: Action

    scope_mode: ScopeMode = pydantic.Field(alias="scopeMode")

    model_config = {"extra": "allow"}

    def to_dict(self) -> ScheduleDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(ScheduleDict, self.model_dump(by_alias=True, exclude_unset=True))
