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

from foundry.v2.core.models._role_id import RoleId
from foundry.v2.filesystem.models._resource_role_dict import ResourceRoleDict
from foundry.v2.filesystem.models._resource_role_principal import ResourceRolePrincipal


class ResourceRole(pydantic.BaseModel):
    """ResourceRole"""

    resource_role_principal: ResourceRolePrincipal = pydantic.Field(alias=str("resourceRolePrincipal"))  # type: ignore[literal-required]

    role_id: RoleId = pydantic.Field(alias=str("roleId"))  # type: ignore[literal-required]

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> ResourceRoleDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(ResourceRoleDict, self.model_dump(by_alias=True, exclude_none=True))
