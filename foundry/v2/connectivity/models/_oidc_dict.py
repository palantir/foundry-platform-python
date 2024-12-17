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

from typing import Literal

from typing_extensions import TypedDict

from foundry.v2.connectivity.models._connection_rid import ConnectionRid


class OidcDict(TypedDict):
    """
    [OpenID Connect (OIDC)](/docs/foundry/data-connection/oidc/) is an open authentication protocol that allows
    you to authenticate to external system resources without the use of static credentials.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    audience: str
    """The configured audience that identifies the external system."""

    issuerUrl: str
    """The URL that identifies Foundry as an OIDC identity provider."""

    subject: ConnectionRid
    """The RID of the Connection that is connecting to the external system."""

    type: Literal["oidc"]
