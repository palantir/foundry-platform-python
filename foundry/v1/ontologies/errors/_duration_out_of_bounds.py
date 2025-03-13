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
from foundry.v1.ontologies import models as ontologies_models


class DurationOutOfBoundsParameters(typing_extensions.TypedDict):
    """The duration specified is out of bounds. The maximum allowed duration is 285,616,414 YEARS."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    value: int
    unit: ontologies_models.PreciseTimeUnit


@dataclass
class DurationOutOfBounds(errors.BadRequestError):
    name: typing.Literal["DurationOutOfBounds"]
    parameters: DurationOutOfBoundsParameters
    error_instance_id: str


__all__ = ["DurationOutOfBounds"]
