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

from foundry.v1.core.models._any_type import AnyType
from foundry.v1.core.models._binary_type import BinaryType
from foundry.v1.core.models._boolean_type import BooleanType
from foundry.v1.core.models._byte_type import ByteType
from foundry.v1.core.models._date_type import DateType
from foundry.v1.core.models._decimal_type import DecimalType
from foundry.v1.core.models._double_type import DoubleType
from foundry.v1.core.models._float_type import FloatType
from foundry.v1.core.models._integer_type import IntegerType
from foundry.v1.core.models._long_type import LongType
from foundry.v1.core.models._marking_type import MarkingType
from foundry.v1.core.models._short_type import ShortType
from foundry.v1.core.models._string_type import StringType
from foundry.v1.core.models._struct_field_name import StructFieldName
from foundry.v1.core.models._timestamp_type import TimestampType
from foundry.v1.core.models._unsupported_type import UnsupportedType
from foundry.v1.ontologies.models._ontology_array_type_dict import OntologyArrayTypeDict
from foundry.v1.ontologies.models._ontology_map_type_dict import OntologyMapTypeDict
from foundry.v1.ontologies.models._ontology_object_set_type import OntologyObjectSetType
from foundry.v1.ontologies.models._ontology_object_type import OntologyObjectType
from foundry.v1.ontologies.models._ontology_set_type_dict import OntologySetTypeDict
from foundry.v1.ontologies.models._ontology_struct_field_dict import OntologyStructFieldDict  # NOQA
from foundry.v1.ontologies.models._ontology_struct_type_dict import OntologyStructTypeDict  # NOQA


class OntologyStructField(pydantic.BaseModel):
    """OntologyStructField"""

    name: StructFieldName

    field_type: OntologyDataType = pydantic.Field(alias="fieldType")

    required: pydantic.StrictBool

    model_config = {"extra": "allow"}

    def to_dict(self) -> OntologyStructFieldDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(OntologyStructFieldDict, self.model_dump(by_alias=True, exclude_unset=True))


class OntologyStructType(pydantic.BaseModel):
    """OntologyStructType"""

    fields: List[OntologyStructField]

    type: Literal["struct"] = "struct"

    model_config = {"extra": "allow"}

    def to_dict(self) -> OntologyStructTypeDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(OntologyStructTypeDict, self.model_dump(by_alias=True, exclude_unset=True))


class OntologySetType(pydantic.BaseModel):
    """OntologySetType"""

    item_type: OntologyDataType = pydantic.Field(alias="itemType")

    type: Literal["set"] = "set"

    model_config = {"extra": "allow"}

    def to_dict(self) -> OntologySetTypeDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(OntologySetTypeDict, self.model_dump(by_alias=True, exclude_unset=True))


class OntologyArrayType(pydantic.BaseModel):
    """OntologyArrayType"""

    item_type: OntologyDataType = pydantic.Field(alias="itemType")

    type: Literal["array"] = "array"

    model_config = {"extra": "allow"}

    def to_dict(self) -> OntologyArrayTypeDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(OntologyArrayTypeDict, self.model_dump(by_alias=True, exclude_unset=True))


class OntologyMapType(pydantic.BaseModel):
    """OntologyMapType"""

    key_type: OntologyDataType = pydantic.Field(alias="keyType")

    value_type: OntologyDataType = pydantic.Field(alias="valueType")

    type: Literal["map"] = "map"

    model_config = {"extra": "allow"}

    def to_dict(self) -> OntologyMapTypeDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(OntologyMapTypeDict, self.model_dump(by_alias=True, exclude_unset=True))


OntologyDataType = Annotated[
    Union[
        DateType,
        OntologyStructType,
        OntologySetType,
        StringType,
        ByteType,
        DoubleType,
        IntegerType,
        FloatType,
        AnyType,
        LongType,
        BooleanType,
        MarkingType,
        UnsupportedType,
        OntologyArrayType,
        OntologyObjectSetType,
        BinaryType,
        ShortType,
        DecimalType,
        OntologyMapType,
        TimestampType,
        OntologyObjectType,
    ],
    pydantic.Field(discriminator="type"),
]
"""A union of all the primitive types used by Palantir's Ontology-based products."""
