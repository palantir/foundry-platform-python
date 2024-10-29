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
from typing import cast

import pydantic

from foundry.v2.datasets.models._branch_name import BranchName
from foundry.v2.datasets.models._dataset_rid import DatasetRid
from foundry.v2.orchestration.models._dataset_updated_trigger_dict import (
    DatasetUpdatedTriggerDict,
)  # NOQA


class DatasetUpdatedTrigger(pydantic.BaseModel):
    """
    Trigger whenever a new transaction is committed to the
    dataset on the target branch.
    """

    dataset_rid: DatasetRid = pydantic.Field(alias="datasetRid")

    branch_name: BranchName = pydantic.Field(alias="branchName")

    type: Literal["datasetUpdated"] = "datasetUpdated"

    model_config = {"extra": "allow"}

    def to_dict(self) -> DatasetUpdatedTriggerDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(DatasetUpdatedTriggerDict, self.model_dump(by_alias=True, exclude_unset=True))
