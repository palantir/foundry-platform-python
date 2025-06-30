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
import typing_extensions

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


class PrimaryKeyLatestWinsResolutionStrategy(pydantic.BaseModel):
    """Picks the row with the highest value of a list of columns, compared in order."""

    columns: typing.List[str]
    type: typing.Literal["latestWins"] = "latestWins"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class PrimaryKeyResolutionDuplicate(pydantic.BaseModel):
    """Duplicate primary key values may exist within the dataset – resolution required."""

    deletion_column: typing.Optional[str] = pydantic.Field(alias=str("deletionColumn"), default=None)  # type: ignore[literal-required]
    """
    The name of the boolean column that indicates whether a row should be considered deleted. Based on the 
    `resolutionStrategy`, if the final row selected for a given primary key has `true` in this column, that 
    row will be excluded from the results. Otherwise, it will be included.
    """

    resolution_strategy: PrimaryKeyResolutionStrategy = pydantic.Field(alias=str("resolutionStrategy"))  # type: ignore[literal-required]
    type: typing.Literal["duplicate"] = "duplicate"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class PrimaryKeyResolutionUnique(pydantic.BaseModel):
    """Primary key values are unique within the dataset – no conflicts."""

    type: typing.Literal["unique"] = "unique"
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


class View(pydantic.BaseModel):
    """View"""

    view_name: DatasetName = pydantic.Field(alias=str("viewName"))  # type: ignore[literal-required]
    dataset_rid: DatasetRid = pydantic.Field(alias=str("datasetRid"))  # type: ignore[literal-required]
    """The rid of the View."""

    parent_folder_rid: filesystem_models.FolderRid = pydantic.Field(alias=str("parentFolderRid"))  # type: ignore[literal-required]
    branch: typing.Optional[BranchName] = None
    """The branch name of the View. If not specified, defaults to `master` for most enrollments."""

    backing_datasets: typing.List[ViewBackingDataset] = pydantic.Field(alias=str("backingDatasets"))  # type: ignore[literal-required]
    primary_key: typing.Optional[ViewPrimaryKey] = pydantic.Field(alias=str("primaryKey"), default=None)  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class ViewBackingDataset(pydantic.BaseModel):
    """One of the Datasets backing a View."""

    branch: BranchName
    dataset_rid: DatasetRid = pydantic.Field(alias=str("datasetRid"))  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class ViewPrimaryKey(pydantic.BaseModel):
    """
    The primary key of the dataset. Primary keys are treated as guarantees provided by the creator of the
    dataset.
    """

    columns: typing.List[str]
    """
    The columns that constitute the primary key. These columns must satisfy the following constraints:
    - The list of columns must be non-empty.
    - The list must not contain duplicate columns after applying column normalization.
    - Each referenced column must exist in the schema.
    - The type of each referenced column must be one of the following: `BYTE`, `SHORT`, `DECIMAL`, `INTEGER`,
      `LONG`, `STRING`, `BOOLEAN`, `TIMESTAMP` or `DATE`.
    """

    resolution: ViewPrimaryKeyResolution
    """
    The semantics of the primary key within the dataset. For example, the unique resolution means that every 
    row in the dataset has a distinct primary key. The value of this field represents a contract for writers 
    of the dataset. Writers are responsible for maintaining any related invariants, and readers may make 
    optimizations based on this. Violating the assumptions of the resolution can cause undefined behavior, 
    for example, having duplicate primary keys with the unique resolution.
    """

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


ViewPrimaryKeyResolution = typing_extensions.Annotated[
    typing.Union[PrimaryKeyResolutionUnique, PrimaryKeyResolutionDuplicate],
    pydantic.Field(discriminator="type"),
]
"""Specifies how primary key conflicts are resolved within the view."""


PrimaryKeyResolutionStrategy = PrimaryKeyLatestWinsResolutionStrategy
"""PrimaryKeyResolutionStrategy"""


core.resolve_forward_references(ViewPrimaryKeyResolution, globalns=globals(), localns=locals())

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
    "PrimaryKeyLatestWinsResolutionStrategy",
    "PrimaryKeyResolutionDuplicate",
    "PrimaryKeyResolutionStrategy",
    "PrimaryKeyResolutionUnique",
    "TableExportFormat",
    "Transaction",
    "TransactionCreatedTime",
    "TransactionRid",
    "TransactionStatus",
    "TransactionType",
    "View",
    "ViewBackingDataset",
    "ViewPrimaryKey",
    "ViewPrimaryKeyResolution",
]
