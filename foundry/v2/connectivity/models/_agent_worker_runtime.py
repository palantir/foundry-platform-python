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

from foundry.v2.connectivity.models._agent_rid import AgentRid
from foundry.v2.connectivity.models._agent_worker_runtime_dict import AgentWorkerRuntimeDict  # NOQA


class AgentWorkerRuntime(pydantic.BaseModel):
    """
    The [agent worker runtime](/docs/foundry/data-connection/core-concepts/#agent-worker-runtime) is used to
    connect to data sources not accessible over the Internet. An agent worker should only be used when the desired
    connector does not support the agent proxy runtime. Agent worker runtimes are associated with a single or
    multiple agents that store the source configuration and credentials locally in an encrypted format,
    and run source capabilities on the agent itself.
    """

    agent_rids: List[AgentRid] = pydantic.Field(alias="agentRids")
    """
    The RIDs of the [agents](/docs/foundry/data-connection/set-up-agent/) configured on the connection.
    These agents are used to provide network connectivity to the external systems or APIs configured on the
    connection.
    """

    type: Literal["agentWorkerRuntime"] = "agentWorkerRuntime"

    model_config = {"extra": "allow"}

    def to_dict(self) -> AgentWorkerRuntimeDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(AgentWorkerRuntimeDict, self.model_dump(by_alias=True, exclude_unset=True))
