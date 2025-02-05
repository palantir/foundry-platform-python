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

from foundry.v2.ontologies.models._absolute_time_range_dict import AbsoluteTimeRangeDict


class AbsoluteTimeRange(pydantic.BaseModel):
    """ISO 8601 timestamps forming a range for a time series query. Start is inclusive and end is exclusive."""

    start_time: Optional[datetime] = pydantic.Field(alias=str("startTime"), default=None)  # type: ignore[literal-required]

    end_time: Optional[datetime] = pydantic.Field(alias=str("endTime"), default=None)  # type: ignore[literal-required]

    type: Literal["absolute"] = "absolute"

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> AbsoluteTimeRangeDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(AbsoluteTimeRangeDict, self.model_dump(by_alias=True, exclude_none=True))
