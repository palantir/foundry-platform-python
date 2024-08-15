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

from typing_extensions import TypedDict

from foundry.v2.models._duration_dict import DurationDict


class RetryBackoffDurationDict(TypedDict):
    """The duration to wait between job retries. Defaults to 0."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    duration: DurationDict
