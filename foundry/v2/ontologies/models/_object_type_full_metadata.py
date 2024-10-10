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
from typing import cast

import pydantic

from foundry.v2.ontologies.models._interface_type_api_name import InterfaceTypeApiName
from foundry.v2.ontologies.models._link_type_side_v2 import LinkTypeSideV2
from foundry.v2.ontologies.models._object_type_full_metadata_dict import (
    ObjectTypeFullMetadataDict,
)  # NOQA
from foundry.v2.ontologies.models._object_type_interface_implementation import (
    ObjectTypeInterfaceImplementation,
)  # NOQA
from foundry.v2.ontologies.models._object_type_v2 import ObjectTypeV2
from foundry.v2.ontologies.models._property_api_name import PropertyApiName
from foundry.v2.ontologies.models._shared_property_type_api_name import (
    SharedPropertyTypeApiName,
)  # NOQA


class ObjectTypeFullMetadata(pydantic.BaseModel):
    """ObjectTypeFullMetadata"""

    object_type: ObjectTypeV2 = pydantic.Field(alias="objectType")

    link_types: List[LinkTypeSideV2] = pydantic.Field(alias="linkTypes")

    implements_interfaces: List[InterfaceTypeApiName] = pydantic.Field(alias="implementsInterfaces")
    """A list of interfaces that this object type implements."""

    implements_interfaces2: Dict[InterfaceTypeApiName, ObjectTypeInterfaceImplementation] = (
        pydantic.Field(alias="implementsInterfaces2")
    )
    """A list of interfaces that this object type implements and how it implements them."""

    shared_property_type_mapping: Dict[SharedPropertyTypeApiName, PropertyApiName] = pydantic.Field(
        alias="sharedPropertyTypeMapping"
    )
    """
    A map from shared property type API name to backing local property API name for the shared property types 
    present on this object type.
    """

    model_config = {"extra": "allow"}

    def to_dict(self) -> ObjectTypeFullMetadataDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(ObjectTypeFullMetadataDict, self.model_dump(by_alias=True, exclude_unset=True))
