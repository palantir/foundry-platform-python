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

from pydantic import Field
from typing_extensions import Annotated
from typing_extensions import TypedDict

from foundry.v2.core.models._attachment_type_dict import AttachmentTypeDict
from foundry.v2.core.models._boolean_type_dict import BooleanTypeDict
from foundry.v2.core.models._date_type_dict import DateTypeDict
from foundry.v2.core.models._double_type_dict import DoubleTypeDict
from foundry.v2.core.models._float_type_dict import FloatTypeDict
from foundry.v2.core.models._integer_type_dict import IntegerTypeDict
from foundry.v2.core.models._long_type_dict import LongTypeDict
from foundry.v2.core.models._null_type_dict import NullTypeDict
from foundry.v2.core.models._string_type_dict import StringTypeDict
from foundry.v2.core.models._timestamp_type_dict import TimestampTypeDict
from foundry.v2.core.models._unsupported_type_dict import UnsupportedTypeDict
from foundry.v2.functions.models._struct_field_name import StructFieldName
from foundry.v2.functions.models._three_dimensional_aggregation_dict import (
    ThreeDimensionalAggregationDict,
)  # NOQA
from foundry.v2.functions.models._two_dimensional_aggregation_dict import (
    TwoDimensionalAggregationDict,
)  # NOQA


class QueryStructFieldDict(TypedDict):
    """QueryStructField"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    name: StructFieldName

    fieldType: QueryDataTypeDict


class QueryStructTypeDict(TypedDict):
    """QueryStructType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    fields: List[QueryStructFieldDict]

    type: Literal["struct"]


class QuerySetTypeDict(TypedDict):
    """QuerySetType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    subType: QueryDataTypeDict

    type: Literal["set"]


class QueryUnionTypeDict(TypedDict):
    """QueryUnionType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    unionTypes: List[QueryDataTypeDict]

    type: Literal["union"]


class QueryArrayTypeDict(TypedDict):
    """QueryArrayType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    subType: QueryDataTypeDict

    type: Literal["array"]


QueryDataTypeDict = Annotated[
    Union[
        DateTypeDict,
        QueryStructTypeDict,
        QuerySetTypeDict,
        StringTypeDict,
        DoubleTypeDict,
        IntegerTypeDict,
        ThreeDimensionalAggregationDict,
        QueryUnionTypeDict,
        FloatTypeDict,
        LongTypeDict,
        BooleanTypeDict,
        UnsupportedTypeDict,
        AttachmentTypeDict,
        NullTypeDict,
        QueryArrayTypeDict,
        TwoDimensionalAggregationDict,
        TimestampTypeDict,
    ],
    Field(discriminator="type"),
]
"""A union of all the types supported by Query parameters or outputs."""
