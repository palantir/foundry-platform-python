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
from typing import List
from typing import Literal

import pydantic
from typing_extensions import TypedDict

from foundry._errors import PalantirRPCException
from foundry.v1.ontologies.models._property_api_name import PropertyApiName
from foundry.v1.ontologies.models._property_filter import PropertyFilter


class PropertyTypesSearchNotSupportedParameters(TypedDict):
    """
    The search on the property types are not supported. See the `Search Objects` documentation for
    a list of supported search queries on different property types.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    parameters: Dict[PropertyFilter, List[PropertyApiName]]


@dataclass
class PropertyTypesSearchNotSupported(PalantirRPCException):
    name: Literal["PropertyTypesSearchNotSupported"]
    parameters: PropertyTypesSearchNotSupportedParameters
    error_instance_id: str


__all__ = ["PropertyTypesSearchNotSupported"]
