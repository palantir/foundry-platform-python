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
from typing import cast

from pydantic import BaseModel

from foundry.v1.models._aggregation_range import AggregationRange
from foundry.v1.models._aggregation_ranges_grouping_dict import (
    AggregationRangesGroupingDict,
)  # NOQA
from foundry.v1.models._field_name_v1 import FieldNameV1


class AggregationRangesGrouping(BaseModel):
    """Divides objects into groups according to specified ranges."""

    field: FieldNameV1

    ranges: List[AggregationRange]

    type: Literal["ranges"]

    model_config = {"extra": "allow"}

    def to_dict(self) -> AggregationRangesGroupingDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(
            AggregationRangesGroupingDict, self.model_dump(by_alias=True, exclude_unset=True)
        )
