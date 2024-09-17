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

from pydantic import BaseModel
from pydantic import Field
from typing_extensions import Annotated

from foundry.v2.core.models._attachment_type import AttachmentType
from foundry.v2.core.models._boolean_type import BooleanType
from foundry.v2.core.models._date_type import DateType
from foundry.v2.core.models._double_type import DoubleType
from foundry.v2.core.models._float_type import FloatType
from foundry.v2.core.models._integer_type import IntegerType
from foundry.v2.core.models._long_type import LongType
from foundry.v2.core.models._null_type import NullType
from foundry.v2.core.models._string_type import StringType
from foundry.v2.core.models._struct_field_name import StructFieldName
from foundry.v2.core.models._timestamp_type import TimestampType
from foundry.v2.core.models._unsupported_type import UnsupportedType
from foundry.v2.ontologies.models._ontology_object_set_type import OntologyObjectSetType
from foundry.v2.ontologies.models._ontology_object_type import OntologyObjectType
from foundry.v2.ontologies.models._query_array_type_dict import QueryArrayTypeDict
from foundry.v2.ontologies.models._query_set_type_dict import QuerySetTypeDict
from foundry.v2.ontologies.models._query_struct_field_dict import QueryStructFieldDict
from foundry.v2.ontologies.models._query_struct_type_dict import QueryStructTypeDict
from foundry.v2.ontologies.models._query_union_type_dict import QueryUnionTypeDict
from foundry.v2.ontologies.models._three_dimensional_aggregation import (
    ThreeDimensionalAggregation,
)  # NOQA
from foundry.v2.ontologies.models._two_dimensional_aggregation import (
    TwoDimensionalAggregation,
)  # NOQA


class QueryStructField(BaseModel):
    """QueryStructField"""

    name: StructFieldName

    field_type: QueryDataType = Field(alias="fieldType")

    model_config = {"extra": "allow"}

    def to_dict(self) -> QueryStructFieldDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(QueryStructFieldDict, self.model_dump(by_alias=True, exclude_unset=True))


class QueryStructType(BaseModel):
    """QueryStructType"""

    fields: List[QueryStructField]

    type: Literal["struct"]

    model_config = {"extra": "allow"}

    def to_dict(self) -> QueryStructTypeDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(QueryStructTypeDict, self.model_dump(by_alias=True, exclude_unset=True))


class QuerySetType(BaseModel):
    """QuerySetType"""

    sub_type: QueryDataType = Field(alias="subType")

    type: Literal["set"]

    model_config = {"extra": "allow"}

    def to_dict(self) -> QuerySetTypeDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(QuerySetTypeDict, self.model_dump(by_alias=True, exclude_unset=True))


class QueryUnionType(BaseModel):
    """QueryUnionType"""

    union_types: List[QueryDataType] = Field(alias="unionTypes")

    type: Literal["union"]

    model_config = {"extra": "allow"}

    def to_dict(self) -> QueryUnionTypeDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(QueryUnionTypeDict, self.model_dump(by_alias=True, exclude_unset=True))


class QueryArrayType(BaseModel):
    """QueryArrayType"""

    sub_type: QueryDataType = Field(alias="subType")

    type: Literal["array"]

    model_config = {"extra": "allow"}

    def to_dict(self) -> QueryArrayTypeDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(QueryArrayTypeDict, self.model_dump(by_alias=True, exclude_unset=True))


QueryDataType = Annotated[
    Union[
        DateType,
        QueryStructType,
        QuerySetType,
        StringType,
        DoubleType,
        IntegerType,
        ThreeDimensionalAggregation,
        QueryUnionType,
        FloatType,
        LongType,
        BooleanType,
        UnsupportedType,
        AttachmentType,
        NullType,
        QueryArrayType,
        OntologyObjectSetType,
        TwoDimensionalAggregation,
        OntologyObjectType,
        TimestampType,
    ],
    Field(discriminator="type"),
]
"""A union of all the types supported by Ontology Query parameters or outputs."""
