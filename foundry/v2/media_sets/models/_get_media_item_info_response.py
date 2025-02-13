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

import pydantic

from foundry.v2.core.models._media_item_path import MediaItemPath
from foundry.v2.core.models._media_set_view_rid import MediaSetViewRid
from foundry.v2.media_sets.models._get_media_item_info_response_dict import (
    GetMediaItemInfoResponseDict,
)  # NOQA
from foundry.v2.media_sets.models._logical_timestamp import LogicalTimestamp
from foundry.v2.media_sets.models._media_attribution import MediaAttribution


class GetMediaItemInfoResponse(pydantic.BaseModel):
    """GetMediaItemInfoResponse"""

    view_rid: MediaSetViewRid = pydantic.Field(alias=str("viewRid"))  # type: ignore[literal-required]

    path: Optional[MediaItemPath] = None

    logical_timestamp: LogicalTimestamp = pydantic.Field(alias=str("logicalTimestamp"))  # type: ignore[literal-required]

    attribution: Optional[MediaAttribution] = None

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> GetMediaItemInfoResponseDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(GetMediaItemInfoResponseDict, self.model_dump(by_alias=True, exclude_none=True))
