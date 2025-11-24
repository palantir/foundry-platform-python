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
from foundry_sdk.v2.models import models as models_models


class CondaSolveFailureForProvidedPackagesParameters(typing_extensions.TypedDict):
    """Thrown when conda solve fails for the provided input packages."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    errorType: str
    errorMessage: str


@dataclass
class CondaSolveFailureForProvidedPackages(errors.BadRequestError):
    name: typing.Literal["CondaSolveFailureForProvidedPackages"]
    parameters: CondaSolveFailureForProvidedPackagesParameters
    error_instance_id: str


class CreateModelPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not create the Model."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class CreateModelPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["CreateModelPermissionDenied"]
    parameters: CreateModelPermissionDeniedParameters
    error_instance_id: str


class CreateModelVersionPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not create the ModelVersion."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    modelRid: models_models.ModelRid


@dataclass
class CreateModelVersionPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["CreateModelVersionPermissionDenied"]
    parameters: CreateModelVersionPermissionDeniedParameters
    error_instance_id: str


class InvalidModelApiParameters(typing_extensions.TypedDict):
    """The model api failed validations"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    errorType: str
    message: str


@dataclass
class InvalidModelApi(errors.BadRequestError):
    name: typing.Literal["InvalidModelApi"]
    parameters: InvalidModelApiParameters
    error_instance_id: str


class ModelNotFoundParameters(typing_extensions.TypedDict):
    """The given Model could not be found."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    modelRid: models_models.ModelRid


@dataclass
class ModelNotFound(errors.NotFoundError):
    name: typing.Literal["ModelNotFound"]
    parameters: ModelNotFoundParameters
    error_instance_id: str


class ModelVersionNotFoundParameters(typing_extensions.TypedDict):
    """The given ModelVersion could not be found."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    modelRid: models_models.ModelRid
    modelVersionRid: models_models.ModelVersionRid


@dataclass
class ModelVersionNotFound(errors.NotFoundError):
    name: typing.Literal["ModelVersionNotFound"]
    parameters: ModelVersionNotFoundParameters
    error_instance_id: str


__all__ = [
    "CondaSolveFailureForProvidedPackages",
    "CreateModelPermissionDenied",
    "CreateModelVersionPermissionDenied",
    "InvalidModelApi",
    "ModelNotFound",
    "ModelVersionNotFound",
]
