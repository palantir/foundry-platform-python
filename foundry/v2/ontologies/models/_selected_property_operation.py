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

from foundry.v2.ontologies.models._get_selected_property_operation import (
    GetSelectedPropertyOperation,
)  # NOQA
from foundry.v2.ontologies.models._selected_property_approximate_distinct_aggregation import (
    SelectedPropertyApproximateDistinctAggregation,
)  # NOQA
from foundry.v2.ontologies.models._selected_property_approximate_percentile_aggregation import (
    SelectedPropertyApproximatePercentileAggregation,
)  # NOQA
from foundry.v2.ontologies.models._selected_property_avg_aggregation import (
    SelectedPropertyAvgAggregation,
)  # NOQA
from foundry.v2.ontologies.models._selected_property_collect_list_aggregation import (
    SelectedPropertyCollectListAggregation,
)  # NOQA
from foundry.v2.ontologies.models._selected_property_collect_set_aggregation import (
    SelectedPropertyCollectSetAggregation,
)  # NOQA
from foundry.v2.ontologies.models._selected_property_count_aggregation import (
    SelectedPropertyCountAggregation,
)  # NOQA
from foundry.v2.ontologies.models._selected_property_exact_distinct_aggregation import (
    SelectedPropertyExactDistinctAggregation,
)  # NOQA
from foundry.v2.ontologies.models._selected_property_max_aggregation import (
    SelectedPropertyMaxAggregation,
)  # NOQA
from foundry.v2.ontologies.models._selected_property_min_aggregation import (
    SelectedPropertyMinAggregation,
)  # NOQA
from foundry.v2.ontologies.models._selected_property_sum_aggregation import (
    SelectedPropertySumAggregation,
)  # NOQA

SelectedPropertyOperation = Annotated[
    Union[
        SelectedPropertyApproximateDistinctAggregation,
        SelectedPropertyMinAggregation,
        SelectedPropertyAvgAggregation,
        SelectedPropertyMaxAggregation,
        SelectedPropertyApproximatePercentileAggregation,
        GetSelectedPropertyOperation,
        SelectedPropertyCountAggregation,
        SelectedPropertySumAggregation,
        SelectedPropertyCollectListAggregation,
        SelectedPropertyExactDistinctAggregation,
        SelectedPropertyCollectSetAggregation,
    ],
    pydantic.Field(discriminator="type"),
]
"""Operation on a selected property, can be an aggregation function or retrieval of a single selected property"""
