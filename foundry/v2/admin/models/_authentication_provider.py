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

from typing import List
from typing import cast

import pydantic

from foundry.v2.admin.models._authentication_protocol import AuthenticationProtocol
from foundry.v2.admin.models._authentication_provider_dict import AuthenticationProviderDict  # NOQA
from foundry.v2.admin.models._authentication_provider_enabled import (
    AuthenticationProviderEnabled,
)  # NOQA
from foundry.v2.admin.models._authentication_provider_name import AuthenticationProviderName  # NOQA
from foundry.v2.admin.models._authentication_provider_rid import AuthenticationProviderRid  # NOQA
from foundry.v2.admin.models._host_name import HostName
from foundry.v2.core.models._realm import Realm


class AuthenticationProvider(pydantic.BaseModel):
    """AuthenticationProvider"""

    rid: AuthenticationProviderRid

    name: AuthenticationProviderName

    realm: Realm

    enabled: AuthenticationProviderEnabled

    """Whether users can log in using this provider."""

    supported_hosts: List[HostName] = pydantic.Field(alias=str("supportedHosts"))  # type: ignore[literal-required]

    """This provider can only be utilized from these hosts."""

    supported_username_patterns: List[str] = pydantic.Field(alias=str("supportedUsernamePatterns"))  # type: ignore[literal-required]

    """Users who enter usernames that match these patterns will be redirected to this authentication provider."""

    protocol: AuthenticationProtocol

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> AuthenticationProviderDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(AuthenticationProviderDict, self.model_dump(by_alias=True, exclude_none=True))
