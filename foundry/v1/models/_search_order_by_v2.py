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

from pydantic import BaseModel

from foundry.v1.models._search_order_by_v2_dict import SearchOrderByV2Dict
from foundry.v1.models._search_ordering_v2 import SearchOrderingV2


class SearchOrderByV2(BaseModel):
    """Specifies the ordering of search results by a field and an ordering direction."""

    fields: List[SearchOrderingV2]

    model_config = {"extra": "allow"}

    def to_dict(self) -> SearchOrderByV2Dict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(SearchOrderByV2Dict, self.model_dump(by_alias=True, exclude_unset=True))
