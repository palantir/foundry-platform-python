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

from foundry.models._approximate_distinct_aggregation_v2_dict import (
    ApproximateDistinctAggregationV2Dict,
)  # NOQA
from foundry.models._approximate_percentile_aggregation_v2_dict import (
    ApproximatePercentileAggregationV2Dict,
)  # NOQA
from foundry.models._avg_aggregation_v2_dict import AvgAggregationV2Dict
from foundry.models._count_aggregation_v2_dict import CountAggregationV2Dict
from foundry.models._max_aggregation_v2_dict import MaxAggregationV2Dict
from foundry.models._min_aggregation_v2_dict import MinAggregationV2Dict
from foundry.models._sum_aggregation_v2_dict import SumAggregationV2Dict

AggregationV2Dict = Annotated[
    Union[
        MaxAggregationV2Dict,
        MinAggregationV2Dict,
        AvgAggregationV2Dict,
        SumAggregationV2Dict,
        CountAggregationV2Dict,
        ApproximateDistinctAggregationV2Dict,
        ApproximatePercentileAggregationV2Dict,
    ],
    Field(discriminator="type"),
]
"""Specifies an aggregation function."""
