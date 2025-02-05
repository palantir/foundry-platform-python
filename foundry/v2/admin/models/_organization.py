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

from foundry.v2.admin.models._host_name import HostName
from foundry.v2.admin.models._organization_dict import OrganizationDict
from foundry.v2.admin.models._organization_name import OrganizationName
from foundry.v2.core.models._marking_id import MarkingId
from foundry.v2.core.models._organization_rid import OrganizationRid


class Organization(pydantic.BaseModel):
    """Organization"""

    rid: OrganizationRid

    name: OrganizationName

    description: Optional[str] = None

    marking_id: MarkingId = pydantic.Field(alias=str("markingId"))  # type: ignore[literal-required]

    """
    The ID of this Organization's underlying marking. Organization guest access can be managed
    by updating the membership of this Marking.
    """

    host: Optional[HostName] = None

    """
    The primary host name of the Organization. This should be used when constructing URLs for users of this
    Organization.
    """

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> OrganizationDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(OrganizationDict, self.model_dump(by_alias=True, exclude_none=True))
