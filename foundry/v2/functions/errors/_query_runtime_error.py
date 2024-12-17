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
from typing import Dict
from typing import Literal

import pydantic
from typing_extensions import NotRequired
from typing_extensions import TypedDict

from foundry._errors import PalantirRPCException
from foundry.v2.functions.models._function_rid import FunctionRid
from foundry.v2.functions.models._function_version import FunctionVersion
from foundry.v2.functions.models._query_runtime_error_parameter import (
    QueryRuntimeErrorParameter,
)  # NOQA


class QueryRuntimeErrorParameters(TypedDict):
    """The authored `Query` failed to execute because of a runtime error."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    functionRid: FunctionRid

    functionVersion: FunctionVersion

    message: NotRequired[str]

    stacktrace: NotRequired[str]

    parameters: Dict[QueryRuntimeErrorParameter, str]


@dataclass
class QueryRuntimeError(PalantirRPCException):
    name: Literal["QueryRuntimeError"]
    parameters: QueryRuntimeErrorParameters
    error_instance_id: str


__all__ = ["QueryRuntimeError"]
