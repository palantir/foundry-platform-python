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

from typing_extensions import NotRequired
from typing_extensions import TypedDict

from foundry.v2.aip_agents.models._session_exchange_contexts_dict import (
    SessionExchangeContextsDict,
)  # NOQA
from foundry.v2.aip_agents.models._session_exchange_result_dict import (
    SessionExchangeResultDict,
)  # NOQA
from foundry.v2.aip_agents.models._user_text_input_dict import UserTextInputDict


class SessionExchangeDict(TypedDict):
    """Represents an individual exchange between a user and an Agent in a conversation session."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    userInput: UserTextInputDict
    """The user message that initiated the exchange."""

    contexts: NotRequired[SessionExchangeContextsDict]
    """
    Additional retrieved context which was included in the prompt to the Agent. This may include
    context which was passed by the client with the user input, or relevant context
    which was automatically retrieved and added based on available data sources configured on the Agent.
    Empty if no additional context was included in the prompt.
    """

    result: SessionExchangeResultDict
    """The final result for the exchange."""
