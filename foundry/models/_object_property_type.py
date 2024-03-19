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
from typing import Literal
from typing import Set
from typing import Union

from pydantic import BaseModel
from pydantic import Field


from foundry.models._attachment_type import AttachmentType
from foundry.models._boolean_type import BooleanType
from foundry.models._byte_type import ByteType
from foundry.models._date_type import DateType
from foundry.models._decimal_type import DecimalType
from foundry.models._double_type import DoubleType
from foundry.models._float_type import FloatType
from foundry.models._geo_point_type import GeoPointType
from foundry.models._geo_shape_type import GeoShapeType
from foundry.models._integer_type import IntegerType
from foundry.models._long_type import LongType
from foundry.models._short_type import ShortType
from foundry.models._string_type import StringType
from foundry.models._timeseries_type import TimeseriesType
from foundry.models._timestamp_type import TimestampType


class OntologyObjectArrayType(BaseModel):
    """OntologyObjectArrayType"""

    sub_type: ObjectPropertyType = Field(alias="subType")
    """A union of all the types supported by Ontology Object properties."""

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
    def from_dict(cls, obj: Dict, *, allow_extra=False) -> "OntologyObjectArrayType":
        """Create an instance of AsyncActionOperation from a dict"""
        # If allowing extra properties and the given object is a dict,
        # then remove any properties in the dict that aren't present
        # in the model properties list
        # We need to do this since the model config forbids additional properties
        # and this cannot be changed at runtime
        if allow_extra and isinstance(obj, dict) and any(key not in cls._properties for key in obj):
            obj = {key: value for key, value in obj.items() if key in cls._properties}

        return cls.model_validate(obj)


ObjectPropertyType = Annotated[
    Union[
        AttachmentType,
        BooleanType,
        ByteType,
        DateType,
        DecimalType,
        DoubleType,
        FloatType,
        GeoPointType,
        GeoShapeType,
        IntegerType,
        LongType,
        OntologyObjectArrayType,
        ShortType,
        StringType,
        TimeseriesType,
        TimestampType,
    ],
    Field(discriminator="type"),
]
"""A union of all the types supported by Ontology Object properties."""
