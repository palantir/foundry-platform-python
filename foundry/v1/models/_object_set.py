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

from typing import Annotated
from typing import List
from typing import Literal
from typing import Union
from typing import cast

from pydantic import BaseModel
from pydantic import Field

from foundry.v1.models._link_type_api_name import LinkTypeApiName
from foundry.v1.models._object_set_base_type import ObjectSetBaseType
from foundry.v1.models._object_set_dict import ObjectSetFilterTypeDict
from foundry.v1.models._object_set_dict import ObjectSetIntersectionTypeDict
from foundry.v1.models._object_set_dict import ObjectSetSearchAroundTypeDict
from foundry.v1.models._object_set_dict import ObjectSetSubtractTypeDict
from foundry.v1.models._object_set_dict import ObjectSetUnionTypeDict
from foundry.v1.models._object_set_reference_type import ObjectSetReferenceType
from foundry.v1.models._object_set_static_type import ObjectSetStaticType
from foundry.v1.models._search_json_query_v2 import SearchJsonQueryV2


class ObjectSetFilterType(BaseModel):
    """ObjectSetFilterType"""

    object_set: ObjectSet = Field(alias="objectSet")

    where: SearchJsonQueryV2

    type: Literal["filter"]

    model_config = {"extra": "allow"}

    def to_dict(self) -> ObjectSetFilterTypeDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(ObjectSetFilterTypeDict, self.model_dump(by_alias=True, exclude_unset=True))


class ObjectSetUnionType(BaseModel):
    """ObjectSetUnionType"""

    object_sets: List[ObjectSet] = Field(alias="objectSets")

    type: Literal["union"]

    model_config = {"extra": "allow"}

    def to_dict(self) -> ObjectSetUnionTypeDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(ObjectSetUnionTypeDict, self.model_dump(by_alias=True, exclude_unset=True))


class ObjectSetIntersectionType(BaseModel):
    """ObjectSetIntersectionType"""

    object_sets: List[ObjectSet] = Field(alias="objectSets")

    type: Literal["intersect"]

    model_config = {"extra": "allow"}

    def to_dict(self) -> ObjectSetIntersectionTypeDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(
            ObjectSetIntersectionTypeDict, self.model_dump(by_alias=True, exclude_unset=True)
        )


class ObjectSetSubtractType(BaseModel):
    """ObjectSetSubtractType"""

    object_sets: List[ObjectSet] = Field(alias="objectSets")

    type: Literal["subtract"]

    model_config = {"extra": "allow"}

    def to_dict(self) -> ObjectSetSubtractTypeDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(ObjectSetSubtractTypeDict, self.model_dump(by_alias=True, exclude_unset=True))


class ObjectSetSearchAroundType(BaseModel):
    """ObjectSetSearchAroundType"""

    object_set: ObjectSet = Field(alias="objectSet")

    link: LinkTypeApiName

    type: Literal["searchAround"]

    model_config = {"extra": "allow"}

    def to_dict(self) -> ObjectSetSearchAroundTypeDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(
            ObjectSetSearchAroundTypeDict, self.model_dump(by_alias=True, exclude_unset=True)
        )


ObjectSet = Annotated[
    Union[
        ObjectSetBaseType,
        ObjectSetStaticType,
        ObjectSetReferenceType,
        ObjectSetFilterType,
        ObjectSetUnionType,
        ObjectSetIntersectionType,
        ObjectSetSubtractType,
        ObjectSetSearchAroundType,
    ],
    Field(discriminator="type"),
]
"""Represents the definition of an `ObjectSet` in the `Ontology`."""
