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
from foundry.v2.orchestration.models._action import Action
from foundry.v2.orchestration.models._schedule_rid import ScheduleRid
from foundry.v2.orchestration.models._schedule_version_dict import ScheduleVersionDict
from foundry.v2.orchestration.models._schedule_version_rid import ScheduleVersionRid
from foundry.v2.orchestration.models._scope_mode import ScopeMode
from foundry.v2.orchestration.models._trigger import Trigger


class ScheduleVersion(pydantic.BaseModel):
    """ScheduleVersion"""

    rid: ScheduleVersionRid

    """The RID of a schedule version"""

    schedule_rid: ScheduleRid = pydantic.Field(alias="scheduleRid")

    created_time: CreatedTime = pydantic.Field(alias="createdTime")

    """The time the schedule version was created"""

    created_by: CreatedBy = pydantic.Field(alias="createdBy")

    """The Foundry user who created the schedule version"""

    trigger: Optional[Trigger] = None

    action: Action

    scope_mode: ScopeMode = pydantic.Field(alias="scopeMode")

    model_config = {"extra": "allow"}

    def to_dict(self) -> ScheduleVersionDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(ScheduleVersionDict, self.model_dump(by_alias=True, exclude_unset=True))
