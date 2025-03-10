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


class InvalidDurationGroupByValueParameters(typing_extensions.TypedDict):
    """
    Duration groupBy value is invalid. Units larger than day must have value `1` and date properties do not support
    filtering on units smaller than day. As examples, neither bucketing by every two weeks nor bucketing a date by
    every two hours are allowed.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class InvalidDurationGroupByValue(errors.BadRequestError):
    name: typing.Literal["InvalidDurationGroupByValue"]
    parameters: InvalidDurationGroupByValueParameters
    error_instance_id: str


__all__ = ["InvalidDurationGroupByValue"]
