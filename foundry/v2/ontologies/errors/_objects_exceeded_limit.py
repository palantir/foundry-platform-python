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


class ObjectsExceededLimitParameters(typing_extensions.TypedDict):
    """
    There are more objects, but they cannot be returned by this API. Only 10,000 objects are available through this
    API for a given request.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class ObjectsExceededLimit(errors.BadRequestError):
    name: typing.Literal["ObjectsExceededLimit"]
    parameters: ObjectsExceededLimitParameters
    error_instance_id: str


__all__ = ["ObjectsExceededLimit"]
