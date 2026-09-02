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
from foundry_sdk.v3.orchestrator import models as orchestrator_models


class CompleteProcessExecutionSignalPermissionDeniedParameters(typing_extensions.TypedDict):
    """
    The token does not have permission to complete this signal. Signals can only be completed by the token
    that originally invoked the process execution.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    processExecutionId: orchestrator_models.ProcessExecutionId
    signalId: orchestrator_models.SignalId


@dataclass
class CompleteProcessExecutionSignalPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["CompleteProcessExecutionSignalPermissionDenied"]
    parameters: CompleteProcessExecutionSignalPermissionDeniedParameters
    error_instance_id: str


class ProcessExecutionExpiredParameters(typing_extensions.TypedDict):
    """
    The process execution can no longer accept signal completions because its data is outside the retention
    window.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    processExecutionId: orchestrator_models.ProcessExecutionId
    expiredTime: core.AwareDatetime
    """The time at which the process execution's data expired."""


@dataclass
class ProcessExecutionExpired(errors.BadRequestError):
    name: typing.Literal["ProcessExecutionExpired"]
    parameters: ProcessExecutionExpiredParameters
    error_instance_id: str


class ProcessExecutionNotFoundParameters(typing_extensions.TypedDict):

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    processExecutionId: orchestrator_models.ProcessExecutionId


@dataclass
class ProcessExecutionNotFound(errors.NotFoundError):
    name: typing.Literal["ProcessExecutionNotFound"]
    parameters: ProcessExecutionNotFoundParameters
    error_instance_id: str


class ProcessExecutionSignalNotFoundParameters(typing_extensions.TypedDict):

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    signalId: orchestrator_models.SignalId
    processExecutionId: orchestrator_models.ProcessExecutionId


@dataclass
class ProcessExecutionSignalNotFound(errors.NotFoundError):
    name: typing.Literal["ProcessExecutionSignalNotFound"]
    parameters: ProcessExecutionSignalNotFoundParameters
    error_instance_id: str


__all__ = [
    "CompleteProcessExecutionSignalPermissionDenied",
    "ProcessExecutionExpired",
    "ProcessExecutionNotFound",
    "ProcessExecutionSignalNotFound",
]
