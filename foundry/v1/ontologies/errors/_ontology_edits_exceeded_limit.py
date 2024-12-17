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


class OntologyEditsExceededLimitParameters(TypedDict):
    """
    The number of edits to the Ontology exceeded the allowed limit.
    This may happen because of the request or because the Action is modifying too many objects.
    Please change the size of your request or contact the Ontology administrator.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    editsCount: int

    editsLimit: int


@dataclass
class OntologyEditsExceededLimit(PalantirRPCException):
    name: Literal["OntologyEditsExceededLimit"]
    parameters: OntologyEditsExceededLimitParameters
    error_instance_id: str


__all__ = ["OntologyEditsExceededLimit"]
