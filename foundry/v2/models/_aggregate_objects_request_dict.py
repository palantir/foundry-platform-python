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

from typing import List

from typing_extensions import NotRequired
from typing_extensions import TypedDict

from foundry.v2.models._aggregation_dict import AggregationDict
from foundry.v2.models._aggregation_group_by_dict import AggregationGroupByDict
from foundry.v2.models._search_json_query_dict import SearchJsonQueryDict


class AggregateObjectsRequestDict(TypedDict):
    """AggregateObjectsRequest"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    aggregation: List[AggregationDict]

    query: NotRequired[SearchJsonQueryDict]

    groupBy: List[AggregationGroupByDict]
