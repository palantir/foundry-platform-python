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

from foundry.v2.ontologies.models._property_api_name import PropertyApiName
from foundry.v2.ontologies.models._struct_field_api_name import StructFieldApiName


class StructFieldSelectorDict(TypedDict):
    """
    A combination of a struct property api name and a struct field api name. This is used to select struct fields
    to query on. Note that you can still select struct properties with only a 'PropertyApiNameSelector'; the queries
    will then become 'OR' queries across the fields of the struct property.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    propertyApiName: PropertyApiName

    structFieldApiName: StructFieldApiName

    type: Literal["structField"]
