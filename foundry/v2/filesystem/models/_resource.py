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

from pydantic import BaseModel
from pydantic import Field
from pydantic import StrictStr

from foundry.v2.core.models._created_by import CreatedBy
from foundry.v2.core.models._created_time import CreatedTime
from foundry.v2.core.models._updated_by import UpdatedBy
from foundry.v2.core.models._updated_time import UpdatedTime
from foundry.v2.filesystem.models._folder_rid import FolderRid
from foundry.v2.filesystem.models._project_rid import ProjectRid
from foundry.v2.filesystem.models._resource_dict import ResourceDict
from foundry.v2.filesystem.models._resource_display_name import ResourceDisplayName
from foundry.v2.filesystem.models._resource_path import ResourcePath
from foundry.v2.filesystem.models._resource_rid import ResourceRid
from foundry.v2.filesystem.models._resource_type import ResourceType
from foundry.v2.filesystem.models._space_rid import SpaceRid
from foundry.v2.filesystem.models._trashed_status import TrashedStatus


class Resource(BaseModel):
    """Resource"""

    rid: ResourceRid

    display_name: ResourceDisplayName = Field(alias="displayName")
    """The display name of the Resource"""

    description: Optional[StrictStr] = None
    """The description of the Resource"""

    documentation: Optional[StrictStr] = None
    """The documentation associated with the Resource"""

    path: ResourcePath
    """The full path to the resource, including the resource name itself"""

    type: ResourceType
    """The type of the Resource derived from the Resource Identifier (RID)."""

    created_by: CreatedBy = Field(alias="createdBy")
    """The user that created the Resource."""

    updated_by: UpdatedBy = Field(alias="updatedBy")
    """The user that last updated the Resource."""

    created_time: CreatedTime = Field(alias="createdTime")
    """The timestamp that the Resource was last created."""

    updated_time: UpdatedTime = Field(alias="updatedTime")
    """
    The timestamp that the Resource was last modified. For folders, this includes any of its descendants. For
    top level folders (spaces and projects), this is not updated by child updates for performance reasons.
    """

    trashed: TrashedStatus
    """
    The trash status of the resource. If trashed, a resource can either be directly trashed or one
    of its ancestors can be trashed.
    """

    parent_folder_rid: FolderRid = Field(alias="parentFolderRid")
    """The parent folder Resource Identifier (RID). For projects, this will be the Space RID."""

    project_rid: ProjectRid = Field(alias="projectRid")
    """
    The Project Resource Identifier (RID) that the Resource lives in. If the Resource itself is a
    Project, this value will still be populated with the Project RID.
    """

    space_rid: SpaceRid = Field(alias="spaceRid")
    """The Space Resource Identifier (RID) that the Resource lives in."""

    model_config = {"extra": "allow"}

    def to_dict(self) -> ResourceDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(ResourceDict, self.model_dump(by_alias=True, exclude_unset=True))
