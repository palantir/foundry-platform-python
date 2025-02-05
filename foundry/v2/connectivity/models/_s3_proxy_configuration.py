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
from typing import Optional
from typing import cast

import pydantic

from foundry.v2.connectivity.models._basic_credentials import BasicCredentials
from foundry.v2.connectivity.models._protocol import Protocol
from foundry.v2.connectivity.models._s3_proxy_configuration_dict import (
    S3ProxyConfigurationDict,
)  # NOQA


class S3ProxyConfiguration(pydantic.BaseModel):
    """S3ProxyConfiguration"""

    host: str

    """
    Domain name, IPv4, or IPv6 address. 
    `protocol` and `port` must be specified separately.
    """

    port: int

    non_proxy_hosts: Optional[List[str]] = pydantic.Field(alias=str("nonProxyHosts"), default=None)  # type: ignore[literal-required]

    """A list of hosts that can bypass the proxy, such as those used for STS Role. You can also use "*" wildcards."""

    protocol: Optional[Protocol] = None

    """If defined, must be "HTTP" or "HTTPS". Defaults to "HTTPS"."""

    credentials: Optional[BasicCredentials] = None

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> S3ProxyConfigurationDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(S3ProxyConfigurationDict, self.model_dump(by_alias=True, exclude_none=True))
