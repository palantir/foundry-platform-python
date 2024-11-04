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

from typing import List
from typing import Literal
from typing import cast

import pydantic

from foundry.v2.connectivity.models._file_changed_since_last_upload_filter_dict import (
    FileChangedSinceLastUploadFilterDict,
)  # NOQA
from foundry.v2.connectivity.models._file_property import FileProperty


class FileChangedSinceLastUploadFilter(pydantic.BaseModel):
    """
    Only import files that have changed or been added since the last import run. Whether or not a file is considered to be changed is determined by the specified file properties.
    This will exclude files uploaded in any previous imports, regardless of the file import mode used. A SNAPSHOT file import mode does not reset the filter.
    """

    file_properties: List[FileProperty] = pydantic.Field(alias="fileProperties")
    """
    The criteria on which to determine whether a file has been changed or not since the last import. 
    If any of the specified criteria have changed, the file is consider changed. The criteria include:

    LAST_MODIFIED: The file's last modified timestamp has changed since the last import.
    SIZE: The file's size has changed since the last import.

    If no criteria are specified, only newly added files will be imported.
    """

    type: Literal["changedSinceLastUploadFilter"] = "changedSinceLastUploadFilter"

    model_config = {"extra": "allow"}

    def to_dict(self) -> FileChangedSinceLastUploadFilterDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(
            FileChangedSinceLastUploadFilterDict, self.model_dump(by_alias=True, exclude_unset=True)
        )
