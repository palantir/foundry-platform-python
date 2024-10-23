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

from typing_extensions import TypedDict

from foundry.v2.connectivity.models._agent_rid import AgentRid


class AgentProxyRuntimeDict(TypedDict):
    """
    The [agent proxy runtime](/docs/foundry/data-connection/core-concepts/#agent-proxy-runtime) is used to connect
    to data sources not accessible over the Internet. The agent acts as an inverting network proxy, forwarding
    network traffic originating in Foundry into the network where the agent is deployed, and relaying traffic
    back to Foundry. This allows capabilities in Foundry to work almost exactly the same as when using a
    direct connection but without requiring you to allow inbound network traffic to your systems originating
    from Foundry's IP addresses.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    agentRids: List[AgentRid]
    """
    The RIDs of the [agents](/docs/foundry/data-connection/set-up-agent/) configured on the connection.
    These agents are used to provide network connectivity to the external systems or APIs configured on the
    connection.
    """

    type: Literal["agentProxyRuntime"]
