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

from foundry.v2.models._action_type_v2 import ActionTypeV2
from foundry.v2.models._list_action_types_response_v2_dict import (
    ListActionTypesResponseV2Dict,
)  # NOQA
from foundry.v2.models._page_token import PageToken


class ListActionTypesResponseV2(BaseModel):
    """ListActionTypesResponseV2"""

    next_page_token: Optional[PageToken] = Field(alias="nextPageToken", default=None)

    data: List[ActionTypeV2]

    model_config = {"extra": "allow"}

    def to_dict(self) -> ListActionTypesResponseV2Dict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(
            ListActionTypesResponseV2Dict, self.model_dump(by_alias=True, exclude_unset=True)
        )
