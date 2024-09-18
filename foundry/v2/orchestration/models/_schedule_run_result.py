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

from typing import Union

from pydantic import Field
from typing_extensions import Annotated

from foundry.v2.orchestration.models._schedule_run_error import ScheduleRunError
from foundry.v2.orchestration.models._schedule_run_ignored import ScheduleRunIgnored
from foundry.v2.orchestration.models._schedule_run_submitted import ScheduleRunSubmitted

ScheduleRunResult = Annotated[
    Union[ScheduleRunIgnored, ScheduleRunSubmitted, ScheduleRunError], Field(discriminator="type")
]
"""
The result of attempting to trigger the schedule. The schedule run will either be submitted as a build,
ignored if all targets are up-to-date or error.
"""
