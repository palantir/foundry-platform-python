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

from typing import Dict

from typing_extensions import TypedDict

from foundry.v2.ontologies.models._derived_property_api_name import DerivedPropertyApiName  # NOQA
from foundry.v2.ontologies.models._derived_property_definition_dict import (
    DerivedPropertyDefinitionDict,
)  # NOQA
from foundry.v2.ontologies.models._object_set_dict import ObjectSetDict


class ObjectSetWithPropertiesTypeDict(TypedDict):
    """
    ObjectSet which returns objects with additional derived properties.

    This feature is experimental and not yet generally available.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    objectSet: ObjectSetDict

    derivedProperties: Dict[DerivedPropertyApiName, DerivedPropertyDefinitionDict]
    """Map of the name of the derived property to return and its definition"""
