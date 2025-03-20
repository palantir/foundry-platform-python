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


class Feature(pydantic.BaseModel):
    """GeoJSon 'Feature' object"""

    geometry: typing.Optional[Geometry] = None
    properties: typing.Dict[FeaturePropertyKey, typing.Any]
    """
    A `Feature` object has a member with the name "properties".  The
    value of the properties member is an object (any JSON object or a
    JSON null value).
    """

    id: typing.Optional[typing.Any] = None
    """
    If a `Feature` has a commonly used identifier, that identifier
    SHOULD be included as a member of the Feature object with the name
    "id", and the value of this member is either a JSON string or
    number.
    """

    bbox: typing.Optional[BBox] = None
    type: typing.Literal["Feature"] = "Feature"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "FeatureDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(FeatureDict, self.model_dump(by_alias=True, exclude_none=True))


class FeatureCollection(pydantic.BaseModel):
    """GeoJSon 'FeatureCollection' object"""

    features: typing.List[FeatureCollectionTypes]
    bbox: typing.Optional[BBox] = None
    type: typing.Literal["FeatureCollection"] = "FeatureCollection"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "FeatureCollectionDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(FeatureCollectionDict, self.model_dump(by_alias=True, exclude_none=True))


class FeatureCollectionDict(typing_extensions.TypedDict):
    """GeoJSon 'FeatureCollection' object"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    features: typing.List[FeatureCollectionTypesDict]
    bbox: typing_extensions.NotRequired[BBox]
    type: typing.Literal["FeatureCollection"]


class FeatureDict(typing_extensions.TypedDict):
    """GeoJSon 'Feature' object"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    geometry: typing_extensions.NotRequired[GeometryDict]
    properties: typing.Dict[FeaturePropertyKey, typing.Any]
    """
    A `Feature` object has a member with the name "properties".  The
    value of the properties member is an object (any JSON object or a
    JSON null value).
    """

    id: typing_extensions.NotRequired[typing.Any]
    """
    If a `Feature` has a commonly used identifier, that identifier
    SHOULD be included as a member of the Feature object with the name
    "id", and the value of this member is either a JSON string or
    number.
    """

    bbox: typing_extensions.NotRequired[BBox]
    type: typing.Literal["Feature"]


FeaturePropertyKey = str
"""FeaturePropertyKey"""


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


Geometry = typing_extensions.Annotated[
    typing.Union[
        "MultiPoint",
        "GeometryCollection",
        "MultiLineString",
        "LineString",
        "MultiPolygon",
        GeoPoint,
        "Polygon",
    ],
    pydantic.Field(discriminator="type"),
]
"""Abstract type for all GeoJSon object except Feature and FeatureCollection"""


class GeometryCollection(pydantic.BaseModel):
    """
    GeoJSon geometry collection

    GeometryCollections composed of a single part or a number of parts of a
    single type SHOULD be avoided when that single part or a single object
    of multipart type (MultiPoint, MultiLineString, or MultiPolygon) could
    be used instead.
    """

    geometries: typing.List[Geometry]
    bbox: typing.Optional[BBox] = None
    type: typing.Literal["GeometryCollection"] = "GeometryCollection"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "GeometryCollectionDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            GeometryCollectionDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class GeometryCollectionDict(typing_extensions.TypedDict):
    """
    GeoJSon geometry collection

    GeometryCollections composed of a single part or a number of parts of a
    single type SHOULD be avoided when that single part or a single object
    of multipart type (MultiPoint, MultiLineString, or MultiPolygon) could
    be used instead.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    geometries: typing.List[GeometryDict]
    bbox: typing_extensions.NotRequired[BBox]
    type: typing.Literal["GeometryCollection"]


GeometryDict = typing_extensions.Annotated[
    typing.Union[
        "MultiPointDict",
        GeometryCollectionDict,
        "MultiLineStringDict",
        "LineStringDict",
        "MultiPolygonDict",
        GeoPointDict,
        "PolygonDict",
    ],
    pydantic.Field(discriminator="type"),
]
"""Abstract type for all GeoJSon object except Feature and FeatureCollection"""


class LineString(pydantic.BaseModel):
    """LineString"""

    coordinates: typing.Optional[LineStringCoordinates] = None
    bbox: typing.Optional[BBox] = None
    type: typing.Literal["LineString"] = "LineString"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "LineStringDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(LineStringDict, self.model_dump(by_alias=True, exclude_none=True))


LineStringCoordinates = typing_extensions.Annotated[
    typing.List["Position"], annotated_types.Len(min_length=2)
]
"""GeoJSon fundamental geometry construct, array of two or more positions."""


class LineStringDict(typing_extensions.TypedDict):
    """LineString"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    coordinates: typing_extensions.NotRequired[LineStringCoordinates]
    bbox: typing_extensions.NotRequired[BBox]
    type: typing.Literal["LineString"]


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


