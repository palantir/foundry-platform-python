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

from foundry.v1.ontologies.models._aggregation_duration_grouping_dict import (
    AggregationDurationGroupingDict,
)  # NOQA
from foundry.v1.ontologies.models._aggregation_exact_grouping_dict import (
    AggregationExactGroupingDict,
)  # NOQA
from foundry.v1.ontologies.models._aggregation_fixed_width_grouping_dict import (
    AggregationFixedWidthGroupingDict,
)  # NOQA
from foundry.v1.ontologies.models._aggregation_ranges_grouping_dict import (
    AggregationRangesGroupingDict,
)  # NOQA

AggregationGroupByDict = Annotated[
    Union[
        AggregationDurationGroupingDict,
        AggregationFixedWidthGroupingDict,
        AggregationRangesGroupingDict,
        AggregationExactGroupingDict,
    ],
    pydantic.Field(discriminator="type"),
]
"""Specifies a grouping for aggregation results."""
