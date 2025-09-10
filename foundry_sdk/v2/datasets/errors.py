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


import typing
from dataclasses import dataclass

import typing_extensions

from foundry_sdk import _errors as errors
from foundry_sdk.v2.core import models as core_models
from foundry_sdk.v2.datasets import models as datasets_models
from foundry_sdk.v2.filesystem import models as filesystem_models


class AbortTransactionPermissionDeniedParameters(typing_extensions.TypedDict):
    """The provided token does not have permission to abort the given transaction on the given dataset."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    datasetRid: datasets_models.DatasetRid
    transactionRid: datasets_models.TransactionRid


@dataclass
class AbortTransactionPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["AbortTransactionPermissionDenied"]
    parameters: AbortTransactionPermissionDeniedParameters
    error_instance_id: str


class AddBackingDatasetsPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not addBackingDatasets the View."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    viewDatasetRid: datasets_models.DatasetRid
    """The rid of the View."""


@dataclass
class AddBackingDatasetsPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["AddBackingDatasetsPermissionDenied"]
    parameters: AddBackingDatasetsPermissionDeniedParameters
    error_instance_id: str


class AddPrimaryKeyPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not addPrimaryKey the View."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    viewDatasetRid: datasets_models.DatasetRid
    """The rid of the View."""


@dataclass
class AddPrimaryKeyPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["AddPrimaryKeyPermissionDenied"]
    parameters: AddPrimaryKeyPermissionDeniedParameters
    error_instance_id: str


class BranchAlreadyExistsParameters(typing_extensions.TypedDict):
    """The branch cannot be created because a branch with that name already exists."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    datasetRid: datasets_models.DatasetRid
    branchName: datasets_models.BranchName


@dataclass
class BranchAlreadyExists(errors.ConflictError):
    name: typing.Literal["BranchAlreadyExists"]
    parameters: BranchAlreadyExistsParameters
    error_instance_id: str


class BranchNotFoundParameters(typing_extensions.TypedDict):
    """The requested branch could not be found, or the client token does not have access to it."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    datasetRid: datasets_models.DatasetRid
    branchName: datasets_models.BranchName


@dataclass
class BranchNotFound(errors.NotFoundError):
    name: typing.Literal["BranchNotFound"]
    parameters: BranchNotFoundParameters
    error_instance_id: str


class BuildTransactionPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not build the Transaction."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    datasetRid: datasets_models.DatasetRid
    transactionRid: datasets_models.TransactionRid


@dataclass
class BuildTransactionPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["BuildTransactionPermissionDenied"]
    parameters: BuildTransactionPermissionDeniedParameters
    error_instance_id: str


class ColumnTypesNotSupportedParameters(typing_extensions.TypedDict):
    """The dataset contains column types that are not supported."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    datasetRid: datasets_models.DatasetRid


@dataclass
class ColumnTypesNotSupported(errors.BadRequestError):
    name: typing.Literal["ColumnTypesNotSupported"]
    parameters: ColumnTypesNotSupportedParameters
    error_instance_id: str


class CommitTransactionPermissionDeniedParameters(typing_extensions.TypedDict):
    """The provided token does not have permission to commit the given transaction on the given dataset."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    datasetRid: datasets_models.DatasetRid
    transactionRid: datasets_models.TransactionRid


@dataclass
class CommitTransactionPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["CommitTransactionPermissionDenied"]
    parameters: CommitTransactionPermissionDeniedParameters
    error_instance_id: str


class CreateBranchPermissionDeniedParameters(typing_extensions.TypedDict):
    """The provided token does not have permission to create a branch of this dataset."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    datasetRid: datasets_models.DatasetRid
    branchName: datasets_models.BranchName


@dataclass
class CreateBranchPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["CreateBranchPermissionDenied"]
    parameters: CreateBranchPermissionDeniedParameters
    error_instance_id: str


class CreateDatasetPermissionDeniedParameters(typing_extensions.TypedDict):
    """The provided token does not have permission to create a dataset in this folder."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    parentFolderRid: filesystem_models.FolderRid
    name: datasets_models.DatasetName


@dataclass
class CreateDatasetPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["CreateDatasetPermissionDenied"]
    parameters: CreateDatasetPermissionDeniedParameters
    error_instance_id: str


class CreateTransactionPermissionDeniedParameters(typing_extensions.TypedDict):
    """The provided token does not have permission to create a transaction on this dataset."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    datasetRid: datasets_models.DatasetRid
    branchName: typing_extensions.NotRequired[datasets_models.BranchName]


