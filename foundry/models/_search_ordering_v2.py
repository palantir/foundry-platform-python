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

from typing import Optional
from typing import cast

from pydantic import BaseModel
from pydantic import StrictStr

from foundry.models._property_api_name import PropertyApiName
from foundry.models._search_ordering_v2_dict import SearchOrderingV2Dict


class SearchOrderingV2(BaseModel):
    """SearchOrderingV2"""

    field: PropertyApiName

    direction: Optional[StrictStr] = None
    """Specifies the ordering direction (can be either `asc` or `desc`)"""

    model_config = {"extra": "allow"}

    def to_dict(self) -> SearchOrderingV2Dict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(SearchOrderingV2Dict, self.model_dump(by_alias=True, exclude_unset=True))
