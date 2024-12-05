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


class CreateConnectionRequestAgentWorkerRuntimeDict(TypedDict):
    """CreateConnectionRequestAgentWorkerRuntime"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    agentRids: List[AgentRid]
    """
    The RIDs of the [agents](/docs/foundry/data-connection/set-up-agent/) configured on the connection.
    These agents are used to provide network connectivity to the external systems or APIs configured on the
    connection.
    """

    type: Literal["agentWorkerRuntime"]
