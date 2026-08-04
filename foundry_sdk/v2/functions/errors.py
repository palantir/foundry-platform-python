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


class AsyncConsistentSnapshotErrorParameters(typing_extensions.TypedDict):
    """
    The async query failed because the Ontology snapshot used for consistent reads became stale. Retrying the
    request typically resolves this.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    functionRid: typing_extensions.NotRequired[functions_models.FunctionRid]
    functionVersion: typing_extensions.NotRequired[functions_models.FunctionVersion]


@dataclass
class AsyncConsistentSnapshotError(errors.ConflictError):
    name: typing.Literal["AsyncConsistentSnapshotError"]
    parameters: AsyncConsistentSnapshotErrorParameters
    error_instance_id: str


class AsyncFunctionNotSupportedWithTransactionParameters(typing_extensions.TypedDict):
    """The function runtime does not support async execution with a transaction."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    functionRid: typing_extensions.NotRequired[functions_models.FunctionRid]
    functionVersion: typing_extensions.NotRequired[functions_models.FunctionVersion]
    message: str


@dataclass
class AsyncFunctionNotSupportedWithTransaction(errors.BadRequestError):
    name: typing.Literal["AsyncFunctionNotSupportedWithTransaction"]
    parameters: AsyncFunctionNotSupportedWithTransactionParameters
    error_instance_id: str


class AsyncInvalidQueryOutputValueParameters(typing_extensions.TypedDict):
    """
    The value of the async query's output is invalid. This may be because the return value did not match the
    specified output type or constraints.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    outputDataType: typing_extensions.NotRequired[functions_models.QueryDataType]
    outputValue: typing_extensions.NotRequired[functions_models.DataValue]
    functionRid: typing_extensions.NotRequired[functions_models.FunctionRid]
    functionVersion: typing_extensions.NotRequired[functions_models.FunctionVersion]


@dataclass
class AsyncInvalidQueryOutputValue(errors.BadRequestError):
    name: typing.Literal["AsyncInvalidQueryOutputValue"]
    parameters: AsyncInvalidQueryOutputValueParameters
    error_instance_id: str


class AsyncQueryEncounteredUserFacingErrorParameters(typing_extensions.TypedDict):
    """
    The authored `Query` failed during async execution because of a user induced error. The message argument
    is meant to be displayed to the user.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    functionRid: typing_extensions.NotRequired[functions_models.FunctionRid]
    functionVersion: typing_extensions.NotRequired[functions_models.FunctionVersion]
    message: str


@dataclass
class AsyncQueryEncounteredUserFacingError(errors.ConflictError):
    name: typing.Literal["AsyncQueryEncounteredUserFacingError"]
    parameters: AsyncQueryEncounteredUserFacingErrorParameters
    error_instance_id: str


class AsyncQueryMemoryExceededLimitParameters(typing_extensions.TypedDict):
    """Memory limits were exceeded during async `Query` execution."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    functionRid: typing_extensions.NotRequired[functions_models.FunctionRid]
    functionVersion: typing_extensions.NotRequired[functions_models.FunctionVersion]


@dataclass
class AsyncQueryMemoryExceededLimit(errors.InternalServerError):
    name: typing.Literal["AsyncQueryMemoryExceededLimit"]
    parameters: AsyncQueryMemoryExceededLimitParameters
    error_instance_id: str


class AsyncQueryRuntimeErrorParameters(typing_extensions.TypedDict):
    """The authored `Query` failed to execute because of a runtime error during async execution."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    functionRid: typing_extensions.NotRequired[functions_models.FunctionRid]
    functionVersion: typing_extensions.NotRequired[functions_models.FunctionVersion]
    message: typing_extensions.NotRequired[str]
    stacktrace: typing_extensions.NotRequired[str]
    parameters: typing.Dict[functions_models.QueryRuntimeErrorParameter, str]


@dataclass
class AsyncQueryRuntimeError(errors.BadRequestError):
    name: typing.Literal["AsyncQueryRuntimeError"]
    parameters: AsyncQueryRuntimeErrorParameters
    error_instance_id: str


