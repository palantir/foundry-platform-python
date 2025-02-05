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

from foundry.v2.admin.models._marking_category_id import MarkingCategoryId
from foundry.v2.admin.models._marking_dict import MarkingDict
from foundry.v2.admin.models._marking_name import MarkingName
from foundry.v2.core.models._created_by import CreatedBy
from foundry.v2.core.models._created_time import CreatedTime
from foundry.v2.core.models._marking_id import MarkingId
from foundry.v2.core.models._organization_rid import OrganizationRid


class Marking(pydantic.BaseModel):
    """Marking"""

    id: MarkingId

    category_id: MarkingCategoryId = pydantic.Field(alias=str("categoryId"))  # type: ignore[literal-required]

    name: MarkingName

    description: Optional[str] = None

    organization: Optional[OrganizationRid] = None

    """If this marking is associated with an Organization, its RID will be populated here."""

    created_time: CreatedTime = pydantic.Field(alias=str("createdTime"))  # type: ignore[literal-required]

    created_by: Optional[CreatedBy] = pydantic.Field(alias=str("createdBy"), default=None)  # type: ignore[literal-required]

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> MarkingDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(MarkingDict, self.model_dump(by_alias=True, exclude_none=True))
