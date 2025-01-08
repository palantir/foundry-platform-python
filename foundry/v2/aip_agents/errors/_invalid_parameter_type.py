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
from foundry.v2.aip_agents.models._parameter_id import ParameterId
from foundry.v2.aip_agents.models._session_rid import SessionRid


class InvalidParameterTypeParameters(TypedDict):
    """
    The provided value does not match the expected type for the application variable configured on the Agent for this session.
    Check the available application variables for the Agent under the `parameters` property, and version through the API with `getAgent`, or in AIP Agent Studio.
    The Agent version used for the session can be checked through the API with `getSession`.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    agentRid: AgentRid

    sessionRid: SessionRid

    parameter: ParameterId

    expectedType: str

    receivedType: str


@dataclass
class InvalidParameterType(PalantirRPCException):
    name: Literal["InvalidParameterType"]
    parameters: InvalidParameterTypeParameters
    error_instance_id: str


__all__ = ["InvalidParameterType"]
