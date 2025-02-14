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

from typing_extensions import NotRequired
from typing_extensions import TypedDict

from foundry.v2.core.models._organization_rid import OrganizationRid
from foundry.v2.filesystem.models._file_system_id import FileSystemId
from foundry.v2.filesystem.models._resource_display_name import ResourceDisplayName
from foundry.v2.filesystem.models._resource_path import ResourcePath
from foundry.v2.filesystem.models._space_rid import SpaceRid
from foundry.v2.filesystem.models._usage_account_rid import UsageAccountRid


class SpaceDict(TypedDict):
    """Space"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    rid: SpaceRid

    displayName: ResourceDisplayName

    description: NotRequired[str]
    """The description of the Space."""

    path: ResourcePath

    fileSystemId: NotRequired[FileSystemId]

    usageAccountRid: NotRequired[UsageAccountRid]

    organizations: List[OrganizationRid]
