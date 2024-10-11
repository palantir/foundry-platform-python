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

from foundry.v1.ontologies.models._approximate_distinct_aggregation_dict import (
    ApproximateDistinctAggregationDict,
)  # NOQA
from foundry.v1.ontologies.models._avg_aggregation_dict import AvgAggregationDict
from foundry.v1.ontologies.models._count_aggregation_dict import CountAggregationDict
from foundry.v1.ontologies.models._max_aggregation_dict import MaxAggregationDict
from foundry.v1.ontologies.models._min_aggregation_dict import MinAggregationDict
from foundry.v1.ontologies.models._sum_aggregation_dict import SumAggregationDict

AggregationDict = Annotated[
    Union[
        ApproximateDistinctAggregationDict,
        MinAggregationDict,
        AvgAggregationDict,
        MaxAggregationDict,
        CountAggregationDict,
        SumAggregationDict,
    ],
    pydantic.Field(discriminator="type"),
]
"""Specifies an aggregation function."""
