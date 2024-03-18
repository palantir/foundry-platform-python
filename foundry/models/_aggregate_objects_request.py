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
from typing import TypedDict

from typing_extensions import NotRequired


from foundry.models._aggregation_group_by_request import AggregationGroupByRequest
from foundry.models._aggregation_request import AggregationRequest
from foundry.models._search_json_query_request import SearchJsonQueryRequest


class AggregateObjectsRequest(TypedDict):
    """AggregateObjectsRequest"""

    __pydantic_config__ = {"extra": "forbid"}  # type: ignore

    aggregation: NotRequired[List[AggregationRequest]]

    query: NotRequired[SearchJsonQueryRequest]
    """SearchJsonQueryRequest"""

    groupBy: NotRequired[List[AggregationGroupByRequest]]
