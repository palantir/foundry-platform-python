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
from datetime import datetime

import pydantic
import typing_extensions

from foundry import _core as core


class Branch(pydantic.BaseModel):
    """A Branch of a Dataset."""

    branch_id: BranchId = pydantic.Field(alias=str("branchId"))  # type: ignore[literal-required]
    transaction_rid: typing.Optional[TransactionRid] = pydantic.Field(alias=str("transactionRid"), default=None)  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "BranchDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(BranchDict, self.model_dump(by_alias=True, exclude_none=True))


class BranchDict(typing_extensions.TypedDict):
    """A Branch of a Dataset."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    branchId: BranchId
    transactionRid: typing_extensions.NotRequired[TransactionRid]


BranchId = str
"""The identifier (name) of a Branch."""


class Dataset(pydantic.BaseModel):
    """Dataset"""

    rid: DatasetRid
    name: DatasetName
    parent_folder_rid: core_models.FolderRid = pydantic.Field(alias=str("parentFolderRid"))  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "DatasetDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(DatasetDict, self.model_dump(by_alias=True, exclude_none=True))


class DatasetDict(typing_extensions.TypedDict):
    """Dataset"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    rid: DatasetRid
    name: DatasetName
    parentFolderRid: core_models.FolderRid


DatasetName = str
"""DatasetName"""


DatasetRid = core.RID
"""The Resource Identifier (RID) of a Dataset."""


class File(pydantic.BaseModel):
    """File"""

    path: core_models.FilePath
    transaction_rid: TransactionRid = pydantic.Field(alias=str("transactionRid"))  # type: ignore[literal-required]
    size_bytes: typing.Optional[core.Long] = pydantic.Field(alias=str("sizeBytes"), default=None)  # type: ignore[literal-required]
    updated_time: datetime = pydantic.Field(alias=str("updatedTime"))  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "FileDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(FileDict, self.model_dump(by_alias=True, exclude_none=True))


class FileDict(typing_extensions.TypedDict):
    """File"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    path: core_models.FilePath
    transactionRid: TransactionRid
    sizeBytes: typing_extensions.NotRequired[core.Long]
    updatedTime: datetime


class ListBranchesResponse(pydantic.BaseModel):
    """ListBranchesResponse"""

    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]
    data: typing.List[Branch]
    """The list of branches in the current page."""

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ListBranchesResponseDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            ListBranchesResponseDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class ListBranchesResponseDict(typing_extensions.TypedDict):
    """ListBranchesResponse"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    nextPageToken: typing_extensions.NotRequired[core_models.PageToken]
    data: typing.List[BranchDict]
    """The list of branches in the current page."""


class ListFilesResponse(pydantic.BaseModel):
    """A page of Files and an optional page token that can be used to retrieve the next page."""

    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]
    data: typing.List[File]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ListFilesResponseDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(ListFilesResponseDict, self.model_dump(by_alias=True, exclude_none=True))


class ListFilesResponseDict(typing_extensions.TypedDict):
    """A page of Files and an optional page token that can be used to retrieve the next page."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    nextPageToken: typing_extensions.NotRequired[core_models.PageToken]
    data: typing.List[FileDict]


TableExportFormat = typing.Literal["ARROW", "CSV"]
"""Format for tabular dataset export."""


class Transaction(pydantic.BaseModel):
    """An operation that modifies the files within a dataset."""

    rid: TransactionRid
    transaction_type: TransactionType = pydantic.Field(alias=str("transactionType"))  # type: ignore[literal-required]
    status: TransactionStatus
    created_time: datetime = pydantic.Field(alias=str("createdTime"))  # type: ignore[literal-required]
    """The timestamp when the transaction was created, in ISO 8601 timestamp format."""

    closed_time: typing.Optional[datetime] = pydantic.Field(alias=str("closedTime"), default=None)  # type: ignore[literal-required]
    """The timestamp when the transaction was closed, in ISO 8601 timestamp format."""

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "TransactionDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(TransactionDict, self.model_dump(by_alias=True, exclude_none=True))


class TransactionDict(typing_extensions.TypedDict):
    """An operation that modifies the files within a dataset."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    rid: TransactionRid
    transactionType: TransactionType
    status: TransactionStatus
    createdTime: datetime
    """The timestamp when the transaction was created, in ISO 8601 timestamp format."""

    closedTime: typing_extensions.NotRequired[datetime]
    """The timestamp when the transaction was closed, in ISO 8601 timestamp format."""


TransactionRid = core.RID
"""The Resource Identifier (RID) of a Transaction."""


TransactionStatus = typing.Literal["ABORTED", "COMMITTED", "OPEN"]
"""The status of a Transaction."""


TransactionType = typing.Literal["APPEND", "UPDATE", "SNAPSHOT", "DELETE"]
"""The type of a Transaction."""


from foundry.v1.core import models as core_models  # noqa: E402

__all__ = [
    "Branch",
    "BranchDict",
    "BranchId",
    "Dataset",
    "DatasetDict",
    "DatasetName",
    "DatasetRid",
    "File",
    "FileDict",
    "ListBranchesResponse",
    "ListBranchesResponseDict",
    "ListFilesResponse",
    "ListFilesResponseDict",
    "TableExportFormat",
    "Transaction",
    "TransactionDict",
    "TransactionRid",
    "TransactionStatus",
    "TransactionType",
]
