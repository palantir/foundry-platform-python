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

from foundry.v2.aip_agents.models._agent_metadata_dict import AgentMetadataDict


class AgentMetadata(pydantic.BaseModel):
    """Metadata for an Agent."""

    display_name: pydantic.StrictStr = pydantic.Field(alias="displayName")
    """The name of the Agent."""

    description: Optional[pydantic.StrictStr] = None
    """The description for the Agent."""

    input_placeholder: Optional[pydantic.StrictStr] = pydantic.Field(
        alias="inputPlaceholder", default=None
    )
    """The default text to show as the placeholder input for chats with the Agent."""

    suggested_prompts: List[pydantic.StrictStr] = pydantic.Field(alias="suggestedPrompts")
    """Prompts to show to the user as example messages to start a conversation with the Agent."""

    model_config = {"extra": "allow"}

    def to_dict(self) -> AgentMetadataDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(AgentMetadataDict, self.model_dump(by_alias=True, exclude_unset=True))
