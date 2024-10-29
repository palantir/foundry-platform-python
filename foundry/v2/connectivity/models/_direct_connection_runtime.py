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
from typing import cast

import pydantic

from foundry.v2.connectivity.models._direct_connection_runtime_dict import (
    DirectConnectionRuntimeDict,
)  # NOQA
from foundry.v2.connectivity.models._network_egress_policy_rid import NetworkEgressPolicyRid  # NOQA


class DirectConnectionRuntime(pydantic.BaseModel):
    """
    [Direct connections](/docs/foundry/data-connection/core-concepts/#direct-connection) enable users to connect
    to data sources accessible over the Internet without needing to set up an agent. If your Foundry stack is
    hosted on-premises, you can also connect to data sources within your on-premises network.

    This is the preferred source connection method if the data source is accessible over the Internet.
    """

    network_egress_policy_rids: List[NetworkEgressPolicyRid] = pydantic.Field(
        alias="networkEgressPolicyRids"
    )
    """
    The RIDs of the [network egress policies](/docs/foundry/administration/configure-egress/#network-egress-policies) 
    configured on the connection.
    These network egress policies represent the set of external destinations that the connection is allowed
    to egress to from a Foundry enrollment
    """

    type: Literal["directConnectionRuntime"] = "directConnectionRuntime"

    model_config = {"extra": "allow"}

    def to_dict(self) -> DirectConnectionRuntimeDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(DirectConnectionRuntimeDict, self.model_dump(by_alias=True, exclude_unset=True))
