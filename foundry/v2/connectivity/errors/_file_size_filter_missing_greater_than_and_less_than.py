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


class FileSizeFilterMissingGreaterThanAndLessThanParameters(typing_extensions.TypedDict):
    """
    Both the `gt` and `lt` properties are missing from the FileSizeFilter. At least one of these
    properties must be present
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class FileSizeFilterMissingGreaterThanAndLessThan(errors.BadRequestError):
    name: typing.Literal["FileSizeFilterMissingGreaterThanAndLessThan"]
    parameters: FileSizeFilterMissingGreaterThanAndLessThanParameters
    error_instance_id: str


__all__ = ["FileSizeFilterMissingGreaterThanAndLessThan"]
