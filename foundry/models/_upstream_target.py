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

from pydantic import BaseModel
from pydantic import Field

from foundry.models._dataset_rid import DatasetRid
from foundry.models._upstream_target_dict import UpstreamTargetDict


class UpstreamTarget(BaseModel):
    """Target the specified datasets along with all upstream datasets except the ignored datasets."""

    dataset_rids: List[DatasetRid] = Field(alias="datasetRids")
    """The target datasets."""

    ignored_dataset_rids: List[DatasetRid] = Field(alias="ignoredDatasetRids")
    """The datasets to ignore when calculating the final set of dataset to build."""

    type: Literal["upstream"]

    model_config = {"extra": "allow"}

    def to_dict(self) -> UpstreamTargetDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(UpstreamTargetDict, self.model_dump(by_alias=True, exclude_unset=True))
