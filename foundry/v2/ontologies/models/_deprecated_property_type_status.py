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
from typing import Literal
from typing import Optional
from typing import cast

import pydantic

from foundry.v2.ontologies.models._deprecated_property_type_status_dict import (
    DeprecatedPropertyTypeStatusDict,
)  # NOQA
from foundry.v2.ontologies.models._property_type_rid import PropertyTypeRid


class DeprecatedPropertyTypeStatus(pydantic.BaseModel):
    """
    This status indicates that the PropertyType is reaching the end of its life and will be removed as per the
    deadline specified.
    """

    message: str

    deadline: datetime

    replaced_by: Optional[PropertyTypeRid] = pydantic.Field(alias=str("replacedBy"), default=None)  # type: ignore[literal-required]

    type: Literal["deprecated"] = "deprecated"

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> DeprecatedPropertyTypeStatusDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(
            DeprecatedPropertyTypeStatusDict, self.model_dump(by_alias=True, exclude_none=True)
        )
