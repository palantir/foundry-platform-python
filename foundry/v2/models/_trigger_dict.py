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

from typing import Annotated
from typing import List
from typing import Literal
from typing import Union

from pydantic import Field
from typing_extensions import TypedDict

from foundry.v2.models._dataset_updated_trigger_dict import DatasetUpdatedTriggerDict
from foundry.v2.models._job_succeeded_trigger_dict import JobSucceededTriggerDict
from foundry.v2.models._media_set_updated_trigger_dict import MediaSetUpdatedTriggerDict
from foundry.v2.models._new_logic_trigger_dict import NewLogicTriggerDict
from foundry.v2.models._schedule_succeeded_trigger_dict import ScheduleSucceededTriggerDict  # NOQA
from foundry.v2.models._time_trigger_dict import TimeTriggerDict


class AndTriggerDict(TypedDict):
    """Trigger after all of the given triggers emit an event."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    triggers: List[TriggerDict]

    type: Literal["and"]


class OrTriggerDict(TypedDict):
    """Trigger whenever any of the given triggers emit an event."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    triggers: List[TriggerDict]

    type: Literal["or"]


TriggerDict = Annotated[
    Union[
        AndTriggerDict,
        OrTriggerDict,
        TimeTriggerDict,
        DatasetUpdatedTriggerDict,
        NewLogicTriggerDict,
        JobSucceededTriggerDict,
        ScheduleSucceededTriggerDict,
        MediaSetUpdatedTriggerDict,
    ],
    Field(discriminator="type"),
]
"""Trigger"""
