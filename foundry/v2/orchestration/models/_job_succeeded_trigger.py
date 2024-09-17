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

from pydantic import BaseModel
from pydantic import Field

from foundry.v2.datasets.models._branch_name import BranchName
from foundry.v2.datasets.models._dataset_rid import DatasetRid
from foundry.v2.orchestration.models._job_succeeded_trigger_dict import (
    JobSucceededTriggerDict,
)  # NOQA


class JobSucceededTrigger(BaseModel):
    """
    Trigger whenever a job succeeds on the dataset and on the target
    branch.
    """

    dataset_rid: DatasetRid = Field(alias="datasetRid")

    branch_name: BranchName = Field(alias="branchName")

    type: Literal["jobSucceeded"]

    model_config = {"extra": "allow"}

    def to_dict(self) -> JobSucceededTriggerDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(JobSucceededTriggerDict, self.model_dump(by_alias=True, exclude_unset=True))
