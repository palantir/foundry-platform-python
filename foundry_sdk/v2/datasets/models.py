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
from foundry_sdk.v2.core import models as core_models
from foundry_sdk.v2.filesystem import models as filesystem_models


class Branch(pydantic.BaseModel):
    """Branch"""

    name: BranchName
    transaction_rid: typing.Optional[TransactionRid] = pydantic.Field(alias=str("transactionRid"), default=None)  # type: ignore[literal-required]
    """The most recent OPEN or COMMITTED transaction on the branch. This will never be an ABORTED transaction."""

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


BranchName = str
"""The name of a Branch."""


class Dataset(pydantic.BaseModel):
    """Dataset"""

    rid: DatasetRid
    name: DatasetName
    parent_folder_rid: filesystem_models.FolderRid = pydantic.Field(alias=str("parentFolderRid"))  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


DatasetName = str
"""DatasetName"""


DatasetRid = core.RID
"""The Resource Identifier (RID) of a Dataset."""


class File(pydantic.BaseModel):
    """File"""

    path: core_models.FilePath
    transaction_rid: TransactionRid = pydantic.Field(alias=str("transactionRid"))  # type: ignore[literal-required]
    size_bytes: typing.Optional[core.Long] = pydantic.Field(alias=str("sizeBytes"), default=None)  # type: ignore[literal-required]
    updated_time: FileUpdatedTime = pydantic.Field(alias=str("updatedTime"))  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


FileUpdatedTime = core.AwareDatetime
"""FileUpdatedTime"""


class ListBranchesResponse(pydantic.BaseModel):
    """ListBranchesResponse"""

    data: typing.List[Branch]
    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class ListFilesResponse(pydantic.BaseModel):
    """ListFilesResponse"""

    data: typing.List[File]
    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class ListSchedulesResponse(pydantic.BaseModel):
    """ListSchedulesResponse"""

    data: typing.List[core_models.ScheduleRid]
    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


TableExportFormat = typing.Literal["ARROW", "CSV"]
"""Format for tabular dataset export."""


class Transaction(pydantic.BaseModel):
    """Transaction"""

    rid: TransactionRid
    transaction_type: TransactionType = pydantic.Field(alias=str("transactionType"))  # type: ignore[literal-required]
    status: TransactionStatus
    created_time: TransactionCreatedTime = pydantic.Field(alias=str("createdTime"))  # type: ignore[literal-required]
    """The timestamp when the transaction was created, in ISO 8601 timestamp format."""

    closed_time: typing.Optional[core.AwareDatetime] = pydantic.Field(alias=str("closedTime"), default=None)  # type: ignore[literal-required]
    """The timestamp when the transaction was closed, in ISO 8601 timestamp format."""

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


TransactionCreatedTime = core.AwareDatetime
"""The timestamp when the transaction was created, in ISO 8601 timestamp format."""


TransactionRid = core.RID
"""The Resource Identifier (RID) of a Transaction."""


TransactionStatus = typing.Literal["ABORTED", "COMMITTED", "OPEN"]
"""The status of a Transaction."""


TransactionType = typing.Literal["APPEND", "UPDATE", "SNAPSHOT", "DELETE"]
"""The type of a Transaction."""


__all__ = [
    "Branch",
    "BranchName",
    "Dataset",
    "DatasetName",
    "DatasetRid",
    "File",
    "FileUpdatedTime",
    "ListBranchesResponse",
    "ListFilesResponse",
    "ListSchedulesResponse",
    "TableExportFormat",
    "Transaction",
    "TransactionCreatedTime",
    "TransactionRid",
    "TransactionStatus",
    "TransactionType",
]
