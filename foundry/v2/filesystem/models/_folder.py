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

from foundry.v2.core.models._created_by import CreatedBy
from foundry.v2.core.models._created_time import CreatedTime
from foundry.v2.core.models._updated_by import UpdatedBy
from foundry.v2.core.models._updated_time import UpdatedTime
from foundry.v2.filesystem.models._folder_dict import FolderDict
from foundry.v2.filesystem.models._folder_rid import FolderRid
from foundry.v2.filesystem.models._folder_type import FolderType
from foundry.v2.filesystem.models._project_rid import ProjectRid
from foundry.v2.filesystem.models._resource_display_name import ResourceDisplayName
from foundry.v2.filesystem.models._resource_path import ResourcePath
from foundry.v2.filesystem.models._space_rid import SpaceRid
from foundry.v2.filesystem.models._trash_status import TrashStatus


class Folder(pydantic.BaseModel):
    """Folder"""

    rid: FolderRid

    display_name: ResourceDisplayName = pydantic.Field(alias="displayName")

    description: Optional[pydantic.StrictStr] = None
    """The description associated with the Folder."""

    documentation: Optional[pydantic.StrictStr] = None
    """The documentation associated with the Folder."""

    path: ResourcePath

    type: FolderType

    created_by: CreatedBy = pydantic.Field(alias="createdBy")

    updated_by: UpdatedBy = pydantic.Field(alias="updatedBy")

    created_time: CreatedTime = pydantic.Field(alias="createdTime")

    updated_time: UpdatedTime = pydantic.Field(alias="updatedTime")

    trash_status: TrashStatus = pydantic.Field(alias="trashStatus")
    """
    The trash status of the Folder. If trashed, this could either be because the Folder itself has been
    trashed or because one of its ancestors has been trashed.
    """

    parent_folder_rid: FolderRid = pydantic.Field(alias="parentFolderRid")
    """
    The parent folder Resource Identifier (RID). For Projects, this will be the Space RID and for Spaces,
    this value will be the root folder (`ri.compass.main.folder.0`).
    """

    project_rid: Optional[ProjectRid] = pydantic.Field(alias="projectRid", default=None)
    """
    The Project Resource Identifier (RID) that the Folder lives in. If the Folder is a Space, this value will
    not be defined.
    """

    space_rid: SpaceRid = pydantic.Field(alias="spaceRid")
    """
    The Space Resource Identifier (RID) that the Folder lives in. If the Folder is a Space, this value will
    be the same as the Folder RID.
    """

    model_config = {"extra": "allow"}

    def to_dict(self) -> FolderDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(FolderDict, self.model_dump(by_alias=True, exclude_unset=True))
