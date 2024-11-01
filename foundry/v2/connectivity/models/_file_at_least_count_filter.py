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

from foundry.v2.connectivity.models._file_at_least_count_filter_dict import (
    FileAtLeastCountFilterDict,
)  # NOQA


class FileAtLeastCountFilter(pydantic.BaseModel):
    """Import all filtered files only if there are at least the specified number of files remaining."""

    min_files_count: pydantic.StrictInt = pydantic.Field(alias="minFilesCount")
    """
    The minimum number of files remaining expected.
    The value specified must be greater than 0.
    """

    type: Literal["atLeastCountFilter"] = "atLeastCountFilter"

    model_config = {"extra": "allow"}

    def to_dict(self) -> FileAtLeastCountFilterDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(FileAtLeastCountFilterDict, self.model_dump(by_alias=True, exclude_unset=True))
