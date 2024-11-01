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

from foundry.v2.connectivity.models._files_count_limit_filter_dict import (
    FilesCountLimitFilterDict,
)  # NOQA


class FilesCountLimitFilter(pydantic.BaseModel):
    """
    Only retain `filesCount` number of files in each transaction.
    The choice of files to retain is made without any guarantee of order.
    This option can increase the reliability of incremental syncs.
    """

    files_count: pydantic.StrictInt = pydantic.Field(alias="filesCount")
    """The number of files to import in the transaction. The value specified must be positive."""

    type: Literal["filesCountLimitFilter"] = "filesCountLimitFilter"

    model_config = {"extra": "allow"}

    def to_dict(self) -> FilesCountLimitFilterDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(FilesCountLimitFilterDict, self.model_dump(by_alias=True, exclude_unset=True))
