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
from typing import cast

import pydantic

from foundry.v2.orchestration.models._search_builds_order_by_dict import (
    SearchBuildsOrderByDict,
)  # NOQA
from foundry.v2.orchestration.models._search_builds_order_by_item import (
    SearchBuildsOrderByItem,
)  # NOQA


class SearchBuildsOrderBy(pydantic.BaseModel):
    """SearchBuildsOrderBy"""

    fields: List[SearchBuildsOrderByItem]

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> SearchBuildsOrderByDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(SearchBuildsOrderByDict, self.model_dump(by_alias=True, exclude_none=True))