@dataclass
class CreateTransactionPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["CreateTransactionPermissionDenied"]
    parameters: CreateTransactionPermissionDeniedParameters
    error_instance_id: str


class CreateViewPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not create the View."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class CreateViewPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["CreateViewPermissionDenied"]
    parameters: CreateViewPermissionDeniedParameters
    error_instance_id: str


class DatasetNotFoundParameters(typing_extensions.TypedDict):
    """The requested dataset could not be found, or the client token does not have access to it."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    datasetRid: datasets_models.DatasetRid


@dataclass
class DatasetNotFound(errors.NotFoundError):
    name: typing.Literal["DatasetNotFound"]
    parameters: DatasetNotFoundParameters
    error_instance_id: str


class DatasetReadNotSupportedParameters(typing_extensions.TypedDict):
    """The dataset does not support being read."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    datasetRid: datasets_models.DatasetRid


@dataclass
class DatasetReadNotSupported(errors.BadRequestError):
    name: typing.Literal["DatasetReadNotSupported"]
    parameters: DatasetReadNotSupportedParameters
    error_instance_id: str


class DatasetViewNotFoundParameters(typing_extensions.TypedDict):
    """
    The requested dataset view could not be found. A dataset view represents the effective file contents of a dataset
    for a branch at a point in time, calculated from transactions (SNAPSHOT, APPEND, UPDATE, DELETE). The view may not
    exist if the dataset has no transactions, contains no files, the branch is not valid, or the client token does not have access to it.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    datasetRid: datasets_models.DatasetRid
    branch: datasets_models.BranchName


@dataclass
class DatasetViewNotFound(errors.NotFoundError):
    name: typing.Literal["DatasetViewNotFound"]
    parameters: DatasetViewNotFoundParameters
    error_instance_id: str


class DeleteBranchPermissionDeniedParameters(typing_extensions.TypedDict):
    """The provided token does not have permission to delete the given branch from this dataset."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    datasetRid: datasets_models.DatasetRid
    branchName: datasets_models.BranchName


@dataclass
class DeleteBranchPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["DeleteBranchPermissionDenied"]
    parameters: DeleteBranchPermissionDeniedParameters
    error_instance_id: str


class DeleteFilePermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not delete the File."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    datasetRid: datasets_models.DatasetRid
    filePath: core_models.FilePath


@dataclass
class DeleteFilePermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["DeleteFilePermissionDenied"]
    parameters: DeleteFilePermissionDeniedParameters
    error_instance_id: str


class DeleteSchemaPermissionDeniedParameters(typing_extensions.TypedDict):
    """todo"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    datasetRid: datasets_models.DatasetRid
    branchName: datasets_models.BranchName
    transactionId: typing_extensions.NotRequired[datasets_models.TransactionRid]


@dataclass
class DeleteSchemaPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["DeleteSchemaPermissionDenied"]
    parameters: DeleteSchemaPermissionDeniedParameters
    error_instance_id: str


class FileAlreadyExistsParameters(typing_extensions.TypedDict):
    """The given file path already exists in the dataset and transaction."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    datasetRid: datasets_models.DatasetRid
    transactionRid: datasets_models.TransactionRid
    path: core_models.FilePath


@dataclass
class FileAlreadyExists(errors.NotFoundError):
    name: typing.Literal["FileAlreadyExists"]
    parameters: FileAlreadyExistsParameters
    error_instance_id: str


class FileNotFoundParameters(typing_extensions.TypedDict):
    """The given File could not be found."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    datasetRid: datasets_models.DatasetRid
    filePath: core_models.FilePath


@dataclass
class FileNotFound(errors.NotFoundError):
    name: typing.Literal["FileNotFound"]
    parameters: FileNotFoundParameters
    error_instance_id: str


class FileNotFoundOnBranchParameters(typing_extensions.TypedDict):
    """The requested file could not be found on the given branch, or the client token does not have access to it."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    datasetRid: datasets_models.DatasetRid
    branchName: datasets_models.BranchName
    path: core_models.FilePath


