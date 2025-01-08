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

from typing import Dict
from typing import cast

import pydantic

from foundry.v2.aip_agents.models._agent_dict import AgentDict
from foundry.v2.aip_agents.models._agent_metadata import AgentMetadata
from foundry.v2.aip_agents.models._agent_rid import AgentRid
from foundry.v2.aip_agents.models._agent_version_string import AgentVersionString
from foundry.v2.aip_agents.models._parameter import Parameter
from foundry.v2.aip_agents.models._parameter_id import ParameterId


class Agent(pydantic.BaseModel):
    """Agent"""

    rid: AgentRid

    """An RID identifying an AIP Agent created in [AIP Agent Studio](/docs/foundry/agent-studio/overview/)."""

    version: AgentVersionString

    """The version of this instance of the Agent."""

    metadata: AgentMetadata

    parameters: Dict[ParameterId, Parameter]

    """
    The types and names of variables configured for the Agent in [AIP Agent Studio](/docs/foundry/agent-studio/overview/) in the [application state](/docs/foundry/agent-studio/application-state/).
    These variables can be used to send custom values in prompts sent to an Agent to customize and control the Agent's behavior.
    """

    model_config = {"extra": "allow"}

    def to_dict(self) -> AgentDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(AgentDict, self.model_dump(by_alias=True, exclude_unset=True))
