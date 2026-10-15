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

import pydantic
import typing_extensions

from foundry_sdk import _core as core
from foundry_sdk.v3.core import models as core_models

Capability: typing_extensions.TypeAlias = typing.Literal[
    "ELEVATION", "IMAGERY_TILES", "VECTOR_TILES", "TERRAIN_TILES"
]
"""
Indicates which operations and tile sets a tile source makes available.

Values:
- **ELEVATION**: The source can answer `computeElevation` queries.
- **IMAGERY_TILES**: The source serves imagery map tiles.
- **TERRAIN_TILES**: The source serves 3D terrain or elevation tiles.
- **VECTOR_TILES**: The source serves vector map tiles.
"""


class ComputeElevationRequest(core.ModelBase):
    """A request to compute elevation at a list of points."""

    points: typing.List[core_models.Position]
    """
    The points to compute elevation for. Results are returned in the same order as the request.
    A request may contain at most 1,000 points by default, though the configured limit may differ;
    exceeding it returns a `MaxElevationPointCountExceeded` error that reports the limit.
    """


class ComputeElevationResponse(core.ModelBase):
    """The elevation results for a batch of requested points."""

    elevations: typing.List[ElevationPointResult]
    """One result per requested point, in the same order as the request."""

    vertical_reference: VerticalReference = pydantic.Field(alias=str("verticalReference"))  # type: ignore[literal-required]
    """
    The vertical reference all elevations in this response are measured against, taken from the
    tile source.
    """


class ElevationPointResult(core.ModelBase):
    """The elevation result for a single requested point."""

    elevation: typing.Optional[float] = None
    """
    The elevation at this point, in meters, relative to the response's `verticalReference`. Empty
    when this source has no elevation data at the point.
    """


class ListTileSourcesResponse(core.ModelBase):
    """ListTileSourcesResponse"""

    data: typing.List[TileSource]
    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]


TileFormat: typing_extensions.TypeAlias = typing.Literal[
    "IMAGERY",
    "MAPBOX_VECTOR_TILE",
    "CESIUM_QUANTIZED_MESH",
    "TERRARIUM_ELEVATION",
    "MAPBOX_ELEVATION",
]
"""
The encoding of the tile data served by a tile set.

Values:
- **CESIUM_QUANTIZED_MESH**: Terrain mesh encoded as Cesium quantized mesh.
- **IMAGERY**: Raster imagery in a standard web image format such as PNG, JPEG, or WebP, ready for display.
- **MAPBOX_ELEVATION**: Elevation data encoded as RGB values in a PNG raster, using the Mapbox encoding.
- **MAPBOX_VECTOR_TILE**: Vector data encoded as Mapbox Vector Tiles.
- **TERRARIUM_ELEVATION**: Elevation data encoded as RGB values in a PNG raster, using the Terrarium encoding.
"""


class TileSet(core.ModelBase):
    """A servable set of tiles for a source, grouping tiles that share a format and layout."""

    format: TileFormat
    """The encoding of the tiles in this set, which also determines the type of tiles the set serves."""

    max_zoom: int = pydantic.Field(alias=str("maxZoom"))  # type: ignore[literal-required]
    """The highest zoom level served by this tile set, inclusive."""

    min_zoom: int = pydantic.Field(alias=str("minZoom"))  # type: ignore[literal-required]
    """The lowest zoom level served by this tile set, inclusive."""

    tiling_scheme: TilingScheme = pydantic.Field(alias=str("tilingScheme"))  # type: ignore[literal-required]


class TileSource(core.ModelBase):
    """
    A source of map data that the platform can serve, such as satellite imagery, vector map layers,
    or elevation models. A source's capabilities indicate which operations it supports.
    """

    attribution: typing.Optional[str] = None
    """
    Attribution text for the source's data, for example a data provider name or copyright notice.
    Empty when the source declares no attribution.
    """

    bounds: typing.Optional[core_models.BBox] = None
    """
    The geographic extent the source covers. Absent when the source has no
    bounded extent, such as a globally-defined or non-geolocated source.
    """

    capabilities: typing.List[Capability]
    description: typing.Optional[str] = None
    """A human-readable description of the source. Empty when the source does not define one."""

    display_name: str = pydantic.Field(alias=str("displayName"))  # type: ignore[literal-required]
    id: TileSourceId
    tile_sets: typing.List[TileSet] = pydantic.Field(alias=str("tileSets"))  # type: ignore[literal-required]
    """The servable tile sets for this source. Empty for sources that serve no tiles."""

    vertical_reference: typing.Optional[VerticalReference] = pydantic.Field(alias=str("verticalReference"), default=None)  # type: ignore[literal-required]
    """
    For elevation-capable sources, the vertical reference that elevations are measured against
    (`WGS84_ELLIPSOID`, `MEAN_SEA_LEVEL`, `UNKNOWN`). Absent for sources that do not provide elevation.
    """


TileSourceId: typing_extensions.TypeAlias = str
"""The identifier of a tile source. Human-entered when the source is configured."""


TilingScheme: typing_extensions.TypeAlias = typing.Literal[
    "WEB_MERCATOR", "GLOBAL_GEODETIC", "CUSTOM"
]
"""
The layout used to arrange and address the tiles in a tile set.

Values:
- **CUSTOM**: A non-standard tiling scheme specific to the source. Clients that do not recognize the
source's scheme should not assume a standard tile layout.

- **GLOBAL_GEODETIC**: Equirectangular longitude/latitude (EPSG:4326).
- **WEB_MERCATOR**: Web Mercator (EPSG:3857): the standard web-map tiling scheme.
"""


VerticalReference: typing_extensions.TypeAlias = typing.Literal[
    "WGS84_ELLIPSOID", "MEAN_SEA_LEVEL", "UNKNOWN"
]
"""
The reference surface an elevation value is measured against.

Values:
- **MEAN_SEA_LEVEL**: Height above mean sea level (EGM2008 geoid).
- **UNKNOWN**: The source's vertical reference is not known. Elevation values are returned as-is from the
source and should be interpreted with caution.

- **WGS84_ELLIPSOID**: Height above the WGS84 ellipsoid.
"""


core.resolve_forward_references_in_module(__name__)

__all__ = [
    "Capability",
    "ComputeElevationRequest",
    "ComputeElevationResponse",
    "ElevationPointResult",
    "ListTileSourcesResponse",
    "TileFormat",
    "TileSet",
    "TileSource",
    "TileSourceId",
    "TilingScheme",
    "VerticalReference",
]
