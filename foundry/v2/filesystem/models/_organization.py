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

from foundry.v2.core.models._marking_id import MarkingId
from foundry.v2.core.models._organization_rid import OrganizationRid
from foundry.v2.filesystem.models._is_directly_applied import IsDirectlyApplied
from foundry.v2.filesystem.models._organization_dict import OrganizationDict


class Organization(pydantic.BaseModel):
    """
    [Organizations](/docs/foundry/security/orgs-and-spaces/#organizations) are access requirements applied to
    Projects that enforce strict silos between groups of users and resources. Every user is a member of only
    one Organization, but can be a guest member of multiple Organizations. In order to meet access requirements,
    users must be a member or guest member of at least one Organization applied to a Project.
    Organizations are inherited via the file hierarchy and direct dependencies.
    """

    marking_id: MarkingId = pydantic.Field(alias=str("markingId"))  # type: ignore[literal-required]

    organization_rid: OrganizationRid = pydantic.Field(alias=str("organizationRid"))  # type: ignore[literal-required]

    is_directly_applied: IsDirectlyApplied = pydantic.Field(alias=str("isDirectlyApplied"))  # type: ignore[literal-required]

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> OrganizationDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(OrganizationDict, self.model_dump(by_alias=True, exclude_none=True))
