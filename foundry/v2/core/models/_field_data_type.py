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
from typing import Optional
from typing import Union
from typing import cast

import pydantic
from typing_extensions import Annotated

from foundry.v2.core.models._array_field_type_dict import ArrayFieldTypeDict
from foundry.v2.core.models._binary_type import BinaryType
from foundry.v2.core.models._boolean_type import BooleanType
from foundry.v2.core.models._byte_type import ByteType
from foundry.v2.core.models._custom_metadata import CustomMetadata
from foundry.v2.core.models._date_type import DateType
from foundry.v2.core.models._decimal_type import DecimalType
from foundry.v2.core.models._double_type import DoubleType
from foundry.v2.core.models._field_dict import FieldDict
from foundry.v2.core.models._field_name import FieldName
from foundry.v2.core.models._field_schema_dict import FieldSchemaDict
from foundry.v2.core.models._float_type import FloatType
from foundry.v2.core.models._integer_type import IntegerType
from foundry.v2.core.models._long_type import LongType
from foundry.v2.core.models._map_field_type_dict import MapFieldTypeDict
from foundry.v2.core.models._short_type import ShortType
from foundry.v2.core.models._string_type import StringType
from foundry.v2.core.models._struct_field_type_dict import StructFieldTypeDict
from foundry.v2.core.models._timestamp_type import TimestampType


class FieldSchema(pydantic.BaseModel):
    """The specification of the type of a Foundry schema field."""

    nullable: pydantic.StrictBool

    custom_metadata: Optional[CustomMetadata] = pydantic.Field(alias="customMetadata", default=None)

    data_type: FieldDataType = pydantic.Field(alias="dataType")

    model_config = {"extra": "allow"}

    def to_dict(self) -> FieldSchemaDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(FieldSchemaDict, self.model_dump(by_alias=True, exclude_unset=True))


class Field(pydantic.BaseModel):
    """
    A field in a Foundry schema. For more information on supported data types, see the
    [supported field types](/docs/foundry/data-integration/datasets/#supported-field-types) user documentation.
    """

    name: FieldName

    schema_: FieldSchema = pydantic.Field(alias="schema")

    model_config = {"extra": "allow"}

    def to_dict(self) -> FieldDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(FieldDict, self.model_dump(by_alias=True, exclude_unset=True))


class StructFieldType(pydantic.BaseModel):
    """StructFieldType"""

    sub_fields: List[Field] = pydantic.Field(alias="subFields")

    type: Literal["struct"] = "struct"

    model_config = {"extra": "allow"}

    def to_dict(self) -> StructFieldTypeDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(StructFieldTypeDict, self.model_dump(by_alias=True, exclude_unset=True))


class ArrayFieldType(pydantic.BaseModel):
    """ArrayFieldType"""

    items_schema: FieldSchema = pydantic.Field(alias="itemsSchema")

    type: Literal["array"] = "array"

    model_config = {"extra": "allow"}

    def to_dict(self) -> ArrayFieldTypeDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(ArrayFieldTypeDict, self.model_dump(by_alias=True, exclude_unset=True))


class MapFieldType(pydantic.BaseModel):
    """MapFieldType"""

    key_schema: FieldSchema = pydantic.Field(alias="keySchema")

    value_schema: FieldSchema = pydantic.Field(alias="valueSchema")

    type: Literal["map"] = "map"

    model_config = {"extra": "allow"}

    def to_dict(self) -> MapFieldTypeDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(MapFieldTypeDict, self.model_dump(by_alias=True, exclude_unset=True))


FieldDataType = Annotated[
    Union[
        StructFieldType,
        DateType,
        StringType,
        ByteType,
        DoubleType,
        IntegerType,
        FloatType,
        LongType,
        BooleanType,
        ArrayFieldType,
        BinaryType,
        ShortType,
        DecimalType,
        MapFieldType,
        TimestampType,
    ],
    pydantic.Field(discriminator="type"),
]
"""FieldDataType"""
