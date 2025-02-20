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

from dataclasses import dataclass
from typing import Literal

from typing_extensions import NotRequired
from typing_extensions import TypedDict

from foundry._errors import BadRequestError
from foundry.v2.datasets.models._branch_name import BranchName
from foundry.v2.datasets.models._dataset_rid import DatasetRid
from foundry.v2.streams.models._view_rid import ViewRid


class InvalidStreamNoSchemaParameters(TypedDict):
    """The requested stream exists but is invalid, as it does not have a schema."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    datasetRid: DatasetRid

    branchName: BranchName

    viewRid: NotRequired[ViewRid]


@dataclass
class InvalidStreamNoSchema(BadRequestError):
    name: Literal["InvalidStreamNoSchema"]
    parameters: InvalidStreamNoSchemaParameters
    error_instance_id: str


__all__ = ["InvalidStreamNoSchema"]
