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

from typing import Annotated
from typing import Union

from pydantic import Field

from foundry.v1.models._approximate_distinct_aggregation_v2 import (
    ApproximateDistinctAggregationV2,
)  # NOQA
from foundry.v1.models._approximate_percentile_aggregation_v2 import (
    ApproximatePercentileAggregationV2,
)  # NOQA
from foundry.v1.models._avg_aggregation_v2 import AvgAggregationV2
from foundry.v1.models._count_aggregation_v2 import CountAggregationV2
from foundry.v1.models._exact_distinct_aggregation_v2 import ExactDistinctAggregationV2
from foundry.v1.models._max_aggregation_v2 import MaxAggregationV2
from foundry.v1.models._min_aggregation_v2 import MinAggregationV2
from foundry.v1.models._sum_aggregation_v2 import SumAggregationV2

AggregationV2 = Annotated[
    Union[
        MaxAggregationV2,
        MinAggregationV2,
        AvgAggregationV2,
        SumAggregationV2,
        CountAggregationV2,
        ApproximateDistinctAggregationV2,
        ApproximatePercentileAggregationV2,
        ExactDistinctAggregationV2,
    ],
    Field(discriminator="type"),
]
"""Specifies an aggregation function."""
