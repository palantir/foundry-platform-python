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

from typing_extensions import NotRequired
from typing_extensions import TypedDict

from foundry._core.utils import DateTime


class AbsoluteTimeRangeDict(TypedDict):
    """ISO 8601 timestamps forming a range for a time series query. Start is inclusive and end is exclusive."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    startTime: NotRequired[DateTime]

    endTime: NotRequired[DateTime]

    type: Literal["absolute"]
