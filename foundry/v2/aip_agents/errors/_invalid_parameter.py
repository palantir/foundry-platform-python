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


import typing
from dataclasses import dataclass

import typing_extensions

from foundry import _errors as errors
from foundry.v2.aip_agents import models as aip_agents_models


class InvalidParameterParameters(typing_extensions.TypedDict):
    """
    The provided application variable is not valid for the Agent for this session.
    Check the available application variables for the Agent under the `parameters` property, and version through the API with `getAgent`, or in AIP Agent Studio.
    The Agent version used for the session can be checked through the API with `getSession`.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    agentRid: aip_agents_models.AgentRid
    sessionRid: aip_agents_models.SessionRid
    parameter: aip_agents_models.ParameterId


@dataclass
class InvalidParameter(errors.BadRequestError):
    name: typing.Literal["InvalidParameter"]
    parameters: InvalidParameterParameters
    error_instance_id: str


__all__ = ["InvalidParameter"]