class MultiLineString(pydantic.BaseModel):
    """MultiLineString"""

    coordinates: typing.List[LineStringCoordinates]
    bbox: typing.Optional[BBox] = None
    type: typing.Literal["MultiLineString"] = "MultiLineString"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "MultiLineStringDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(MultiLineStringDict, self.model_dump(by_alias=True, exclude_none=True))


class MultiLineStringDict(typing_extensions.TypedDict):
    """MultiLineString"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    coordinates: typing.List[LineStringCoordinates]
    bbox: typing_extensions.NotRequired[BBox]
    type: typing.Literal["MultiLineString"]


class MultiPoint(pydantic.BaseModel):
    """MultiPoint"""

    coordinates: typing.List[Position]
    bbox: typing.Optional[BBox] = None
    type: typing.Literal["MultiPoint"] = "MultiPoint"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "MultiPointDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(MultiPointDict, self.model_dump(by_alias=True, exclude_none=True))


class MultiPointDict(typing_extensions.TypedDict):
    """MultiPoint"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    coordinates: typing.List[Position]
    bbox: typing_extensions.NotRequired[BBox]
    type: typing.Literal["MultiPoint"]


class MultiPolygon(pydantic.BaseModel):
    """MultiPolygon"""

    coordinates: typing.List[typing.List[LinearRing]]
    bbox: typing.Optional[BBox] = None
    type: typing.Literal["MultiPolygon"] = "MultiPolygon"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "MultiPolygonDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(MultiPolygonDict, self.model_dump(by_alias=True, exclude_none=True))


class MultiPolygonDict(typing_extensions.TypedDict):
    """MultiPolygon"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    coordinates: typing.List[typing.List[LinearRing]]
    bbox: typing_extensions.NotRequired[BBox]
    type: typing.Literal["MultiPolygon"]


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


FeatureCollectionTypes = Feature
"""FeatureCollectionTypes"""


FeatureCollectionTypesDict = FeatureDict
"""FeatureCollectionTypes"""


core.resolve_forward_references(BBox, globalns=globals(), localns=locals())
core.resolve_forward_references(Geometry, globalns=globals(), localns=locals())
core.resolve_forward_references(GeometryDict, globalns=globals(), localns=locals())
core.resolve_forward_references(LineStringCoordinates, globalns=globals(), localns=locals())
core.resolve_forward_references(LinearRing, globalns=globals(), localns=locals())
core.resolve_forward_references(Position, globalns=globals(), localns=locals())

__all__ = [
    "BBox",
    "Coordinate",
    "Feature",
    "FeatureCollection",
    "FeatureCollectionDict",
    "FeatureCollectionTypes",
    "FeatureCollectionTypesDict",
    "FeatureDict",
    "FeaturePropertyKey",
    "GeoPoint",
    "GeoPointDict",
    "Geometry",
    "GeometryCollection",
    "GeometryCollectionDict",
    "GeometryDict",
    "LineString",
    "LineStringCoordinates",
    "LineStringDict",
    "LinearRing",
    "MultiLineString",
    "MultiLineStringDict",
    "MultiPoint",
    "MultiPointDict",
    "MultiPolygon",
    "MultiPolygonDict",
    "Polygon",
    "PolygonDict",
    "Position",
]
