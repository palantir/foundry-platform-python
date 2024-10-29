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

from typing import List
from typing import Literal
from typing import cast

import pydantic

from foundry.v2.orchestration.models._buildable_rid import BuildableRid
from foundry.v2.orchestration.models._connecting_target_dict import ConnectingTargetDict


class ConnectingTarget(pydantic.BaseModel):
    """
    All datasets between the input datasets (exclusive) and the
    target datasets (inclusive) except for the datasets to ignore.
    """

    input_rids: List[BuildableRid] = pydantic.Field(alias="inputRids")
    """The upstream input datasets (exclusive)."""

    target_rids: List[BuildableRid] = pydantic.Field(alias="targetRids")
    """The downstream target datasets (inclusive)."""

    ignored_rids: List[BuildableRid] = pydantic.Field(alias="ignoredRids")
    """The datasets between the input datasets and target datasets to exclude."""

    type: Literal["connecting"] = "connecting"

    model_config = {"extra": "allow"}

    def to_dict(self) -> ConnectingTargetDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(ConnectingTargetDict, self.model_dump(by_alias=True, exclude_unset=True))
