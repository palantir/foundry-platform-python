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

from pydantic import BaseModel
from pydantic import Field

from foundry.v2.models._branch_name import BranchName
from foundry.v2.models._media_set_rid import MediaSetRid
from foundry.v2.models._media_set_updated_trigger_dict import MediaSetUpdatedTriggerDict


class MediaSetUpdatedTrigger(BaseModel):
    """
    Trigger whenever an update is made to a media set on the target
    branch. For transactional media sets, this happens when a transaction
    is committed. For non-transactional media sets, this event happens
    eventually (but not necessary immediately) after an update.
    """

    media_set_rid: MediaSetRid = Field(alias="mediaSetRid")

    branch_name: BranchName = Field(alias="branchName")

    type: Literal["mediaSetUpdated"]

    model_config = {"extra": "allow"}

    def to_dict(self) -> MediaSetUpdatedTriggerDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(MediaSetUpdatedTriggerDict, self.model_dump(by_alias=True, exclude_unset=True))
