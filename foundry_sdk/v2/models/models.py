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
from foundry_sdk.v2.orchestration import models as orchestration_models


class BooleanParameter(core.ModelBase):
    """A boolean parameter value."""

    value: bool
    type: typing.Literal["boolean"] = "boolean"


class ChangelogTooLongError(core.ModelBase):
    """The provided changelog exceeds the maximum allowed length."""

    max_length: int = pydantic.Field(alias=str("maxLength"))  # type: ignore[literal-required]
    """The maximum allowed changelog length."""

    actual_length: int = pydantic.Field(alias=str("actualLength"))  # type: ignore[literal-required]
    """The actual length of the provided changelog."""

    type: typing.Literal["changelogTooLong"] = "changelogTooLong"


ColumnTypeSpecId = str
"""An identifier for a column type specification."""


CreateConfigValidationFailureReason = typing_extensions.Annotated[
    typing.Union[
        "JsonSchemaValidationError",
        "OutputResourceInDifferentProjectError",
        "OtherValidationError",
        "MissingWorkerConfigOutputError",
        "MissingRequiredDatasetColumnError",
        "MultiplePropertiesNotAllowedForTrainerError",
        "FieldValidationError",
        "ChangelogTooLongError",
        "UnknownColumnSpecIdInConfigColumnMappingError",
        "MultipleColumnsNotAllowedForTrainerError",
        "MissingWorkerConfigInputDatasetColumnMappingError",
        "DatasetSchemaNotFoundError",
        "MissingWorkerConfigInputError",
        "MissingWorkerConfigInputObjectSetPropertyMappingError",
        "OutputResourceNotFoundError",
        "InvalidResourceConfigurationError",
    ],
    pydantic.Field(discriminator="type"),
]
"""A specific reason why configuration validation failed."""


class CreateModelRequest(core.ModelBase):
    """CreateModelRequest"""

    name: ModelName
    parent_folder_rid: filesystem_models.FolderRid = pydantic.Field(alias=str("parentFolderRid"))  # type: ignore[literal-required]


class CreateModelStudioConfigVersionRequest(core.ModelBase):
    """CreateModelStudioConfigVersionRequest"""

    name: ModelStudioConfigVersionName
    """Human readable name of the configuration version and experiment."""

    resources: ResourceConfiguration
    """The compute resources allocated for training runs."""

    changelog: typing.Optional[str] = None
    """Changelog describing changes in this version."""

    worker_config: ModelStudioWorkerConfig = pydantic.Field(alias=str("workerConfig"))  # type: ignore[literal-required]
    """The worker configuration including inputs, outputs, and custom settings."""

    trainer_id: TrainerId = pydantic.Field(alias=str("trainerId"))  # type: ignore[literal-required]
    """The identifier of the trainer to use for this configuration."""


class CreateModelStudioRequest(core.ModelBase):
    """CreateModelStudioRequest"""

    name: str
    """The name of the Model Studio."""

    parent_folder_rid: filesystem_models.FolderRid = pydantic.Field(alias=str("parentFolderRid"))  # type: ignore[literal-required]
    """The RID of the parent folder where the studio will be created."""


class CreateModelVersionRequest(core.ModelBase):
    """CreateModelVersionRequest"""

    model_files: ModelFiles = pydantic.Field(alias=str("modelFiles"))  # type: ignore[literal-required]
    backing_repositories: typing.List[core.RID] = pydantic.Field(alias=str("backingRepositories"))  # type: ignore[literal-required]
    conda_requirements: typing.List[str] = pydantic.Field(alias=str("condaRequirements"))  # type: ignore[literal-required]
    model_api: ModelApi = pydantic.Field(alias=str("modelApi"))  # type: ignore[literal-required]


class DatasetInput(core.ModelBase):
    """Dataset input configuration."""

    rid: core.RID
    """The RID of the input dataset."""

    column_mapping: typing.Dict[ColumnTypeSpecId, typing.List[core_models.ColumnName]] = pydantic.Field(alias=str("columnMapping"))  # type: ignore[literal-required]
    """Mapping of column type spec IDs to column names."""

    ignore_columns: typing.List[core_models.ColumnName] = pydantic.Field(alias=str("ignoreColumns"))  # type: ignore[literal-required]
    """Columns to ignore from the dataset."""

    select_columns: typing.List[core_models.ColumnName] = pydantic.Field(alias=str("selectColumns"))  # type: ignore[literal-required]
    """Columns to select from the dataset. If empty, all columns not in ignoreColumns will be used."""

    type: typing.Literal["dataset"] = "dataset"


class DatasetSchemaNotFoundError(core.ModelBase):
    """A schema could not be found for the specified dataset."""

    dataset_rid: core.RID = pydantic.Field(alias=str("datasetRid"))  # type: ignore[literal-required]
    """The RID of the dataset whose schema was not found."""

    type: typing.Literal["datasetSchemaNotFound"] = "datasetSchemaNotFound"


class DatetimeParameter(core.ModelBase):
    """A datetime parameter value."""

    value: core.AwareDatetime
    type: typing.Literal["datetime"] = "datetime"


class DillModelFiles(core.ModelBase):
    """DillModelFiles"""

    serialized_model_function: str = pydantic.Field(alias=str("serializedModelFunction"))  # type: ignore[literal-required]
    type: typing.Literal["dill"] = "dill"


class DoubleParameter(core.ModelBase):
    """A double parameter value."""

    value: float
    type: typing.Literal["double"] = "double"


class DoubleSeriesAggregations(core.ModelBase):
    """Aggregated statistics for numeric series."""

    min: typing.Optional[float] = None
    """Minimum value in the series. Absent if the metric has not been computed."""

    max: typing.Optional[float] = None
    """Maximum value in the series. Absent if the metric has not been computed."""

    last: typing.Optional[float] = None
    """Most recent value in the series. Absent if the metric has not been computed."""

    type: typing.Literal["double"] = "double"


class DoubleSeriesV1(core.ModelBase):
    """A series of double values."""

    series: typing.List[DoubleSeriesValueV1]
    type: typing.Literal["doubleV1"] = "doubleV1"


class DoubleSeriesValueV1(core.ModelBase):
    """A single double value in a series."""

    value: float
    timestamp: EpochMillis
    """Milliseconds since unix time zero"""

    step: core.Long


EpochMillis = core.Long
"""
Milliseconds since unix time zero. This representation is used to maintain consistency with the Parquet
format.
"""


