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

from foundry import _errors as errors
from foundry.v2.datasets import models as datasets_models
from foundry.v2.filesystem import models as filesystem_models


class CreateDatasetPermissionDeniedParameters(typing_extensions.TypedDict):
    """The provided token does not have permission to create a dataset in this folder."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    parentFolderRid: filesystem_models.FolderRid
    name: datasets_models.DatasetName


@dataclass
class CreateDatasetPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["CreateDatasetPermissionDenied"]
    parameters: CreateDatasetPermissionDeniedParameters
    error_instance_id: str


__all__ = ["CreateDatasetPermissionDenied"]
