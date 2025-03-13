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

from foundry import _core as core
from foundry import _errors as errors


class FileSizeLimitExceededParameters(typing_extensions.TypedDict):
    """
    A file inside the .zip archive is too big. You must ensure that all files inside
    the .zip archive are within the limit.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    fileSizeBytesLimit: core.Long
    currentFileSizeBytes: core.Long
    currentFilePath: str


@dataclass
class FileSizeLimitExceeded(errors.BadRequestError):
    name: typing.Literal["FileSizeLimitExceeded"]
    parameters: FileSizeLimitExceededParameters
    error_instance_id: str


__all__ = ["FileSizeLimitExceeded"]
