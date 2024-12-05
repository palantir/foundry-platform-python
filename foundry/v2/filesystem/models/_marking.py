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

from typing import cast

import pydantic

from foundry.v2.core.models._marking_id import MarkingId
from foundry.v2.filesystem.models._is_directly_applied import IsDirectlyApplied
from foundry.v2.filesystem.models._marking_dict import MarkingDict


class Marking(pydantic.BaseModel):
    """
    [Markings](/docs/foundry/security/markings/) provide an additional level of access control for files,
    folders, and Projects within Foundry. Markings define eligibility criteria that restrict visibility
    and actions to users who meet those criteria. To access a resource, a user must be a member of all
    Markings applied to a resource to access it.
    """

    marking_id: MarkingId = pydantic.Field(alias="markingId")

    is_directly_applied: IsDirectlyApplied = pydantic.Field(alias="isDirectlyApplied")

    model_config = {"extra": "allow"}

    def to_dict(self) -> MarkingDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(MarkingDict, self.model_dump(by_alias=True, exclude_unset=True))