class Experiment(core.ModelBase):
    """Experiment"""

    rid: ExperimentRid
    model_rid: ModelRid = pydantic.Field(alias=str("modelRid"))  # type: ignore[literal-required]
    created_time: core_models.CreatedTime = pydantic.Field(alias=str("createdTime"))  # type: ignore[literal-required]
    created_by: core_models.CreatedBy = pydantic.Field(alias=str("createdBy"))  # type: ignore[literal-required]
    source: ExperimentSource
    status: ExperimentStatus
    status_message: typing.Optional[str] = pydantic.Field(alias=str("statusMessage"), default=None)  # type: ignore[literal-required]
    branch: ExperimentBranch
    parameters: typing.List[Parameter]
    series: typing.List[SeriesAggregations]
    summary_metrics: typing.List[SummaryMetric] = pydantic.Field(alias=str("summaryMetrics"))  # type: ignore[literal-required]
    artifacts: typing.Dict[ExperimentArtifactName, ExperimentArtifactMetadata]
    tags: typing.List[ExperimentTagText]
    linked_model_version: typing.Optional[ModelVersionRid] = pydantic.Field(alias=str("linkedModelVersion"), default=None)  # type: ignore[literal-required]
    job_rid: typing.Optional[core_models.JobRid] = pydantic.Field(alias=str("jobRid"), default=None)  # type: ignore[literal-required]


class ExperimentArtifactMetadata(core.ModelBase):
    """Metadata about an experiment artifact."""

    name: ExperimentArtifactName
    description: typing.Optional[str] = None
    size_bytes: core_models.SizeBytes = pydantic.Field(alias=str("sizeBytes"))  # type: ignore[literal-required]
    details: ExperimentArtifactDetails


ExperimentArtifactName = str
"""The name of an experiment artifact."""


class ExperimentAuthoringSource(core.ModelBase):
    """Experiment created from an authoring repository."""

    stemma_rid: core.RID = pydantic.Field(alias=str("stemmaRid"))  # type: ignore[literal-required]
    type: typing.Literal["authoring"] = "authoring"


ExperimentBranch = str
"""ExperimentBranch"""


class ExperimentCodeWorkspaceSource(core.ModelBase):
    """Experiment created from a code workspace."""

    container_rid: core.RID = pydantic.Field(alias=str("containerRid"))  # type: ignore[literal-required]
    deployment_rid: typing.Optional[core.RID] = pydantic.Field(alias=str("deploymentRid"), default=None)  # type: ignore[literal-required]
    type: typing.Literal["codeWorkspace"] = "codeWorkspace"


ExperimentRid = core.RID
"""The Resource Identifier (RID) of an Experiment."""


class ExperimentSdkSource(core.ModelBase):
    """Experiment created from the SDK."""

    type: typing.Literal["sdk"] = "sdk"


ExperimentSource = typing_extensions.Annotated[
    typing.Union[
        "ExperimentCodeWorkspaceSource", "ExperimentAuthoringSource", "ExperimentSdkSource"
    ],
    pydantic.Field(discriminator="type"),
]
"""The source from which the experiment was created."""


ExperimentStatus = typing.Literal["RUNNING", "SUCCEEDED", "FAILED"]
"""The current status of an experiment."""


ExperimentTagText = str
"""A tag associated with an experiment."""


class FieldValidationError(core.ModelBase):
    """A dataset column type is not compatible with the trainer's supported column types."""

    dataset_rid: core.RID = pydantic.Field(alias=str("datasetRid"))  # type: ignore[literal-required]
    """The RID of the dataset containing the invalid field."""

    field_name: typing.Optional[str] = pydantic.Field(alias=str("fieldName"), default=None)  # type: ignore[literal-required]
    """The name of the dataset column or field that failed validation."""

    field_type: str = pydantic.Field(alias=str("fieldType"))  # type: ignore[literal-required]
    """The type of the dataset field."""

    type: typing.Literal["fieldValidationFailure"] = "fieldValidationFailure"


GpuType = typing.Literal["V100", "T4", "A10G", "A100", "H100", "H200", "L4", "A16", "L40S"]
"""The specific type of GPU to use."""


class InconsistentArrayDimensionsError(core.ModelBase):
    """Array elements have inconsistent dimensions."""

    first_element_shape: typing.List[int] = pydantic.Field(alias=str("firstElementShape"))  # type: ignore[literal-required]
    """The shape of the first array element"""

    conflicting_element_shape: typing.List[int] = pydantic.Field(alias=str("conflictingElementShape"))  # type: ignore[literal-required]
    """The shape of the conflicting array element"""

    type: typing.Literal["inconsistentArrayDimensions"] = "inconsistentArrayDimensions"


InferenceInputErrorType = typing_extensions.Annotated[
    typing.Union[
        "InvalidArrayShapeError",
        "TypeMismatchError",
        "UnsupportedTypeError",
        "UnknownInputNameError",
        "InvalidTabularFormatError",
        "InconsistentArrayDimensionsError",
        "RequiredValueMissingError",
        "InvalidMapFormatError",
    ],
    pydantic.Field(discriminator="type"),
]
"""
The specific type and details of an input validation error for inference requests.
Each variant carries parameters relevant to that specific error category.
"""


InputAlias = str
"""A string alias used to identify inputs in a Model Studio configuration."""


class IntegerParameter(core.ModelBase):
    """An integer parameter value."""

    value: core.Long
    type: typing.Literal["integer"] = "integer"


class InvalidArrayShapeError(core.ModelBase):
    """Array dimensions do not match expected ndarray shape."""

    expected_shape: typing.List[int] = pydantic.Field(alias=str("expectedShape"))  # type: ignore[literal-required]
    """The expected array shape from the model API specification"""

    actual_shape: typing.Optional[typing.List[int]] = pydantic.Field(alias=str("actualShape"), default=None)  # type: ignore[literal-required]
    """The actual shape of the provided array"""

    type: typing.Literal["invalidArrayShape"] = "invalidArrayShape"


class InvalidMapFormatError(core.ModelBase):
    """Map input has incorrect structure or null keys."""

    type: typing.Literal["invalidMapFormat"] = "invalidMapFormat"


class InvalidResourceConfigurationError(core.ModelBase):
    """A resource configuration field has an invalid format."""

    field: str
    """The name of the invalid field (e.g. "cpu", "memory")."""

    message: str
    """A description of why the value is invalid."""

    type: typing.Literal["invalidResourceConfiguration"] = "invalidResourceConfiguration"


class InvalidTabularFormatError(core.ModelBase):
    """Tabular input has incorrect JSON structure."""

    input_field_name: str = pydantic.Field(alias=str("inputFieldName"))  # type: ignore[literal-required]
    """The name of the tabular input field with incorrect format"""

    type: typing.Literal["invalidTabularFormat"] = "invalidTabularFormat"


