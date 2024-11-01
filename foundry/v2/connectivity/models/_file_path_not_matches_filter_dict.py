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

from typing import Literal

import pydantic
from typing_extensions import TypedDict


class FilePathNotMatchesFilterDict(TypedDict):
    """
    Only import files whose path (relative to the root of the source) does not match the regular expression.

    **Example**
    Suppose we are importing files from `relative/subfolder`.
    `relative/subfolder` contains:
    - `relative/subfolder/include-file.txt`
    - `relative/subfolder/exclude-file.txt`
    - `relative/subfolder/other-file.txt`

    With the `relative/subfolder/exclude-.*.txt` regex, both `relative/subfolder/include-file.txt` and `relative/subfolder/other-file.txt` will be imported,
    and `relative/subfolder/exclude-file.txt` will be excluded from the import.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    regex: pydantic.StrictStr
    """Must be written to match the paths relative to the root of the source, even if a subfolder is specified."""

    type: Literal["pathNotMatchesFilter"]
