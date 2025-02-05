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

from foundry.v1.ontologies.models._aggregation_fixed_width_grouping_dict import (
    AggregationFixedWidthGroupingDict,
)  # NOQA
from foundry.v1.ontologies.models._field_name_v1 import FieldNameV1


class AggregationFixedWidthGrouping(pydantic.BaseModel):
    """Divides objects into groups with the specified width."""

    field: FieldNameV1

    fixed_width: int = pydantic.Field(alias=str("fixedWidth"))  # type: ignore[literal-required]

    type: Literal["fixedWidth"] = "fixedWidth"

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> AggregationFixedWidthGroupingDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(
            AggregationFixedWidthGroupingDict, self.model_dump(by_alias=True, exclude_none=True)
        )
