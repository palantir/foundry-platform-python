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
from typing import cast

from pydantic import BaseModel

from foundry.v2.ontologies.models._bounding_box_value import BoundingBoxValue
from foundry.v2.ontologies.models._does_not_intersect_bounding_box_query_dict import (
    DoesNotIntersectBoundingBoxQueryDict,
)  # NOQA
from foundry.v2.ontologies.models._property_api_name import PropertyApiName


class DoesNotIntersectBoundingBoxQuery(BaseModel):
    """Returns objects where the specified field does not intersect the bounding box provided."""

    field: PropertyApiName

    value: BoundingBoxValue

    type: Literal["doesNotIntersectBoundingBox"]

    model_config = {"extra": "allow"}

    def to_dict(self) -> DoesNotIntersectBoundingBoxQueryDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(
            DoesNotIntersectBoundingBoxQueryDict, self.model_dump(by_alias=True, exclude_unset=True)
        )
