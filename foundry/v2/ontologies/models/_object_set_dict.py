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
from typing import Literal
from typing import Union

import pydantic
from typing_extensions import Annotated
from typing_extensions import TypedDict

from foundry.v2.ontologies.models._derived_property_api_name import DerivedPropertyApiName  # NOQA
from foundry.v2.ontologies.models._link_type_api_name import LinkTypeApiName
from foundry.v2.ontologies.models._nearest_neighbors_query_dict import (
    NearestNeighborsQueryDict,
)  # NOQA
from foundry.v2.ontologies.models._object_set_base_type_dict import ObjectSetBaseTypeDict  # NOQA
from foundry.v2.ontologies.models._object_set_interface_base_type_dict import (
    ObjectSetInterfaceBaseTypeDict,
)  # NOQA
from foundry.v2.ontologies.models._object_set_method_input_type_dict import (
    ObjectSetMethodInputTypeDict,
)  # NOQA
from foundry.v2.ontologies.models._object_set_reference_type_dict import (
    ObjectSetReferenceTypeDict,
)  # NOQA
from foundry.v2.ontologies.models._object_set_static_type_dict import (
    ObjectSetStaticTypeDict,
)  # NOQA
from foundry.v2.ontologies.models._property_identifier_dict import PropertyIdentifierDict  # NOQA
from foundry.v2.ontologies.models._search_json_query_v2_dict import SearchJsonQueryV2Dict  # NOQA
from foundry.v2.ontologies.models._selected_property_operation_dict import (
    SelectedPropertyOperationDict,
)  # NOQA


class ObjectSetSearchAroundTypeDict(TypedDict):
    """ObjectSetSearchAroundType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    objectSet: ObjectSetDict

    link: LinkTypeApiName

    type: Literal["searchAround"]


class ObjectSetIntersectionTypeDict(TypedDict):
    """ObjectSetIntersectionType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    objectSets: List[ObjectSetDict]

    type: Literal["intersect"]


class ObjectSetWithPropertiesTypeDict(TypedDict):
    """
    ObjectSet which returns objects with additional derived properties.

    This feature is experimental and not yet generally available.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    objectSet: ObjectSetDict

    derivedProperties: Dict[DerivedPropertyApiName, DerivedPropertyDefinitionDict]
    """Map of the name of the derived property to return and its definition"""

    type: Literal["withProperties"]


class SelectedPropertyDefinitionDict(TypedDict):
    """Definition for a selected property over a MethodObjectSet."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    objectSet: MethodObjectSetDict

    operation: SelectedPropertyOperationDict

    type: Literal["selection"]


DerivedPropertyDefinitionDict = SelectedPropertyDefinitionDict
"""Definition of a derived property."""


class ObjectSetSubtractTypeDict(TypedDict):
    """ObjectSetSubtractType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    objectSets: List[ObjectSetDict]

    type: Literal["subtract"]


class ObjectSetNearestNeighborsTypeDict(TypedDict):
    """
    ObjectSet containing the top `numNeighbors` objects with `propertyIdentifier` nearest to the input vector or
    text. This can only be performed on a property with type vector that has been configured to be searched with
    approximate nearest neighbors using a similarity function configured in the Ontology.

    A non-zero score for each resulting object is returned when the `orderType` in the `orderBy` field is set to
    `relevance`. Note that:
      - Scores will not be returned if a nearestNeighbors object set is composed through union, subtraction
        or intersection with non-nearestNeighbors object sets.
      - If results have scores, the order of the scores will be decreasing (duplicate scores are possible).
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    objectSet: ObjectSetDict

    propertyIdentifier: PropertyIdentifierDict

    numNeighbors: int
    """
    The number of objects to return. If the number of documents in the objectType is less than the provided
    value, all objects will be returned. This value is limited to 1 &lt;= numNeighbors &lt;= 500.
    """

    query: NearestNeighborsQueryDict

    type: Literal["nearestNeighbors"]


class ObjectSetUnionTypeDict(TypedDict):
    """ObjectSetUnionType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    objectSets: List[ObjectSetDict]

    type: Literal["union"]


class ObjectSetAsTypeTypeDict(TypedDict):
    """
    Casts an object set to a specified object type or interface type API name. Any object whose object type does
    not match the object type provided or implement the interface type provided will be dropped from the resulting
    object set. This is currently unsupported and an exception will be thrown if used.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    entityType: str
    """An object type or interface type API name."""

    objectSet: ObjectSetDict

    type: Literal["asType"]


class ObjectSetFilterTypeDict(TypedDict):
    """ObjectSetFilterType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    objectSet: ObjectSetDict

    where: SearchJsonQueryV2Dict

    type: Literal["filter"]


class ObjectSetAsBaseObjectTypesTypeDict(TypedDict):
    """
    Casts the objects in the object set to their base type and thus ensures objects are returned with all of their
    properties in the resulting object set, not just the properties that implement interface properties. This is
    currently unsupported and an exception will be thrown if used.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    objectSet: ObjectSetDict

    type: Literal["asBaseObjectTypes"]


ObjectSetDict = Annotated[
    Union[
        ObjectSetSearchAroundTypeDict,
        ObjectSetStaticTypeDict,
        ObjectSetIntersectionTypeDict,
        ObjectSetWithPropertiesTypeDict,
        ObjectSetSubtractTypeDict,
        ObjectSetNearestNeighborsTypeDict,
        ObjectSetUnionTypeDict,
        ObjectSetAsTypeTypeDict,
        ObjectSetMethodInputTypeDict,
        ObjectSetReferenceTypeDict,
        ObjectSetFilterTypeDict,
        ObjectSetInterfaceBaseTypeDict,
        ObjectSetAsBaseObjectTypesTypeDict,
        ObjectSetBaseTypeDict,
    ],
    pydantic.Field(discriminator="type"),
]
"""Represents the definition of an `ObjectSet` in the `Ontology`."""


MethodObjectSetDict = ObjectSetDict
"""MethodObjectSet"""
