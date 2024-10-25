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

from typing_extensions import TypedDict

from foundry.v2.aip_agents.models._agent_rid import AgentRid
from foundry.v2.aip_agents.models._agent_version_string import AgentVersionString
from foundry.v2.aip_agents.models._session_metadata_dict import SessionMetadataDict
from foundry.v2.aip_agents.models._session_rid import SessionRid


class SessionDict(TypedDict):
    """Session"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    rid: SessionRid
    """The Resource Identifier (RID) of the conversation session."""

    metadata: SessionMetadataDict
    """Metadata about the session."""

    agentRid: AgentRid
    """The Resource Identifier (RID) of the Agent that the session is with."""

    agentVersion: AgentVersionString
    """
    The version of the Agent that the session is with.
    This can be set by clients on session creation. If not specified, defaults to use the latest
    published version of the Agent at session creation time.
    """
