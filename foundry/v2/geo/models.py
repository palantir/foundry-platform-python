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

import typing

import annotated_types
import pydantic
import typing_extensions

from foundry import _core as core

BBox = typing.List["Coordinate"]
"""
A GeoJSON object MAY have a member named "bbox" to include
information on the coordinate range for its Geometries, Features, or
FeatureCollections. The value of the bbox member MUST be an array of
length 2*n where n is the number of dimensions represented in the
contained geometries, with all axes of the most southwesterly point
followed by all axes of the more northeasterly point. The axes order
of a bbox follows the axes order of geometries.
"""


Coordinate = float
"""Coordinate"""


class GeoPoint(pydantic.BaseModel):
    """GeoPoint"""

    coordinates: Position
    bbox: typing.Optional[BBox] = None
    type: typing.Literal["Point"] = "Point"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "GeoPointDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(GeoPointDict, self.model_dump(by_alias=True, exclude_none=True))


class GeoPointDict(typing_extensions.TypedDict):
    """GeoPoint"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    coordinates: Position
    bbox: typing_extensions.NotRequired[BBox]
    type: typing.Literal["Point"]


LinearRing = typing_extensions.Annotated[typing.List["Position"], annotated_types.Len(min_length=4)]
"""
A linear ring is a closed LineString with four or more positions.

The first and last positions are equivalent, and they MUST contain
identical values; their representation SHOULD also be identical.

A linear ring is the boundary of a surface or the boundary of a hole in
a surface.

A linear ring MUST follow the right-hand rule with respect to the area
it bounds, i.e., exterior rings are counterclockwise, and holes are
clockwise.
"""


class Polygon(pydantic.BaseModel):
    """Polygon"""

    coordinates: typing.List[LinearRing]
    bbox: typing.Optional[BBox] = None
    type: typing.Literal["Polygon"] = "Polygon"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "PolygonDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(PolygonDict, self.model_dump(by_alias=True, exclude_none=True))


class PolygonDict(typing_extensions.TypedDict):
    """Polygon"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    coordinates: typing.List[LinearRing]
    bbox: typing_extensions.NotRequired[BBox]
    type: typing.Literal["Polygon"]


Position = typing_extensions.Annotated[
    typing.List[Coordinate], annotated_types.Len(min_length=2, max_length=3)
]
"""
GeoJSon fundamental geometry construct.

A position is an array of numbers. There MUST be two or more elements.
The first two elements are longitude and latitude, precisely in that order and using decimal numbers.
Altitude or elevation MAY be included as an optional third element.

Implementations SHOULD NOT extend positions beyond three elements
because the semantics of extra elements are unspecified and ambiguous.
Historically, some implementations have used a fourth element to carry
a linear referencing measure (sometimes denoted as "M") or a numerical
timestamp, but in most situations a parser will not be able to properly
interpret these values. The interpretation and meaning of additional
elements is beyond the scope of this specification, and additional
elements MAY be ignored by parsers.
"""


core.resolve_forward_references(BBox, globalns=globals(), localns=locals())
core.resolve_forward_references(LinearRing, globalns=globals(), localns=locals())
core.resolve_forward_references(Position, globalns=globals(), localns=locals())

__all__ = [
    "BBox",
    "Coordinate",
    "GeoPoint",
    "GeoPointDict",
    "LinearRing",
    "Polygon",
    "PolygonDict",
    "Position",
]
