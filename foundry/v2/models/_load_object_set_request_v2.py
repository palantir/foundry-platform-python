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
from pydantic import StrictBool

from foundry.v2.models._load_object_set_request_v2_dict import LoadObjectSetRequestV2Dict  # NOQA
from foundry.v2.models._object_set import ObjectSet
from foundry.v2.models._page_size import PageSize
from foundry.v2.models._page_token import PageToken
from foundry.v2.models._search_order_by_v2 import SearchOrderByV2
from foundry.v2.models._selected_property_api_name import SelectedPropertyApiName


class LoadObjectSetRequestV2(BaseModel):
    """Represents the API POST body when loading an `ObjectSet`."""

    object_set: ObjectSet = Field(alias="objectSet")

    order_by: Optional[SearchOrderByV2] = Field(alias="orderBy", default=None)

    select: List[SelectedPropertyApiName]

    page_token: Optional[PageToken] = Field(alias="pageToken", default=None)

    page_size: Optional[PageSize] = Field(alias="pageSize", default=None)

    exclude_rid: Optional[StrictBool] = Field(alias="excludeRid", default=None)
    """
    A flag to exclude the retrieval of the `__rid` property.
    Setting this to true may improve performance of this endpoint for object types in OSV2.
    """

    model_config = {"extra": "allow"}

    def to_dict(self) -> LoadObjectSetRequestV2Dict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(LoadObjectSetRequestV2Dict, self.model_dump(by_alias=True, exclude_unset=True))