class AsyncQueryTimeExceededLimitParameters(typing_extensions.TypedDict):
    """Time limits were exceeded during async `Query` execution."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    functionRid: typing_extensions.NotRequired[functions_models.FunctionRid]
    functionVersion: typing_extensions.NotRequired[functions_models.FunctionVersion]


@dataclass
class AsyncQueryTimeExceededLimit(errors.BadRequestError):
    name: typing.Literal["AsyncQueryTimeExceededLimit"]
    parameters: AsyncQueryTimeExceededLimitParameters
    error_instance_id: str


class CancelExecutionNotSupportedParameters(typing_extensions.TypedDict):
    """The function runtime does not support cancelling executions."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    functionRid: typing_extensions.NotRequired[functions_models.FunctionRid]
    functionVersion: typing_extensions.NotRequired[functions_models.FunctionVersion]


@dataclass
class CancelExecutionNotSupported(errors.InternalServerError):
    name: typing.Literal["CancelExecutionNotSupported"]
    parameters: CancelExecutionNotSupportedParameters
    error_instance_id: str


class CancelExecutionPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not cancel the Execution."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    executionId: functions_models.ExecutionId


@dataclass
class CancelExecutionPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["CancelExecutionPermissionDenied"]
    parameters: CancelExecutionPermissionDeniedParameters
    error_instance_id: str


class ConsistentSnapshotErrorParameters(typing_extensions.TypedDict):
    """
    The query failed because the Ontology snapshot used for consistent reads became stale. Retrying the request
    typically resolves this.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    functionRid: functions_models.FunctionRid
    functionVersion: functions_models.FunctionVersion


@dataclass
class ConsistentSnapshotError(errors.ConflictError):
    name: typing.Literal["ConsistentSnapshotError"]
    parameters: ConsistentSnapshotErrorParameters
    error_instance_id: str


class ExecuteAsyncQueryPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not executeAsync the Query."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    queryApiName: functions_models.QueryApiName


@dataclass
class ExecuteAsyncQueryPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["ExecuteAsyncQueryPermissionDenied"]
    parameters: ExecuteAsyncQueryPermissionDeniedParameters
    error_instance_id: str


class ExecuteQueryPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not execute the Query."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    queryApiName: functions_models.QueryApiName


@dataclass
class ExecuteQueryPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["ExecuteQueryPermissionDenied"]
    parameters: ExecuteQueryPermissionDeniedParameters
    error_instance_id: str


class ExecutionNotFoundParameters(typing_extensions.TypedDict):
    """No async query execution found with the given ID."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    executionId: functions_models.ExecutionId


@dataclass
class ExecutionNotFound(errors.NotFoundError):
    name: typing.Literal["ExecutionNotFound"]
    parameters: ExecutionNotFoundParameters
    error_instance_id: str


class FunctionHasNoPublishedVersionParameters(typing_extensions.TypedDict):
    """The query function has no published versions."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    functionRid: functions_models.FunctionRid


@dataclass
class FunctionHasNoPublishedVersion(errors.NotFoundError):
    name: typing.Literal["FunctionHasNoPublishedVersion"]
    parameters: FunctionHasNoPublishedVersionParameters
    error_instance_id: str


class FunctionNotFoundParameters(typing_extensions.TypedDict):
    """The query function could not be found."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    functionRid: functions_models.FunctionRid


@dataclass
class FunctionNotFound(errors.NotFoundError):
    name: typing.Literal["FunctionNotFound"]
    parameters: FunctionNotFoundParameters
    error_instance_id: str


