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

from foundry.v2.ontologies.models._search_order_by_type import SearchOrderByType
from foundry.v2.ontologies.models._search_ordering_v2_dict import SearchOrderingV2Dict


class SearchOrderByV2Dict(TypedDict):
    """Specifies the ordering of search results by a field and an ordering direction or by relevance if scores are required in a nearestNeighbors query. By default `orderType` is set to `fields`."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    orderType: NotRequired[SearchOrderByType]

    fields: List[SearchOrderingV2Dict]
