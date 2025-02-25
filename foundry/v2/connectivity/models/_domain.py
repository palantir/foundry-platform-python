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

from foundry.v2.connectivity.models._domain_dict import DomainDict
from foundry.v2.connectivity.models._rest_authentication_mode import RestAuthenticationMode  # NOQA
from foundry.v2.connectivity.models._uri_scheme import UriScheme


class Domain(pydantic.BaseModel):
    """The domain that the connection is allowed to access."""

    scheme: Optional[UriScheme] = None

    """
    The scheme of the domain that the connection is allowed to access.
    If not specified, defaults to HTTPS.
    """

    host: str

    """The domain name, IPv4, or IPv6 address."""

    port: Optional[int] = None

    """The port number of the domain that the connection is allowed to access."""

    auth: Optional[RestAuthenticationMode] = None

    """
    The URI scheme must be HTTPS if using any authentication.
    If not specified, no authentication is required.
    """

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> DomainDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(DomainDict, self.model_dump(by_alias=True, exclude_none=True))
