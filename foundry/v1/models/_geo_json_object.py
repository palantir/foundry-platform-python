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
from typing import Union

from pydantic import Field

from foundry.v1.models._feature import Feature
from foundry.v1.models._feature_collection import FeatureCollection
from foundry.v1.models._geo_point import GeoPoint
from foundry.v1.models._geometry import GeometryCollection
from foundry.v1.models._line_string import LineString
from foundry.v1.models._multi_line_string import MultiLineString
from foundry.v1.models._multi_point import MultiPoint
from foundry.v1.models._multi_polygon import MultiPolygon
from foundry.v1.models._polygon import Polygon

GeoJsonObject = Annotated[
    Union[
        Feature,
        FeatureCollection,
        GeoPoint,
        MultiPoint,
        LineString,
        MultiLineString,
        Polygon,
        MultiPolygon,
        GeometryCollection,
    ],
    Field(discriminator="type"),
]
"""
GeoJSon object

The coordinate reference system for all GeoJSON coordinates is a
geographic coordinate reference system, using the World Geodetic System
1984 (WGS 84) datum, with longitude and latitude units of decimal
degrees.
This is equivalent to the coordinate reference system identified by the
Open Geospatial Consortium (OGC) URN
An OPTIONAL third-position element SHALL be the height in meters above
or below the WGS 84 reference ellipsoid.
In the absence of elevation values, applications sensitive to height or
depth SHOULD interpret positions as being at local ground or sea level.
"""
