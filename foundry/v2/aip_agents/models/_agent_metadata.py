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

    display_name: str = pydantic.Field(alias=str("displayName"))  # type: ignore[literal-required]

    """The name of the Agent."""

    description: Optional[str] = None

    """The description for the Agent."""

    input_placeholder: Optional[str] = pydantic.Field(alias=str("inputPlaceholder"), default=None)  # type: ignore[literal-required]

    """The default text to show as the placeholder input for chats with the Agent."""

    suggested_prompts: List[str] = pydantic.Field(alias=str("suggestedPrompts"))  # type: ignore[literal-required]

    """Prompts to show to the user as example messages to start a conversation with the Agent."""

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> AgentMetadataDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(AgentMetadataDict, self.model_dump(by_alias=True, exclude_none=True))
