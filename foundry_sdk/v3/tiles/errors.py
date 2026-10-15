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


import typing
from dataclasses import dataclass

import typing_extensions

from foundry_sdk import _errors as errors
from foundry_sdk.v3.tiles import models as tiles_models


class MaxElevationPointCountExceededParameters(typing_extensions.TypedDict):
    """
    The request contained more points than a single elevation computation allows. Reduce the number of
    points, or split the points across multiple requests.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    maxElevationPointCount: int
    """The maximum number of points allowed in a single elevation computation."""


@dataclass
class MaxElevationPointCountExceeded(errors.BadRequestError):
    name: typing.Literal["MaxElevationPointCountExceeded"]
    parameters: MaxElevationPointCountExceededParameters
    error_instance_id: str


class TileSourceCapabilityNotSupportedParameters(typing_extensions.TypedDict):
    """
    The tile source cannot compute elevation because it does not provide elevation data. Use the
    list operation with `capability=ELEVATION` to find sources that can.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    tileSourceId: tiles_models.TileSourceId
    capability: tiles_models.Capability


@dataclass
class TileSourceCapabilityNotSupported(errors.BadRequestError):
    name: typing.Literal["TileSourceCapabilityNotSupported"]
    parameters: TileSourceCapabilityNotSupportedParameters
    error_instance_id: str


class TileSourceNotFoundParameters(typing_extensions.TypedDict):

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    tileSourceId: tiles_models.TileSourceId


@dataclass
class TileSourceNotFound(errors.NotFoundError):
    name: typing.Literal["TileSourceNotFound"]
    parameters: TileSourceNotFoundParameters
    error_instance_id: str


__all__ = [
    "MaxElevationPointCountExceeded",
    "TileSourceCapabilityNotSupported",
    "TileSourceNotFound",
]