class JsonSchemaValidationError(core.ModelBase):
    """The custom configuration failed JSON schema validation."""

    field: str
    """The field in the provided JSON that is invalid."""

    message: str
    """A description of the validation failure."""

    type: typing.Literal["jsonSchemaValidationFailure"] = "jsonSchemaValidationFailure"


class ListModelStudioConfigVersionsResponse(core.ModelBase):
    """ListModelStudioConfigVersionsResponse"""

    data: typing.List[ModelStudioConfigVersion]
    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]


class ListModelStudioRunsResponse(core.ModelBase):
    """ListModelStudioRunsResponse"""

    data: typing.List[ModelStudioRun]
    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]


class ListModelStudioTrainersResponse(core.ModelBase):
    """ListModelStudioTrainersResponse"""

    data: typing.List[ModelStudioTrainer]
    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]


class ListModelVersionsResponse(core.ModelBase):
    """ListModelVersionsResponse"""

    data: typing.List[ModelVersion]
    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]


LiveDeploymentRid = core.RID
"""The Resource Identifier (RID) of a Live Deployment."""


class MissingRequiredDatasetColumnError(core.ModelBase):
    """The user-provided dataset is missing a column required by the trainer."""

    dataset_rid: core.RID = pydantic.Field(alias=str("datasetRid"))  # type: ignore[literal-required]
    """The RID of the dataset missing the required column."""

    column_type_spec_id: ColumnTypeSpecId = pydantic.Field(alias=str("columnTypeSpecId"))  # type: ignore[literal-required]
    """The trainer column type spec ID for the required column."""

    column_names: typing.List[core_models.ColumnName] = pydantic.Field(alias=str("columnNames"))  # type: ignore[literal-required]
    """The valid dataset column names that could map to this trainer column."""

    type: typing.Literal["missingRequiredDatasetColumn"] = "missingRequiredDatasetColumn"


class MissingWorkerConfigInputDatasetColumnMappingError(core.ModelBase):
    """The provided worker config input dataset is missing a column mapping required by the trainer."""

    dataset_rid: core.RID = pydantic.Field(alias=str("datasetRid"))  # type: ignore[literal-required]
    """The RID of the dataset with the missing column mapping."""

    column_type_spec_id: ColumnTypeSpecId = pydantic.Field(alias=str("columnTypeSpecId"))  # type: ignore[literal-required]
    """The column type spec ID for the missing column."""

    type: typing.Literal["missingWorkerConfigInputDatasetColumnMapping"] = (
        "missingWorkerConfigInputDatasetColumnMapping"
    )


class MissingWorkerConfigInputError(core.ModelBase):
    """The worker configuration is missing an input required by the trainer."""

    input_alias: InputAlias = pydantic.Field(alias=str("inputAlias"))  # type: ignore[literal-required]
    """The alias of the missing input."""

    type: typing.Literal["missingWorkerConfigInput"] = "missingWorkerConfigInput"


class MissingWorkerConfigInputObjectSetPropertyMappingError(core.ModelBase):
    """The provided worker config input object set is missing a property mapping required by the trainer."""

    object_set_rid: core.RID = pydantic.Field(alias=str("objectSetRid"))  # type: ignore[literal-required]
    """The RID of the object set with the missing property mapping."""

    property_type_spec_id: str = pydantic.Field(alias=str("propertyTypeSpecId"))  # type: ignore[literal-required]
    """The property type spec ID for the missing property."""

    type: typing.Literal["missingWorkerConfigInputObjectSetPropertyMapping"] = (
        "missingWorkerConfigInputObjectSetPropertyMapping"
    )


class MissingWorkerConfigOutputError(core.ModelBase):
    """The worker configuration is missing an output required by the trainer."""

    output_alias: OutputAlias = pydantic.Field(alias=str("outputAlias"))  # type: ignore[literal-required]
    """The alias of the missing output."""

    type: typing.Literal["missingWorkerConfigOutput"] = "missingWorkerConfigOutput"


class Model(core.ModelBase):
    """Model"""

    rid: ModelRid


class ModelApi(core.ModelBase):
    """The Model API is a specification that describes the inputs and outputs of a machine learning model. It is used to define the interface for the model, including the types of data that can be passed to it and the types of data that it will return."""

    inputs: typing.List[ModelApiInput]
    outputs: typing.List[ModelApiOutput]


class ModelApiAnyType(core.ModelBase):
    """ModelApiAnyType"""

    type: typing.Literal["any"] = "any"


class ModelApiArrayType(core.ModelBase):
    """ModelApiArrayType"""

    item_type: ModelApiDataType = pydantic.Field(alias=str("itemType"))  # type: ignore[literal-required]
    type: typing.Literal["array"] = "array"


class ModelApiColumn(core.ModelBase):
    """ModelApiColumn"""

    name: str
    required: typing.Optional[bool] = None
    """true by default; false if the column can be null or omitted"""

    data_type: ModelApiDataType = pydantic.Field(alias=str("dataType"))  # type: ignore[literal-required]


ModelApiDataType = typing_extensions.Annotated[
    typing.Union[
        core_models.DateType,
        core_models.BooleanType,
        core_models.UnsupportedType,
        core_models.StringType,
        "ModelApiArrayType",
        core_models.DoubleType,
        core_models.IntegerType,
        core_models.FloatType,
        "ModelApiAnyType",
        "ModelApiMapType",
        core_models.LongType,
        core_models.TimestampType,
    ],
    pydantic.Field(discriminator="type"),
]
"""ModelApiDataType"""


ModelApiInput = typing_extensions.Annotated[
    typing.Union[core_models.UnsupportedType, "ModelApiParameterType", "ModelApiTabularType"],
    pydantic.Field(discriminator="type"),
]
"""ModelApiInput"""


class ModelApiMapType(core.ModelBase):
    """ModelApiMapType"""

    key_type: ModelApiDataType = pydantic.Field(alias=str("keyType"))  # type: ignore[literal-required]
    value_type: ModelApiDataType = pydantic.Field(alias=str("valueType"))  # type: ignore[literal-required]
    type: typing.Literal["map"] = "map"


ModelApiOutput = typing_extensions.Annotated[
    typing.Union[core_models.UnsupportedType, "ModelApiParameterType", "ModelApiTabularType"],
    pydantic.Field(discriminator="type"),
]
"""ModelApiOutput"""


class ModelApiParameterType(core.ModelBase):
    """ModelApiParameterType"""

    name: str
    required: typing.Optional[bool] = None
    """true by default; false if the input or output can be null or omitted"""

    data_type: ModelApiDataType = pydantic.Field(alias=str("dataType"))  # type: ignore[literal-required]
    type: typing.Literal["parameter"] = "parameter"


