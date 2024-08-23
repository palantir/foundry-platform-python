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
from typing import List

from typing_extensions import TypedDict

from foundry.v2.models._interface_type_api_name import InterfaceTypeApiName
from foundry.v2.models._link_type_side_v2_dict import LinkTypeSideV2Dict
from foundry.v2.models._object_type_interface_implementation_dict import (
    ObjectTypeInterfaceImplementationDict,
)  # NOQA
from foundry.v2.models._object_type_v2_dict import ObjectTypeV2Dict
from foundry.v2.models._property_api_name import PropertyApiName
from foundry.v2.models._shared_property_type_api_name import SharedPropertyTypeApiName


class ObjectTypeFullMetadataDict(TypedDict):
    """ObjectTypeFullMetadata"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    objectType: ObjectTypeV2Dict

    linkTypes: List[LinkTypeSideV2Dict]

    implementsInterfaces: List[InterfaceTypeApiName]
    """A list of interfaces that this object type implements."""

    implementsInterfaces2: Dict[InterfaceTypeApiName, ObjectTypeInterfaceImplementationDict]
    """A list of interfaces that this object type implements and how it implements them."""

    sharedPropertyTypeMapping: Dict[SharedPropertyTypeApiName, PropertyApiName]
    """
    A map from shared property type API name to backing local property API name for the shared property types 
    present on this object type.
    """
