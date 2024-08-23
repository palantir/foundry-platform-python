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

from typing import cast

from pydantic import BaseModel
from pydantic import Field

from foundry.v1.models._bounding_box_value_dict import BoundingBoxValueDict
from foundry.v1.models._within_bounding_box_point import WithinBoundingBoxPoint


class BoundingBoxValue(BaseModel):
    """The top left and bottom right coordinate points that make up the bounding box."""

    top_left: WithinBoundingBoxPoint = Field(alias="topLeft")

    bottom_right: WithinBoundingBoxPoint = Field(alias="bottomRight")

    model_config = {"extra": "allow"}

    def to_dict(self) -> BoundingBoxValueDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(BoundingBoxValueDict, self.model_dump(by_alias=True, exclude_unset=True))