ModelApiTabularFormat = typing.Literal["PANDAS", "SPARK"]
"""ModelApiTabularFormat"""


class ModelApiTabularType(core.ModelBase):
    """ModelApiTabularType"""

    name: str
    required: typing.Optional[bool] = None
    """true by default; false if the input or output can be null or omitted"""

    columns: typing.List[ModelApiColumn]
    format: typing.Optional[ModelApiTabularFormat] = None
    """Dataframe format the model will receive or is expected to return for this input or output. PANDAS is the default."""

    type: typing.Literal["tabular"] = "tabular"


ModelName = str
"""ModelName"""


class ModelOutput(core.ModelBase):
    """Model output configuration."""

    model_rid: core.RID = pydantic.Field(alias=str("modelRid"))  # type: ignore[literal-required]
    """The RID of the output model."""

    type: typing.Literal["model"] = "model"


ModelRid = core.RID
"""The Resource Identifier (RID) of a Model."""


class ModelStudio(core.ModelBase):
    """ModelStudio"""

    rid: ModelStudioRid
    folder_rid: filesystem_models.FolderRid = pydantic.Field(alias=str("folderRid"))  # type: ignore[literal-required]
    """The parent folder containing this Model Studio."""

    created_time: core_models.CreatedTime = pydantic.Field(alias=str("createdTime"))  # type: ignore[literal-required]


class ModelStudioConfigVersion(core.ModelBase):
    """ModelStudioConfigVersion"""

    name: ModelStudioConfigVersionName
    """Human readable name of the configuration version and experiment."""

    version: ModelStudioConfigVersionNumber
    """The version number of this configuration."""

    trainer_id: TrainerId = pydantic.Field(alias=str("trainerId"))  # type: ignore[literal-required]
    """The identifier of the trainer to use for this configuration."""

    trainer: TrainerVersionLocator
    """The trainer and version used for this configuration."""

    worker_config: ModelStudioWorkerConfig = pydantic.Field(alias=str("workerConfig"))  # type: ignore[literal-required]
    """The worker configuration including inputs, outputs, and custom settings."""

    resources: ResourceConfiguration
    """The compute resources allocated for training runs."""

    changelog: typing.Optional[str] = None
    """Changelog describing changes in this version."""

    created_by: core_models.CreatedBy = pydantic.Field(alias=str("createdBy"))  # type: ignore[literal-required]
    created_time: core_models.CreatedTime = pydantic.Field(alias=str("createdTime"))  # type: ignore[literal-required]


ModelStudioConfigVersionName = str
"""Human readable name of the configuration version and experiment."""


ModelStudioConfigVersionNumber = int
"""The version number of a Model Studio Configuration."""


ModelStudioRid = core.RID
"""The Resource Identifier (RID) of a Model Studio."""


class ModelStudioRun(core.ModelBase):
    """ModelStudioRun"""

    run_id: RunId = pydantic.Field(alias=str("runId"))  # type: ignore[literal-required]
    """A unique identifier for this run, derived from the studio, config, and build."""

    build_rid: ModelStudioRunBuildRid = pydantic.Field(alias=str("buildRid"))  # type: ignore[literal-required]
    """The RID of the build associated with this run."""

    job_rid: ModelStudioRunJobRid = pydantic.Field(alias=str("jobRid"))  # type: ignore[literal-required]
    """The RID of the job associated with this run."""

    config_version: ModelStudioConfigVersionNumber = pydantic.Field(alias=str("configVersion"))  # type: ignore[literal-required]
    """The configuration version used for this run."""

    started_by: core_models.CreatedBy = pydantic.Field(alias=str("startedBy"))  # type: ignore[literal-required]
    """The user who started this run."""

    started_time: core_models.CreatedTime = pydantic.Field(alias=str("startedTime"))  # type: ignore[literal-required]
    """When this run was started."""

    build_status: typing.Optional[orchestration_models.BuildStatus] = pydantic.Field(alias=str("buildStatus"), default=None)  # type: ignore[literal-required]
    """Status of the build."""

    resolved_outputs: typing.Dict[OutputAlias, ModelStudioRunOutput] = pydantic.Field(alias=str("resolvedOutputs"))  # type: ignore[literal-required]
    """Map of alias to resolved output details (e.g., for models, contains the version RID and experiment)."""


ModelStudioRunBuildRid = core.RID
"""The RID of the build associated with this run."""


ModelStudioRunJobRid = core.RID
"""The RID of the job associated with this run."""


class ModelStudioRunModelOutput(core.ModelBase):
    """Resolved model output details for a Model Studio run."""

    model_rid: core.RID = pydantic.Field(alias=str("modelRid"))  # type: ignore[literal-required]
    """The RID of the model."""

    model_version_rid: core.RID = pydantic.Field(alias=str("modelVersionRid"))  # type: ignore[literal-required]
    """The RID of the model version created by this run."""

    experiment_rid: typing.Optional[core.RID] = pydantic.Field(alias=str("experimentRid"), default=None)  # type: ignore[literal-required]
    """The RID of the experiment associated with this run, if any."""

    type: typing.Literal["model"] = "model"


class ModelStudioTrainer(core.ModelBase):
    """ModelStudioTrainer"""

    trainer_id: TrainerId = pydantic.Field(alias=str("trainerId"))  # type: ignore[literal-required]
    version: TrainerVersion
    """The version of this trainer."""

    name: TrainerName
    """Human-readable name of the trainer."""

    type: TrainerType
    """The type/category of this trainer (e.g., TABULAR_CLASSIFICATION, TIME_SERIES)."""

    description: TrainerDescription
    """Description of what this trainer does and its capabilities."""

    custom_config_schema: TrainerSchemaDefinition = pydantic.Field(alias=str("customConfigSchema"))  # type: ignore[literal-required]
    """JSON schema defining the custom configuration parameters for this trainer."""

    inputs: TrainerInputsSpecification
    """Input specifications for this trainer."""

    outputs: TrainerOutputsSpecification
    """Output specifications for this trainer."""

    experimental: ModelStudioTrainerExperimental
    """Whether this trainer is experimental and may have breaking changes."""


ModelStudioTrainerExperimental = bool
"""Whether this trainer is experimental and may have breaking changes."""


class ModelStudioWorkerConfig(core.ModelBase):
    """Configuration for the Model Studio worker."""

    custom_config: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(alias=str("customConfig"), default=None)  # type: ignore[literal-required]
    """Custom configuration matching the trainer's JSON schema."""

    inputs: typing.Dict[InputAlias, ModelStudioInput]
    """Input configurations keyed by alias."""

    outputs: typing.Dict[OutputAlias, ModelStudioOutput]
    """Output configurations keyed by alias."""


