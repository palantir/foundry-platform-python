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
from typing import Optional
from typing import cast

import pydantic

from foundry.v2.core.models._display_name import DisplayName
from foundry.v2.ontologies.models._interface_link_type import InterfaceLinkType
from foundry.v2.ontologies.models._interface_link_type_api_name import (
    InterfaceLinkTypeApiName,
)  # NOQA
from foundry.v2.ontologies.models._interface_shared_property_type import (
    InterfaceSharedPropertyType,
)  # NOQA
from foundry.v2.ontologies.models._interface_type_api_name import InterfaceTypeApiName
from foundry.v2.ontologies.models._interface_type_dict import InterfaceTypeDict
from foundry.v2.ontologies.models._interface_type_rid import InterfaceTypeRid
from foundry.v2.ontologies.models._object_type_api_name import ObjectTypeApiName
from foundry.v2.ontologies.models._shared_property_type_api_name import (
    SharedPropertyTypeApiName,
)  # NOQA


class InterfaceType(pydantic.BaseModel):
    """Represents an interface type in the Ontology."""

    rid: InterfaceTypeRid

    api_name: InterfaceTypeApiName = pydantic.Field(alias=str("apiName"))  # type: ignore[literal-required]

    display_name: DisplayName = pydantic.Field(alias=str("displayName"))  # type: ignore[literal-required]

    description: Optional[str] = None

    """The description of the interface."""

    properties: Dict[SharedPropertyTypeApiName, InterfaceSharedPropertyType]

    """
    A map from a shared property type API name to the corresponding shared property type. The map describes the 
    set of properties the interface has. A shared property type must be unique across all of the properties.
    """

    all_properties: Dict[SharedPropertyTypeApiName, InterfaceSharedPropertyType] = pydantic.Field(alias=str("allProperties"))  # type: ignore[literal-required]

    """
    A map from a shared property type API name to the corresponding shared property type. The map describes the 
    set of properties the interface has, including properties from all directly and indirectly extended 
    interfaces.
    """

    extends_interfaces: List[InterfaceTypeApiName] = pydantic.Field(alias=str("extendsInterfaces"))  # type: ignore[literal-required]

    """
    A list of interface API names that this interface extends. An interface can extend other interfaces to 
    inherit their properties.
    """

    all_extends_interfaces: List[InterfaceTypeApiName] = pydantic.Field(alias=str("allExtendsInterfaces"))  # type: ignore[literal-required]

    """A list of interface API names that this interface extends, both directly and indirectly."""

    implemented_by_object_types: List[ObjectTypeApiName] = pydantic.Field(alias=str("implementedByObjectTypes"))  # type: ignore[literal-required]

    """A list of object API names that implement this interface."""

    links: Dict[InterfaceLinkTypeApiName, InterfaceLinkType]

    """
    A map from an interface link type API name to the corresponding interface link type. The map describes the
    set of link types the interface has.
    """

    all_links: Dict[InterfaceLinkTypeApiName, InterfaceLinkType] = pydantic.Field(alias=str("allLinks"))  # type: ignore[literal-required]

    """
    A map from an interface link type API name to the corresponding interface link type. The map describes the
    set of link types the interface has, including links from all directly and indirectly extended interfaces.
    """

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> InterfaceTypeDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(InterfaceTypeDict, self.model_dump(by_alias=True, exclude_none=True))
