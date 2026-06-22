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

from foundry_sdk import _core as core
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
    validationFailures: typing.List[models_models.CreateConfigValidationFailureReason]


@dataclass
class CreateConfigValidationError(errors.BadRequestError):
    name: typing.Literal["CreateConfigValidationError"]
    parameters: CreateConfigValidationErrorParameters
    error_instance_id: str


class CreateLiveDeploymentPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not create the LiveDeployment."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class CreateLiveDeploymentPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["CreateLiveDeploymentPermissionDenied"]
    parameters: CreateLiveDeploymentPermissionDeniedParameters
    error_instance_id: str


class CreateModelFunctionPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not create the ModelFunction."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    modelRid: models_models.ModelRid


@dataclass
class CreateModelFunctionPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["CreateModelFunctionPermissionDenied"]
    parameters: CreateModelFunctionPermissionDeniedParameters
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


class ExperimentArtifactNotFoundParameters(typing_extensions.TypedDict):
    """The requested artifact was not found in the experiment."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    modelRid: core.RID
    experimentRid: core.RID
    artifactName: str


@dataclass
class ExperimentArtifactNotFound(errors.NotFoundError):
    name: typing.Literal["ExperimentArtifactNotFound"]
    parameters: ExperimentArtifactNotFoundParameters
    error_instance_id: str


class ExperimentNotFoundParameters(typing_extensions.TypedDict):
    """The given Experiment could not be found."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    experimentRid: models_models.ExperimentRid
    modelRid: models_models.ModelRid


@dataclass
class ExperimentNotFound(errors.NotFoundError):
    name: typing.Literal["ExperimentNotFound"]
    parameters: ExperimentNotFoundParameters
    error_instance_id: str


class ExperimentSeriesNotFoundParameters(typing_extensions.TypedDict):
    """The requested series was not found in the experiment."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    modelRid: core.RID
    experimentRid: core.RID
    seriesName: str


@dataclass
class ExperimentSeriesNotFound(errors.NotFoundError):
    name: typing.Literal["ExperimentSeriesNotFound"]
    parameters: ExperimentSeriesNotFoundParameters
    error_instance_id: str


class FunctionAlreadyExistsParameters(typing_extensions.TypedDict):
    """A function already exists for this model."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    modelRid: models_models.ModelRid


@dataclass
class FunctionAlreadyExists(errors.ConflictError):
    name: typing.Literal["FunctionAlreadyExists"]
    parameters: FunctionAlreadyExistsParameters
    error_instance_id: str


class GpuTypeNotAvailableParameters(typing_extensions.TypedDict):
    """
    The requested GPU type is not available. Use a GPU type that is available in
    the deployment's resource queue.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    requestedGpuType: models_models.GpuType
    """The GPU type that was requested."""

    availableGpuTypes: typing.List[models_models.GpuType]
    """The GPU types available in the resource queue."""


@dataclass
class GpuTypeNotAvailable(errors.BadRequestError):
    name: typing.Literal["GpuTypeNotAvailable"]
    parameters: GpuTypeNotAvailableParameters
    error_instance_id: str


class InferenceFailureParameters(typing_extensions.TypedDict):
    """
    The inference request failed due to a model execution error or unexpected internal issue.
    This typically indicates a problem with the model itself rather than the input data.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    liveDeploymentRid: models_models.LiveDeploymentRid
    errorMessage: str


@dataclass
class InferenceFailure(errors.BadRequestError):
    name: typing.Literal["InferenceFailure"]
    parameters: InferenceFailureParameters
    error_instance_id: str


class InferenceInvalidInputParameters(typing_extensions.TypedDict):
    """
    The inference request contains invalid input data that does not match the model's API specification.
    Check the error type for specific validation failure details.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    liveDeploymentRid: models_models.LiveDeploymentRid
    errorType: models_models.InferenceInputErrorType
    """The specific type and details of the input validation error"""


@dataclass
class InferenceInvalidInput(errors.BadRequestError):
    name: typing.Literal["InferenceInvalidInput"]
    parameters: InferenceInvalidInputParameters
    error_instance_id: str


class InferenceTimeoutParameters(typing_extensions.TypedDict):
    """
    The live deployment took longer than 5 minutes to respond to the inference request.
    This typically indicates the model execution is taking too long or the deployment is under heavy load.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    liveDeploymentRid: models_models.LiveDeploymentRid


@dataclass
class InferenceTimeout(errors.InternalServerError):
    name: typing.Literal["InferenceTimeout"]
    parameters: InferenceTimeoutParameters
    error_instance_id: str


class InvalidExperimentSearchFilterParameters(typing_extensions.TypedDict):
    """
    The search filter is invalid. This can occur when using an unsupported operator and value type
    combination in a parameter filter, filtering by an unsupported status, or providing a malformed filter.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    reason: str
    """A human-readable description of why the filter is invalid."""


@dataclass
class InvalidExperimentSearchFilter(errors.BadRequestError):
    name: typing.Literal["InvalidExperimentSearchFilter"]
    parameters: InvalidExperimentSearchFilterParameters
    error_instance_id: str


class InvalidFunctionApiNameParameters(typing_extensions.TypedDict):
    """The provided API name for the function is invalid."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    apiName: str


