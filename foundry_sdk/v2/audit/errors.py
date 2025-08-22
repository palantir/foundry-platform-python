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
from foundry_sdk.v2.audit import models as audit_models
from foundry_sdk.v2.core import models as core_models


class GetLogFileContentPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not content the LogFile."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    organizationRid: core_models.OrganizationRid
    logFileId: audit_models.FileId


@dataclass
class GetLogFileContentPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["GetLogFileContentPermissionDenied"]
    parameters: GetLogFileContentPermissionDeniedParameters
    error_instance_id: str


class ListLogFilesPermissionDeniedParameters(typing_extensions.TypedDict):
    """The provided token does not have permission to list audit log files."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class ListLogFilesPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["ListLogFilesPermissionDenied"]
    parameters: ListLogFilesPermissionDeniedParameters
    error_instance_id: str


__all__ = [
    "GetLogFileContentPermissionDenied",
    "ListLogFilesPermissionDenied",
]
