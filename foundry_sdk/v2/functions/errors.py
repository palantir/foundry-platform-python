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
from foundry_sdk.v2.functions import models as functions_models


class ExecuteQueryPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not execute the Query."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    queryApiName: functions_models.QueryApiName


@dataclass
class ExecuteQueryPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["ExecuteQueryPermissionDenied"]
    parameters: ExecuteQueryPermissionDeniedParameters
    error_instance_id: str


class GetByRidQueriesPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not getByRid the Query."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class GetByRidQueriesPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["GetByRidQueriesPermissionDenied"]
    parameters: GetByRidQueriesPermissionDeniedParameters
    error_instance_id: str


class InvalidQueryParameterValueParameters(typing_extensions.TypedDict):
    """
    The value of the given parameter is invalid. See the documentation of `DataValue` for details on
    how parameters are represented.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    parameterDataType: functions_models.QueryDataType
    parameterId: functions_models.ParameterId
    parameterValue: typing_extensions.NotRequired[functions_models.DataValue]


@dataclass
class InvalidQueryParameterValue(errors.BadRequestError):
    name: typing.Literal["InvalidQueryParameterValue"]
    parameters: InvalidQueryParameterValueParameters
    error_instance_id: str


class MissingParameterParameters(typing_extensions.TypedDict):
    """
    Required parameters are missing. Please look at the `parameters` field to see which required parameters are
    missing from the request.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    parameters: typing.List[functions_models.ParameterId]


@dataclass
class MissingParameter(errors.BadRequestError):
    name: typing.Literal["MissingParameter"]
    parameters: MissingParameterParameters
    error_instance_id: str


class QueryEncounteredUserFacingErrorParameters(typing_extensions.TypedDict):
    """
    The authored `Query` failed to execute because of a user induced error. The message argument
    is meant to be displayed to the user.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    functionRid: functions_models.FunctionRid
    functionVersion: functions_models.FunctionVersion
    message: str


@dataclass
class QueryEncounteredUserFacingError(errors.ConflictError):
    name: typing.Literal["QueryEncounteredUserFacingError"]
    parameters: QueryEncounteredUserFacingErrorParameters
    error_instance_id: str


class QueryMemoryExceededLimitParameters(typing_extensions.TypedDict):
    """Memory limits were exceeded for the `Query` execution."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    functionRid: functions_models.FunctionRid
    functionVersion: functions_models.FunctionVersion


@dataclass
class QueryMemoryExceededLimit(errors.InternalServerError):
    name: typing.Literal["QueryMemoryExceededLimit"]
    parameters: QueryMemoryExceededLimitParameters
    error_instance_id: str


class QueryNotFoundParameters(typing_extensions.TypedDict):
    """The given Query could not be found."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    queryApiName: functions_models.QueryApiName


@dataclass
class QueryNotFound(errors.NotFoundError):
    name: typing.Literal["QueryNotFound"]
    parameters: QueryNotFoundParameters
    error_instance_id: str


class QueryRuntimeErrorParameters(typing_extensions.TypedDict):
    """The authored `Query` failed to execute because of a runtime error."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    functionRid: functions_models.FunctionRid
    functionVersion: functions_models.FunctionVersion
    message: typing_extensions.NotRequired[str]
    stacktrace: typing_extensions.NotRequired[str]
    parameters: typing.Dict[functions_models.QueryRuntimeErrorParameter, str]


@dataclass
class QueryRuntimeError(errors.BadRequestError):
    name: typing.Literal["QueryRuntimeError"]
    parameters: QueryRuntimeErrorParameters
    error_instance_id: str


class QueryTimeExceededLimitParameters(typing_extensions.TypedDict):
    """Time limits were exceeded for the `Query` execution."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    functionRid: functions_models.FunctionRid
    functionVersion: functions_models.FunctionVersion


@dataclass
class QueryTimeExceededLimit(errors.InternalServerError):
    name: typing.Literal["QueryTimeExceededLimit"]
    parameters: QueryTimeExceededLimitParameters
    error_instance_id: str


class UnknownParameterParameters(typing_extensions.TypedDict):
    """
    The provided parameters were not found. Please look at the `knownParameters` field
    to see which ones are available.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    unknownParameters: typing.List[functions_models.ParameterId]
    expectedParameters: typing.List[functions_models.ParameterId]


@dataclass
class UnknownParameter(errors.BadRequestError):
    name: typing.Literal["UnknownParameter"]
    parameters: UnknownParameterParameters
    error_instance_id: str


class ValueTypeNotFoundParameters(typing_extensions.TypedDict):
    """The given ValueType could not be found."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    valueTypeRid: functions_models.ValueTypeRid


@dataclass
class ValueTypeNotFound(errors.NotFoundError):
    name: typing.Literal["ValueTypeNotFound"]
    parameters: ValueTypeNotFoundParameters
    error_instance_id: str


class VersionIdNotFoundParameters(typing_extensions.TypedDict):
    """The given VersionId could not be found."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    valueTypeRid: functions_models.ValueTypeRid
    versionIdVersionId: functions_models.ValueTypeVersionId


@dataclass
class VersionIdNotFound(errors.NotFoundError):
    name: typing.Literal["VersionIdNotFound"]
    parameters: VersionIdNotFoundParameters
    error_instance_id: str


__all__ = [
    "ExecuteQueryPermissionDenied",
    "GetByRidQueriesPermissionDenied",
    "InvalidQueryParameterValue",
    "MissingParameter",
    "QueryEncounteredUserFacingError",
    "QueryMemoryExceededLimit",
    "QueryNotFound",
    "QueryRuntimeError",
    "QueryTimeExceededLimit",
    "UnknownParameter",
    "ValueTypeNotFound",
    "VersionIdNotFound",
]
