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

from typing_extensions import NotRequired
from typing_extensions import TypedDict

from foundry.v2.geo.models._b_box import BBox
from foundry.v2.geo.models._geometry_dict import GeometryDict


class GeometryCollectionDict(TypedDict):
    """
    GeoJSon geometry collection

    GeometryCollections composed of a single part or a number of parts of a
    single type SHOULD be avoided when that single part or a single object
    of multipart type (MultiPoint, MultiLineString, or MultiPolygon) could
    be used instead.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    geometries: List[GeometryDict]

    bbox: NotRequired[BBox]

    type: Literal["GeometryCollection"]
