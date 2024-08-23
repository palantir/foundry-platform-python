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

from foundry.v2.models._attribute_name import AttributeName
from foundry.v2.models._attribute_values import AttributeValues
from foundry.v2.models._group_name import GroupName
from foundry.v2.models._organization_rid import OrganizationRid


class CreateGroupRequestDict(TypedDict):
    """CreateGroupRequest"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    name: GroupName
    """The name of the Group."""

    organizations: List[OrganizationRid]
    """The RIDs of the Organizations whose members can see this group. At least one Organization RID must be listed."""

    description: NotRequired[StrictStr]
    """A description of the Group."""

    attributes: Dict[AttributeName, AttributeValues]
    """A map of the Group's attributes. Attributes prefixed with "multipass:" are reserved for internal use by Foundry and are subject to change."""
