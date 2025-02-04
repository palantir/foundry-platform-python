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

from foundry.v2.ontologies.models._get_selected_property_operation_dict import (
    GetSelectedPropertyOperationDict,
)  # NOQA
from foundry.v2.ontologies.models._selected_property_approximate_distinct_aggregation_dict import (
    SelectedPropertyApproximateDistinctAggregationDict,
)  # NOQA
from foundry.v2.ontologies.models._selected_property_approximate_percentile_aggregation_dict import (
    SelectedPropertyApproximatePercentileAggregationDict,
)  # NOQA
from foundry.v2.ontologies.models._selected_property_avg_aggregation_dict import (
    SelectedPropertyAvgAggregationDict,
)  # NOQA
from foundry.v2.ontologies.models._selected_property_collect_list_aggregation_dict import (
    SelectedPropertyCollectListAggregationDict,
)  # NOQA
from foundry.v2.ontologies.models._selected_property_collect_set_aggregation_dict import (
    SelectedPropertyCollectSetAggregationDict,
)  # NOQA
from foundry.v2.ontologies.models._selected_property_count_aggregation_dict import (
    SelectedPropertyCountAggregationDict,
)  # NOQA
from foundry.v2.ontologies.models._selected_property_exact_distinct_aggregation_dict import (
    SelectedPropertyExactDistinctAggregationDict,
)  # NOQA
from foundry.v2.ontologies.models._selected_property_max_aggregation_dict import (
    SelectedPropertyMaxAggregationDict,
)  # NOQA
from foundry.v2.ontologies.models._selected_property_min_aggregation_dict import (
    SelectedPropertyMinAggregationDict,
)  # NOQA
from foundry.v2.ontologies.models._selected_property_sum_aggregation_dict import (
    SelectedPropertySumAggregationDict,
)  # NOQA

SelectedPropertyOperationDict = Annotated[
    Union[
        SelectedPropertyApproximateDistinctAggregationDict,
        SelectedPropertyMinAggregationDict,
        SelectedPropertyAvgAggregationDict,
        SelectedPropertyMaxAggregationDict,
        SelectedPropertyApproximatePercentileAggregationDict,
        GetSelectedPropertyOperationDict,
        SelectedPropertyCountAggregationDict,
        SelectedPropertySumAggregationDict,
        SelectedPropertyCollectListAggregationDict,
        SelectedPropertyExactDistinctAggregationDict,
        SelectedPropertyCollectSetAggregationDict,
    ],
    pydantic.Field(discriminator="type"),
]
"""Operation on a selected property, can be an aggregation function or retrieval of a single selected property"""
