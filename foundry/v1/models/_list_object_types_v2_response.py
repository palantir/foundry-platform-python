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

from foundry.v1.models._list_object_types_v2_response_dict import (
    ListObjectTypesV2ResponseDict,
)  # NOQA
from foundry.v1.models._object_type_v2 import ObjectTypeV2
from foundry.v1.models._page_token import PageToken


class ListObjectTypesV2Response(BaseModel):
    """ListObjectTypesV2Response"""

    next_page_token: Optional[PageToken] = Field(alias="nextPageToken", default=None)

    data: List[ObjectTypeV2]
    """The list of object types in the current page."""

    model_config = {"extra": "allow"}

    def to_dict(self) -> ListObjectTypesV2ResponseDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(
            ListObjectTypesV2ResponseDict, self.model_dump(by_alias=True, exclude_unset=True)
        )