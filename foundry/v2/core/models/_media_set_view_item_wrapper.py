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

from typing import Literal
from typing import cast

import pydantic

from foundry.v2.core.models._media_set_view_item import MediaSetViewItem
from foundry.v2.core.models._media_set_view_item_wrapper_dict import (
    MediaSetViewItemWrapperDict,
)  # NOQA


class MediaSetViewItemWrapper(pydantic.BaseModel):
    """MediaSetViewItemWrapper"""

    media_set_view_item: MediaSetViewItem = pydantic.Field(alias=str("mediaSetViewItem"))  # type: ignore[literal-required]

    type: Literal["mediaSetViewItem"] = "mediaSetViewItem"

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> MediaSetViewItemWrapperDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(MediaSetViewItemWrapperDict, self.model_dump(by_alias=True, exclude_none=True))
