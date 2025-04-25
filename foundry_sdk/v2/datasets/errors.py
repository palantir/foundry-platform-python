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


class GetDatasetSchedulesPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not getSchedules the Dataset."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    datasetRid: datasets_models.DatasetRid


@dataclass
class GetDatasetSchedulesPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["GetDatasetSchedulesPermissionDenied"]
    parameters: GetDatasetSchedulesPermissionDeniedParameters
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


__all__ = [
    "AbortTransactionPermissionDenied",
    "BranchAlreadyExists",
    "BranchNotFound",
    "BuildTransactionPermissionDenied",
    "ColumnTypesNotSupported",
    "CommitTransactionPermissionDenied",
    "CreateBranchPermissionDenied",
    "CreateDatasetPermissionDenied",
    "CreateTransactionPermissionDenied",
    "DatasetNotFound",
    "DatasetReadNotSupported",
    "DeleteBranchPermissionDenied",
    "DeleteFilePermissionDenied",
    "DeleteSchemaPermissionDenied",
    "FileAlreadyExists",
    "FileNotFound",
    "FileNotFoundOnBranch",
    "FileNotFoundOnTransactionRange",
    "GetDatasetSchedulesPermissionDenied",
    "GetFileContentPermissionDenied",
    "InvalidBranchName",
    "InvalidTransactionType",
    "JobTransactionPermissionDenied",
    "OpenTransactionAlreadyExists",
    "PutSchemaPermissionDenied",
    "ReadTableDatasetPermissionDenied",
    "ReadTableError",
    "ReadTableRowLimitExceeded",
    "ReadTableTimeout",
    "SchemaNotFound",
    "TransactionNotCommitted",
    "TransactionNotFound",
    "TransactionNotOpen",
    "UploadFilePermissionDenied",
]
