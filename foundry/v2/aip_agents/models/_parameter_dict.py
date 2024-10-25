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

import pydantic
from typing_extensions import NotRequired
from typing_extensions import TypedDict

from foundry.v2.aip_agents.models._parameter_access_mode import ParameterAccessMode
from foundry.v2.aip_agents.models._parameter_type_dict import ParameterTypeDict


class ParameterDict(TypedDict):
    """A parameter configured for an Agent in AIP Agent Studio."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    parameterType: ParameterTypeDict
    """Details of the types of values accepted and defaults for this parameter."""

    access: ParameterAccessMode
    """The access mode controls how the Agent is able to interact with the parameter."""

    description: NotRequired[pydantic.StrictStr]
    """
    A description to explain the use of this parameter. This description is injected with the
    parameter value into the Agent's prompt, to provide context for when to use the parameter.
    """
