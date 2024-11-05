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
from foundry.v2.filesystem.models._project_dict import ProjectDict
from foundry.v2.filesystem.models._project_rid import ProjectRid
from foundry.v2.filesystem.models._resource_display_name import ResourceDisplayName
from foundry.v2.filesystem.models._resource_path import ResourcePath
from foundry.v2.filesystem.models._space_rid import SpaceRid
from foundry.v2.filesystem.models._trash_status import TrashStatus


class Project(pydantic.BaseModel):
    """Project"""

    rid: ProjectRid

    display_name: ResourceDisplayName = pydantic.Field(alias="displayName")
    """The display name of the Project. Must be unique and cannot contain a /"""

    description: Optional[pydantic.StrictStr] = None
    """The description associated with the Project."""

    documentation: Optional[pydantic.StrictStr] = None
    """The documentation associated with the Project."""

    path: ResourcePath

    created_by: CreatedBy = pydantic.Field(alias="createdBy")

    updated_by: UpdatedBy = pydantic.Field(alias="updatedBy")

    created_time: CreatedTime = pydantic.Field(alias="createdTime")

    updated_time: UpdatedTime = pydantic.Field(alias="updatedTime")

    trash_status: TrashStatus = pydantic.Field(alias="trashStatus")
    """The trash status of the Project."""

    space_rid: SpaceRid = pydantic.Field(alias="spaceRid")
    """The Space Resource Identifier (RID) that the Project lives in."""

    model_config = {"extra": "allow"}

    def to_dict(self) -> ProjectDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(ProjectDict, self.model_dump(by_alias=True, exclude_unset=True))
