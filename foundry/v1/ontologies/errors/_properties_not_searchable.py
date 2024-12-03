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
from typing import List
from typing import Literal

import pydantic
from typing_extensions import TypedDict

from foundry._errors import PalantirRPCException
from foundry.v1.ontologies.models._property_api_name import PropertyApiName


class PropertiesNotSearchableParameters(TypedDict):
    """
    Search is not enabled on the specified properties. Please mark the properties as *Searchable*
    in the **Ontology Manager** to enable search on them. There may be a short delay
    between the time a property is marked *Searchable* and when it can be used.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    propertyApiNames: List[PropertyApiName]


@dataclass
class PropertiesNotSearchable(PalantirRPCException):
    name: Literal["PropertiesNotSearchable"]
    parameters: PropertiesNotSearchableParameters
    error_instance_id: str


__all__ = ["PropertiesNotSearchable"]
