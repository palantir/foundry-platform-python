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
from typing import Optional
from typing import cast

from pydantic import BaseModel
from pydantic import Field

from foundry.v1.models._page_size import PageSize
from foundry.v1.models._page_token import PageToken
from foundry.v1.models._property_api_name import PropertyApiName
from foundry.v1.models._search_json_query import SearchJsonQuery
from foundry.v1.models._search_objects_request_dict import SearchObjectsRequestDict
from foundry.v1.models._search_order_by import SearchOrderBy


class SearchObjectsRequest(BaseModel):
    """SearchObjectsRequest"""

    query: SearchJsonQuery

    order_by: Optional[SearchOrderBy] = Field(alias="orderBy", default=None)

    page_size: Optional[PageSize] = Field(alias="pageSize", default=None)

    page_token: Optional[PageToken] = Field(alias="pageToken", default=None)

    fields: List[PropertyApiName]
    """The API names of the object type properties to include in the response."""

    model_config = {"extra": "allow"}

    def to_dict(self) -> SearchObjectsRequestDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(SearchObjectsRequestDict, self.model_dump(by_alias=True, exclude_unset=True))
