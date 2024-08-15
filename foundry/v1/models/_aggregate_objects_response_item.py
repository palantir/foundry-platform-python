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

from typing import Dict
from typing import List
from typing import cast

from pydantic import BaseModel

from foundry.v1.models._aggregate_objects_response_item_dict import (
    AggregateObjectsResponseItemDict,
)  # NOQA
from foundry.v1.models._aggregation_group_key import AggregationGroupKey
from foundry.v1.models._aggregation_group_value import AggregationGroupValue
from foundry.v1.models._aggregation_metric_result import AggregationMetricResult


class AggregateObjectsResponseItem(BaseModel):
    """AggregateObjectsResponseItem"""

    group: Dict[AggregationGroupKey, AggregationGroupValue]

    metrics: List[AggregationMetricResult]

    model_config = {"extra": "allow"}

    def to_dict(self) -> AggregateObjectsResponseItemDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(
            AggregateObjectsResponseItemDict, self.model_dump(by_alias=True, exclude_unset=True)
        )
