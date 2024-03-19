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
from typing import Any
from typing import ClassVar
from typing import Dict
from typing import List
from typing import Literal
from typing import Optional
from typing import Set
from typing import Union

from pydantic import BaseModel
from pydantic import Field


from foundry.models._attachment_type import AttachmentType
from foundry.models._boolean_type import BooleanType
from foundry.models._date_type import DateType
from foundry.models._double_type import DoubleType
from foundry.models._float_type import FloatType
from foundry.models._integer_type import IntegerType
from foundry.models._long_type import LongType
from foundry.models._null_type import NullType
from foundry.models._ontology_object_set_type import OntologyObjectSetType
from foundry.models._ontology_object_type import OntologyObjectType
from foundry.models._string_type import StringType
from foundry.models._struct_field_name import StructFieldName
from foundry.models._three_dimensional_aggregation import ThreeDimensionalAggregation
from foundry.models._timestamp_type import TimestampType
from foundry.models._two_dimensional_aggregation import TwoDimensionalAggregation
from foundry.models._unsupported_type import UnsupportedType


class QueryArrayType(BaseModel):
    """QueryArrayType"""

    sub_type: QueryDataType = Field(alias="subType")
    """A union of all the types supported by Ontology Query parameters or outputs."""

    type: Literal["array"] = Field()

    _properties: ClassVar[Set[str]] = set(["subType", "type"])

    model_config = {"populate_by_name": True, "validate_assignment": True, "extra": "forbid"}

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:
        """
        return self.model_dump(by_alias=True)

    @classmethod
    def from_dict(cls, obj: Dict, *, allow_extra=False) -> "QueryArrayType":
        """Create an instance of AsyncActionOperation from a dict"""
        # If allowing extra properties and the given object is a dict,
        # then remove any properties in the dict that aren't present
        # in the model properties list
        # We need to do this since the model config forbids additional properties
        # and this cannot be changed at runtime
        if allow_extra and isinstance(obj, dict) and any(key not in cls._properties for key in obj):
            obj = {key: value for key, value in obj.items() if key in cls._properties}

        return cls.model_validate(obj)


class QuerySetType(BaseModel):
    """QuerySetType"""

    sub_type: QueryDataType = Field(alias="subType")
    """A union of all the types supported by Ontology Query parameters or outputs."""

    type: Literal["set"] = Field()

    _properties: ClassVar[Set[str]] = set(["subType", "type"])

    model_config = {"populate_by_name": True, "validate_assignment": True, "extra": "forbid"}

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:
        """
        return self.model_dump(by_alias=True)

    @classmethod
    def from_dict(cls, obj: Dict, *, allow_extra=False) -> "QuerySetType":
        """Create an instance of AsyncActionOperation from a dict"""
        # If allowing extra properties and the given object is a dict,
        # then remove any properties in the dict that aren't present
        # in the model properties list
        # We need to do this since the model config forbids additional properties
        # and this cannot be changed at runtime
        if allow_extra and isinstance(obj, dict) and any(key not in cls._properties for key in obj):
            obj = {key: value for key, value in obj.items() if key in cls._properties}

        return cls.model_validate(obj)


class QueryStructField(BaseModel):
    """QueryStructField"""

    name: StructFieldName = Field()
    """The name of a field in a `Struct`."""

    field_type: QueryDataType = Field(alias="fieldType")
    """A union of all the types supported by Ontology Query parameters or outputs."""

    _properties: ClassVar[Set[str]] = set(["name", "fieldType"])

    model_config = {"populate_by_name": True, "validate_assignment": True, "extra": "forbid"}

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:
        """
        return self.model_dump(by_alias=True)

    @classmethod
    def from_dict(cls, obj: Dict, *, allow_extra=False) -> "QueryStructField":
        """Create an instance of AsyncActionOperation from a dict"""
        # If allowing extra properties and the given object is a dict,
        # then remove any properties in the dict that aren't present
        # in the model properties list
        # We need to do this since the model config forbids additional properties
        # and this cannot be changed at runtime
        if allow_extra and isinstance(obj, dict) and any(key not in cls._properties for key in obj):
            obj = {key: value for key, value in obj.items() if key in cls._properties}

        return cls.model_validate(obj)


class QueryStructType(BaseModel):
    """QueryStructType"""

    fields: Optional[List[QueryStructField]] = Field(default=None)

    type: Literal["struct"] = Field()

    _properties: ClassVar[Set[str]] = set(["fields", "type"])

    model_config = {"populate_by_name": True, "validate_assignment": True, "extra": "forbid"}

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:
        """
        return self.model_dump(by_alias=True)

    @classmethod
    def from_dict(cls, obj: Dict, *, allow_extra=False) -> "QueryStructType":
        """Create an instance of AsyncActionOperation from a dict"""
        # If allowing extra properties and the given object is a dict,
        # then remove any properties in the dict that aren't present
        # in the model properties list
        # We need to do this since the model config forbids additional properties
        # and this cannot be changed at runtime
        if allow_extra and isinstance(obj, dict) and any(key not in cls._properties for key in obj):
            obj = {key: value for key, value in obj.items() if key in cls._properties}

        return cls.model_validate(obj)


class QueryUnionType(BaseModel):
    """QueryUnionType"""

    union_types: Optional[List[QueryDataType]] = Field(alias="unionTypes", default=None)

    type: Literal["union"] = Field()

    _properties: ClassVar[Set[str]] = set(["unionTypes", "type"])

    model_config = {"populate_by_name": True, "validate_assignment": True, "extra": "forbid"}

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:
        """
        return self.model_dump(by_alias=True)

    @classmethod
    def from_dict(cls, obj: Dict, *, allow_extra=False) -> "QueryUnionType":
        """Create an instance of AsyncActionOperation from a dict"""
        # If allowing extra properties and the given object is a dict,
        # then remove any properties in the dict that aren't present
        # in the model properties list
        # We need to do this since the model config forbids additional properties
        # and this cannot be changed at runtime
        if allow_extra and isinstance(obj, dict) and any(key not in cls._properties for key in obj):
            obj = {key: value for key, value in obj.items() if key in cls._properties}

        return cls.model_validate(obj)


QueryDataType = Annotated[
    Union[
        AttachmentType,
        BooleanType,
        DateType,
        DoubleType,
        FloatType,
        IntegerType,
        LongType,
        NullType,
        OntologyObjectSetType,
        OntologyObjectType,
        QueryArrayType,
        QuerySetType,
        QueryStructType,
        QueryUnionType,
        StringType,
        ThreeDimensionalAggregation,
        TimestampType,
        TwoDimensionalAggregation,
        UnsupportedType,
    ],
    Field(discriminator="type"),
]
"""A union of all the types supported by Ontology Query parameters or outputs."""
