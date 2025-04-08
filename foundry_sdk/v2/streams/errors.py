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
from foundry_sdk.v2.datasets import models as datasets_models
from foundry_sdk.v2.filesystem import models as filesystem_models
from foundry_sdk.v2.streams import models as streams_models


class CannotCreateStreamingDatasetInUserFolderParameters(typing_extensions.TypedDict):
    """Cannot create a streaming dataset in a user folder."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    parentFolderRid: filesystem_models.FolderRid


@dataclass
class CannotCreateStreamingDatasetInUserFolder(errors.BadRequestError):
    name: typing.Literal["CannotCreateStreamingDatasetInUserFolder"]
    parameters: CannotCreateStreamingDatasetInUserFolderParameters
    error_instance_id: str


class CannotWriteToTrashedStreamParameters(typing_extensions.TypedDict):
    """Cannot write to a stream that is in the trash."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    datasetRid: datasets_models.DatasetRid


@dataclass
class CannotWriteToTrashedStream(errors.BadRequestError):
    name: typing.Literal["CannotWriteToTrashedStream"]
    parameters: CannotWriteToTrashedStreamParameters
    error_instance_id: str


class CreateStreamPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not create the Stream."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    datasetRid: datasets_models.DatasetRid
    streamBranchName: datasets_models.BranchName


@dataclass
class CreateStreamPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["CreateStreamPermissionDenied"]
    parameters: CreateStreamPermissionDeniedParameters
    error_instance_id: str


class CreateStreamingDatasetPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not create the Dataset."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class CreateStreamingDatasetPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["CreateStreamingDatasetPermissionDenied"]
    parameters: CreateStreamingDatasetPermissionDeniedParameters
    error_instance_id: str


class FailedToProcessBinaryRecordParameters(typing_extensions.TypedDict):
    """The byte stream could not be processed."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class FailedToProcessBinaryRecord(errors.InternalServerError):
    name: typing.Literal["FailedToProcessBinaryRecord"]
    parameters: FailedToProcessBinaryRecordParameters
    error_instance_id: str


class InvalidStreamNoSchemaParameters(typing_extensions.TypedDict):
    """The requested stream exists but is invalid, as it does not have a schema."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    datasetRid: datasets_models.DatasetRid
    branchName: datasets_models.BranchName
    viewRid: typing_extensions.NotRequired[streams_models.ViewRid]


@dataclass
class InvalidStreamNoSchema(errors.BadRequestError):
    name: typing.Literal["InvalidStreamNoSchema"]
    parameters: InvalidStreamNoSchemaParameters
    error_instance_id: str


class InvalidStreamTypeParameters(typing_extensions.TypedDict):
    """The stream type is invalid."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    streamType: str


@dataclass
class InvalidStreamType(errors.BadRequestError):
    name: typing.Literal["InvalidStreamType"]
    parameters: InvalidStreamTypeParameters
    error_instance_id: str


class PublishBinaryRecordToStreamPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not publishBinaryRecord the Stream."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    datasetRid: datasets_models.DatasetRid
    streamBranchName: datasets_models.BranchName


@dataclass
class PublishBinaryRecordToStreamPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["PublishBinaryRecordToStreamPermissionDenied"]
    parameters: PublishBinaryRecordToStreamPermissionDeniedParameters
    error_instance_id: str


class PublishRecordToStreamPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not publishRecord the Stream."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    datasetRid: datasets_models.DatasetRid
    streamBranchName: datasets_models.BranchName


@dataclass
class PublishRecordToStreamPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["PublishRecordToStreamPermissionDenied"]
    parameters: PublishRecordToStreamPermissionDeniedParameters
    error_instance_id: str


class PublishRecordsToStreamPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not publishRecords the Stream."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    datasetRid: datasets_models.DatasetRid
    streamBranchName: datasets_models.BranchName


@dataclass
class PublishRecordsToStreamPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["PublishRecordsToStreamPermissionDenied"]
    parameters: PublishRecordsToStreamPermissionDeniedParameters
    error_instance_id: str


class RecordDoesNotMatchStreamSchemaParameters(typing_extensions.TypedDict):
    """A provided record does not match the stream schema"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    datasetRid: datasets_models.DatasetRid
    branchName: datasets_models.BranchName
    viewRid: typing_extensions.NotRequired[streams_models.ViewRid]


@dataclass
class RecordDoesNotMatchStreamSchema(errors.BadRequestError):
    name: typing.Literal["RecordDoesNotMatchStreamSchema"]
    parameters: RecordDoesNotMatchStreamSchemaParameters
    error_instance_id: str


class RecordTooLargeParameters(typing_extensions.TypedDict):
    """A record is too large to be published to the stream. On most enrollments, the maximum record size is 1MB."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class RecordTooLarge(errors.RequestEntityTooLargeError):
    name: typing.Literal["RecordTooLarge"]
    parameters: RecordTooLargeParameters
    error_instance_id: str


class ResetStreamPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not reset the Stream."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    datasetRid: datasets_models.DatasetRid
    streamBranchName: datasets_models.BranchName


@dataclass
class ResetStreamPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["ResetStreamPermissionDenied"]
    parameters: ResetStreamPermissionDeniedParameters
    error_instance_id: str


class StreamNotFoundParameters(typing_extensions.TypedDict):
    """The given Stream could not be found."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    datasetRid: datasets_models.DatasetRid
    streamBranchName: datasets_models.BranchName


@dataclass
class StreamNotFound(errors.NotFoundError):
    name: typing.Literal["StreamNotFound"]
    parameters: StreamNotFoundParameters
    error_instance_id: str


class ViewNotFoundParameters(typing_extensions.TypedDict):
    """No view for the provided view rid provided could be found."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    viewRid: streams_models.ViewRid


@dataclass
class ViewNotFound(errors.NotFoundError):
    name: typing.Literal["ViewNotFound"]
    parameters: ViewNotFoundParameters
    error_instance_id: str


__all__ = [
    "CannotCreateStreamingDatasetInUserFolder",
    "CannotWriteToTrashedStream",
    "CreateStreamPermissionDenied",
    "CreateStreamingDatasetPermissionDenied",
    "FailedToProcessBinaryRecord",
    "InvalidStreamNoSchema",
    "InvalidStreamType",
    "PublishBinaryRecordToStreamPermissionDenied",
    "PublishRecordToStreamPermissionDenied",
    "PublishRecordsToStreamPermissionDenied",
    "RecordDoesNotMatchStreamSchema",
    "RecordTooLarge",
    "ResetStreamPermissionDenied",
    "StreamNotFound",
    "ViewNotFound",
]
