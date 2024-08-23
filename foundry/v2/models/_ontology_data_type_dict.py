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

from pydantic import Field
from pydantic import StrictBool
from typing_extensions import TypedDict

from foundry.v2.models._any_type_dict import AnyTypeDict
from foundry.v2.models._binary_type_dict import BinaryTypeDict
from foundry.v2.models._boolean_type_dict import BooleanTypeDict
from foundry.v2.models._byte_type_dict import ByteTypeDict
from foundry.v2.models._date_type_dict import DateTypeDict
from foundry.v2.models._decimal_type_dict import DecimalTypeDict
from foundry.v2.models._double_type_dict import DoubleTypeDict
from foundry.v2.models._float_type_dict import FloatTypeDict
from foundry.v2.models._integer_type_dict import IntegerTypeDict
from foundry.v2.models._long_type_dict import LongTypeDict
from foundry.v2.models._marking_type_dict import MarkingTypeDict
from foundry.v2.models._ontology_object_set_type_dict import OntologyObjectSetTypeDict
from foundry.v2.models._ontology_object_type_dict import OntologyObjectTypeDict
from foundry.v2.models._short_type_dict import ShortTypeDict
from foundry.v2.models._string_type_dict import StringTypeDict
from foundry.v2.models._struct_field_name import StructFieldName
from foundry.v2.models._timestamp_type_dict import TimestampTypeDict
from foundry.v2.models._unsupported_type_dict import UnsupportedTypeDict


class OntologyArrayTypeDict(TypedDict):
    """OntologyArrayType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    itemType: OntologyDataTypeDict

    type: Literal["array"]


class OntologyMapTypeDict(TypedDict):
    """OntologyMapType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    keyType: OntologyDataTypeDict

    valueType: OntologyDataTypeDict

    type: Literal["map"]


class OntologySetTypeDict(TypedDict):
    """OntologySetType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    itemType: OntologyDataTypeDict

    type: Literal["set"]


class OntologyStructFieldDict(TypedDict):
    """OntologyStructField"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    name: StructFieldName

    fieldType: OntologyDataTypeDict

    required: StrictBool


class OntologyStructTypeDict(TypedDict):
    """OntologyStructType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    fields: List[OntologyStructFieldDict]

    type: Literal["struct"]


OntologyDataTypeDict = Annotated[
    Union[
        AnyTypeDict,
        BinaryTypeDict,
        BooleanTypeDict,
        ByteTypeDict,
        DateTypeDict,
        DecimalTypeDict,
        DoubleTypeDict,
        FloatTypeDict,
        IntegerTypeDict,
        LongTypeDict,
        MarkingTypeDict,
        ShortTypeDict,
        StringTypeDict,
        TimestampTypeDict,
        OntologyArrayTypeDict,
        OntologyMapTypeDict,
        OntologySetTypeDict,
        OntologyStructTypeDict,
        OntologyObjectTypeDict,
        OntologyObjectSetTypeDict,
        UnsupportedTypeDict,
    ],
    Field(discriminator="type"),
]
"""A union of all the primitive types used by Palantir's Ontology-based products."""