@dataclass
class FileNotFoundOnBranch(errors.NotFoundError):
    name: typing.Literal["FileNotFoundOnBranch"]
    parameters: FileNotFoundOnBranchParameters
    error_instance_id: str


class FileNotFoundOnTransactionRangeParameters(typing_extensions.TypedDict):
    """The requested file could not be found on the given transaction range, or the client token does not have access to it."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    datasetRid: datasets_models.DatasetRid
    startTransactionRid: typing_extensions.NotRequired[datasets_models.TransactionRid]
    endTransactionRid: datasets_models.TransactionRid
    path: core_models.FilePath


@dataclass
class FileNotFoundOnTransactionRange(errors.NotFoundError):
    name: typing.Literal["FileNotFoundOnTransactionRange"]
    parameters: FileNotFoundOnTransactionRangeParameters
    error_instance_id: str


class GetBranchTransactionHistoryPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not transactions the Branch."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    datasetRid: datasets_models.DatasetRid
    branchName: datasets_models.BranchName


@dataclass
class GetBranchTransactionHistoryPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["GetBranchTransactionHistoryPermissionDenied"]
    parameters: GetBranchTransactionHistoryPermissionDeniedParameters
    error_instance_id: str


class GetDatasetJobsPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not jobs the Dataset."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    datasetRid: datasets_models.DatasetRid


@dataclass
class GetDatasetJobsPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["GetDatasetJobsPermissionDenied"]
    parameters: GetDatasetJobsPermissionDeniedParameters
    error_instance_id: str


class GetDatasetSchedulesPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not getSchedules the Dataset."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    datasetRid: datasets_models.DatasetRid


@dataclass
class GetDatasetSchedulesPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["GetDatasetSchedulesPermissionDenied"]
    parameters: GetDatasetSchedulesPermissionDeniedParameters
    error_instance_id: str


class GetDatasetSchemaPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not getSchema the Dataset."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    datasetRid: datasets_models.DatasetRid


@dataclass
class GetDatasetSchemaPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["GetDatasetSchemaPermissionDenied"]
    parameters: GetDatasetSchemaPermissionDeniedParameters
    error_instance_id: str


class GetFileContentPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not content the File."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    datasetRid: datasets_models.DatasetRid
    filePath: core_models.FilePath


@dataclass
class GetFileContentPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["GetFileContentPermissionDenied"]
    parameters: GetFileContentPermissionDeniedParameters
    error_instance_id: str


class InputBackingDatasetNotInOutputViewProjectParameters(typing_extensions.TypedDict):
    """
    One or more backing datasets do not live in the same project as the view. Either move the input datasets to
    the same project as the view or add them as project references.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class InputBackingDatasetNotInOutputViewProject(errors.BadRequestError):
    name: typing.Literal["InputBackingDatasetNotInOutputViewProject"]
    parameters: InputBackingDatasetNotInOutputViewProjectParameters
    error_instance_id: str


class InvalidBranchNameParameters(typing_extensions.TypedDict):
    """The requested branch name cannot be used. Branch names cannot be empty and must not look like RIDs or UUIDs."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    branchName: datasets_models.BranchName


@dataclass
class InvalidBranchName(errors.BadRequestError):
    name: typing.Literal["InvalidBranchName"]
    parameters: InvalidBranchNameParameters
    error_instance_id: str


class InvalidTransactionTypeParameters(typing_extensions.TypedDict):
    """The given transaction type is not valid. Valid transaction types are `SNAPSHOT`, `UPDATE`, `APPEND`, and `DELETE`."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    datasetRid: datasets_models.DatasetRid
    transactionRid: datasets_models.TransactionRid
    transactionType: datasets_models.TransactionType


@dataclass
class InvalidTransactionType(errors.BadRequestError):
    name: typing.Literal["InvalidTransactionType"]
    parameters: InvalidTransactionTypeParameters
    error_instance_id: str


class InvalidViewBackingDatasetParameters(typing_extensions.TypedDict):
    """Either you do not have access to one or more of the backing datasets or it does not exist."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class InvalidViewBackingDataset(errors.BadRequestError):
    name: typing.Literal["InvalidViewBackingDataset"]
    parameters: InvalidViewBackingDatasetParameters
    error_instance_id: str


class InvalidViewPrimaryKeyColumnTypeParameters(typing_extensions.TypedDict):
    """
    The type of each referenced column in the primary key must be one of the following: BYTE, SHORT, DECIMAL,
    INTEGER, LONG, STRING, BOOLEAN, TIMESTAMP or DATE.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    primaryKeyColumns: typing.List[str]
    invalidColumns: typing.List[str]


