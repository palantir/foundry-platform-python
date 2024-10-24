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
from typing import cast

import pydantic

from foundry.v2.admin.models._get_user_markings_response_dict import (
    GetUserMarkingsResponseDict,
)  # NOQA
from foundry.v2.core.models._marking_id import MarkingId


class GetUserMarkingsResponse(pydantic.BaseModel):
    """GetUserMarkingsResponse"""

    view: List[MarkingId]
    """
    The markings that the user has access to. The user will be able to access resources protected with these
    markings. This includes organization markings for organizations in which the user is a guest member.
    """

    model_config = {"extra": "allow"}

    def to_dict(self) -> GetUserMarkingsResponseDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(GetUserMarkingsResponseDict, self.model_dump(by_alias=True, exclude_unset=True))