class ModelVersion(core.ModelBase):
    """ModelVersion"""

    rid: ModelVersionRid
    model_api: ModelApi = pydantic.Field(alias=str("modelApi"))  # type: ignore[literal-required]
    conda_requirements: typing.List[str] = pydantic.Field(alias=str("condaRequirements"))  # type: ignore[literal-required]
    backing_repositories: typing.List[core.RID] = pydantic.Field(alias=str("backingRepositories"))  # type: ignore[literal-required]
    created_time: core_models.CreatedTime = pydantic.Field(alias=str("createdTime"))  # type: ignore[literal-required]
    source: typing.Optional[ModelVersionSource] = None
    linked_experiment: typing.Optional[ExperimentRid] = pydantic.Field(alias=str("linkedExperiment"), default=None)  # type: ignore[literal-required]
    """The Experiment linked to this Model Version, if one exists."""


class ModelVersionCodeRepositorySource(core.ModelBase):
    """Model version created from a code repository."""

    repository_rid: core.RID = pydantic.Field(alias=str("repositoryRid"))  # type: ignore[literal-required]
    branch: str
    type: typing.Literal["codeRepository"] = "codeRepository"


class ModelVersionCodeWorkspaceSource(core.ModelBase):
    """Model version created from a code workspace."""

    code_workspace_rid: core.RID = pydantic.Field(alias=str("codeWorkspaceRid"))  # type: ignore[literal-required]
    branch: str
    type: typing.Literal["codeWorkspace"] = "codeWorkspace"


class ModelVersionContainerizedSource(core.ModelBase):
    """Model version imported from a containerized model."""

    type: typing.Literal["importedContainerizedModel"] = "importedContainerizedModel"


class ModelVersionExternalSource(core.ModelBase):
    """Model version backed by an external model."""

    type: typing.Literal["external"] = "external"


class ModelVersionModelStudioSource(core.ModelBase):
    """Model version created from Model Studio."""

    model_studio_rid: core.RID = pydantic.Field(alias=str("modelStudioRid"))  # type: ignore[literal-required]
    type: typing.Literal["modelStudio"] = "modelStudio"


class ModelVersionPromotedSource(core.ModelBase):
    """Model version promoted from another model version."""

    previous_model_rid: ModelRid = pydantic.Field(alias=str("previousModelRid"))  # type: ignore[literal-required]
    previous_model_version_rid: ModelVersionRid = pydantic.Field(alias=str("previousModelVersionRid"))  # type: ignore[literal-required]
    type: typing.Literal["promoted"] = "promoted"


ModelVersionRid = core.RID
"""The Resource Identifier (RID) of a Model Version."""


class ModelVersionSdkSource(core.ModelBase):
    """Model version created via the SDK."""

    type: typing.Literal["sdk"] = "sdk"


ModelVersionSource = typing_extensions.Annotated[
    typing.Union[
        "ModelVersionContainerizedSource",
        "ModelVersionExternalSource",
        "ModelVersionCodeWorkspaceSource",
        "ModelVersionModelStudioSource",
        "ModelVersionCodeRepositorySource",
        "ModelVersionSdkSource",
        "ModelVersionPromotedSource",
    ],
    pydantic.Field(discriminator="type"),
]
"""The source from which this model version was created."""


class MultipleColumnsNotAllowedForTrainerError(core.ModelBase):
    """Multiple columns were mapped but the trainer only allows a single column for this spec."""

    dataset_rid: core.RID = pydantic.Field(alias=str("datasetRid"))  # type: ignore[literal-required]
    """The RID of the dataset with multiple columns mapped."""

    column_type_spec_id: ColumnTypeSpecId = pydantic.Field(alias=str("columnTypeSpecId"))  # type: ignore[literal-required]
    """The column type spec ID that does not allow multiple columns."""

    type: typing.Literal["multipleColumnsNotAllowedForTrainer"] = (
        "multipleColumnsNotAllowedForTrainer"
    )


class MultiplePropertiesNotAllowedForTrainerError(core.ModelBase):
    """Multiple properties were mapped but the trainer only allows a single property for this spec."""

    object_set_rid: core.RID = pydantic.Field(alias=str("objectSetRid"))  # type: ignore[literal-required]
    """The RID of the object set with multiple properties mapped."""

    property_type_spec_id: str = pydantic.Field(alias=str("propertyTypeSpecId"))  # type: ignore[literal-required]
    """The property type spec ID that does not allow multiple properties."""

    type: typing.Literal["multiplePropertiesNotAllowedForTrainer"] = (
        "multiplePropertiesNotAllowedForTrainer"
    )


class OtherValidationError(core.ModelBase):
    """A validation error that does not match any specific known type."""

    message: str
    """A description of the validation failure."""

    type: typing.Literal["other"] = "other"


OutputAlias = str
"""A string alias used to identify outputs in a Model Studio configuration."""


class OutputResourceInDifferentProjectError(core.ModelBase):
    """The output resource is in a different project than the Model Studio."""

    resource_rid: core.RID = pydantic.Field(alias=str("resourceRid"))  # type: ignore[literal-required]
    """The RID of the resource in a different project."""

    output_alias: OutputAlias = pydantic.Field(alias=str("outputAlias"))  # type: ignore[literal-required]
    """The alias of the output referencing the resource."""

    type: typing.Literal["outputResourceInDifferentProject"] = "outputResourceInDifferentProject"


class OutputResourceNotFoundError(core.ModelBase):
    """The output resource does not exist or is in the trash."""

    resource_rid: core.RID = pydantic.Field(alias=str("resourceRid"))  # type: ignore[literal-required]
    """The RID of the resource that was not found."""

    output_alias: OutputAlias = pydantic.Field(alias=str("outputAlias"))  # type: ignore[literal-required]
    """The alias of the output referencing the missing resource."""

    type: typing.Literal["outputResourceNotFound"] = "outputResourceNotFound"


class Parameter(core.ModelBase):
    """A parameter with its name and value."""

    name: ParameterName
    """The parameter name"""

    value: ParameterValue
    """The parameter value"""


ParameterName = str
"""The name of an experiment parameter."""


ParameterValue = typing_extensions.Annotated[
    typing.Union[
        "DatetimeParameter",
        "BooleanParameter",
        "StringParameter",
        "DoubleParameter",
        "IntegerParameter",
    ],
    pydantic.Field(discriminator="type"),
]
"""A parameter value logged for an experiment."""


