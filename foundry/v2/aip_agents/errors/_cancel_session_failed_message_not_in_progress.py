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

from dataclasses import dataclass
from typing import Literal

import pydantic
from typing_extensions import TypedDict

from foundry._errors import PalantirRPCException
from foundry.v2.aip_agents.models._agent_rid import AgentRid
from foundry.v2.aip_agents.models._message_id import MessageId
from foundry.v2.aip_agents.models._session_rid import SessionRid


class CancelSessionFailedMessageNotInProgressParameters(TypedDict):
    """
    Unable to cancel the requested session exchange as no in-progress exchange was found
    for the provided message identifier.
    This is expected if no exchange was initiated with the provided message identifier
    through a `streamingContinue` request, or if the exchange for this identifier has already completed
    and cannot be canceled, or if the exchange has already been canceled.
    This error can also occur if the cancellation was requested immediately after requesting the exchange
    through a `streamingContinue` request, and the exchange has not started yet.
    Clients should handle these errors gracefully, and can reload the session content to get the latest
    conversation state.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    messageId: MessageId
    """The message identifier that was requested for cancellation."""

    agentRid: AgentRid

    sessionRid: SessionRid


@dataclass
class CancelSessionFailedMessageNotInProgress(PalantirRPCException):
    name: Literal["CancelSessionFailedMessageNotInProgress"]
    parameters: CancelSessionFailedMessageNotInProgressParameters
    error_instance_id: str


__all__ = ["CancelSessionFailedMessageNotInProgress"]
