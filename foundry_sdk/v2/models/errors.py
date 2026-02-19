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


class CreateConfigValidationErrorParameters(typing_extensions.TypedDict):
    """The provided configuration is invalid."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    studioRid: models_models.ModelStudioRid
    validationFailures: str


@dataclass
class CreateConfigValidationError(errors.BadRequestError):
    name: typing.Literal["CreateConfigValidationError"]
    parameters: CreateConfigValidationErrorParameters
    error_instance_id: str


class CreateModelPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not create the Model."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class CreateModelPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["CreateModelPermissionDenied"]
    parameters: CreateModelPermissionDeniedParameters
    error_instance_id: str


class CreateModelStudioConfigVersionPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not create the ModelStudioConfigVersion."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    modelStudioRid: models_models.ModelStudioRid


@dataclass
class CreateModelStudioConfigVersionPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["CreateModelStudioConfigVersionPermissionDenied"]
    parameters: CreateModelStudioConfigVersionPermissionDeniedParameters
    error_instance_id: str


class CreateModelStudioPermissionDeniedParameters(typing_extensions.TypedDict):
    """Permission denied to create a Model Studio."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class CreateModelStudioPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["CreateModelStudioPermissionDenied"]
    parameters: CreateModelStudioPermissionDeniedParameters
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


class InvalidModelStudioCreateRequestParameters(typing_extensions.TypedDict):
    """The request to create a Model Studio contains invalid arguments."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class InvalidModelStudioCreateRequest(errors.BadRequestError):
    name: typing.Literal["InvalidModelStudioCreateRequest"]
    parameters: InvalidModelStudioCreateRequestParameters
    error_instance_id: str


class LatestModelStudioConfigVersionsPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not latest the ModelStudioConfigVersion."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    modelStudioRid: models_models.ModelStudioRid


@dataclass
class LatestModelStudioConfigVersionsPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["LatestModelStudioConfigVersionsPermissionDenied"]
    parameters: LatestModelStudioConfigVersionsPermissionDeniedParameters
    error_instance_id: str


class LaunchModelStudioPermissionDeniedParameters(typing_extensions.TypedDict):
    """Permission denied to launch a Model Studio run."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    studioRid: models_models.ModelStudioRid


@dataclass
class LaunchModelStudioPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["LaunchModelStudioPermissionDenied"]
    parameters: LaunchModelStudioPermissionDeniedParameters
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


class ModelStudioConfigVersionNotFoundParameters(typing_extensions.TypedDict):
    """The requested Model Studio configuration version was not found."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    studioRid: models_models.ModelStudioRid
    configVersion: models_models.ModelStudioConfigVersionNumber


@dataclass
class ModelStudioConfigVersionNotFound(errors.NotFoundError):
    name: typing.Literal["ModelStudioConfigVersionNotFound"]
    parameters: ModelStudioConfigVersionNotFoundParameters
    error_instance_id: str


class ModelStudioNotFoundParameters(typing_extensions.TypedDict):
    """The requested Model Studio was not found."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    studioRid: models_models.ModelStudioRid


@dataclass
class ModelStudioNotFound(errors.NotFoundError):
    name: typing.Literal["ModelStudioNotFound"]
    parameters: ModelStudioNotFoundParameters
    error_instance_id: str


class ModelStudioTrainerNotFoundParameters(typing_extensions.TypedDict):
    """The given ModelStudioTrainer could not be found."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    modelStudioTrainerTrainerId: models_models.TrainerId


@dataclass
class ModelStudioTrainerNotFound(errors.NotFoundError):
    name: typing.Literal["ModelStudioTrainerNotFound"]
    parameters: ModelStudioTrainerNotFoundParameters
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


class TrainerNotFoundParameters(typing_extensions.TypedDict):
    """The specified trainer does not exist."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    trainerId: str


@dataclass
class TrainerNotFound(errors.NotFoundError):
    name: typing.Literal["TrainerNotFound"]
    parameters: TrainerNotFoundParameters
    error_instance_id: str


__all__ = [
    "CondaSolveFailureForProvidedPackages",
    "CreateConfigValidationError",
    "CreateModelPermissionDenied",
    "CreateModelStudioConfigVersionPermissionDenied",
    "CreateModelStudioPermissionDenied",
    "CreateModelVersionPermissionDenied",
    "InvalidModelApi",
    "InvalidModelStudioCreateRequest",
    "LatestModelStudioConfigVersionsPermissionDenied",
    "LaunchModelStudioPermissionDenied",
    "ModelNotFound",
    "ModelStudioConfigVersionNotFound",
    "ModelStudioNotFound",
    "ModelStudioTrainerNotFound",
    "ModelVersionNotFound",
    "TrainerNotFound",
]
