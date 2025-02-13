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

from foundry.v2.core.models._media_item_read_token import MediaItemReadToken
from foundry.v2.core.models._media_item_rid import MediaItemRid
from foundry.v2.core.models._media_set_rid import MediaSetRid
from foundry.v2.core.models._media_set_view_item_dict import MediaSetViewItemDict
from foundry.v2.core.models._media_set_view_rid import MediaSetViewRid


class MediaSetViewItem(pydantic.BaseModel):
    """MediaSetViewItem"""

    media_set_rid: MediaSetRid = pydantic.Field(alias=str("mediaSetRid"))  # type: ignore[literal-required]

    media_set_view_rid: MediaSetViewRid = pydantic.Field(alias=str("mediaSetViewRid"))  # type: ignore[literal-required]

    media_item_rid: MediaItemRid = pydantic.Field(alias=str("mediaItemRid"))  # type: ignore[literal-required]

    token: Optional[MediaItemReadToken] = None

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> MediaSetViewItemDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(MediaSetViewItemDict, self.model_dump(by_alias=True, exclude_none=True))
