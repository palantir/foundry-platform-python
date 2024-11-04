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

from foundry.v2.functions.models._value_type_data_type_array_type_dict import (
    ValueTypeDataTypeArrayTypeDict,
)  # NOQA
from foundry.v2.functions.models._value_type_data_type_binary_type import (
    ValueTypeDataTypeBinaryType,
)  # NOQA
from foundry.v2.functions.models._value_type_data_type_boolean_type import (
    ValueTypeDataTypeBooleanType,
)  # NOQA
from foundry.v2.functions.models._value_type_data_type_byte_type import (
    ValueTypeDataTypeByteType,
)  # NOQA
from foundry.v2.functions.models._value_type_data_type_date_type import (
    ValueTypeDataTypeDateType,
)  # NOQA
from foundry.v2.functions.models._value_type_data_type_decimal_type import (
    ValueTypeDataTypeDecimalType,
)  # NOQA
from foundry.v2.functions.models._value_type_data_type_double_type import (
    ValueTypeDataTypeDoubleType,
)  # NOQA
from foundry.v2.functions.models._value_type_data_type_float_type import (
    ValueTypeDataTypeFloatType,
)  # NOQA
from foundry.v2.functions.models._value_type_data_type_integer_type import (
    ValueTypeDataTypeIntegerType,
)  # NOQA
from foundry.v2.functions.models._value_type_data_type_long_type import (
    ValueTypeDataTypeLongType,
)  # NOQA
from foundry.v2.functions.models._value_type_data_type_map_type_dict import (
    ValueTypeDataTypeMapTypeDict,
)  # NOQA
from foundry.v2.functions.models._value_type_data_type_optional_type_dict import (
    ValueTypeDataTypeOptionalTypeDict,
)  # NOQA
from foundry.v2.functions.models._value_type_data_type_referenced_type import (
    ValueTypeDataTypeReferencedType,
)  # NOQA
from foundry.v2.functions.models._value_type_data_type_short_type import (
    ValueTypeDataTypeShortType,
)  # NOQA
from foundry.v2.functions.models._value_type_data_type_string_type import (
    ValueTypeDataTypeStringType,
)  # NOQA
from foundry.v2.functions.models._value_type_data_type_struct_element_dict import (
    ValueTypeDataTypeStructElementDict,
)  # NOQA
from foundry.v2.functions.models._value_type_data_type_struct_field_identifier import (
    ValueTypeDataTypeStructFieldIdentifier,
)  # NOQA
from foundry.v2.functions.models._value_type_data_type_struct_type_dict import (
    ValueTypeDataTypeStructTypeDict,
)  # NOQA
from foundry.v2.functions.models._value_type_data_type_timestamp_type import (
    ValueTypeDataTypeTimestampType,
)  # NOQA
from foundry.v2.functions.models._value_type_data_type_union_type_dict import (
    ValueTypeDataTypeUnionTypeDict,
)  # NOQA


class ValueTypeDataTypeStructElement(pydantic.BaseModel):
    """ValueTypeDataTypeStructElement"""

    identifier: ValueTypeDataTypeStructFieldIdentifier

    base_type: ValueTypeDataType = pydantic.Field(alias="baseType")

    model_config = {"extra": "allow"}

    def to_dict(self) -> ValueTypeDataTypeStructElementDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(
            ValueTypeDataTypeStructElementDict, self.model_dump(by_alias=True, exclude_unset=True)
        )


class ValueTypeDataTypeStructType(pydantic.BaseModel):
    """ValueTypeDataTypeStructType"""

    fields: List[ValueTypeDataTypeStructElement]

    type: Literal["struct"] = "struct"

    model_config = {"extra": "allow"}

    def to_dict(self) -> ValueTypeDataTypeStructTypeDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(
            ValueTypeDataTypeStructTypeDict, self.model_dump(by_alias=True, exclude_unset=True)
        )


class ValueTypeDataTypeOptionalType(pydantic.BaseModel):
    """ValueTypeDataTypeOptionalType"""

    wrapped_type: ValueTypeDataType = pydantic.Field(alias="wrappedType")

    type: Literal["optional"] = "optional"

    model_config = {"extra": "allow"}

    def to_dict(self) -> ValueTypeDataTypeOptionalTypeDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(
            ValueTypeDataTypeOptionalTypeDict, self.model_dump(by_alias=True, exclude_unset=True)
        )


class ValueTypeDataTypeUnionType(pydantic.BaseModel):
    """ValueTypeDataTypeUnionType"""

    member_types: List[ValueTypeDataType] = pydantic.Field(alias="memberTypes")

    type: Literal["union"] = "union"

    model_config = {"extra": "allow"}

    def to_dict(self) -> ValueTypeDataTypeUnionTypeDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(
            ValueTypeDataTypeUnionTypeDict, self.model_dump(by_alias=True, exclude_unset=True)
        )


class ValueTypeDataTypeArrayType(pydantic.BaseModel):
    """ValueTypeDataTypeArrayType"""

    sub_type: ValueTypeDataType = pydantic.Field(alias="subType")

    type: Literal["array"] = "array"

    model_config = {"extra": "allow"}

    def to_dict(self) -> ValueTypeDataTypeArrayTypeDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(
            ValueTypeDataTypeArrayTypeDict, self.model_dump(by_alias=True, exclude_unset=True)
        )


class ValueTypeDataTypeMapType(pydantic.BaseModel):
    """ValueTypeDataTypeMapType"""

    key_type: ValueTypeDataType = pydantic.Field(alias="keyType")

    value_type: ValueTypeDataType = pydantic.Field(alias="valueType")

    type: Literal["map"] = "map"

    model_config = {"extra": "allow"}

    def to_dict(self) -> ValueTypeDataTypeMapTypeDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(
            ValueTypeDataTypeMapTypeDict, self.model_dump(by_alias=True, exclude_unset=True)
        )


ValueTypeDataType = Annotated[
    Union[
        ValueTypeDataTypeDateType,
        ValueTypeDataTypeStructType,
        ValueTypeDataTypeStringType,
        ValueTypeDataTypeByteType,
        ValueTypeDataTypeDoubleType,
        ValueTypeDataTypeOptionalType,
        ValueTypeDataTypeIntegerType,
        ValueTypeDataTypeUnionType,
        ValueTypeDataTypeFloatType,
        ValueTypeDataTypeLongType,
        ValueTypeDataTypeBooleanType,
        ValueTypeDataTypeArrayType,
        ValueTypeDataTypeReferencedType,
        ValueTypeDataTypeBinaryType,
        ValueTypeDataTypeShortType,
        ValueTypeDataTypeDecimalType,
        ValueTypeDataTypeMapType,
        ValueTypeDataTypeTimestampType,
    ],
    pydantic.Field(discriminator="type"),
]
"""The underlying base type of a value type."""
