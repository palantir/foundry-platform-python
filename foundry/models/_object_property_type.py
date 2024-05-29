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
from typing import Literal
from typing import Union
from typing import cast

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
from foundry.models._marking_type import MarkingType
from foundry.models._object_property_type_dict import OntologyObjectArrayTypeDict
from foundry.models._short_type import ShortType
from foundry.models._string_type import StringType
from foundry.models._timeseries_type import TimeseriesType
from foundry.models._timestamp_type import TimestampType


class OntologyObjectArrayType(BaseModel):
    """OntologyObjectArrayType"""

    sub_type: ObjectPropertyType = Field(alias="subType")

    type: Literal["array"]

    model_config = {"extra": "allow"}

    def to_dict(self) -> OntologyObjectArrayTypeDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(OntologyObjectArrayTypeDict, self.model_dump(by_alias=True, exclude_unset=True))


ObjectPropertyType = Annotated[
    Union[
        OntologyObjectArrayType,
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
        MarkingType,
        ShortType,
        StringType,
        TimestampType,
        TimeseriesType,
    ],
    Field(discriminator="type"),
]
"""A union of all the types supported by Ontology Object properties."""
