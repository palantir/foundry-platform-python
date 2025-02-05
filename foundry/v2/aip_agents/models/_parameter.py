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

from foundry.v2.aip_agents.models._parameter_access_mode import ParameterAccessMode
from foundry.v2.aip_agents.models._parameter_dict import ParameterDict
from foundry.v2.aip_agents.models._parameter_type import ParameterType


class Parameter(pydantic.BaseModel):
    """A variable configured in the application state of an Agent in [AIP Agent Studio](/docs/foundry/agent-studio/overview/)."""

    parameter_type: ParameterType = pydantic.Field(alias=str("parameterType"))  # type: ignore[literal-required]

    """Details of the types of values accepted and defaults for this variable."""

    access: ParameterAccessMode

    """The access mode controls how the Agent is able to interact with the variable."""

    description: Optional[str] = None

    """
    A description to explain the use of this variable.
    This description is injected into the Agent's prompt to provide context for when to use the variable.
    """

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> ParameterDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(ParameterDict, self.model_dump(by_alias=True, exclude_none=True))
