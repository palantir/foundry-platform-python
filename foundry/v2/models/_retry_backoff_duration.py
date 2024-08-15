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

from typing import cast

from pydantic import BaseModel

from foundry.v2.models._duration import Duration
from foundry.v2.models._retry_backoff_duration_dict import RetryBackoffDurationDict


class RetryBackoffDuration(BaseModel):
    """The duration to wait between job retries. Defaults to 0."""

    duration: Duration

    model_config = {"extra": "allow"}

    def to_dict(self) -> RetryBackoffDurationDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(RetryBackoffDurationDict, self.model_dump(by_alias=True, exclude_unset=True))