class PromoteVersionModelRequest(core.ModelBase):
    """PromoteVersionModelRequest"""

    source_model_version_rid: ModelVersionRid = pydantic.Field(alias=str("sourceModelVersionRid"))  # type: ignore[literal-required]


class RequiredValueMissingError(core.ModelBase):
    """Required input field is null or missing."""

    field_name: str = pydantic.Field(alias=str("fieldName"))  # type: ignore[literal-required]
    """The name of the required field that was null or missing"""

    type: typing.Literal["requiredValueMissing"] = "requiredValueMissing"


class ResourceConfiguration(core.ModelBase):
    """Compute resource configuration for training runs."""

    memory: str
    """Memory allocation (e.g., "4G")."""

    cpu: str
    """CPU allocation (e.g., "2")."""

    gpu: typing.Optional[GpuType] = None
    """GPU allocation (must be available in the project's resource queue)."""


RunId = str
"""A unique identifier for a Model Studio run, derived from the studio, config, and build."""


class SearchExperimentsAndFilter(core.ModelBase):
    """Returns experiments where every filter is satisfied."""

    filters: typing.List[SearchExperimentsFilter]
    type: typing.Literal["and"] = "and"


class SearchExperimentsContainsFilter(core.ModelBase):
    """Filter for substring containment matches."""

    field: SearchExperimentsContainsFilterField
    value: typing.Any
    type: typing.Literal["contains"] = "contains"


SearchExperimentsContainsFilterField = typing.Literal[
    "EXPERIMENT_NAME", "PARAMETER_NAME", "SERIES_NAME"
]
"""Fields that support substring containment filtering."""


class SearchExperimentsEqualsFilter(core.ModelBase):
    """Filter for exact field value matches."""

    field: SearchExperimentsEqualsFilterField
    value: typing.Any
    type: typing.Literal["eq"] = "eq"


SearchExperimentsEqualsFilterField = typing.Literal[
    "STATUS",
    "BRANCH",
    "EXPERIMENT_NAME",
    "EXPERIMENT_RID",
    "JOB_RID",
    "TAG",
    "PARAMETER_NAME",
    "SERIES_NAME",
]
"""Fields that support equality filtering."""


SearchExperimentsFilter = typing_extensions.Annotated[
    typing.Union[
        "SearchExperimentsSeriesFilter",
        "SearchExperimentsContainsFilter",
        "SearchExperimentsNotFilter",
        "SearchExperimentsOrFilter",
        "SearchExperimentsAndFilter",
        "SearchExperimentsParameterFilter",
        "SearchExperimentsSummaryMetricFilter",
        "SearchExperimentsEqualsFilter",
        "SearchExperimentsStartsWithFilter",
    ],
    pydantic.Field(discriminator="type"),
]
"""
Filter for searching experiments using operator-based composition.
Supports equality, text matching, boolean combination operators, and compound filters
that atomically bind a name to a value comparison.

Example filters:
- Simple status: {"eq": {"field": "STATUS", "value": "RUNNING"}}
- Branch match: {"eq": {"field": "BRANCH", "value": "master"}}
- Parameter filter: {"parameterFilter": {"parameterName": "learning_rate", "operator": "GT", "value": 0.01}}
- Combined: {"and": {"filters": [
    {"eq": {"field": "STATUS", "value": "SUCCEEDED"}},
    {"parameterFilter": {"parameterName": "learning_rate", "operator": "GT", "value": 0.5}}
  ]}}
"""


class SearchExperimentsNotFilter(core.ModelBase):
    """Returns experiments where the filter is not satisfied."""

    value: SearchExperimentsFilter
    type: typing.Literal["not"] = "not"


SearchExperimentsNumericFilterOperator = typing.Literal["EQ", "GT", "LT"]
"""Comparison operator for numeric filter predicates (series and summary metrics)."""


class SearchExperimentsOrFilter(core.ModelBase):
    """Returns experiments where at least one filter is satisfied."""

    filters: typing.List[SearchExperimentsFilter]
    type: typing.Literal["or"] = "or"


class SearchExperimentsOrderBy(core.ModelBase):
    """Ordering configuration for experiment search results."""

    field: SearchExperimentsOrderByField
    direction: core_models.OrderByDirection


SearchExperimentsOrderByField = typing.Literal["EXPERIMENT_NAME", "CREATED_TIME"]
"""Fields to order experiment search results by."""


class SearchExperimentsParameterFilter(core.ModelBase):
    """
    Filter that atomically binds a parameter name to a value comparison,
    ensuring both conditions are evaluated on the same parameter.
    Supported combinations:
    - EQ: boolean, double, integer, or datetime value
    - GT/LT: double, integer, or datetime value
    - CONTAINS: string value (substring match on the parameter's string value)
    """

    parameter_name: ParameterName = pydantic.Field(alias=str("parameterName"))  # type: ignore[literal-required]
    """The exact name of the parameter to filter on."""

    operator: SearchExperimentsParameterFilterOperator
    """The comparison operator to apply."""

    value: typing.Any
    """The value to compare against."""

    type: typing.Literal["parameterFilter"] = "parameterFilter"


SearchExperimentsParameterFilterOperator = typing.Literal["EQ", "GT", "LT", "CONTAINS"]
"""Comparison operator for parameter filter predicates."""


class SearchExperimentsRequest(core.ModelBase):
    """SearchExperimentsRequest"""

    where: typing.Optional[SearchExperimentsFilter] = None
    """Optional search filter for filtering experiments. If not provided, all experiments for the model are returned."""

    order_by: typing.Optional[SearchExperimentsOrderBy] = pydantic.Field(alias=str("orderBy"), default=None)  # type: ignore[literal-required]
    """The field to sort by. Default is to sort by relevance."""

    page_size: typing.Optional[core_models.PageSize] = pydantic.Field(alias=str("pageSize"), default=None)  # type: ignore[literal-required]
    """The maximum number of results to return. Default 50, maximum of 100."""

    page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("pageToken"), default=None)  # type: ignore[literal-required]
    """PageToken to identify the next page to retrieve. Leave empty for the first request."""


class SearchExperimentsResponse(core.ModelBase):
    """Response from searching experiments."""

    data: typing.List[Experiment]
    """List of experiments matching the search criteria."""

    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]
    """Token for retrieving the next page of results, if more results are available."""


class SearchExperimentsSeriesFilter(core.ModelBase):
    """
    Filter that atomically binds a series name to a metric comparison,
    ensuring all conditions are evaluated on the same series.
    """

    series_name: SeriesName = pydantic.Field(alias=str("seriesName"))  # type: ignore[literal-required]
    """The name of the series to filter on."""

    field: SearchExperimentsSeriesFilterField
    """The series metric to compare."""

    operator: SearchExperimentsNumericFilterOperator
    """The comparison operator (EQ, GT, or LT)."""

    value: typing.Any
    """The value to compare against."""

    type: typing.Literal["seriesFilter"] = "seriesFilter"


