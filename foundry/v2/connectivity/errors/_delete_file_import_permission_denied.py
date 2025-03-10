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
from foundry.v2.connectivity import models as connectivity_models


class DeleteFileImportPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not delete the FileImport."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    fileImportRid: connectivity_models.FileImportRid
    connectionRid: connectivity_models.ConnectionRid


@dataclass
class DeleteFileImportPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["DeleteFileImportPermissionDenied"]
    parameters: DeleteFileImportPermissionDeniedParameters
    error_instance_id: str


__all__ = ["DeleteFileImportPermissionDenied"]