@dataclass
class InvalidFunctionApiName(errors.BadRequestError):
    name: typing.Literal["InvalidFunctionApiName"]
    parameters: InvalidFunctionApiNameParameters
    error_instance_id: str


class InvalidGpuCountParameters(typing_extensions.TypedDict):
    """
    The GPU count is invalid. The GPU count must be between 1 and the maximum allowed
    for the requested GPU type.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    providedGpuCount: int
    """The GPU count that was provided in the request."""

    maxGpuCount: int
    """The maximum allowed GPU count for the requested GPU type."""


@dataclass
class InvalidGpuCount(errors.BadRequestError):
    name: typing.Literal["InvalidGpuCount"]
    parameters: InvalidGpuCountParameters
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


class JsonExperimentArtifactTablePermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not json the ExperimentArtifactTable."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    experimentRid: models_models.ExperimentRid
    experimentArtifactTableName: models_models.ExperimentArtifactName
    modelRid: models_models.ModelRid


@dataclass
class JsonExperimentArtifactTablePermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["JsonExperimentArtifactTablePermissionDenied"]
    parameters: JsonExperimentArtifactTablePermissionDeniedParameters
    error_instance_id: str


class JsonExperimentSeriesPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not json the ExperimentSeries."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    experimentSeriesName: models_models.SeriesName
    experimentRid: models_models.ExperimentRid
    modelRid: models_models.ModelRid


@dataclass
class JsonExperimentSeriesPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["JsonExperimentSeriesPermissionDenied"]
    parameters: JsonExperimentSeriesPermissionDeniedParameters
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


class LiveDeploymentNotFoundParameters(typing_extensions.TypedDict):
    """The specified live deployment was not found."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    liveDeploymentRid: models_models.LiveDeploymentRid


@dataclass
class LiveDeploymentNotFound(errors.NotFoundError):
    name: typing.Literal["LiveDeploymentNotFound"]
    parameters: LiveDeploymentNotFoundParameters
    error_instance_id: str


class ModelApiTypeUnsupportedForFunctionParameters(typing_extensions.TypedDict):
    """The model API contains a data type that is not supported for Ontology function creation."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    fieldName: str
    unsupportedType: str


@dataclass
class ModelApiTypeUnsupportedForFunction(errors.BadRequestError):
    name: typing.Literal["ModelApiTypeUnsupportedForFunction"]
    parameters: ModelApiTypeUnsupportedForFunctionParameters
    error_instance_id: str


class ModelExperimentNotFoundParameters(typing_extensions.TypedDict):
    """The requested experiment was not found or the user lacks permission to access it."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    modelRid: core.RID
    experimentRid: core.RID


@dataclass
class ModelExperimentNotFound(errors.NotFoundError):
    name: typing.Literal["ModelExperimentNotFound"]
    parameters: ModelExperimentNotFoundParameters
    error_instance_id: str


class ModelFunctionNotFoundParameters(typing_extensions.TypedDict):
    """The given ModelFunction could not be found."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    modelRid: models_models.ModelRid


@dataclass
class ModelFunctionNotFound(errors.NotFoundError):
    name: typing.Literal["ModelFunctionNotFound"]
    parameters: ModelFunctionNotFoundParameters
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


class OntologyBindingRequiredParameters(typing_extensions.TypedDict):
    """An ontologyBinding is required when creating or replacing a model function."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class OntologyBindingRequired(errors.BadRequestError):
    name: typing.Literal["OntologyBindingRequired"]
    parameters: OntologyBindingRequiredParameters
    error_instance_id: str


class OntologyNotFoundParameters(typing_extensions.TypedDict):
    """The specified ontology was not found."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    ontologyRid: core.RID


@dataclass
class OntologyNotFound(errors.NotFoundError):
    name: typing.Literal["OntologyNotFound"]
    parameters: OntologyNotFoundParameters
    error_instance_id: str


class ParquetExperimentArtifactTablePermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not parquet the ExperimentArtifactTable."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    experimentRid: models_models.ExperimentRid
    experimentArtifactTableName: models_models.ExperimentArtifactName
    modelRid: models_models.ModelRid


@dataclass
class ParquetExperimentArtifactTablePermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["ParquetExperimentArtifactTablePermissionDenied"]
    parameters: ParquetExperimentArtifactTablePermissionDeniedParameters
    error_instance_id: str


class ParquetExperimentSeriesPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not parquet the ExperimentSeries."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    experimentSeriesName: models_models.SeriesName
    experimentRid: models_models.ExperimentRid
    modelRid: models_models.ModelRid


@dataclass
class ParquetExperimentSeriesPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["ParquetExperimentSeriesPermissionDenied"]
    parameters: ParquetExperimentSeriesPermissionDeniedParameters
    error_instance_id: str


class PromoteVersionModelPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not promoteVersion the Model."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    modelRid: models_models.ModelRid


@dataclass
class PromoteVersionModelPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["PromoteVersionModelPermissionDenied"]
    parameters: PromoteVersionModelPermissionDeniedParameters
    error_instance_id: str


class ReplaceLiveDeploymentPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not replace the LiveDeployment."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    liveDeploymentRid: models_models.LiveDeploymentRid


@dataclass
class ReplaceLiveDeploymentPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["ReplaceLiveDeploymentPermissionDenied"]
    parameters: ReplaceLiveDeploymentPermissionDeniedParameters
    error_instance_id: str


class ReplaceModelFunctionPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not replace the ModelFunction."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    modelRid: models_models.ModelRid


@dataclass
class ReplaceModelFunctionPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["ReplaceModelFunctionPermissionDenied"]
    parameters: ReplaceModelFunctionPermissionDeniedParameters
    error_instance_id: str


class SearchExperimentsPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not search the Experiment."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    modelRid: models_models.ModelRid


@dataclass
class SearchExperimentsPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["SearchExperimentsPermissionDenied"]
    parameters: SearchExperimentsPermissionDeniedParameters
    error_instance_id: str


class ThreadCountTooHighParameters(typing_extensions.TypedDict):
    """The specified thread count exceeds the maximum allowed value."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    maxThreadCount: int
    """The maximum allowed thread count."""

    providedThreadCount: int
    """The thread count that was provided in the request."""


