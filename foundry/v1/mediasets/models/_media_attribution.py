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

from datetime import datetime
from typing import cast

import pydantic

from foundry.v1.core.models._user_id import UserId
from foundry.v1.mediasets.models._media_attribution_dict import MediaAttributionDict


class MediaAttribution(pydantic.BaseModel):
    """MediaAttribution"""

    creator_id: UserId = pydantic.Field(alias="creatorId")

    creation_timestamp: datetime = pydantic.Field(alias="creationTimestamp")

    """The timestamp when the media item was created, in ISO 8601 timestamp format."""

    model_config = {"extra": "allow"}

    def to_dict(self) -> MediaAttributionDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(MediaAttributionDict, self.model_dump(by_alias=True, exclude_unset=True))
