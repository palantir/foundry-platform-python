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

from typing import Any
from typing import Dict
from typing import Literal

from typing_extensions import NotRequired
from typing_extensions import TypedDict

from foundry.v2.models._b_box import BBox
from foundry.v2.models._feature_property_key import FeaturePropertyKey
from foundry.v2.models._geometry_dict import GeometryDict


class FeatureDict(TypedDict):
    """GeoJSon 'Feature' object"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    geometry: NotRequired[GeometryDict]

    properties: Dict[FeaturePropertyKey, Any]
    """
    A `Feature` object has a member with the name "properties".  The
    value of the properties member is an object (any JSON object or a
    JSON null value).
    """

    id: NotRequired[Any]
    """
    If a `Feature` has a commonly used identifier, that identifier
    SHOULD be included as a member of the Feature object with the name
    "id", and the value of this member is either a JSON string or
    number.
    """

    bbox: NotRequired[BBox]

    type: Literal["Feature"]
