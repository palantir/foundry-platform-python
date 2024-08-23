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

from foundry.v1.models._interface_type_api_name import InterfaceTypeApiName
from foundry.v1.models._object_type_api_name import ObjectTypeApiName
from foundry.v1.models._page_size import PageSize
from foundry.v1.models._page_token import PageToken
from foundry.v1.models._property_api_name import PropertyApiName
from foundry.v1.models._search_json_query_v2_dict import SearchJsonQueryV2Dict
from foundry.v1.models._search_order_by_v2_dict import SearchOrderByV2Dict
from foundry.v1.models._shared_property_type_api_name import SharedPropertyTypeApiName


class SearchObjectsForInterfaceRequestDict(TypedDict):
    """SearchObjectsForInterfaceRequest"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    where: NotRequired[SearchJsonQueryV2Dict]

    orderBy: NotRequired[SearchOrderByV2Dict]

    augmentedProperties: Dict[ObjectTypeApiName, List[PropertyApiName]]
    """
    A map from object type API name to a list of property type API names. For each returned object, if the 
    object’s object type is a key in the map, then we augment the response for that object type with the list 
    of properties specified in the value.
    """

    augmentedSharedPropertyTypes: Dict[InterfaceTypeApiName, List[SharedPropertyTypeApiName]]
    """
    A map from interface type API name to a list of shared property type API names. For each returned object, if
    the object implements an interface that is a key in the map, then we augment the response for that object 
    type with the list of properties specified in the value.
    """

    selectedSharedPropertyTypes: List[SharedPropertyTypeApiName]
    """
    A list of shared property type API names of the interface type that should be included in the response. 
    Omit this parameter to include all properties of the interface type in the response.
    """

    selectedObjectTypes: List[ObjectTypeApiName]
    """
    A list of object type API names that should be included in the response. If non-empty, object types that are
    not mentioned will not be included in the response even if they implement the specified interface. Omit the 
    parameter to include all object types.
    """

    otherInterfaceTypes: List[InterfaceTypeApiName]
    """
    A list of interface type API names. Object types must implement all the mentioned interfaces in order to be 
    included in the response.
    """

    pageSize: NotRequired[PageSize]

    pageToken: NotRequired[PageToken]
