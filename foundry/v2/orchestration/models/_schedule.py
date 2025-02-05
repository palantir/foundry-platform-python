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

    display_name: Optional[str] = pydantic.Field(alias=str("displayName"), default=None)  # type: ignore[literal-required]

    description: Optional[str] = None

    current_version_rid: ScheduleVersionRid = pydantic.Field(alias=str("currentVersionRid"))  # type: ignore[literal-required]

    """The RID of the current schedule version"""

    created_time: CreatedTime = pydantic.Field(alias=str("createdTime"))  # type: ignore[literal-required]

    created_by: CreatedBy = pydantic.Field(alias=str("createdBy"))  # type: ignore[literal-required]

    updated_time: UpdatedTime = pydantic.Field(alias=str("updatedTime"))  # type: ignore[literal-required]

    updated_by: UpdatedBy = pydantic.Field(alias=str("updatedBy"))  # type: ignore[literal-required]

    paused: SchedulePaused

    trigger: Optional[Trigger] = None

    """
    The schedule trigger. If the requesting user does not have
    permission to see the trigger, this will be empty.
    """

    action: Action

    scope_mode: ScopeMode = pydantic.Field(alias=str("scopeMode"))  # type: ignore[literal-required]

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> ScheduleDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(ScheduleDict, self.model_dump(by_alias=True, exclude_none=True))
