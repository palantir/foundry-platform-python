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
from typing import Optional
from typing import cast

from pydantic import BaseModel

from foundry.v1.models._aggregation_range_dict import AggregationRangeDict


class AggregationRange(BaseModel):
    """Specifies a date range from an inclusive start date to an exclusive end date."""

    lt: Optional[Any] = None
    """Exclusive end date."""

    lte: Optional[Any] = None
    """Inclusive end date."""

    gt: Optional[Any] = None
    """Exclusive start date."""

    gte: Optional[Any] = None
    """Inclusive start date."""

    model_config = {"extra": "allow"}

    def to_dict(self) -> AggregationRangeDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(AggregationRangeDict, self.model_dump(by_alias=True, exclude_unset=True))
