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
from typing import cast

import pydantic

from foundry.v2.aip_agents.models._agent_session_rag_context_response_dict import (
    AgentSessionRagContextResponseDict,
)  # NOQA
from foundry.v2.aip_agents.models._function_retrieved_context import (
    FunctionRetrievedContext,
)  # NOQA
from foundry.v2.aip_agents.models._object_context import ObjectContext


class AgentSessionRagContextResponse(pydantic.BaseModel):
    """Context retrieved from an Agent's configured context data sources which was relevant to the supplied user message."""

    object_contexts: List[ObjectContext] = pydantic.Field(alias=str("objectContexts"))  # type: ignore[literal-required]

    function_retrieved_contexts: List[FunctionRetrievedContext] = pydantic.Field(alias=str("functionRetrievedContexts"))  # type: ignore[literal-required]

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> AgentSessionRagContextResponseDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(
            AgentSessionRagContextResponseDict, self.model_dump(by_alias=True, exclude_none=True)
        )
