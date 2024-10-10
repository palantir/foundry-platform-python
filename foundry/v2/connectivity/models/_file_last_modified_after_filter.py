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

from datetime import datetime
from typing import Literal
from typing import Optional
from typing import cast

import pydantic

from foundry.v2.connectivity.models._file_last_modified_after_filter_dict import (
    FileLastModifiedAfterFilterDict,
)  # NOQA


class FileLastModifiedAfterFilter(pydantic.BaseModel):
    """Only import files that have been modified after a specified timestamp"""

    after_timestamp: Optional[datetime] = pydantic.Field(alias="afterTimestamp", default=None)
    """
    Timestamp threshold, specified in ISO-8601 format.
    If not specified, defaults to the timestamp the file import is executed.
    """

    type: Literal["lastModifiedAfterFilter"]

    model_config = {"extra": "allow"}

    def to_dict(self) -> FileLastModifiedAfterFilterDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(
            FileLastModifiedAfterFilterDict, self.model_dump(by_alias=True, exclude_unset=True)
        )
