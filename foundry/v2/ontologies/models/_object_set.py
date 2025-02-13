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
from typing import cast

import pydantic
from typing_extensions import Annotated

from foundry.v2.ontologies.models._derived_property_api_name import DerivedPropertyApiName  # NOQA
from foundry.v2.ontologies.models._link_type_api_name import LinkTypeApiName
from foundry.v2.ontologies.models._nearest_neighbors_query import NearestNeighborsQuery
from foundry.v2.ontologies.models._object_set_base_type import ObjectSetBaseType
from foundry.v2.ontologies.models._object_set_dict import ObjectSetAsBaseObjectTypesTypeDict  # NOQA
from foundry.v2.ontologies.models._object_set_dict import ObjectSetAsTypeTypeDict
from foundry.v2.ontologies.models._object_set_dict import ObjectSetFilterTypeDict
from foundry.v2.ontologies.models._object_set_dict import ObjectSetIntersectionTypeDict
from foundry.v2.ontologies.models._object_set_dict import ObjectSetNearestNeighborsTypeDict  # NOQA
from foundry.v2.ontologies.models._object_set_dict import ObjectSetSearchAroundTypeDict
from foundry.v2.ontologies.models._object_set_dict import ObjectSetSubtractTypeDict
from foundry.v2.ontologies.models._object_set_dict import ObjectSetUnionTypeDict
from foundry.v2.ontologies.models._object_set_dict import ObjectSetWithPropertiesTypeDict  # NOQA
from foundry.v2.ontologies.models._object_set_dict import SelectedPropertyDefinitionDict
from foundry.v2.ontologies.models._object_set_interface_base_type import (
    ObjectSetInterfaceBaseType,
)  # NOQA
from foundry.v2.ontologies.models._object_set_method_input_type import (
    ObjectSetMethodInputType,
)  # NOQA
from foundry.v2.ontologies.models._object_set_reference_type import ObjectSetReferenceType  # NOQA
from foundry.v2.ontologies.models._object_set_static_type import ObjectSetStaticType
from foundry.v2.ontologies.models._property_identifier import PropertyIdentifier
from foundry.v2.ontologies.models._search_json_query_v2 import SearchJsonQueryV2
from foundry.v2.ontologies.models._selected_property_operation import (
    SelectedPropertyOperation,
)  # NOQA


