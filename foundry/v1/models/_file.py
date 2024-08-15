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
from typing import Optional
from typing import cast

from pydantic import BaseModel
from pydantic import Field
from pydantic import StrictStr

from foundry.v1.models._file_dict import FileDict
from foundry.v1.models._file_path import FilePath
from foundry.v1.models._transaction_rid import TransactionRid


class File(BaseModel):
    """File"""

    path: FilePath

    transaction_rid: TransactionRid = Field(alias="transactionRid")

    size_bytes: Optional[StrictStr] = Field(alias="sizeBytes", default=None)

    updated_time: datetime = Field(alias="updatedTime")

    model_config = {"extra": "allow"}

    def to_dict(self) -> FileDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(FileDict, self.model_dump(by_alias=True, exclude_unset=True))
