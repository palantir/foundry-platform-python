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

from typing import Literal

from typing_extensions import TypedDict

from foundry.v2.ontologies.models._center_point_dict import CenterPointDict
from foundry.v2.ontologies.models._property_api_name import PropertyApiName


class WithinDistanceOfQueryDict(TypedDict):
    """Returns objects where the specified field contains a point within the distance provided of the center point."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    field: PropertyApiName

    value: CenterPointDict

    type: Literal["withinDistanceOf"]
