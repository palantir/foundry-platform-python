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

from foundry.v2.orchestration.models._schedule_run_error_dict import ScheduleRunErrorDict  # NOQA
from foundry.v2.orchestration.models._schedule_run_ignored_dict import (
    ScheduleRunIgnoredDict,
)  # NOQA
from foundry.v2.orchestration.models._schedule_run_submitted_dict import (
    ScheduleRunSubmittedDict,
)  # NOQA

ScheduleRunResultDict = Annotated[
    Union[ScheduleRunIgnoredDict, ScheduleRunSubmittedDict, ScheduleRunErrorDict],
    Field(discriminator="type"),
]
"""
The result of attempting to trigger the schedule. The schedule run will either be submitted as a build,
ignored if all targets are up-to-date or error.
"""
