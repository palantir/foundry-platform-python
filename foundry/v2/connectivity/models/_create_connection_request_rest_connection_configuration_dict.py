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
from typing import Literal

from typing_extensions import NotRequired
from typing_extensions import TypedDict

from foundry._core.utils import RID
from foundry.v2.connectivity.models._domain_dict import DomainDict
from foundry.v2.connectivity.models._rest_connection_additional_secrets_dict import (
    RestConnectionAdditionalSecretsDict,
)  # NOQA


class CreateConnectionRequestRestConnectionConfigurationDict(TypedDict):
    """CreateConnectionRequestRestConnectionConfiguration"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    additionalSecrets: NotRequired[RestConnectionAdditionalSecretsDict]
    """
    Additional secrets that can be referenced in code and webhook configurations.
    If not provided, no additional secrets will be created.
    """

    oauth2ClientRid: NotRequired[RID]
    """
    The RID of the [Outbound application](/docs/foundry/administration/configure-outbound-applications) that is used to authenticate to the external system via OAuth2.
    Currently, a connection may use only one outbound application for OAuth 2.0 authentication.
    Selecting a different outbound application will update the configuration for all domains with OAuth 2.0 as the selected authorization.
    """

    domains: List[DomainDict]
    """
    The domains that the connection is allowed to access.
    At least one domain must be specified.
    """

    type: Literal["rest"]
