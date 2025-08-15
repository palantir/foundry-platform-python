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

import typing

import pydantic

from foundry_sdk import _core as core
from foundry_sdk.v1.core import models as core_models


class Branch(core.ModelBase):
    """A Branch of a Dataset."""

    branch_id: BranchId = pydantic.Field(alias=str("branchId"))  # type: ignore[literal-required]
    transaction_rid: typing.Optional[TransactionRid] = pydantic.Field(alias=str("transactionRid"), default=None)  # type: ignore[literal-required]


BranchId = str
"""The identifier (name) of a Branch."""


class Dataset(core.ModelBase):
    """Dataset"""

    rid: DatasetRid
    name: DatasetName
    parent_folder_rid: core_models.FolderRid = pydantic.Field(alias=str("parentFolderRid"))  # type: ignore[literal-required]


DatasetName = str
"""DatasetName"""


DatasetRid = core.RID
"""The Resource Identifier (RID) of a Dataset."""


class File(core.ModelBase):
    """File"""

    path: core_models.FilePath
    transaction_rid: TransactionRid = pydantic.Field(alias=str("transactionRid"))  # type: ignore[literal-required]
    size_bytes: typing.Optional[core.Long] = pydantic.Field(alias=str("sizeBytes"), default=None)  # type: ignore[literal-required]
    updated_time: core.AwareDatetime = pydantic.Field(alias=str("updatedTime"))  # type: ignore[literal-required]


class ListBranchesResponse(core.ModelBase):
    """ListBranchesResponse"""

    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]
    data: typing.List[Branch]
    """The list of branches in the current page."""


class ListFilesResponse(core.ModelBase):
    """A page of Files and an optional page token that can be used to retrieve the next page."""

    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]
    data: typing.List[File]


TableExportFormat = typing.Literal["ARROW", "CSV"]
"""Format for tabular dataset export."""


class Transaction(core.ModelBase):
    """An operation that modifies the files within a dataset."""

    rid: TransactionRid
    transaction_type: TransactionType = pydantic.Field(alias=str("transactionType"))  # type: ignore[literal-required]
    status: TransactionStatus
    created_time: core.AwareDatetime = pydantic.Field(alias=str("createdTime"))  # type: ignore[literal-required]
    """The timestamp when the transaction was created, in ISO 8601 timestamp format."""

    closed_time: typing.Optional[core.AwareDatetime] = pydantic.Field(alias=str("closedTime"), default=None)  # type: ignore[literal-required]
    """The timestamp when the transaction was closed, in ISO 8601 timestamp format."""


TransactionRid = core.RID
"""The Resource Identifier (RID) of a Transaction."""


TransactionStatus = typing.Literal["ABORTED", "COMMITTED", "OPEN"]
"""The status of a Transaction."""


TransactionType = typing.Literal["APPEND", "UPDATE", "SNAPSHOT", "DELETE"]
"""The type of a Transaction."""


__all__ = [
    "Branch",
    "BranchId",
    "Dataset",
    "DatasetName",
    "DatasetRid",
    "File",
    "ListBranchesResponse",
    "ListFilesResponse",
    "TableExportFormat",
    "Transaction",
    "TransactionRid",
    "TransactionStatus",
    "TransactionType",
]
