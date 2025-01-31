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

from typing_extensions import NotRequired
from typing_extensions import TypedDict

from foundry.v2.connectivity.models._basic_credentials_dict import BasicCredentialsDict
from foundry.v2.connectivity.models._protocol import Protocol


class S3ProxyConfigurationDict(TypedDict):
    """S3ProxyConfiguration"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    host: str
    """
    Domain name, IPv4, or IPv6 address. 
    `protocol` and `port` must be specified separately.
    """

    port: int

    nonProxyHosts: NotRequired[List[str]]
    """A list of hosts that can bypass the proxy, such as those used for STS Role. You can also use "*" wildcards."""

    protocol: NotRequired[Protocol]
    """If defined, must be "HTTP" or "HTTPS". Defaults to "HTTPS"."""

    credentials: NotRequired[BasicCredentialsDict]
