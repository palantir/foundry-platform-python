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

from pydantic import StrictBool
from typing_extensions import NotRequired
from typing_extensions import TypedDict

from foundry.v1.models._object_set_dict import ObjectSetDict
from foundry.v1.models._page_size import PageSize
from foundry.v1.models._page_token import PageToken
from foundry.v1.models._search_order_by_v2_dict import SearchOrderByV2Dict
from foundry.v1.models._selected_property_api_name import SelectedPropertyApiName


class LoadObjectSetRequestV2Dict(TypedDict):
    """Represents the API POST body when loading an `ObjectSet`."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    objectSet: ObjectSetDict

    orderBy: NotRequired[SearchOrderByV2Dict]

    select: List[SelectedPropertyApiName]

    pageToken: NotRequired[PageToken]

    pageSize: NotRequired[PageSize]

    excludeRid: NotRequired[StrictBool]
    """
    A flag to exclude the retrieval of the `__rid` property.
    Setting this to true may improve performance of this endpoint for object types in OSV2.
    """
