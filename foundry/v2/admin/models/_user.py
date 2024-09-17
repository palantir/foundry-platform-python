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
from typing import Optional
from typing import cast

from pydantic import BaseModel
from pydantic import Field
from pydantic import StrictStr

from foundry.v2.admin.models._attribute_name import AttributeName
from foundry.v2.admin.models._attribute_values import AttributeValues
from foundry.v2.admin.models._user_dict import UserDict
from foundry.v2.admin.models._user_username import UserUsername
from foundry.v2.core.models._organization_rid import OrganizationRid
from foundry.v2.core.models._principal_id import PrincipalId
from foundry.v2.core.models._realm import Realm


class User(BaseModel):
    """User"""

    id: PrincipalId

    username: UserUsername
    """The Foundry username of the User. This is unique within the realm."""

    given_name: Optional[StrictStr] = Field(alias="givenName", default=None)
    """The given name of the User."""

    family_name: Optional[StrictStr] = Field(alias="familyName", default=None)
    """The family name (last name) of the User."""

    email: Optional[StrictStr] = None
    """The email at which to contact a User. Multiple users may have the same email address."""

    realm: Realm

    organization: Optional[OrganizationRid] = None
    """The RID of the user's primary Organization. This will be blank for third-party application service users."""

    attributes: Dict[AttributeName, AttributeValues]
    """
    A map of the User's attributes. Attributes prefixed with "multipass:" are reserved for internal use by
    Foundry and are subject to change. Additional attributes may be configured by Foundry administrators in 
    Control Panel and populated by the User's SSO provider upon login.
    """

    model_config = {"extra": "allow"}

    def to_dict(self) -> UserDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(UserDict, self.model_dump(by_alias=True, exclude_unset=True))
