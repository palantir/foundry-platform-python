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

from foundry.v2.ontologies.models._aggregation_duration_grouping_v2_dict import (
    AggregationDurationGroupingV2Dict,
)  # NOQA
from foundry.v2.ontologies.models._aggregation_exact_grouping_v2_dict import (
    AggregationExactGroupingV2Dict,
)  # NOQA
from foundry.v2.ontologies.models._aggregation_fixed_width_grouping_v2_dict import (
    AggregationFixedWidthGroupingV2Dict,
)  # NOQA
from foundry.v2.ontologies.models._aggregation_ranges_grouping_v2_dict import (
    AggregationRangesGroupingV2Dict,
)  # NOQA

AggregationGroupByV2Dict = Annotated[
    Union[
        AggregationDurationGroupingV2Dict,
        AggregationFixedWidthGroupingV2Dict,
        AggregationRangesGroupingV2Dict,
        AggregationExactGroupingV2Dict,
    ],
    pydantic.Field(discriminator="type"),
]
"""Specifies a grouping for aggregation results."""
