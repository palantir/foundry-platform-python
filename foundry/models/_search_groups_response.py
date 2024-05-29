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

from foundry.models._group import Group
from foundry.models._page_token import PageToken
from foundry.models._search_groups_response_dict import SearchGroupsResponseDict


class SearchGroupsResponse(BaseModel):
    """SearchGroupsResponse"""

    data: List[Group]

    next_page_token: Optional[PageToken] = Field(alias="nextPageToken", default=None)

    model_config = {"extra": "allow"}

    def to_dict(self) -> SearchGroupsResponseDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(SearchGroupsResponseDict, self.model_dump(by_alias=True, exclude_unset=True))
