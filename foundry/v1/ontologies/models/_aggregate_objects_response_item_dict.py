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

from typing_extensions import TypedDict

from foundry.v1.ontologies.models._aggregation_group_key import AggregationGroupKey
from foundry.v1.ontologies.models._aggregation_group_value import AggregationGroupValue
from foundry.v1.ontologies.models._aggregation_metric_result_dict import (
    AggregationMetricResultDict,
)  # NOQA


class AggregateObjectsResponseItemDict(TypedDict):
    """AggregateObjectsResponseItem"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    group: Dict[AggregationGroupKey, AggregationGroupValue]

    metrics: List[AggregationMetricResultDict]
