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

from typing import Any
from typing import cast

import pydantic

from foundry.v2.ontologies.models._aggregation_range_v2_dict import AggregationRangeV2Dict  # NOQA


class AggregationRangeV2(pydantic.BaseModel):
    """Specifies a range from an inclusive start value to an exclusive end value."""

    start_value: Any = pydantic.Field(alias=str("startValue"))  # type: ignore[literal-required]

    """Inclusive start."""

    end_value: Any = pydantic.Field(alias=str("endValue"))  # type: ignore[literal-required]

    """Exclusive end."""

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> AggregationRangeV2Dict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(AggregationRangeV2Dict, self.model_dump(by_alias=True, exclude_none=True))
