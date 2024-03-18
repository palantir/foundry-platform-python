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


from foundry.models._approximate_distinct_aggregation_request import (
    ApproximateDistinctAggregationRequest,
)
from foundry.models._avg_aggregation_request import AvgAggregationRequest
from foundry.models._count_aggregation_request import CountAggregationRequest
from foundry.models._max_aggregation_request import MaxAggregationRequest
from foundry.models._min_aggregation_request import MinAggregationRequest
from foundry.models._sum_aggregation_request import SumAggregationRequest


AggregationRequest = Annotated[
    Union[
        ApproximateDistinctAggregationRequest,
        AvgAggregationRequest,
        CountAggregationRequest,
        MaxAggregationRequest,
        MinAggregationRequest,
        SumAggregationRequest,
    ],
    Field(discriminator="type"),
]
"""Specifies an aggregation function."""