@dataclass
class InvalidViewPrimaryKeyColumnType(errors.BadRequestError):
    name: typing.Literal["InvalidViewPrimaryKeyColumnType"]
    parameters: InvalidViewPrimaryKeyColumnTypeParameters
    error_instance_id: str


class InvalidViewPrimaryKeyDeletionColumnParameters(typing_extensions.TypedDict):
    """The deletion column must be a boolean."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    deletionColumn: str
    deletionColumnType: core_models.SchemaFieldType


@dataclass
class InvalidViewPrimaryKeyDeletionColumn(errors.BadRequestError):
    name: typing.Literal["InvalidViewPrimaryKeyDeletionColumn"]
    parameters: InvalidViewPrimaryKeyDeletionColumnParameters
    error_instance_id: str


class JobTransactionPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not job the Transaction."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    datasetRid: datasets_models.DatasetRid
    transactionRid: datasets_models.TransactionRid


@dataclass
class JobTransactionPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["JobTransactionPermissionDenied"]
    parameters: JobTransactionPermissionDeniedParameters
    error_instance_id: str


class NotAllColumnsInPrimaryKeyArePresentParameters(typing_extensions.TypedDict):
    """Not all columns in the View's primary key are present in the dataset(s)."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    primaryKeyColumns: typing.List[str]
    missingColumns: typing.List[str]


@dataclass
class NotAllColumnsInPrimaryKeyArePresent(errors.BadRequestError):
    name: typing.Literal["NotAllColumnsInPrimaryKeyArePresent"]
    parameters: NotAllColumnsInPrimaryKeyArePresentParameters
    error_instance_id: str


class OpenTransactionAlreadyExistsParameters(typing_extensions.TypedDict):
    """A transaction is already open on this dataset and branch. A branch of a dataset can only have one open transaction at a time."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    datasetRid: datasets_models.DatasetRid
    branchName: datasets_models.BranchName


@dataclass
class OpenTransactionAlreadyExists(errors.ConflictError):
    name: typing.Literal["OpenTransactionAlreadyExists"]
    parameters: OpenTransactionAlreadyExistsParameters
    error_instance_id: str


class PutDatasetSchemaPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not putSchema the Dataset."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    datasetRid: datasets_models.DatasetRid


@dataclass
class PutDatasetSchemaPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["PutDatasetSchemaPermissionDenied"]
    parameters: PutDatasetSchemaPermissionDeniedParameters
    error_instance_id: str


class PutSchemaPermissionDeniedParameters(typing_extensions.TypedDict):
    """todo"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    datasetRid: datasets_models.DatasetRid
    branchName: datasets_models.BranchName


@dataclass
class PutSchemaPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["PutSchemaPermissionDenied"]
    parameters: PutSchemaPermissionDeniedParameters
    error_instance_id: str


class ReadTableDatasetPermissionDeniedParameters(typing_extensions.TypedDict):
    """The provided token does not have permission to read the given dataset as a table."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    datasetRid: datasets_models.DatasetRid


@dataclass
class ReadTableDatasetPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["ReadTableDatasetPermissionDenied"]
    parameters: ReadTableDatasetPermissionDeniedParameters
    error_instance_id: str


class ReadTableErrorParameters(typing_extensions.TypedDict):
    """An error occurred while reading the table. Refer to the message for more details."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    datasetRid: datasets_models.DatasetRid
    message: str


@dataclass
class ReadTableError(errors.InternalServerError):
    name: typing.Literal["ReadTableError"]
    parameters: ReadTableErrorParameters
    error_instance_id: str


class ReadTableRowLimitExceededParameters(typing_extensions.TypedDict):
    """
    The request to read the table generates a result that exceeds the allowed number of rows. For datasets not
    stored as Parquet there is a limit of 1 million rows. For datasets stored as Parquet there is no limit.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    datasetRid: datasets_models.DatasetRid


@dataclass
class ReadTableRowLimitExceeded(errors.BadRequestError):
    name: typing.Literal["ReadTableRowLimitExceeded"]
    parameters: ReadTableRowLimitExceededParameters
    error_instance_id: str


class ReadTableTimeoutParameters(typing_extensions.TypedDict):
    """The request to read the table timed out."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    datasetRid: datasets_models.DatasetRid