class FunctionNotSupportedWithTransactionParameters(typing_extensions.TypedDict):
    """The function runtime does not support execution with a transaction."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    functionRid: functions_models.FunctionRid
    functionVersion: functions_models.FunctionVersion
    message: str


@dataclass
class FunctionNotSupportedWithTransaction(errors.BadRequestError):
    name: typing.Literal["FunctionNotSupportedWithTransaction"]
    parameters: FunctionNotSupportedWithTransactionParameters
    error_instance_id: str


class GetByRidPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not getByRid the Query."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class GetByRidPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["GetByRidPermissionDenied"]
    parameters: GetByRidPermissionDeniedParameters
    error_instance_id: str


class GetResultExecutionPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not getResult the Execution."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    executionId: functions_models.ExecutionId


@dataclass
class GetResultExecutionPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["GetResultExecutionPermissionDenied"]
    parameters: GetResultExecutionPermissionDeniedParameters
    error_instance_id: str


class InvalidQueryOutputValueParameters(typing_extensions.TypedDict):
    """
    The value of the query's output is invalid. This may be because the return value did not match the specified
    output type or constraints.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    outputDataType: functions_models.QueryDataType
    outputValue: typing_extensions.NotRequired[functions_models.DataValue]
    functionRid: functions_models.FunctionRid
    functionVersion: functions_models.FunctionVersion


@dataclass
class InvalidQueryOutputValue(errors.BadRequestError):
    name: typing.Literal["InvalidQueryOutputValue"]
    parameters: InvalidQueryOutputValueParameters
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


class InvalidVersionResolutionParametersParameters(typing_extensions.TypedDict):
    """
    The combination of `version`, `latestVersionResolution`, and `includePrerelease` provided is not
    supported.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    message: str


@dataclass
class InvalidVersionResolutionParameters(errors.BadRequestError):
    name: typing.Literal["InvalidVersionResolutionParameters"]
    parameters: InvalidVersionResolutionParametersParameters
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
class QueryTimeExceededLimit(errors.BadRequestError):
    name: typing.Literal["QueryTimeExceededLimit"]
    parameters: QueryTimeExceededLimitParameters
    error_instance_id: str


class QueryVersionNotFoundParameters(typing_extensions.TypedDict):
    """The query could not be found at the provided version."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    apiName: functions_models.QueryApiName
    version: functions_models.FunctionVersion


@dataclass
class QueryVersionNotFound(errors.NotFoundError):
    name: typing.Literal["QueryVersionNotFound"]
    parameters: QueryVersionNotFoundParameters
    error_instance_id: str


class StreamingExecuteEventsQueryPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not streamingExecuteEvents the Query."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    queryApiName: functions_models.QueryApiName


@dataclass
class StreamingExecuteEventsQueryPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["StreamingExecuteEventsQueryPermissionDenied"]
    parameters: StreamingExecuteEventsQueryPermissionDeniedParameters
    error_instance_id: str


class StreamingExecuteQueryPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not streamingExecute the Query."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    queryApiName: functions_models.QueryApiName


@dataclass
class StreamingExecuteQueryPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["StreamingExecuteQueryPermissionDenied"]
    parameters: StreamingExecuteQueryPermissionDeniedParameters
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
    "AsyncConsistentSnapshotError",
    "AsyncFunctionNotSupportedWithTransaction",
    "AsyncInvalidQueryOutputValue",
    "AsyncQueryEncounteredUserFacingError",
    "AsyncQueryMemoryExceededLimit",
    "AsyncQueryRuntimeError",
    "AsyncQueryTimeExceededLimit",
    "CancelExecutionNotSupported",
    "CancelExecutionPermissionDenied",
    "ConsistentSnapshotError",
    "ExecuteAsyncQueryPermissionDenied",
    "ExecuteQueryPermissionDenied",
    "ExecutionNotFound",
    "FunctionHasNoPublishedVersion",
    "FunctionNotFound",
    "FunctionNotSupportedWithTransaction",
    "GetByRidPermissionDenied",
    "GetResultExecutionPermissionDenied",
    "InvalidQueryOutputValue",
    "InvalidQueryParameterValue",
    "InvalidVersionResolutionParameters",
    "MissingParameter",
    "QueryEncounteredUserFacingError",
    "QueryMemoryExceededLimit",
    "QueryNotFound",
    "QueryRuntimeError",
    "QueryTimeExceededLimit",
    "QueryVersionNotFound",
    "StreamingExecuteEventsQueryPermissionDenied",
    "StreamingExecuteQueryPermissionDenied",
    "UnknownParameter",
    "ValueTypeNotFound",
    "VersionIdNotFound",
]
