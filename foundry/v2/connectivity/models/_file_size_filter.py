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
from typing import Optional
from typing import cast

import pydantic

from foundry.v2.connectivity.models._file_size_filter_dict import FileSizeFilterDict
from foundry.v2.core.models._size_bytes import SizeBytes


class FileSizeFilter(pydantic.BaseModel):
    """
    Only import files whose size is between the specified minimum and maximum values.
    At least one of `gt` or `lt` should be present.
    If both are present, the value specified for `gt` must be strictly less than `lt - 1`.
    """

    gt: Optional[SizeBytes] = None
    """
    File size must be greater than this number for it to be imported.
    The value specified cannot be a negative number.
    """

    lt: Optional[SizeBytes] = None
    """
    File size must be less than this number for it to be imported.
    The value specified must be at least 1 byte.
    """

    type: Literal["fileSizeFilter"] = "fileSizeFilter"

    model_config = {"extra": "allow"}

    def to_dict(self) -> FileSizeFilterDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(FileSizeFilterDict, self.model_dump(by_alias=True, exclude_unset=True))