@dataclass
class ReadTableTimeout(errors.InternalServerError):
    name: typing.Literal["ReadTableTimeout"]
    parameters: ReadTableTimeoutParameters
    error_instance_id: str


class RemoveBackingDatasetsPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not removeBackingDatasets the View."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    viewDatasetRid: datasets_models.DatasetRid
    """The rid of the View."""


@dataclass
class RemoveBackingDatasetsPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["RemoveBackingDatasetsPermissionDenied"]
    parameters: RemoveBackingDatasetsPermissionDeniedParameters
    error_instance_id: str


class ReplaceBackingDatasetsPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not replaceBackingDatasets the View."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    viewDatasetRid: datasets_models.DatasetRid
    """The rid of the View."""


@dataclass
class ReplaceBackingDatasetsPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["ReplaceBackingDatasetsPermissionDenied"]
    parameters: ReplaceBackingDatasetsPermissionDeniedParameters
    error_instance_id: str


class SchemaNotFoundParameters(typing_extensions.TypedDict):
    """A schema could not be found for the given dataset and branch, or the client token does not have access to it."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    datasetRid: datasets_models.DatasetRid
    branchName: datasets_models.BranchName
    transactionRid: typing_extensions.NotRequired[datasets_models.TransactionRid]


@dataclass
class SchemaNotFound(errors.NotFoundError):
    name: typing.Literal["SchemaNotFound"]
    parameters: SchemaNotFoundParameters
    error_instance_id: str


class TransactionNotCommittedParameters(typing_extensions.TypedDict):
    """The given transaction has not been committed."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    datasetRid: datasets_models.DatasetRid
    transactionRid: datasets_models.TransactionRid
    transactionStatus: datasets_models.TransactionStatus


@dataclass
class TransactionNotCommitted(errors.BadRequestError):
    name: typing.Literal["TransactionNotCommitted"]
    parameters: TransactionNotCommittedParameters
    error_instance_id: str


class TransactionNotFoundParameters(typing_extensions.TypedDict):
    """The requested transaction could not be found on the dataset, or the client token does not have access to it."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    datasetRid: datasets_models.DatasetRid
    transactionRid: datasets_models.TransactionRid


@dataclass
class TransactionNotFound(errors.NotFoundError):
    name: typing.Literal["TransactionNotFound"]
    parameters: TransactionNotFoundParameters
    error_instance_id: str


class TransactionNotOpenParameters(typing_extensions.TypedDict):
    """The given transaction is not open."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    datasetRid: datasets_models.DatasetRid
    transactionRid: datasets_models.TransactionRid
    transactionStatus: datasets_models.TransactionStatus


@dataclass
class TransactionNotOpen(errors.BadRequestError):
    name: typing.Literal["TransactionNotOpen"]
    parameters: TransactionNotOpenParameters
    error_instance_id: str


class UploadFilePermissionDeniedParameters(typing_extensions.TypedDict):
    """The provided token does not have permission to upload the given file to the given dataset and transaction."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    datasetRid: datasets_models.DatasetRid
    transactionRid: datasets_models.TransactionRid
    path: core_models.FilePath


@dataclass
class UploadFilePermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["UploadFilePermissionDenied"]
    parameters: UploadFilePermissionDeniedParameters
    error_instance_id: str


class ViewDatasetCleanupFailedParameters(typing_extensions.TypedDict):
    """Failed to delete dataset following View creation failure."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    viewDatasetRid: datasets_models.DatasetRid


@dataclass
class ViewDatasetCleanupFailed(errors.InternalServerError):
    name: typing.Literal["ViewDatasetCleanupFailed"]
    parameters: ViewDatasetCleanupFailedParameters
    error_instance_id: str


class ViewNotFoundParameters(typing_extensions.TypedDict):
    """
    The requested View could not be found. Either the view does not exist, the branch is not valid or the
    client token does not have access to it.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    viewDatasetRid: datasets_models.DatasetRid
    branch: datasets_models.BranchName


@dataclass
class ViewNotFound(errors.NotFoundError):
    name: typing.Literal["ViewNotFound"]
    parameters: ViewNotFoundParameters
    error_instance_id: str


class ViewPrimaryKeyCannotBeModifiedParameters(typing_extensions.TypedDict):
    """A primary key already exits."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class ViewPrimaryKeyCannotBeModified(errors.ConflictError):
    name: typing.Literal["ViewPrimaryKeyCannotBeModified"]
    parameters: ViewPrimaryKeyCannotBeModifiedParameters
    error_instance_id: str


