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
from typing import Optional
from typing import Union
from typing import cast

from pydantic import BaseModel
from pydantic import Field

from foundry.models._b_box import BBox
from foundry.models._geo_point import GeoPoint
from foundry.models._geometry_dict import GeometryCollectionDict
from foundry.models._line_string import LineString
from foundry.models._multi_line_string import MultiLineString
from foundry.models._multi_point import MultiPoint
from foundry.models._multi_polygon import MultiPolygon
from foundry.models._polygon import Polygon


class GeometryCollection(BaseModel):
    """
    GeoJSon geometry collection

    GeometryCollections composed of a single part or a number of parts of a
    single type SHOULD be avoided when that single part or a single object
    of multipart type (MultiPoint, MultiLineString, or MultiPolygon) could
    be used instead.
    """

    geometries: List[Geometry]

    bbox: Optional[BBox] = None

    type: Literal["GeometryCollection"]

    model_config = {"extra": "allow"}

    def to_dict(self) -> GeometryCollectionDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(GeometryCollectionDict, self.model_dump(by_alias=True, exclude_unset=True))


Geometry = Annotated[
    Union[
        GeoPoint, MultiPoint, LineString, MultiLineString, Polygon, MultiPolygon, GeometryCollection
    ],
    Field(discriminator="type"),
]
"""Abstract type for all GeoJSon object except Feature and FeatureCollection"""
