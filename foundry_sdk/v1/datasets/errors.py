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
from foundry_sdk.v1.core import models as core_models
from foundry_sdk.v1.datasets import models as datasets_models


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
    branchId: datasets_models.BranchId


@dataclass
class BranchAlreadyExists(errors.ConflictError):
    name: typing.Literal["BranchAlreadyExists"]
    parameters: BranchAlreadyExistsParameters
    error_instance_id: str


class BranchNotFoundParameters(typing_extensions.TypedDict):
    """The requested branch could not be found, or the client token does not have access to it."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    datasetRid: datasets_models.DatasetRid
    branchId: datasets_models.BranchId


@dataclass
class BranchNotFound(errors.NotFoundError):
    name: typing.Literal["BranchNotFound"]
    parameters: BranchNotFoundParameters
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
    branchId: datasets_models.BranchId


@dataclass
class CreateBranchPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["CreateBranchPermissionDenied"]
    parameters: CreateBranchPermissionDeniedParameters
    error_instance_id: str


class CreateDatasetPermissionDeniedParameters(typing_extensions.TypedDict):
    """The provided token does not have permission to create a dataset in this folder."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    parentFolderRid: core_models.FolderRid
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
    branchId: datasets_models.BranchId


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
    branchId: datasets_models.BranchId


@dataclass
class DeleteBranchPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["DeleteBranchPermissionDenied"]
    parameters: DeleteBranchPermissionDeniedParameters
    error_instance_id: str


class DeleteSchemaPermissionDeniedParameters(typing_extensions.TypedDict):
    """todo"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    datasetRid: datasets_models.DatasetRid
    branchId: datasets_models.BranchId
    transactionRid: typing_extensions.NotRequired[datasets_models.TransactionRid]


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


class FileNotFoundOnBranchParameters(typing_extensions.TypedDict):
    """The requested file could not be found on the given branch, or the client token does not have access to it."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    datasetRid: datasets_models.DatasetRid
    branchId: datasets_models.BranchId
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


class InvalidBranchIdParameters(typing_extensions.TypedDict):
    """The requested branch name cannot be used. Branch names cannot be empty and must not look like RIDs or UUIDs."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    branchId: datasets_models.BranchId


@dataclass
class InvalidBranchId(errors.BadRequestError):
    name: typing.Literal["InvalidBranchId"]
    parameters: InvalidBranchIdParameters
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


class OpenTransactionAlreadyExistsParameters(typing_extensions.TypedDict):
    """A transaction is already open on this dataset and branch. A branch of a dataset can only have one open transaction at a time."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    datasetRid: datasets_models.DatasetRid
    branchId: datasets_models.BranchId


@dataclass
class OpenTransactionAlreadyExists(errors.ConflictError):
    name: typing.Literal["OpenTransactionAlreadyExists"]
    parameters: OpenTransactionAlreadyExistsParameters
    error_instance_id: str


class PutSchemaPermissionDeniedParameters(typing_extensions.TypedDict):
    """todo"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    datasetRid: datasets_models.DatasetRid
    branchId: datasets_models.BranchId


@dataclass
class PutSchemaPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["PutSchemaPermissionDenied"]
    parameters: PutSchemaPermissionDeniedParameters
    error_instance_id: str


class ReadTablePermissionDeniedParameters(typing_extensions.TypedDict):
    """The provided token does not have permission to read the given dataset as a table."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    datasetRid: datasets_models.DatasetRid


@dataclass
class ReadTablePermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["ReadTablePermissionDenied"]
    parameters: ReadTablePermissionDeniedParameters
    error_instance_id: str


class SchemaNotFoundParameters(typing_extensions.TypedDict):
    """A schema could not be found for the given dataset and branch, or the client token does not have access to it."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    datasetRid: datasets_models.DatasetRid
    branchId: datasets_models.BranchId
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
    "ColumnTypesNotSupported",
    "CommitTransactionPermissionDenied",
    "CreateBranchPermissionDenied",
    "CreateDatasetPermissionDenied",
    "CreateTransactionPermissionDenied",
    "DatasetNotFound",
    "DatasetReadNotSupported",
    "DeleteBranchPermissionDenied",
    "DeleteSchemaPermissionDenied",
    "FileAlreadyExists",
    "FileNotFoundOnBranch",
    "FileNotFoundOnTransactionRange",
    "InvalidBranchId",
    "InvalidTransactionType",
    "OpenTransactionAlreadyExists",
    "PutSchemaPermissionDenied",
    "ReadTablePermissionDenied",
    "SchemaNotFound",
    "TransactionNotCommitted",
    "TransactionNotFound",
    "TransactionNotOpen",
    "UploadFilePermissionDenied",
]
