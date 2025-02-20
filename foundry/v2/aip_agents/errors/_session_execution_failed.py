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

from typing_extensions import TypedDict

from foundry._errors import InternalServerError
from foundry.v2.aip_agents.models._agent_rid import AgentRid
from foundry.v2.aip_agents.models._session_rid import SessionRid


class SessionExecutionFailedParameters(TypedDict):
    """Failed to generate a response for a session due to an unexpected error."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    agentRid: AgentRid

    sessionRid: SessionRid

    message: str
    """The error message."""
    details: str
    """Any additional details provided for the error."""


@dataclass
class SessionExecutionFailed(InternalServerError):
    name: Literal["SessionExecutionFailed"]
    parameters: SessionExecutionFailedParameters
    error_instance_id: str


__all__ = ["SessionExecutionFailed"]
