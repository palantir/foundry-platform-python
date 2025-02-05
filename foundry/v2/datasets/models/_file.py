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

from typing import Optional
from typing import cast

import pydantic

from foundry._core.utils import Long
from foundry.v2.core.models._file_path import FilePath
from foundry.v2.datasets.models._file_dict import FileDict
from foundry.v2.datasets.models._file_updated_time import FileUpdatedTime
from foundry.v2.datasets.models._transaction_rid import TransactionRid


class File(pydantic.BaseModel):
    """File"""

    path: FilePath

    transaction_rid: TransactionRid = pydantic.Field(alias=str("transactionRid"))  # type: ignore[literal-required]

    size_bytes: Optional[Long] = pydantic.Field(alias=str("sizeBytes"), default=None)  # type: ignore[literal-required]

    updated_time: FileUpdatedTime = pydantic.Field(alias=str("updatedTime"))  # type: ignore[literal-required]

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> FileDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(FileDict, self.model_dump(by_alias=True, exclude_none=True))
