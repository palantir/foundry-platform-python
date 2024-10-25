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

from typing import Optional
from typing import cast

import pydantic

from foundry.v2.aip_agents.models._session_exchange_contexts import SessionExchangeContexts  # NOQA
from foundry.v2.aip_agents.models._session_exchange_dict import SessionExchangeDict
from foundry.v2.aip_agents.models._session_exchange_result import SessionExchangeResult
from foundry.v2.aip_agents.models._user_text_input import UserTextInput


class SessionExchange(pydantic.BaseModel):
    """Represents an individual exchange between a user and an Agent in a conversation session."""

    user_input: UserTextInput = pydantic.Field(alias="userInput")
    """The user message that initiated the exchange."""

    contexts: Optional[SessionExchangeContexts] = None
    """
    Additional retrieved context which was included in the prompt to the Agent. This may include
    context which was passed by the client with the user input, or relevant context
    which was automatically retrieved and added based on available data sources configured on the Agent.
    Empty if no additional context was included in the prompt.
    """

    result: SessionExchangeResult
    """The final result for the exchange."""

    model_config = {"extra": "allow"}

    def to_dict(self) -> SessionExchangeDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(SessionExchangeDict, self.model_dump(by_alias=True, exclude_unset=True))
