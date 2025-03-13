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


import typing
from dataclasses import dataclass

import typing_extensions

from foundry import _errors as errors
from foundry.v2.orchestration import models as orchestration_models


class TargetNotSupportedParameters(typing_extensions.TypedDict):
    """
    The schedule target is not supported. The schedule target must be either a connecting target, upstream
    target or list of single dataset targets.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    scheduleRid: orchestration_models.ScheduleRid


@dataclass
class TargetNotSupported(errors.BadRequestError):
    name: typing.Literal["TargetNotSupported"]
    parameters: TargetNotSupportedParameters
    error_instance_id: str


__all__ = ["TargetNotSupported"]
