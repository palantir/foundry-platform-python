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
from typing import Optional
from typing import cast

import pydantic

from foundry._core.utils import RID
from foundry.v2.connectivity.models._domain import Domain
from foundry.v2.connectivity.models._rest_connection_additional_secrets import (
    RestConnectionAdditionalSecrets,
)  # NOQA
from foundry.v2.connectivity.models._rest_connection_configuration_dict import (
    RestConnectionConfigurationDict,
)  # NOQA


class RestConnectionConfiguration(pydantic.BaseModel):
    """The configuration needed to connect to a [REST external system](/docs/foundry/available-connectors/rest-apis)."""

    domains: List[Domain]

    """
    The domains that the connection is allowed to access.
    At least one domain must be specified.
    """

    additional_secrets: Optional[RestConnectionAdditionalSecrets] = pydantic.Field(alias=str("additionalSecrets"), default=None)  # type: ignore[literal-required]

    """
    Additional secrets that can be referenced in code and webhook configurations.
    If not provided, no additional secrets will be created.
    """

    oauth2_client_rid: Optional[RID] = pydantic.Field(alias=str("oauth2ClientRid"), default=None)  # type: ignore[literal-required]

    """
    The RID of the [Outbound application](/docs/foundry/administration/configure-outbound-applications) that is used to authenticate to the external system via OAuth2.
    Currently, a connection may use only one outbound application for OAuth 2.0 authentication.
    Selecting a different outbound application will update the configuration for all domains with OAuth 2.0 as the selected authorization.
    """

    type: Literal["rest"] = "rest"

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> RestConnectionConfigurationDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(
            RestConnectionConfigurationDict, self.model_dump(by_alias=True, exclude_none=True)
        )
