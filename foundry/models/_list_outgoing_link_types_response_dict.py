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

from typing_extensions import NotRequired
from typing_extensions import TypedDict

from foundry.models._link_type_side_dict import LinkTypeSideDict
from foundry.models._page_token import PageToken


class ListOutgoingLinkTypesResponseDict(TypedDict):
    """ListOutgoingLinkTypesResponse"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    nextPageToken: NotRequired[PageToken]

    data: List[LinkTypeSideDict]
    """The list of link type sides in the current page."""
