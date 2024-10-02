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

from typing_extensions import NotRequired
from typing_extensions import TypedDict

from foundry.v2.connectivity.models._connection_rid import ConnectionRid
from foundry.v2.connectivity.models._file_import_display_name import FileImportDisplayName  # NOQA
from foundry.v2.connectivity.models._file_import_rid import FileImportRid
from foundry.v2.datasets.models._branch_name import BranchName
from foundry.v2.datasets.models._dataset_rid import DatasetRid


class FileImportDict(TypedDict):
    """FileImport"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    rid: FileImportRid

    connectionRid: ConnectionRid
    """The RID of the Connection (formerly known as a source) that the File Import uses to import data."""

    datasetRid: DatasetRid
    """The RID of the output dataset."""

    branchName: NotRequired[BranchName]
    """The branch name in the output dataset that will contain the imported data. Defaults to `master` for most enrollments."""

    displayName: FileImportDisplayName
