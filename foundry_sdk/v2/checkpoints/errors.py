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
from foundry_sdk.v2.checkpoints import models as checkpoints_models


class CheckpointRecordNotFoundParameters(typing_extensions.TypedDict):
    """The checkpoint record could not be found."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    recordRid: checkpoints_models.RecordRid


@dataclass
class CheckpointRecordNotFound(errors.NotFoundError):
    name: typing.Literal["CheckpointRecordNotFound"]
    parameters: CheckpointRecordNotFoundParameters
    error_instance_id: str


class CheckpointRecordPermissionDeniedParameters(typing_extensions.TypedDict):
    """The caller does not have permission to access the checkpoint record."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    recordRid: checkpoints_models.RecordRid


@dataclass
class CheckpointRecordPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["CheckpointRecordPermissionDenied"]
    parameters: CheckpointRecordPermissionDeniedParameters
    error_instance_id: str


class RecordNotFoundParameters(typing_extensions.TypedDict):
    """The given Record could not be found."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    recordRid: checkpoints_models.RecordRid


@dataclass
class RecordNotFound(errors.NotFoundError):
    name: typing.Literal["RecordNotFound"]
    parameters: RecordNotFoundParameters
    error_instance_id: str


class SearchRecordsPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not search the Record."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class SearchRecordsPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["SearchRecordsPermissionDenied"]
    parameters: SearchRecordsPermissionDeniedParameters
    error_instance_id: str


__all__ = [
    "CheckpointRecordNotFound",
    "CheckpointRecordPermissionDenied",
    "RecordNotFound",
    "SearchRecordsPermissionDenied",
]
