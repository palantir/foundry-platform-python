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

from typing import cast

import pydantic

from foundry.v2.aip_agents.models._agent_version_details import AgentVersionDetails
from foundry.v2.aip_agents.models._agent_version_dict import AgentVersionDict
from foundry.v2.aip_agents.models._agent_version_string import AgentVersionString


class AgentVersion(pydantic.BaseModel):
    """AgentVersion"""

    string: AgentVersionString
    """The semantic version of the Agent, formatted as "<majorVersion>.<minorVersion>"."""

    version: AgentVersionDetails
    """Semantic version details of the Agent."""

    model_config = {"extra": "allow"}

    def to_dict(self) -> AgentVersionDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(AgentVersionDict, self.model_dump(by_alias=True, exclude_unset=True))
