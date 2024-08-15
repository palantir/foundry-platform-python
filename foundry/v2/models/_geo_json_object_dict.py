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

from foundry.v2.models._feature_collection_dict import FeatureCollectionDict
from foundry.v2.models._feature_dict import FeatureDict
from foundry.v2.models._geo_point_dict import GeoPointDict
from foundry.v2.models._geometry_dict import GeometryCollectionDict
from foundry.v2.models._line_string_dict import LineStringDict
from foundry.v2.models._multi_line_string_dict import MultiLineStringDict
from foundry.v2.models._multi_point_dict import MultiPointDict
from foundry.v2.models._multi_polygon_dict import MultiPolygonDict
from foundry.v2.models._polygon_dict import PolygonDict

GeoJsonObjectDict = Annotated[
    Union[
        FeatureDict,
        FeatureCollectionDict,
        GeoPointDict,
        MultiPointDict,
        LineStringDict,
        MultiLineStringDict,
        PolygonDict,
        MultiPolygonDict,
        GeometryCollectionDict,
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
