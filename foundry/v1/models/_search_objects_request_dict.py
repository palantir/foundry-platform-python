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

from foundry.v1.models._page_size import PageSize
from foundry.v1.models._page_token import PageToken
from foundry.v1.models._property_api_name import PropertyApiName
from foundry.v1.models._search_json_query_dict import SearchJsonQueryDict
from foundry.v1.models._search_order_by_dict import SearchOrderByDict


class SearchObjectsRequestDict(TypedDict):
    """SearchObjectsRequest"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    query: SearchJsonQueryDict

    orderBy: NotRequired[SearchOrderByDict]

    pageSize: NotRequired[PageSize]

    pageToken: NotRequired[PageToken]

    fields: List[PropertyApiName]
    """The API names of the object type properties to include in the response."""
