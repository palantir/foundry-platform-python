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

from typing import Any
from typing import Literal
from typing import cast

from pydantic import BaseModel

from foundry.v2.connectivity.models._file_import_custom_filter_dict import (
    FileImportCustomFilterDict,
)  # NOQA


class FileImportCustomFilter(BaseModel):
    """
    A custom file import filter. Custom file import filters can be fetched but cannot currently be used
    when creating or updating file imports.
    """

    config: Any

    type: Literal["customFilter"]

    model_config = {"extra": "allow"}

    def to_dict(self) -> FileImportCustomFilterDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(FileImportCustomFilterDict, self.model_dump(by_alias=True, exclude_unset=True))
