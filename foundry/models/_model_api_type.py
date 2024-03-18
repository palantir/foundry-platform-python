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
from pydantic import StrictStr


from foundry.models._any_type import AnyType
from foundry.models._boolean_type import BooleanType
from foundry.models._date_type import DateType
from foundry.models._float_type import FloatType
from foundry.models._integer_type import IntegerType
from foundry.models._null_type import NullType
from foundry.models._string_type import StringType
from foundry.models._timestamp_type import TimestampType


class ModelApiArrayType(BaseModel):
    """ModelApiArrayType"""

    sub_type: ModelApiType = Field(alias="subType")
    """A union of all the types supported by models."""

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
    def from_dict(cls, obj: Dict, *, allow_extra=False) -> "ModelApiArrayType":
        """Create an instance of AsyncActionOperation from a dict"""
        # If allowing extra properties and the given object is a dict,
        # then remove any properties in the dict that aren't present
        # in the model properties list
        # We need to do this since the model config forbids additional properties
        # and this cannot be changed at runtime
        if allow_extra and isinstance(obj, dict) and any(key not in cls._properties for key in obj):
            obj = {key: value for key, value in obj.items() if key in cls._properties}

        return cls.model_validate(obj)


class ModelApiMapType(BaseModel):
    """ModelApiMapType"""

    key_type: ModelApiType = Field(alias="keyType")
    """A union of all the types supported by models."""

    value_type: ModelApiType = Field(alias="valueType")
    """A union of all the types supported by models."""

    type: Literal["map"] = Field()

    _properties: ClassVar[Set[str]] = set(["keyType", "valueType", "type"])

    model_config = {"populate_by_name": True, "validate_assignment": True, "extra": "forbid"}

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:
        """
        return self.model_dump(by_alias=True)

    @classmethod
    def from_dict(cls, obj: Dict, *, allow_extra=False) -> "ModelApiMapType":
        """Create an instance of AsyncActionOperation from a dict"""
        # If allowing extra properties and the given object is a dict,
        # then remove any properties in the dict that aren't present
        # in the model properties list
        # We need to do this since the model config forbids additional properties
        # and this cannot be changed at runtime
        if allow_extra and isinstance(obj, dict) and any(key not in cls._properties for key in obj):
            obj = {key: value for key, value in obj.items() if key in cls._properties}

        return cls.model_validate(obj)


class ModelApiStructField(BaseModel):
    """ModelApiStructField"""

    name: StrictStr = Field()

    field_type: ModelApiType = Field(alias="fieldType")
    """A union of all the types supported by models."""

    _properties: ClassVar[Set[str]] = set(["name", "fieldType"])

    model_config = {"populate_by_name": True, "validate_assignment": True, "extra": "forbid"}

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:
        """
        return self.model_dump(by_alias=True)

    @classmethod
    def from_dict(cls, obj: Dict, *, allow_extra=False) -> "ModelApiStructField":
        """Create an instance of AsyncActionOperation from a dict"""
        # If allowing extra properties and the given object is a dict,
        # then remove any properties in the dict that aren't present
        # in the model properties list
        # We need to do this since the model config forbids additional properties
        # and this cannot be changed at runtime
        if allow_extra and isinstance(obj, dict) and any(key not in cls._properties for key in obj):
            obj = {key: value for key, value in obj.items() if key in cls._properties}

        return cls.model_validate(obj)


class ModelApiStructType(BaseModel):
    """ModelApiStructType"""

    fields: Optional[List[ModelApiStructField]] = Field(default=None)

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
    def from_dict(cls, obj: Dict, *, allow_extra=False) -> "ModelApiStructType":
        """Create an instance of AsyncActionOperation from a dict"""
        # If allowing extra properties and the given object is a dict,
        # then remove any properties in the dict that aren't present
        # in the model properties list
        # We need to do this since the model config forbids additional properties
        # and this cannot be changed at runtime
        if allow_extra and isinstance(obj, dict) and any(key not in cls._properties for key in obj):
            obj = {key: value for key, value in obj.items() if key in cls._properties}

        return cls.model_validate(obj)


class ModelApiUnionType(BaseModel):
    """ModelApiUnionType"""

    union_types: Optional[List[ModelApiType]] = Field(alias="unionTypes", default=None)

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
    def from_dict(cls, obj: Dict, *, allow_extra=False) -> "ModelApiUnionType":
        """Create an instance of AsyncActionOperation from a dict"""
        # If allowing extra properties and the given object is a dict,
        # then remove any properties in the dict that aren't present
        # in the model properties list
        # We need to do this since the model config forbids additional properties
        # and this cannot be changed at runtime
        if allow_extra and isinstance(obj, dict) and any(key not in cls._properties for key in obj):
            obj = {key: value for key, value in obj.items() if key in cls._properties}

        return cls.model_validate(obj)


ModelApiType = Annotated[
    Union[
        AnyType,
        BooleanType,
        DateType,
        FloatType,
        IntegerType,
        ModelApiArrayType,
        ModelApiMapType,
        ModelApiStructType,
        ModelApiUnionType,
        NullType,
        StringType,
        TimestampType,
    ],
    Field(discriminator="type"),
]
"""A union of all the types supported by models."""
