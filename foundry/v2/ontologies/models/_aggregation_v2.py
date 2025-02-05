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

from typing import Union

import pydantic
from typing_extensions import Annotated

from foundry.v2.ontologies.models._approximate_distinct_aggregation_v2 import (
    ApproximateDistinctAggregationV2,
)  # NOQA
from foundry.v2.ontologies.models._approximate_percentile_aggregation_v2 import (
    ApproximatePercentileAggregationV2,
)  # NOQA
from foundry.v2.ontologies.models._avg_aggregation_v2 import AvgAggregationV2
from foundry.v2.ontologies.models._count_aggregation_v2 import CountAggregationV2
from foundry.v2.ontologies.models._exact_distinct_aggregation_v2 import (
    ExactDistinctAggregationV2,
)  # NOQA
from foundry.v2.ontologies.models._max_aggregation_v2 import MaxAggregationV2
from foundry.v2.ontologies.models._min_aggregation_v2 import MinAggregationV2
from foundry.v2.ontologies.models._sum_aggregation_v2 import SumAggregationV2

AggregationV2 = Annotated[
    Union[
        ApproximateDistinctAggregationV2,
        MinAggregationV2,
        AvgAggregationV2,
        MaxAggregationV2,
        ApproximatePercentileAggregationV2,
        CountAggregationV2,
        SumAggregationV2,
        ExactDistinctAggregationV2,
    ],
    pydantic.Field(discriminator="type"),
]
"""Specifies an aggregation function."""
