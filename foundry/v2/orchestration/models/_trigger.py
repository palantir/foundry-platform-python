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

from typing import List
from typing import Literal
from typing import Union
from typing import cast

from pydantic import BaseModel
from pydantic import Field
from typing_extensions import Annotated

from foundry.v2.orchestration.models._and_trigger_dict import AndTriggerDict
from foundry.v2.orchestration.models._dataset_updated_trigger import DatasetUpdatedTrigger  # NOQA
from foundry.v2.orchestration.models._job_succeeded_trigger import JobSucceededTrigger
from foundry.v2.orchestration.models._media_set_updated_trigger import (
    MediaSetUpdatedTrigger,
)  # NOQA
from foundry.v2.orchestration.models._new_logic_trigger import NewLogicTrigger
from foundry.v2.orchestration.models._or_trigger_dict import OrTriggerDict
from foundry.v2.orchestration.models._schedule_succeeded_trigger import (
    ScheduleSucceededTrigger,
)  # NOQA
from foundry.v2.orchestration.models._time_trigger import TimeTrigger


class OrTrigger(BaseModel):
    """Trigger whenever any of the given triggers emit an event."""

    triggers: List[Trigger]

    type: Literal["or"]

    model_config = {"extra": "allow"}

    def to_dict(self) -> OrTriggerDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(OrTriggerDict, self.model_dump(by_alias=True, exclude_unset=True))


class AndTrigger(BaseModel):
    """Trigger after all of the given triggers emit an event."""

    triggers: List[Trigger]

    type: Literal["and"]

    model_config = {"extra": "allow"}

    def to_dict(self) -> AndTriggerDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(AndTriggerDict, self.model_dump(by_alias=True, exclude_unset=True))


Trigger = Annotated[
    Union[
        JobSucceededTrigger,
        OrTrigger,
        NewLogicTrigger,
        AndTrigger,
        DatasetUpdatedTrigger,
        ScheduleSucceededTrigger,
        MediaSetUpdatedTrigger,
        TimeTrigger,
    ],
    Field(discriminator="type"),
]
"""Trigger"""
