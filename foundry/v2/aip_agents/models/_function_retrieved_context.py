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

from typing import Literal
from typing import cast

import pydantic

from foundry.v2.aip_agents.models._function_retrieved_context_dict import (
    FunctionRetrievedContextDict,
)  # NOQA
from foundry.v2.functions.models._function_rid import FunctionRid
from foundry.v2.functions.models._function_version import FunctionVersion


class FunctionRetrievedContext(pydantic.BaseModel):
    """Context retrieved from running a function to include as additional context in the prompt to the Agent."""

    function_rid: FunctionRid = pydantic.Field(alias=str("functionRid"))  # type: ignore[literal-required]

    function_version: FunctionVersion = pydantic.Field(alias=str("functionVersion"))  # type: ignore[literal-required]

    retrieved_prompt: str = pydantic.Field(alias=str("retrievedPrompt"))  # type: ignore[literal-required]

    """String content returned from a context retrieval function."""

    type: Literal["functionRetrievedContext"] = "functionRetrievedContext"

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> FunctionRetrievedContextDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(FunctionRetrievedContextDict, self.model_dump(by_alias=True, exclude_none=True))
