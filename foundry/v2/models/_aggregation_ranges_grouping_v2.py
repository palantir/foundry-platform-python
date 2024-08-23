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

from foundry.v2.models._aggregation_range_v2 import AggregationRangeV2
from foundry.v2.models._aggregation_ranges_grouping_v2_dict import (
    AggregationRangesGroupingV2Dict,
)  # NOQA
from foundry.v2.models._property_api_name import PropertyApiName


class AggregationRangesGroupingV2(BaseModel):
    """Divides objects into groups according to specified ranges."""

    field: PropertyApiName

    ranges: List[AggregationRangeV2]

    type: Literal["ranges"]

    model_config = {"extra": "allow"}

    def to_dict(self) -> AggregationRangesGroupingV2Dict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(
            AggregationRangesGroupingV2Dict, self.model_dump(by_alias=True, exclude_unset=True)
        )
