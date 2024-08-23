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

from foundry.v2.models._interface_type_api_name import InterfaceTypeApiName
from foundry.v2.models._object_type_api_name import ObjectTypeApiName
from foundry.v2.models._page_size import PageSize
from foundry.v2.models._page_token import PageToken
from foundry.v2.models._property_api_name import PropertyApiName
from foundry.v2.models._search_json_query_v2 import SearchJsonQueryV2
from foundry.v2.models._search_objects_for_interface_request_dict import (
    SearchObjectsForInterfaceRequestDict,
)  # NOQA
from foundry.v2.models._search_order_by_v2 import SearchOrderByV2
from foundry.v2.models._shared_property_type_api_name import SharedPropertyTypeApiName


class SearchObjectsForInterfaceRequest(BaseModel):
    """SearchObjectsForInterfaceRequest"""

    where: Optional[SearchJsonQueryV2] = None

    order_by: Optional[SearchOrderByV2] = Field(alias="orderBy", default=None)

    augmented_properties: Dict[ObjectTypeApiName, List[PropertyApiName]] = Field(
        alias="augmentedProperties"
    )
    """
    A map from object type API name to a list of property type API names. For each returned object, if the 
    object’s object type is a key in the map, then we augment the response for that object type with the list 
    of properties specified in the value.
    """

    augmented_shared_property_types: Dict[
        InterfaceTypeApiName, List[SharedPropertyTypeApiName]
    ] = Field(alias="augmentedSharedPropertyTypes")
    """
    A map from interface type API name to a list of shared property type API names. For each returned object, if
    the object implements an interface that is a key in the map, then we augment the response for that object 
    type with the list of properties specified in the value.
    """

    selected_shared_property_types: List[SharedPropertyTypeApiName] = Field(
        alias="selectedSharedPropertyTypes"
    )
    """
    A list of shared property type API names of the interface type that should be included in the response. 
    Omit this parameter to include all properties of the interface type in the response.
    """

    selected_object_types: List[ObjectTypeApiName] = Field(alias="selectedObjectTypes")
    """
    A list of object type API names that should be included in the response. If non-empty, object types that are
    not mentioned will not be included in the response even if they implement the specified interface. Omit the 
    parameter to include all object types.
    """

    other_interface_types: List[InterfaceTypeApiName] = Field(alias="otherInterfaceTypes")
    """
    A list of interface type API names. Object types must implement all the mentioned interfaces in order to be 
    included in the response.
    """

    page_size: Optional[PageSize] = Field(alias="pageSize", default=None)

    page_token: Optional[PageToken] = Field(alias="pageToken", default=None)

    model_config = {"extra": "allow"}

    def to_dict(self) -> SearchObjectsForInterfaceRequestDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(
            SearchObjectsForInterfaceRequestDict, self.model_dump(by_alias=True, exclude_unset=True)
        )
