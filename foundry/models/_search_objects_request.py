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


from foundry.models._page_size import PageSize
from foundry.models._page_token import PageToken
from foundry.models._property_api_name import PropertyApiName
from foundry.models._search_json_query_request import SearchJsonQueryRequest
from foundry.models._search_order_by_request import SearchOrderByRequest


class SearchObjectsRequest(TypedDict):
    """SearchObjectsRequest"""

    __pydantic_config__ = {"extra": "forbid"}  # type: ignore

    query: SearchJsonQueryRequest
    """SearchJsonQueryRequest"""

    orderBy: NotRequired[SearchOrderByRequest]
    """Specifies the ordering of search results by a field and an ordering direction."""

    pageSize: NotRequired[PageSize]
    """The page size to use for the endpoint."""

    pageToken: NotRequired[PageToken]
    """
    The page token indicates where to start paging. This should be omitted from the first page's request.
    To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response
    and populate the next request's `pageToken` field with it.
    """

    fields: NotRequired[List[PropertyApiName]]
    """The API names of the object type properties to include in the response."""