SearchExperimentsSeriesFilterField = typing.Literal[
    "LENGTH", "AGGREGATION_MIN", "AGGREGATION_MAX", "AGGREGATION_LAST"
]
"""The series metric to filter on."""


class SearchExperimentsStartsWithFilter(core.ModelBase):
    """Filter for prefix matches."""

    field: SearchExperimentsStartsWithFilterField
    value: typing.Any
    type: typing.Literal["startsWith"] = "startsWith"


SearchExperimentsStartsWithFilterField = typing.Literal[
    "EXPERIMENT_NAME", "PARAMETER_NAME", "SERIES_NAME"
]
"""Fields that support prefix filtering."""


class SearchExperimentsSummaryMetricFilter(core.ModelBase):
    """
    Filter that atomically binds a series name and aggregation type to a value comparison,
    ensuring all conditions are evaluated on the same summary metric.
    """

    series_name: SeriesName = pydantic.Field(alias=str("seriesName"))  # type: ignore[literal-required]
    """The name of the series this metric belongs to."""

    aggregation: SummaryMetricAggregation
    """The aggregation type (MIN, MAX, LAST)."""

    operator: SearchExperimentsNumericFilterOperator
    """The comparison operator (EQ, GT, or LT)."""

    value: typing.Any
    """The value to compare against."""

    type: typing.Literal["summaryMetricFilter"] = "summaryMetricFilter"


class SeriesAggregations(core.ModelBase):
    """Series with precomputed aggregation values."""

    name: SeriesName
    """The series name"""

    length: typing.Optional[core.Long] = None
    """Number of values in the series. This field may be absent when series aggregations are derived from summary metrics rather than the full series data."""

    value: SeriesAggregationsValue
    """Aggregated values for this series"""


SeriesName = str
"""The name of a series (metrics tracked over time)."""


class StringParameter(core.ModelBase):
    """A string parameter value."""

    value: str
    type: typing.Literal["string"] = "string"


class SummaryMetric(core.ModelBase):
    """A summary metric with series name, aggregation type, and computed value."""

    series_name: SeriesName = pydantic.Field(alias=str("seriesName"))  # type: ignore[literal-required]
    """Name of the series this metric belongs to"""

    aggregation: SummaryMetricAggregation
    """Type of aggregation (MIN, MAX, LAST)"""

    value: float
    """The computed value"""


SummaryMetricAggregation = typing.Literal["MIN", "MAX", "LAST"]
"""The type of aggregation computed for a summary metric."""


class TableArtifactDetails(core.ModelBase):
    """Details about a table artifact."""

    row_count: core.Long = pydantic.Field(alias=str("rowCount"))  # type: ignore[literal-required]
    type: typing.Literal["table"] = "table"


TrainerDescription = str
"""Description of what a trainer does and its capabilities."""


TrainerId = str
"""The identifier for a trainer."""


TrainerInputsSpecification = typing.Any
"""Specification of the inputs required by a trainer. When creating a ModelStudioConfigVersion, the workerConfig.inputs must conform to this specification, providing entries for each required input defined here."""


TrainerName = str
"""Human-readable name of a trainer."""


TrainerOutputsSpecification = typing.Any
"""Specification of the outputs produced by a trainer. When creating a ModelStudioConfigVersion, the workerConfig.outputs must conform to this specification, providing entries for each required output defined here."""


TrainerSchemaDefinition = typing.Any
"""JSON schema defining the custom configuration parameters for a trainer."""


TrainerType = str
"""The type/category of a trainer."""


TrainerVersion = str
"""A specific version identifier for a trainer."""


class TrainerVersionLocator(core.ModelBase):
    """Identifies a specific version of a trainer."""

    trainer_id: TrainerId = pydantic.Field(alias=str("trainerId"))  # type: ignore[literal-required]
    version: str


class TransformJsonLiveDeploymentRequest(core.ModelBase):
    """TransformJsonLiveDeploymentRequest"""

    input: typing.Dict[str, typing.Any]
    """The input data for the model inference. The structure should match the model's transform API specification, where each key is an input name and the value is the corresponding input data."""


class TransformLiveDeploymentResponse(core.ModelBase):
    """The response from transforming input data using a live deployment."""

    output: typing.Dict[str, typing.Any]
    """The output data from the model inference. The structure depends on the model's defined API specification, where each key is an output name and the value is the corresponding output data."""


class TypeMismatchError(core.ModelBase):
    """Input type does not match expected type in model API."""

    expected_type: str = pydantic.Field(alias=str("expectedType"))  # type: ignore[literal-required]
    """The expected type from the model API specification"""

    actual_type: str = pydantic.Field(alias=str("actualType"))  # type: ignore[literal-required]
    """The actual type provided in the input"""

    type: typing.Literal["typeMismatch"] = "typeMismatch"


class UnknownColumnSpecIdInConfigColumnMappingError(core.ModelBase):
    """The worker config column mapping contains an unknown column spec ID not found in the trainer's column specification."""

    dataset_rid: core.RID = pydantic.Field(alias=str("datasetRid"))  # type: ignore[literal-required]
    """The RID of the dataset containing the unknown column mapping."""

    column_type_spec_id: ColumnTypeSpecId = pydantic.Field(alias=str("columnTypeSpecId"))  # type: ignore[literal-required]
    """The unknown column type spec ID."""

    type: typing.Literal["unknownColumnSpecIdInConfigColumnMapping"] = (
        "unknownColumnSpecIdInConfigColumnMapping"
    )


class UnknownInputNameError(core.ModelBase):
    """Provided input name not found in model API specification."""

    input_name: str = pydantic.Field(alias=str("inputName"))  # type: ignore[literal-required]
    """The input name that was not found in the model API specification"""

    type: typing.Literal["unknownInputName"] = "unknownInputName"


class UnsupportedTypeError(core.ModelBase):
    """Input contains an unsupported data type."""

    unsupported_type: str = pydantic.Field(alias=str("unsupportedType"))  # type: ignore[literal-required]
    """The unsupported data type"""

    type: typing.Literal["unsupportedType"] = "unsupportedType"


ExperimentArtifactDetails = TableArtifactDetails
"""Details about an experiment artifact."""


ModelFiles = DillModelFiles
"""
The serialized data of a machine learning model. This can include the model's parameters, architecture, and any other relevant information needed to reconstruct the model.
Must be a base64-encoded string of a dill-serialized model function.
"""


ModelStudioInput = DatasetInput
"""Input specification for a Model Studio configuration."""


