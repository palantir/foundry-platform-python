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
from typing import Optional
from typing import cast

import pydantic

from foundry.v2.ontologies.models._aggregation_exact_grouping_v2_dict import (
    AggregationExactGroupingV2Dict,
)  # NOQA
from foundry.v2.ontologies.models._property_api_name import PropertyApiName


class AggregationExactGroupingV2(pydantic.BaseModel):
    """Divides objects into groups according to an exact value."""

    field: PropertyApiName

    max_group_count: Optional[int] = pydantic.Field(alias=str("maxGroupCount"), default=None)  # type: ignore[literal-required]

    default_value: Optional[str] = pydantic.Field(alias=str("defaultValue"), default=None)  # type: ignore[literal-required]

    type: Literal["exact"] = "exact"

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> AggregationExactGroupingV2Dict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(
            AggregationExactGroupingV2Dict, self.model_dump(by_alias=True, exclude_none=True)
        )
