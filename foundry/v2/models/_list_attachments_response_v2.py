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
from typing import Literal
from typing import Optional
from typing import cast

from pydantic import BaseModel
from pydantic import Field

from foundry.v2.models._attachment_v2 import AttachmentV2
from foundry.v2.models._list_attachments_response_v2_dict import (
    ListAttachmentsResponseV2Dict,
)  # NOQA
from foundry.v2.models._page_token import PageToken


class ListAttachmentsResponseV2(BaseModel):
    """ListAttachmentsResponseV2"""

    data: List[AttachmentV2]

    next_page_token: Optional[PageToken] = Field(alias="nextPageToken", default=None)

    type: Literal["multiple"]

    model_config = {"extra": "allow"}

    def to_dict(self) -> ListAttachmentsResponseV2Dict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(
            ListAttachmentsResponseV2Dict, self.model_dump(by_alias=True, exclude_unset=True)
        )