ModelStudioOutput = ModelOutput
"""Output specification for a Model Studio configuration."""


ModelStudioRunOutput = ModelStudioRunModelOutput
"""Resolved output details for a Model Studio run."""


Series = DoubleSeriesV1
"""A series of values logged over time."""


SeriesAggregationsValue = DoubleSeriesAggregations
"""Union of aggregation values by series type."""


core.resolve_forward_references(
    CreateConfigValidationFailureReason, globalns=globals(), localns=locals()
)
core.resolve_forward_references(ExperimentSource, globalns=globals(), localns=locals())
core.resolve_forward_references(InferenceInputErrorType, globalns=globals(), localns=locals())
core.resolve_forward_references(ModelApiDataType, globalns=globals(), localns=locals())
core.resolve_forward_references(ModelApiInput, globalns=globals(), localns=locals())
core.resolve_forward_references(ModelApiOutput, globalns=globals(), localns=locals())
core.resolve_forward_references(ModelVersionSource, globalns=globals(), localns=locals())
core.resolve_forward_references(ParameterValue, globalns=globals(), localns=locals())
core.resolve_forward_references(SearchExperimentsFilter, globalns=globals(), localns=locals())

__all__ = [
    "BooleanParameter",
    "ChangelogTooLongError",
    "ColumnTypeSpecId",
    "CreateConfigValidationFailureReason",
    "CreateModelRequest",
    "CreateModelStudioConfigVersionRequest",
    "CreateModelStudioRequest",
    "CreateModelVersionRequest",
    "DatasetInput",
    "DatasetSchemaNotFoundError",
    "DatetimeParameter",
    "DillModelFiles",
    "DoubleParameter",
    "DoubleSeriesAggregations",
    "DoubleSeriesV1",
    "DoubleSeriesValueV1",
    "EpochMillis",
    "Experiment",
    "ExperimentArtifactDetails",
    "ExperimentArtifactMetadata",
    "ExperimentArtifactName",
    "ExperimentAuthoringSource",
    "ExperimentBranch",
    "ExperimentCodeWorkspaceSource",
    "ExperimentRid",
    "ExperimentSdkSource",
    "ExperimentSource",
    "ExperimentStatus",
    "ExperimentTagText",
    "FieldValidationError",
    "GpuType",
    "InconsistentArrayDimensionsError",
    "InferenceInputErrorType",
    "InputAlias",
    "IntegerParameter",
    "InvalidArrayShapeError",
    "InvalidMapFormatError",
    "InvalidResourceConfigurationError",
    "InvalidTabularFormatError",
    "JsonSchemaValidationError",
    "ListModelStudioConfigVersionsResponse",
    "ListModelStudioRunsResponse",
    "ListModelStudioTrainersResponse",
    "ListModelVersionsResponse",
    "LiveDeploymentRid",
    "MissingRequiredDatasetColumnError",
    "MissingWorkerConfigInputDatasetColumnMappingError",
    "MissingWorkerConfigInputError",
    "MissingWorkerConfigInputObjectSetPropertyMappingError",
    "MissingWorkerConfigOutputError",
    "Model",
    "ModelApi",
    "ModelApiAnyType",
    "ModelApiArrayType",
    "ModelApiColumn",
    "ModelApiDataType",
    "ModelApiInput",
    "ModelApiMapType",
    "ModelApiOutput",
    "ModelApiParameterType",
    "ModelApiTabularFormat",
    "ModelApiTabularType",
    "ModelFiles",
    "ModelName",
    "ModelOutput",
    "ModelRid",
    "ModelStudio",
    "ModelStudioConfigVersion",
    "ModelStudioConfigVersionName",
    "ModelStudioConfigVersionNumber",
    "ModelStudioInput",
    "ModelStudioOutput",
    "ModelStudioRid",
    "ModelStudioRun",
    "ModelStudioRunBuildRid",
    "ModelStudioRunJobRid",
    "ModelStudioRunModelOutput",
    "ModelStudioRunOutput",
    "ModelStudioTrainer",
    "ModelStudioTrainerExperimental",
    "ModelStudioWorkerConfig",
    "ModelVersion",
    "ModelVersionCodeRepositorySource",
    "ModelVersionCodeWorkspaceSource",
    "ModelVersionContainerizedSource",
    "ModelVersionExternalSource",
    "ModelVersionModelStudioSource",
    "ModelVersionPromotedSource",
    "ModelVersionRid",
    "ModelVersionSdkSource",
    "ModelVersionSource",
    "MultipleColumnsNotAllowedForTrainerError",
    "MultiplePropertiesNotAllowedForTrainerError",
    "OtherValidationError",
    "OutputAlias",
    "OutputResourceInDifferentProjectError",
    "OutputResourceNotFoundError",
    "Parameter",
    "ParameterName",
    "ParameterValue",
    "PromoteVersionModelRequest",
    "RequiredValueMissingError",
    "ResourceConfiguration",
    "RunId",
    "SearchExperimentsAndFilter",
    "SearchExperimentsContainsFilter",
    "SearchExperimentsContainsFilterField",
    "SearchExperimentsEqualsFilter",
    "SearchExperimentsEqualsFilterField",
    "SearchExperimentsFilter",
    "SearchExperimentsNotFilter",
    "SearchExperimentsNumericFilterOperator",
    "SearchExperimentsOrFilter",
    "SearchExperimentsOrderBy",
    "SearchExperimentsOrderByField",
    "SearchExperimentsParameterFilter",
    "SearchExperimentsParameterFilterOperator",
    "SearchExperimentsRequest",
    "SearchExperimentsResponse",
    "SearchExperimentsSeriesFilter",
    "SearchExperimentsSeriesFilterField",
    "SearchExperimentsStartsWithFilter",
    "SearchExperimentsStartsWithFilterField",
    "SearchExperimentsSummaryMetricFilter",
    "Series",
    "SeriesAggregations",
    "SeriesAggregationsValue",
    "SeriesName",
    "StringParameter",
    "SummaryMetric",
    "SummaryMetricAggregation",
    "TableArtifactDetails",
    "TrainerDescription",
    "TrainerId",
    "TrainerInputsSpecification",
    "TrainerName",
    "TrainerOutputsSpecification",
    "TrainerSchemaDefinition",
    "TrainerType",
    "TrainerVersion",
    "TrainerVersionLocator",
    "TransformJsonLiveDeploymentRequest",
    "TransformLiveDeploymentResponse",
    "TypeMismatchError",
    "UnknownColumnSpecIdInConfigColumnMappingError",
    "UnknownInputNameError",
    "UnsupportedTypeError",
]
