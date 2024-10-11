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

import pydantic
from typing_extensions import Annotated
from typing_extensions import NotRequired
from typing_extensions import TypedDict

from foundry.v2.core.models._binary_type_dict import BinaryTypeDict
from foundry.v2.core.models._boolean_type_dict import BooleanTypeDict
from foundry.v2.core.models._byte_type_dict import ByteTypeDict
from foundry.v2.core.models._custom_metadata import CustomMetadata
from foundry.v2.core.models._date_type_dict import DateTypeDict
from foundry.v2.core.models._decimal_type_dict import DecimalTypeDict
from foundry.v2.core.models._double_type_dict import DoubleTypeDict
from foundry.v2.core.models._field_name import FieldName
from foundry.v2.core.models._float_type_dict import FloatTypeDict
from foundry.v2.core.models._integer_type_dict import IntegerTypeDict
from foundry.v2.core.models._long_type_dict import LongTypeDict
from foundry.v2.core.models._short_type_dict import ShortTypeDict
from foundry.v2.core.models._string_type_dict import StringTypeDict
from foundry.v2.core.models._timestamp_type_dict import TimestampTypeDict


class FieldSchemaDict(TypedDict):
    """The specification of the type of a Foundry schema field."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    nullable: pydantic.StrictBool

    customMetadata: NotRequired[CustomMetadata]

    dataType: FieldDataTypeDict


class FieldDict(TypedDict):
    """
    A field in a Foundry schema. For more information on supported data types, see the
    [supported field types](/docs/foundry/data-integration/datasets/#supported-field-types) user documentation.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    name: FieldName

    schema: FieldSchemaDict


class StructFieldTypeDict(TypedDict):
    """StructFieldType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    subFields: List[FieldDict]

    type: Literal["struct"]


class ArrayFieldTypeDict(TypedDict):
    """ArrayFieldType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    itemsSchema: FieldSchemaDict

    type: Literal["array"]


class MapFieldTypeDict(TypedDict):
    """MapFieldType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    keySchema: FieldSchemaDict

    valueSchema: FieldSchemaDict

    type: Literal["map"]


FieldDataTypeDict = Annotated[
    Union[
        StructFieldTypeDict,
        DateTypeDict,
        StringTypeDict,
        ByteTypeDict,
        DoubleTypeDict,
        IntegerTypeDict,
        FloatTypeDict,
        LongTypeDict,
        BooleanTypeDict,
        ArrayFieldTypeDict,
        BinaryTypeDict,
        ShortTypeDict,
        DecimalTypeDict,
        MapFieldTypeDict,
        TimestampTypeDict,
    ],
    pydantic.Field(discriminator="type"),
]
"""FieldDataType"""
