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
from foundry_sdk.v2.data_health import models as data_health_models


class CheckAlreadyExistsParameters(typing_extensions.TypedDict):
    """
    A check of the given type for the given subject(s) already exists. The conflicting check will be returned
    if the provided token has permission to view it.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    conflictingCheck: typing_extensions.NotRequired[data_health_models.Check]


@dataclass
class CheckAlreadyExists(errors.ConflictError):
    name: typing.Literal["CheckAlreadyExists"]
    parameters: CheckAlreadyExistsParameters
    error_instance_id: str


class CheckNotFoundParameters(typing_extensions.TypedDict):
    """The given Check could not be found."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    checkRid: data_health_models.CheckRid


@dataclass
class CheckNotFound(errors.NotFoundError):
    name: typing.Literal["CheckNotFound"]
    parameters: CheckNotFoundParameters
    error_instance_id: str


class CreateCheckPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not create the Check."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class CreateCheckPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["CreateCheckPermissionDenied"]
    parameters: CreateCheckPermissionDeniedParameters
    error_instance_id: str


class DeleteCheckPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not delete the Check."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    checkRid: data_health_models.CheckRid


@dataclass
class DeleteCheckPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["DeleteCheckPermissionDenied"]
    parameters: DeleteCheckPermissionDeniedParameters
    error_instance_id: str


class InvalidTimeCheckConfigParameters(typing_extensions.TypedDict):
    """The TimeCheckConfig is invalid. It must contain at least one of timeBounds or medianDeviation."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class InvalidTimeCheckConfig(errors.BadRequestError):
    name: typing.Literal["InvalidTimeCheckConfig"]
    parameters: InvalidTimeCheckConfigParameters
    error_instance_id: str


__all__ = [
    "CheckAlreadyExists",
    "CheckNotFound",
    "CreateCheckPermissionDenied",
    "DeleteCheckPermissionDenied",
    "InvalidTimeCheckConfig",
]