class ObjectSetSearchAroundType(pydantic.BaseModel):
    """ObjectSetSearchAroundType"""

    object_set: ObjectSet = pydantic.Field(alias=str("objectSet"))  # type: ignore[literal-required]

    link: LinkTypeApiName

    type: Literal["searchAround"] = "searchAround"

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> ObjectSetSearchAroundTypeDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(
            ObjectSetSearchAroundTypeDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class ObjectSetIntersectionType(pydantic.BaseModel):
    """ObjectSetIntersectionType"""

    object_sets: List[ObjectSet] = pydantic.Field(alias=str("objectSets"))  # type: ignore[literal-required]

    type: Literal["intersect"] = "intersect"

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> ObjectSetIntersectionTypeDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(
            ObjectSetIntersectionTypeDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class ObjectSetWithPropertiesType(pydantic.BaseModel):
    """
    ObjectSet which returns objects with additional derived properties.

    This feature is experimental and not yet generally available.
    """

    object_set: ObjectSet = pydantic.Field(alias=str("objectSet"))  # type: ignore[literal-required]

    derived_properties: Dict[DerivedPropertyApiName, DerivedPropertyDefinition] = pydantic.Field(alias=str("derivedProperties"))  # type: ignore[literal-required]

    """Map of the name of the derived property to return and its definition"""

    type: Literal["withProperties"] = "withProperties"

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> ObjectSetWithPropertiesTypeDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(
            ObjectSetWithPropertiesTypeDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class SelectedPropertyDefinition(pydantic.BaseModel):
    """Definition for a selected property over a MethodObjectSet."""

    object_set: MethodObjectSet = pydantic.Field(alias=str("objectSet"))  # type: ignore[literal-required]

    operation: SelectedPropertyOperation

    type: Literal["selection"] = "selection"

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> SelectedPropertyDefinitionDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(
            SelectedPropertyDefinitionDict, self.model_dump(by_alias=True, exclude_none=True)
        )


DerivedPropertyDefinition = SelectedPropertyDefinition
"""Definition of a derived property."""


class ObjectSetSubtractType(pydantic.BaseModel):
    """ObjectSetSubtractType"""

    object_sets: List[ObjectSet] = pydantic.Field(alias=str("objectSets"))  # type: ignore[literal-required]

    type: Literal["subtract"] = "subtract"

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> ObjectSetSubtractTypeDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(ObjectSetSubtractTypeDict, self.model_dump(by_alias=True, exclude_none=True))


class ObjectSetNearestNeighborsType(pydantic.BaseModel):
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

    object_set: ObjectSet = pydantic.Field(alias=str("objectSet"))  # type: ignore[literal-required]

    property_identifier: PropertyIdentifier = pydantic.Field(alias=str("propertyIdentifier"))  # type: ignore[literal-required]

    num_neighbors: int = pydantic.Field(alias=str("numNeighbors"))  # type: ignore[literal-required]

    """
    The number of objects to return. If the number of documents in the objectType is less than the provided
    value, all objects will be returned. This value is limited to 1 &lt;= numNeighbors &lt;= 500.
    """

    query: NearestNeighborsQuery

    type: Literal["nearestNeighbors"] = "nearestNeighbors"

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> ObjectSetNearestNeighborsTypeDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(
            ObjectSetNearestNeighborsTypeDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class ObjectSetUnionType(pydantic.BaseModel):
    """ObjectSetUnionType"""

    object_sets: List[ObjectSet] = pydantic.Field(alias=str("objectSets"))  # type: ignore[literal-required]

    type: Literal["union"] = "union"

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> ObjectSetUnionTypeDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(ObjectSetUnionTypeDict, self.model_dump(by_alias=True, exclude_none=True))


class ObjectSetAsTypeType(pydantic.BaseModel):
    """
    Casts an object set to a specified object type or interface type API name. Any object whose object type does
    not match the object type provided or implement the interface type provided will be dropped from the resulting
    object set. This is currently unsupported and an exception will be thrown if used.
    """

    entity_type: str = pydantic.Field(alias=str("entityType"))  # type: ignore[literal-required]

    """An object type or interface type API name."""

    object_set: ObjectSet = pydantic.Field(alias=str("objectSet"))  # type: ignore[literal-required]

    type: Literal["asType"] = "asType"

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> ObjectSetAsTypeTypeDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(ObjectSetAsTypeTypeDict, self.model_dump(by_alias=True, exclude_none=True))


class ObjectSetFilterType(pydantic.BaseModel):
    """ObjectSetFilterType"""

    object_set: ObjectSet = pydantic.Field(alias=str("objectSet"))  # type: ignore[literal-required]

    where: SearchJsonQueryV2

    type: Literal["filter"] = "filter"

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> ObjectSetFilterTypeDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(ObjectSetFilterTypeDict, self.model_dump(by_alias=True, exclude_none=True))


class ObjectSetAsBaseObjectTypesType(pydantic.BaseModel):
    """
    Casts the objects in the object set to their base type and thus ensures objects are returned with all of their
    properties in the resulting object set, not just the properties that implement interface properties. This is
    currently unsupported and an exception will be thrown if used.
    """

    object_set: ObjectSet = pydantic.Field(alias=str("objectSet"))  # type: ignore[literal-required]

    type: Literal["asBaseObjectTypes"] = "asBaseObjectTypes"

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> ObjectSetAsBaseObjectTypesTypeDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(
            ObjectSetAsBaseObjectTypesTypeDict, self.model_dump(by_alias=True, exclude_none=True)
        )


ObjectSet = Annotated[
    Union[
        ObjectSetSearchAroundType,
        ObjectSetStaticType,
        ObjectSetIntersectionType,
        ObjectSetWithPropertiesType,
        ObjectSetSubtractType,
        ObjectSetNearestNeighborsType,
        ObjectSetUnionType,
        ObjectSetAsTypeType,
        ObjectSetMethodInputType,
        ObjectSetReferenceType,
        ObjectSetFilterType,
        ObjectSetInterfaceBaseType,
        ObjectSetAsBaseObjectTypesType,
        ObjectSetBaseType,
    ],
    pydantic.Field(discriminator="type"),
]
"""Represents the definition of an `ObjectSet` in the `Ontology`."""


MethodObjectSet = ObjectSet
"""MethodObjectSet"""
