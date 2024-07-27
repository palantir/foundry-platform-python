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

from pydantic import StrictStr
from typing_extensions import NotRequired
from typing_extensions import TypedDict

from foundry.models._attribute_name import AttributeName
from foundry.models._attribute_values import AttributeValues
from foundry.models._group_name import GroupName
from foundry.models._organization_rid import OrganizationRid
from foundry.models._principal_id import PrincipalId
from foundry.models._realm import Realm


class GroupDict(TypedDict):
    """Group"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    id: PrincipalId

    name: GroupName

    description: NotRequired[StrictStr]

    realm: Realm

    organizations: List[OrganizationRid]

    attributes: Dict[AttributeName, AttributeValues]
    """A map of the Group's attributes. Attributes prefixed with "multipass:" are reserved for internal use by Foundry and are subject to change."""
