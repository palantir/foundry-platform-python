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

from typing import Dict
from typing import List
from typing import Optional
from typing import cast

from pydantic import BaseModel
from pydantic import StrictStr

from foundry.v2.admin.models._attribute_name import AttributeName
from foundry.v2.admin.models._attribute_values import AttributeValues
from foundry.v2.admin.models._group_dict import GroupDict
from foundry.v2.admin.models._group_name import GroupName
from foundry.v2.core.models._organization_rid import OrganizationRid
from foundry.v2.core.models._principal_id import PrincipalId
from foundry.v2.core.models._realm import Realm


class Group(BaseModel):
    """Group"""

    id: PrincipalId

    name: GroupName
    """The name of the Group."""

    description: Optional[StrictStr] = None
    """A description of the Group."""

    realm: Realm

    organizations: List[OrganizationRid]
    """The RIDs of the Organizations whose members can see this group. At least one Organization RID must be listed."""

    attributes: Dict[AttributeName, AttributeValues]
    """A map of the Group's attributes. Attributes prefixed with "multipass:" are reserved for internal use by Foundry and are subject to change."""

    model_config = {"extra": "allow"}

    def to_dict(self) -> GroupDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(GroupDict, self.model_dump(by_alias=True, exclude_unset=True))
