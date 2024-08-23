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

from pydantic import StrictInt
from typing_extensions import TypedDict

from foundry.v2.models._relative_time_relation import RelativeTimeRelation
from foundry.v2.models._relative_time_series_time_unit import RelativeTimeSeriesTimeUnit


class RelativeTimeDict(TypedDict):
    """A relative time, such as "3 days before" or "2 hours after" the current moment."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    when: RelativeTimeRelation

    value: StrictInt

    unit: RelativeTimeSeriesTimeUnit
