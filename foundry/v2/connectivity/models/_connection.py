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

from typing import cast

import pydantic

from foundry.v2.connectivity.models._connection_configuration import ConnectionConfiguration  # NOQA
from foundry.v2.connectivity.models._connection_dict import ConnectionDict
from foundry.v2.connectivity.models._connection_display_name import ConnectionDisplayName  # NOQA
from foundry.v2.connectivity.models._connection_rid import ConnectionRid
from foundry.v2.connectivity.models._runtime_platform import RuntimePlatform
from foundry.v2.filesystem.models._folder_rid import FolderRid


class Connection(pydantic.BaseModel):
    """Connection"""

    rid: ConnectionRid

    parent_folder_rid: FolderRid = pydantic.Field(alias=str("parentFolderRid"))  # type: ignore[literal-required]

    display_name: ConnectionDisplayName = pydantic.Field(alias=str("displayName"))  # type: ignore[literal-required]

    """The display name of the Connection. The display name must not be blank."""

    runtime_platform: RuntimePlatform = pydantic.Field(alias=str("runtimePlatform"))  # type: ignore[literal-required]

    configuration: ConnectionConfiguration

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> ConnectionDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(ConnectionDict, self.model_dump(by_alias=True, exclude_none=True))
