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

from foundry.v2.core.models._principal_id import PrincipalId
from foundry.v2.core.models._principal_type import PrincipalType
from foundry.v2.filesystem.models._principal_with_id_dict import PrincipalWithIdDict


class PrincipalWithId(pydantic.BaseModel):
    """Represents a user principal or group principal with an ID."""

    principal_id: PrincipalId = pydantic.Field(alias=str("principalId"))  # type: ignore[literal-required]

    principal_type: PrincipalType = pydantic.Field(alias=str("principalType"))  # type: ignore[literal-required]

    type: Literal["principalWithId"] = "principalWithId"

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> PrincipalWithIdDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(PrincipalWithIdDict, self.model_dump(by_alias=True, exclude_none=True))
