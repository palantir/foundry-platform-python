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

from typing_extensions import TypedDict

from foundry.v2.admin.models._authentication_protocol_dict import AuthenticationProtocolDict  # NOQA
from foundry.v2.admin.models._authentication_provider_enabled import (
    AuthenticationProviderEnabled,
)  # NOQA
from foundry.v2.admin.models._authentication_provider_name import AuthenticationProviderName  # NOQA
from foundry.v2.admin.models._authentication_provider_rid import AuthenticationProviderRid  # NOQA
from foundry.v2.admin.models._host_name import HostName
from foundry.v2.core.models._realm import Realm


class AuthenticationProviderDict(TypedDict):
    """AuthenticationProvider"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    rid: AuthenticationProviderRid

    name: AuthenticationProviderName

    realm: Realm

    enabled: AuthenticationProviderEnabled
    """Whether users can log in using this provider."""

    supportedHosts: List[HostName]
    """This provider can only be utilized from these hosts."""

    supportedUsernamePatterns: List[str]
    """Users who enter usernames that match these patterns will be redirected to this authentication provider."""

    protocol: AuthenticationProtocolDict
