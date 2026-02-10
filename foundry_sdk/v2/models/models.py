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


class CreateModelRequest(core.ModelBase):
    """CreateModelRequest"""

    name: ModelName
    parent_folder_rid: filesystem_models.FolderRid = pydantic.Field(alias=str("parentFolderRid"))  # type: ignore[literal-required]


class CreateModelVersionRequest(core.ModelBase):
    """CreateModelVersionRequest"""

    model_files: ModelFiles = pydantic.Field(alias=str("modelFiles"))  # type: ignore[literal-required]
    backing_repositories: typing.List[core.RID] = pydantic.Field(alias=str("backingRepositories"))  # type: ignore[literal-required]
    conda_requirements: typing.List[str] = pydantic.Field(alias=str("condaRequirements"))  # type: ignore[literal-required]
    model_api: ModelApi = pydantic.Field(alias=str("modelApi"))  # type: ignore[literal-required]


class DillModelFiles(core.ModelBase):
    """DillModelFiles"""

    serialized_model_function: str = pydantic.Field(alias=str("serializedModelFunction"))  # type: ignore[literal-required]
    type: typing.Literal["dill"] = "dill"


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


ModelRid = core.RID
"""The Resource Identifier (RID) of a Model."""


class ModelVersion(core.ModelBase):
    """ModelVersion"""

    rid: ModelVersionRid
    model_api: ModelApi = pydantic.Field(alias=str("modelApi"))  # type: ignore[literal-required]
    conda_requirements: typing.List[str] = pydantic.Field(alias=str("condaRequirements"))  # type: ignore[literal-required]
    backing_repositories: typing.List[core.RID] = pydantic.Field(alias=str("backingRepositories"))  # type: ignore[literal-required]


ModelVersionRid = core.RID
"""The Resource Identifier (RID) of a Model Version."""


ModelFiles = DillModelFiles
"""
The serialized data of a machine learning model. This can include the model's parameters, architecture, and any other relevant information needed to reconstruct the model.
Must be a base64-encoded string of a dill-serialized model function.
"""


core.resolve_forward_references(ModelApiDataType, globalns=globals(), localns=locals())
core.resolve_forward_references(ModelApiInput, globalns=globals(), localns=locals())
core.resolve_forward_references(ModelApiOutput, globalns=globals(), localns=locals())

__all__ = [
    "CreateModelRequest",
    "CreateModelVersionRequest",
    "DillModelFiles",
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
    "ModelRid",
    "ModelVersion",
    "ModelVersionRid",
]
