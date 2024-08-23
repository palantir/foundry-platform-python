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

from foundry.v2.models._aggregate_objects_response_item_v2_dict import (
    AggregateObjectsResponseItemV2Dict,
)  # NOQA
from foundry.v2.models._aggregation_group_key_v2 import AggregationGroupKeyV2
from foundry.v2.models._aggregation_group_value_v2 import AggregationGroupValueV2
from foundry.v2.models._aggregation_metric_result_v2 import AggregationMetricResultV2


class AggregateObjectsResponseItemV2(BaseModel):
    """AggregateObjectsResponseItemV2"""

    group: Dict[AggregationGroupKeyV2, AggregationGroupValueV2]

    metrics: List[AggregationMetricResultV2]

    model_config = {"extra": "allow"}

    def to_dict(self) -> AggregateObjectsResponseItemV2Dict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(
            AggregateObjectsResponseItemV2Dict, self.model_dump(by_alias=True, exclude_unset=True)
        )
