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

from foundry.models._attribute_name import AttributeName
from foundry.models._attribute_values import AttributeValues
from foundry.models._create_group_request_dict import CreateGroupRequestDict
from foundry.models._group_name import GroupName
from foundry.models._organization_rid import OrganizationRid


class CreateGroupRequest(BaseModel):
    """CreateGroupRequest"""

    attributes: Dict[AttributeName, AttributeValues]
    """A map of the Group's attributes. Attributes prefixed with "multipass:" are reserved for internal use by Foundry and are subject to change."""

    description: Optional[StrictStr] = None

    name: GroupName

    organizations: List[OrganizationRid]

    model_config = {"extra": "allow"}

    def to_dict(self) -> CreateGroupRequestDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(CreateGroupRequestDict, self.model_dump(by_alias=True, exclude_unset=True))
