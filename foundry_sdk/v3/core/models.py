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

BBox: typing_extensions.TypeAlias = typing.List["Coordinate"]
"""
A rectangular geographic extent, encoded as a GeoJSON bounding box array
`[west, south, east, north]` in WGS84 decimal degrees.
"""


Coordinate: typing_extensions.TypeAlias = float
"""A single ordinate value within a position, such as a longitude, latitude, or elevation."""


CreatedTime: typing_extensions.TypeAlias = core.AwareDatetime
"""CreatedTime"""


FolderRid: typing_extensions.TypeAlias = core.RID
"""The unique resource identifier (RID) of a folder."""


NamespaceRid: typing_extensions.TypeAlias = core.RID
"""The unique resource identifier (RID) of a namespace."""


OntologyRid: typing_extensions.TypeAlias = core.RID
"""The unique resource identifier (RID) of an ontology."""


PageSize: typing_extensions.TypeAlias = int
"""The page size to use for the endpoint."""


PageToken: typing_extensions.TypeAlias = str
"""
The page token indicates where to start paging. This should be omitted from the first page's request.
To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response
and use it to populate the `pageToken` field of the next request.
"""


Position: typing_extensions.TypeAlias = typing.List["Coordinate"]
"""
A GeoJSON position array of either two elements (`[longitude, latitude]`) or three elements
(`[longitude, latitude, elevation]`). Longitude and latitude are represented in WGS84 decimal
degrees and elevation in meters.
"""


PreviewMode: typing_extensions.TypeAlias = bool
"""Enables the use of preview functionality."""


PrincipalId: typing_extensions.TypeAlias = core.UUID
"""The ID of a user or group."""


UpdatedTime: typing_extensions.TypeAlias = core.AwareDatetime
"""UpdatedTime"""


core.resolve_forward_references_in_module(__name__)

__all__ = [
    "BBox",
    "Coordinate",
    "CreatedTime",
    "FolderRid",
    "NamespaceRid",
    "OntologyRid",
    "PageSize",
    "PageToken",
    "Position",
    "PreviewMode",
    "PrincipalId",
    "UpdatedTime",
]
