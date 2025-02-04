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

from foundry.v2.admin.models._provider_id import ProviderId
from foundry.v2.admin.models._user_provider_info_dict import UserProviderInfoDict


class UserProviderInfo(pydantic.BaseModel):
    """UserProviderInfo"""

    provider_id: ProviderId = pydantic.Field(alias="providerId")

    """
    The ID of the User in the external authentication provider. This value is determined by the authentication provider.
    At most one User can have a given provider ID in a given Realm.
    """

    model_config = {"extra": "allow"}

    def to_dict(self) -> UserProviderInfoDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(UserProviderInfoDict, self.model_dump(by_alias=True, exclude_unset=True))