class ViewPrimaryKeyDeletionColumnNotInDatasetSchemaParameters(typing_extensions.TypedDict):
    """The deletion column is not present in the dataset."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    deletionColumn: str


@dataclass
class ViewPrimaryKeyDeletionColumnNotInDatasetSchema(errors.BadRequestError):
    name: typing.Literal["ViewPrimaryKeyDeletionColumnNotInDatasetSchema"]
    parameters: ViewPrimaryKeyDeletionColumnNotInDatasetSchemaParameters
    error_instance_id: str


class ViewPrimaryKeyMustContainAtLeastOneColumnParameters(typing_extensions.TypedDict):
    """No columns were provided as part of the primary key"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class ViewPrimaryKeyMustContainAtLeastOneColumn(errors.BadRequestError):
    name: typing.Literal["ViewPrimaryKeyMustContainAtLeastOneColumn"]
    parameters: ViewPrimaryKeyMustContainAtLeastOneColumnParameters
    error_instance_id: str


class ViewPrimaryKeyRequiresBackingDatasetsParameters(typing_extensions.TypedDict):
    """Cannot add a primary key to a View that does not have any backing datasets."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class ViewPrimaryKeyRequiresBackingDatasets(errors.BadRequestError):
    name: typing.Literal["ViewPrimaryKeyRequiresBackingDatasets"]
    parameters: ViewPrimaryKeyRequiresBackingDatasetsParameters
    error_instance_id: str


__all__ = [
    "AbortTransactionPermissionDenied",
    "AddBackingDatasetsPermissionDenied",
    "AddPrimaryKeyPermissionDenied",
    "BranchAlreadyExists",
    "BranchNotFound",
    "BuildTransactionPermissionDenied",
    "ColumnTypesNotSupported",
    "CommitTransactionPermissionDenied",
    "CreateBranchPermissionDenied",
    "CreateDatasetPermissionDenied",
    "CreateTransactionPermissionDenied",
    "CreateViewPermissionDenied",
    "DatasetNotFound",
    "DatasetReadNotSupported",
    "DatasetViewNotFound",
    "DeleteBranchPermissionDenied",
    "DeleteFilePermissionDenied",
    "DeleteSchemaPermissionDenied",
    "FileAlreadyExists",
    "FileNotFound",
    "FileNotFoundOnBranch",
    "FileNotFoundOnTransactionRange",
    "GetBranchTransactionHistoryPermissionDenied",
    "GetDatasetJobsPermissionDenied",
    "GetDatasetSchedulesPermissionDenied",
    "GetDatasetSchemaPermissionDenied",
    "GetFileContentPermissionDenied",
    "InputBackingDatasetNotInOutputViewProject",
    "InvalidBranchName",
    "InvalidTransactionType",
    "InvalidViewBackingDataset",
    "InvalidViewPrimaryKeyColumnType",
    "InvalidViewPrimaryKeyDeletionColumn",
    "JobTransactionPermissionDenied",
    "NotAllColumnsInPrimaryKeyArePresent",
    "OpenTransactionAlreadyExists",
    "PutDatasetSchemaPermissionDenied",
    "PutSchemaPermissionDenied",
    "ReadTableDatasetPermissionDenied",
    "ReadTableError",
    "ReadTableRowLimitExceeded",
    "ReadTableTimeout",
    "RemoveBackingDatasetsPermissionDenied",
    "ReplaceBackingDatasetsPermissionDenied",
    "SchemaNotFound",
    "TransactionNotCommitted",
    "TransactionNotFound",
    "TransactionNotOpen",
    "UploadFilePermissionDenied",
    "ViewDatasetCleanupFailed",
    "ViewNotFound",
    "ViewPrimaryKeyCannotBeModified",
    "ViewPrimaryKeyDeletionColumnNotInDatasetSchema",
    "ViewPrimaryKeyMustContainAtLeastOneColumn",
    "ViewPrimaryKeyRequiresBackingDatasets",
]
