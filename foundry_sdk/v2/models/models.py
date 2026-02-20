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

ColumnTypeSpecId = str
"""An identifier for a column type specification."""


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


class DillModelFiles(core.ModelBase):
    """DillModelFiles"""

    serialized_model_function: str = pydantic.Field(alias=str("serializedModelFunction"))  # type: ignore[literal-required]
    type: typing.Literal["dill"] = "dill"


InputAlias = str
"""A string alias used to identify inputs in a Model Studio configuration."""


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


ModelVersionRid = core.RID
"""The Resource Identifier (RID) of a Model Version."""


OutputAlias = str
"""A string alias used to identify outputs in a Model Studio configuration."""


class ResourceConfiguration(core.ModelBase):
    """Compute resource configuration for training runs."""

    memory: str
    """Memory allocation (e.g., "4Gi")."""

    cpu: str
    """CPU allocation (e.g., "2")."""


RunId = str
"""A unique identifier for a Model Studio run, derived from the studio, config, and build."""


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


core.resolve_forward_references(ModelApiDataType, globalns=globals(), localns=locals())
core.resolve_forward_references(ModelApiInput, globalns=globals(), localns=locals())
core.resolve_forward_references(ModelApiOutput, globalns=globals(), localns=locals())

__all__ = [
    "ColumnTypeSpecId",
    "CreateModelRequest",
    "CreateModelStudioConfigVersionRequest",
    "CreateModelStudioRequest",
    "CreateModelVersionRequest",
    "DatasetInput",
    "DillModelFiles",
    "InputAlias",
    "ListModelStudioConfigVersionsResponse",
    "ListModelStudioRunsResponse",
    "ListModelStudioTrainersResponse",
    "ListModelVersionsResponse",
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
    "ModelVersionRid",
    "OutputAlias",
    "ResourceConfiguration",
    "RunId",
    "TrainerDescription",
    "TrainerId",
    "TrainerInputsSpecification",
    "TrainerName",
    "TrainerOutputsSpecification",
    "TrainerSchemaDefinition",
    "TrainerType",
    "TrainerVersion",
    "TrainerVersionLocator",
]
