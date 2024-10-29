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
from typing import cast

import pydantic

from foundry.v2.connectivity.models._file_path_matches_filter_dict import (
    FilePathMatchesFilterDict,
)  # NOQA


class FilePathMatchesFilter(pydantic.BaseModel):
    """
    Only import files whose path (relative to the root of the source) matches the regular expression.

    **Example**
    Suppose we are importing files from `relative/subfolder`.
    `relative/subfolder` contains:
    - `relative/subfolder/include-file.txt`
    - `relative/subfolder/exclude-file.txt`
    - `relative/subfolder/other-file.txt`

    With the `relative/subfolder/include-.*.txt` regex, only `relative/subfolder/include-file.txt` will be imported.
    """

    regex: pydantic.StrictStr
    """Must be written to match the paths relative to the root of the source, even if a subfolder is specified."""

    type: Literal["pathMatchesFilter"] = "pathMatchesFilter"

    model_config = {"extra": "allow"}

    def to_dict(self) -> FilePathMatchesFilterDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(FilePathMatchesFilterDict, self.model_dump(by_alias=True, exclude_unset=True))
