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
from typing_extensions import TypedDict

from foundry.v2.functions.models._value_type_data_type_binary_type_dict import (
    ValueTypeDataTypeBinaryTypeDict,
)  # NOQA
from foundry.v2.functions.models._value_type_data_type_boolean_type_dict import (
    ValueTypeDataTypeBooleanTypeDict,
)  # NOQA
from foundry.v2.functions.models._value_type_data_type_byte_type_dict import (
    ValueTypeDataTypeByteTypeDict,
)  # NOQA
from foundry.v2.functions.models._value_type_data_type_date_type_dict import (
    ValueTypeDataTypeDateTypeDict,
)  # NOQA
from foundry.v2.functions.models._value_type_data_type_decimal_type_dict import (
    ValueTypeDataTypeDecimalTypeDict,
)  # NOQA
from foundry.v2.functions.models._value_type_data_type_double_type_dict import (
    ValueTypeDataTypeDoubleTypeDict,
)  # NOQA
from foundry.v2.functions.models._value_type_data_type_float_type_dict import (
    ValueTypeDataTypeFloatTypeDict,
)  # NOQA
from foundry.v2.functions.models._value_type_data_type_integer_type_dict import (
    ValueTypeDataTypeIntegerTypeDict,
)  # NOQA
from foundry.v2.functions.models._value_type_data_type_long_type_dict import (
    ValueTypeDataTypeLongTypeDict,
)  # NOQA
from foundry.v2.functions.models._value_type_data_type_referenced_type_dict import (
    ValueTypeDataTypeReferencedTypeDict,
)  # NOQA
from foundry.v2.functions.models._value_type_data_type_short_type_dict import (
    ValueTypeDataTypeShortTypeDict,
)  # NOQA
from foundry.v2.functions.models._value_type_data_type_string_type_dict import (
    ValueTypeDataTypeStringTypeDict,
)  # NOQA
from foundry.v2.functions.models._value_type_data_type_struct_field_identifier import (
    ValueTypeDataTypeStructFieldIdentifier,
)  # NOQA
from foundry.v2.functions.models._value_type_data_type_timestamp_type_dict import (
    ValueTypeDataTypeTimestampTypeDict,
)  # NOQA


class ValueTypeDataTypeStructElementDict(TypedDict):
    """ValueTypeDataTypeStructElement"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    identifier: ValueTypeDataTypeStructFieldIdentifier

    baseType: ValueTypeDataTypeDict


class ValueTypeDataTypeStructTypeDict(TypedDict):
    """ValueTypeDataTypeStructType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    fields: List[ValueTypeDataTypeStructElementDict]

    type: Literal["struct"]


class ValueTypeDataTypeOptionalTypeDict(TypedDict):
    """ValueTypeDataTypeOptionalType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    wrappedType: ValueTypeDataTypeDict

    type: Literal["optional"]


class ValueTypeDataTypeUnionTypeDict(TypedDict):
    """ValueTypeDataTypeUnionType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    memberTypes: List[ValueTypeDataTypeDict]

    type: Literal["union"]


class ValueTypeDataTypeArrayTypeDict(TypedDict):
    """ValueTypeDataTypeArrayType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    subType: ValueTypeDataTypeDict

    type: Literal["array"]


class ValueTypeDataTypeMapTypeDict(TypedDict):
    """ValueTypeDataTypeMapType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    keyType: ValueTypeDataTypeDict

    valueType: ValueTypeDataTypeDict

    type: Literal["map"]


ValueTypeDataTypeDict = Annotated[
    Union[
        ValueTypeDataTypeDateTypeDict,
        ValueTypeDataTypeStructTypeDict,
        ValueTypeDataTypeStringTypeDict,
        ValueTypeDataTypeByteTypeDict,
        ValueTypeDataTypeDoubleTypeDict,
        ValueTypeDataTypeOptionalTypeDict,
        ValueTypeDataTypeIntegerTypeDict,
        ValueTypeDataTypeUnionTypeDict,
        ValueTypeDataTypeFloatTypeDict,
        ValueTypeDataTypeLongTypeDict,
        ValueTypeDataTypeBooleanTypeDict,
        ValueTypeDataTypeArrayTypeDict,
        ValueTypeDataTypeReferencedTypeDict,
        ValueTypeDataTypeBinaryTypeDict,
        ValueTypeDataTypeShortTypeDict,
        ValueTypeDataTypeDecimalTypeDict,
        ValueTypeDataTypeMapTypeDict,
        ValueTypeDataTypeTimestampTypeDict,
    ],
    pydantic.Field(discriminator="type"),
]
"""The underlying base type of a value type."""
