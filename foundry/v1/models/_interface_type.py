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

from pydantic import BaseModel
from pydantic import Field
from pydantic import StrictStr

from foundry.v1.models._display_name import DisplayName
from foundry.v1.models._interface_link_type import InterfaceLinkType
from foundry.v1.models._interface_link_type_api_name import InterfaceLinkTypeApiName
from foundry.v1.models._interface_type_api_name import InterfaceTypeApiName
from foundry.v1.models._interface_type_dict import InterfaceTypeDict
from foundry.v1.models._interface_type_rid import InterfaceTypeRid
from foundry.v1.models._shared_property_type import SharedPropertyType
from foundry.v1.models._shared_property_type_api_name import SharedPropertyTypeApiName


class InterfaceType(BaseModel):
    """Represents an interface type in the Ontology."""

    rid: InterfaceTypeRid

    api_name: InterfaceTypeApiName = Field(alias="apiName")

    display_name: DisplayName = Field(alias="displayName")

    description: Optional[StrictStr] = None
    """The description of the interface."""

    properties: Dict[SharedPropertyTypeApiName, SharedPropertyType]
    """
    A map from a shared property type API name to the corresponding shared property type. The map describes the 
    set of properties the interface has. A shared property type must be unique across all of the properties.
    """

    extends_interfaces: List[InterfaceTypeApiName] = Field(alias="extendsInterfaces")
    """
    A list of interface API names that this interface extends. An interface can extend other interfaces to 
    inherit their properties.
    """

    links: Dict[InterfaceLinkTypeApiName, InterfaceLinkType]
    """
    A map from an interface link type API name to the corresponding interface link type. The map describes the
    set of link types the interface has.
    """

    model_config = {"extra": "allow"}

    def to_dict(self) -> InterfaceTypeDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(InterfaceTypeDict, self.model_dump(by_alias=True, exclude_unset=True))
