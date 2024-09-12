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

from pydantic import StrictStr
from typing_extensions import NotRequired
from typing_extensions import TypedDict

from foundry.v2.models._created_by import CreatedBy
from foundry.v2.models._created_time import CreatedTime
from foundry.v2.models._folder_rid import FolderRid
from foundry.v2.models._project_rid import ProjectRid
from foundry.v2.models._resource_display_name import ResourceDisplayName
from foundry.v2.models._resource_path import ResourcePath
from foundry.v2.models._resource_rid import ResourceRid
from foundry.v2.models._resource_type import ResourceType
from foundry.v2.models._space_rid import SpaceRid
from foundry.v2.models._trashed_status import TrashedStatus
from foundry.v2.models._updated_by import UpdatedBy
from foundry.v2.models._updated_time import UpdatedTime


class ResourceDict(TypedDict):
    """Resource"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    rid: ResourceRid

    displayName: ResourceDisplayName
    """The display name of the Resource"""

    description: NotRequired[StrictStr]
    """The description of the Resource"""

    documentation: NotRequired[StrictStr]
    """The documentation associated with the Resource"""

    path: ResourcePath
    """The full path to the resource, including the resource name itself"""

    type: ResourceType
    """The type of the Resource derived from the Resource Identifier (RID)."""

    createdBy: CreatedBy
    """The user that created the Resource."""

    updatedBy: UpdatedBy
    """The user that last updated the Resource."""

    createdTime: CreatedTime
    """The timestamp that the Resource was last created."""

    updatedTime: UpdatedTime
    """
    The timestamp that the Resource was last modified. For folders, this includes any of its descendants. For
    top level folders (spaces and projects), this is not updated by child updates for performance reasons.
    """

    trashed: TrashedStatus
    """
    The trash status of the resource. If trashed, a resource can either be directly trashed or one
    of its ancestors can be trashed.
    """

    parentFolderRid: FolderRid
    """The parent folder Resource Identifier (RID). For projects, this will be the Space RID."""

    projectRid: ProjectRid
    """
    The Project Resource Identifier (RID) that the Resource lives in. If the Resource itself is a
    Project, this value will still be populated with the Project RID.
    """

    spaceRid: SpaceRid
    """The Space Resource Identifier (RID) that the Resource lives in."""
