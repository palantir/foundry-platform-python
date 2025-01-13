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

from foundry.v2.admin.models._marking_role import MarkingRole
from foundry.v2.admin.models._marking_role_assignment_dict import MarkingRoleAssignmentDict  # NOQA
from foundry.v2.core.models._principal_id import PrincipalId
from foundry.v2.core.models._principal_type import PrincipalType


class MarkingRoleAssignment(pydantic.BaseModel):
    """MarkingRoleAssignment"""

    principal_type: PrincipalType = pydantic.Field(alias="principalType")

    principal_id: PrincipalId = pydantic.Field(alias="principalId")

    role: MarkingRole

    model_config = {"extra": "allow"}

    def to_dict(self) -> MarkingRoleAssignmentDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(MarkingRoleAssignmentDict, self.model_dump(by_alias=True, exclude_unset=True))