@dataclass
class ThreadCountTooHigh(errors.BadRequestError):
    name: typing.Literal["ThreadCountTooHigh"]
    parameters: ThreadCountTooHighParameters
    error_instance_id: str


class TrainerNotFoundParameters(typing_extensions.TypedDict):
    """The specified trainer does not exist."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    trainerId: models_models.TrainerId


@dataclass
class TrainerNotFound(errors.NotFoundError):
    name: typing.Literal["TrainerNotFound"]
    parameters: TrainerNotFoundParameters
    error_instance_id: str


class TransformJsonLiveDeploymentPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not transformJson the LiveDeployment."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    liveDeploymentRid: models_models.LiveDeploymentRid


@dataclass
class TransformJsonLiveDeploymentPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["TransformJsonLiveDeploymentPermissionDenied"]
    parameters: TransformJsonLiveDeploymentPermissionDeniedParameters
    error_instance_id: str


class UnsupportedLiveDeploymentParameters(typing_extensions.TypedDict):
    """The Live Deployment type is not supported by the API."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class UnsupportedLiveDeployment(errors.BadRequestError):
    name: typing.Literal["UnsupportedLiveDeployment"]
    parameters: UnsupportedLiveDeploymentParameters
    error_instance_id: str


class UnsupportedModelSourceParameters(typing_extensions.TypedDict):
    """The Model Version has a source type that is not supported by the API. This can occur when the model was created through a legacy or internal workflow that is not exposed through the public API."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class UnsupportedModelSource(errors.BadRequestError):
    name: typing.Literal["UnsupportedModelSource"]
    parameters: UnsupportedModelSourceParameters
    error_instance_id: str


__all__ = [
    "CondaSolveFailureForProvidedPackages",
    "CreateConfigValidationError",
    "CreateLiveDeploymentPermissionDenied",
    "CreateModelFunctionPermissionDenied",
    "CreateModelPermissionDenied",
    "CreateModelStudioConfigVersionPermissionDenied",
    "CreateModelStudioPermissionDenied",
    "CreateModelVersionPermissionDenied",
    "ExperimentArtifactNotFound",
    "ExperimentNotFound",
    "ExperimentSeriesNotFound",
    "FunctionAlreadyExists",
    "GpuTypeNotAvailable",
    "InferenceFailure",
    "InferenceInvalidInput",
    "InferenceTimeout",
    "InvalidExperimentSearchFilter",
    "InvalidFunctionApiName",
    "InvalidGpuCount",
    "InvalidModelApi",
    "InvalidModelStudioCreateRequest",
    "JsonExperimentArtifactTablePermissionDenied",
    "JsonExperimentSeriesPermissionDenied",
    "LatestModelStudioConfigVersionsPermissionDenied",
    "LaunchModelStudioPermissionDenied",
    "LiveDeploymentNotFound",
    "ModelApiTypeUnsupportedForFunction",
    "ModelExperimentNotFound",
    "ModelFunctionNotFound",
    "ModelNotFound",
    "ModelStudioConfigVersionNotFound",
    "ModelStudioNotFound",
    "ModelStudioTrainerNotFound",
    "ModelVersionNotFound",
    "OntologyBindingRequired",
    "OntologyNotFound",
    "ParquetExperimentArtifactTablePermissionDenied",
    "ParquetExperimentSeriesPermissionDenied",
    "PromoteVersionModelPermissionDenied",
    "ReplaceLiveDeploymentPermissionDenied",
    "ReplaceModelFunctionPermissionDenied",
    "SearchExperimentsPermissionDenied",
    "ThreadCountTooHigh",
    "TrainerNotFound",
    "TransformJsonLiveDeploymentPermissionDenied",
    "UnsupportedLiveDeployment",
    "UnsupportedModelSource",
]
