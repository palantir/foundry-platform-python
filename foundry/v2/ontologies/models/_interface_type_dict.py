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

from typing_extensions import NotRequired
from typing_extensions import TypedDict

from foundry.v2.core.models._display_name import DisplayName
from foundry.v2.ontologies.models._interface_link_type_api_name import (
    InterfaceLinkTypeApiName,
)  # NOQA
from foundry.v2.ontologies.models._interface_link_type_dict import InterfaceLinkTypeDict
from foundry.v2.ontologies.models._interface_shared_property_type_dict import (
    InterfaceSharedPropertyTypeDict,
)  # NOQA
from foundry.v2.ontologies.models._interface_type_api_name import InterfaceTypeApiName
from foundry.v2.ontologies.models._interface_type_rid import InterfaceTypeRid
from foundry.v2.ontologies.models._object_type_api_name import ObjectTypeApiName
from foundry.v2.ontologies.models._shared_property_type_api_name import (
    SharedPropertyTypeApiName,
)  # NOQA


class InterfaceTypeDict(TypedDict):
    """Represents an interface type in the Ontology."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    rid: InterfaceTypeRid

    apiName: InterfaceTypeApiName

    displayName: DisplayName

    description: NotRequired[str]
    """The description of the interface."""

    properties: Dict[SharedPropertyTypeApiName, InterfaceSharedPropertyTypeDict]
    """
    A map from a shared property type API name to the corresponding shared property type. The map describes the 
    set of properties the interface has. A shared property type must be unique across all of the properties.
    """

    allProperties: Dict[SharedPropertyTypeApiName, InterfaceSharedPropertyTypeDict]
    """
    A map from a shared property type API name to the corresponding shared property type. The map describes the 
    set of properties the interface has, including properties from all directly and indirectly extended 
    interfaces.
    """

    extendsInterfaces: List[InterfaceTypeApiName]
    """
    A list of interface API names that this interface extends. An interface can extend other interfaces to 
    inherit their properties.
    """

    allExtendsInterfaces: List[InterfaceTypeApiName]
    """A list of interface API names that this interface extends, both directly and indirectly."""

    implementedByObjectTypes: List[ObjectTypeApiName]
    """A list of object API names that implement this interface."""

    links: Dict[InterfaceLinkTypeApiName, InterfaceLinkTypeDict]
    """
    A map from an interface link type API name to the corresponding interface link type. The map describes the
    set of link types the interface has.
    """

    allLinks: Dict[InterfaceLinkTypeApiName, InterfaceLinkTypeDict]
    """
    A map from an interface link type API name to the corresponding interface link type. The map describes the
    set of link types the interface has, including links from all directly and indirectly extended interfaces.
    """
