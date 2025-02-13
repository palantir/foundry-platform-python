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

from typing_extensions import NotRequired
from typing_extensions import TypedDict

from foundry.v2.core.models._media_item_path import MediaItemPath
from foundry.v2.core.models._media_set_view_rid import MediaSetViewRid
from foundry.v2.media_sets.models._logical_timestamp import LogicalTimestamp
from foundry.v2.media_sets.models._media_attribution_dict import MediaAttributionDict


class GetMediaItemInfoResponseDict(TypedDict):
    """GetMediaItemInfoResponse"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    viewRid: MediaSetViewRid

    path: NotRequired[MediaItemPath]

    logicalTimestamp: LogicalTimestamp

    attribution: NotRequired[MediaAttributionDict]
