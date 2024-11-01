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

from foundry.v2.connectivity.models._file_any_path_matches_filter_dict import (
    FileAnyPathMatchesFilterDict,
)  # NOQA


class FileAnyPathMatchesFilter(pydantic.BaseModel):
    """If any file has a relative path matching the regular expression, sync all files in the subfolder that are not otherwise filtered."""

    regex: pydantic.StrictStr
    """The regular expression for the relative path to match against."""

    type: Literal["anyPathMatchesFilter"] = "anyPathMatchesFilter"

    model_config = {"extra": "allow"}

    def to_dict(self) -> FileAnyPathMatchesFilterDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(
            FileAnyPathMatchesFilterDict, self.model_dump(by_alias=True, exclude_unset=True)
        )
