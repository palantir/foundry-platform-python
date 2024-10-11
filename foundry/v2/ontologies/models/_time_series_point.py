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
from typing import Any
from typing import cast

import pydantic

from foundry.v2.ontologies.models._time_series_point_dict import TimeSeriesPointDict


class TimeSeriesPoint(pydantic.BaseModel):
    """A time and value pair."""

    time: datetime
    """An ISO 8601 timestamp"""

    value: Any
    """An object which is either an enum String or a double number."""

    model_config = {"extra": "allow"}

    def to_dict(self) -> TimeSeriesPointDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(TimeSeriesPointDict, self.model_dump(by_alias=True, exclude_unset=True))
