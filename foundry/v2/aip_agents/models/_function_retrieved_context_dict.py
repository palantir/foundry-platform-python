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

from typing_extensions import TypedDict

from foundry.v2.functions.models._function_rid import FunctionRid
from foundry.v2.functions.models._function_version import FunctionVersion


class FunctionRetrievedContextDict(TypedDict):
    """Context retrieved from running a function to include as additional context in the prompt to the Agent."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    functionRid: FunctionRid

    functionVersion: FunctionVersion

    retrievedPrompt: str
    """String content returned from a context retrieval function."""

    type: Literal["functionRetrievedContext"]
