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

import pydantic
from typing_extensions import NotRequired
from typing_extensions import TypedDict

from foundry.v2.core.models._display_name import DisplayName
from foundry.v2.ontologies.models._interface_link_type_api_name import (
    InterfaceLinkTypeApiName,
)  # NOQA
from foundry.v2.ontologies.models._interface_link_type_dict import InterfaceLinkTypeDict
from foundry.v2.ontologies.models._interface_type_api_name import InterfaceTypeApiName
from foundry.v2.ontologies.models._interface_type_rid import InterfaceTypeRid
from foundry.v2.ontologies.models._shared_property_type_api_name import (
    SharedPropertyTypeApiName,
)  # NOQA
from foundry.v2.ontologies.models._shared_property_type_dict import SharedPropertyTypeDict  # NOQA


class InterfaceTypeDict(TypedDict):
    """Represents an interface type in the Ontology."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    rid: InterfaceTypeRid

    apiName: InterfaceTypeApiName

    displayName: DisplayName

    description: NotRequired[pydantic.StrictStr]
    """The description of the interface."""

    properties: Dict[SharedPropertyTypeApiName, SharedPropertyTypeDict]
    """
    A map from a shared property type API name to the corresponding shared property type. The map describes the 
    set of properties the interface has. A shared property type must be unique across all of the properties.
    """

    extendsInterfaces: List[InterfaceTypeApiName]
    """
    A list of interface API names that this interface extends. An interface can extend other interfaces to 
    inherit their properties.
    """

    links: Dict[InterfaceLinkTypeApiName, InterfaceLinkTypeDict]
    """
    A map from an interface link type API name to the corresponding interface link type. The map describes the
    set of link types the interface has.
    """
