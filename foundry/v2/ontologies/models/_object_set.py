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

from typing import List
from typing import Literal
from typing import Union
from typing import cast

import pydantic
from typing_extensions import Annotated

from foundry.v2.ontologies.models._link_type_api_name import LinkTypeApiName
from foundry.v2.ontologies.models._object_set_as_base_object_types_type_dict import (
    ObjectSetAsBaseObjectTypesTypeDict,
)  # NOQA
from foundry.v2.ontologies.models._object_set_as_type_type_dict import (
    ObjectSetAsTypeTypeDict,
)  # NOQA
from foundry.v2.ontologies.models._object_set_base_type import ObjectSetBaseType
from foundry.v2.ontologies.models._object_set_filter_type_dict import (
    ObjectSetFilterTypeDict,
)  # NOQA
from foundry.v2.ontologies.models._object_set_interface_base_type import (
    ObjectSetInterfaceBaseType,
)  # NOQA
from foundry.v2.ontologies.models._object_set_intersection_type_dict import (
    ObjectSetIntersectionTypeDict,
)  # NOQA
from foundry.v2.ontologies.models._object_set_method_input_type import (
    ObjectSetMethodInputType,
)  # NOQA
from foundry.v2.ontologies.models._object_set_nearest_neighbors_type import (
    ObjectSetNearestNeighborsType,
)  # NOQA
from foundry.v2.ontologies.models._object_set_reference_type import ObjectSetReferenceType  # NOQA
from foundry.v2.ontologies.models._object_set_search_around_type_dict import (
    ObjectSetSearchAroundTypeDict,
)  # NOQA
from foundry.v2.ontologies.models._object_set_static_type import ObjectSetStaticType
from foundry.v2.ontologies.models._object_set_subtract_type_dict import (
    ObjectSetSubtractTypeDict,
)  # NOQA
from foundry.v2.ontologies.models._object_set_union_type_dict import ObjectSetUnionTypeDict  # NOQA
from foundry.v2.ontologies.models._object_set_with_properties_type import (
    ObjectSetWithPropertiesType,
)  # NOQA
from foundry.v2.ontologies.models._search_json_query_v2 import SearchJsonQueryV2


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


class ObjectSetSubtractType(pydantic.BaseModel):
    """ObjectSetSubtractType"""

    object_sets: List[ObjectSet] = pydantic.Field(alias=str("objectSets"))  # type: ignore[literal-required]

    type: Literal["subtract"] = "subtract"

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> ObjectSetSubtractTypeDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(ObjectSetSubtractTypeDict, self.model_dump(by_alias=True, exclude_none=True))


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
    """ObjectSetAsBaseObjectTypesType"""

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
"""Represents the definition of an `ObjectSet` in the ontology."""
