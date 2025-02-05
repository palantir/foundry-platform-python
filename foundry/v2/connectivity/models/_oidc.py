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
from typing import cast

import pydantic

from foundry.v2.connectivity.models._connection_rid import ConnectionRid
from foundry.v2.connectivity.models._oidc_dict import OidcDict


class Oidc(pydantic.BaseModel):
    """
    [OpenID Connect (OIDC)](/docs/foundry/data-connection/oidc/) is an open authentication protocol that allows
    you to authenticate to external system resources without the use of static credentials.
    """

    audience: str

    """The configured audience that identifies the external system."""

    issuer_url: str = pydantic.Field(alias=str("issuerUrl"))  # type: ignore[literal-required]

    """The URL that identifies Foundry as an OIDC identity provider."""

    subject: ConnectionRid

    """The RID of the Connection that is connecting to the external system."""

    type: Literal["oidc"] = "oidc"

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> OidcDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(OidcDict, self.model_dump(by_alias=True, exclude_none=True))
