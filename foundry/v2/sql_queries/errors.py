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

from foundry import _core as core
from foundry import _errors as errors
from foundry.v2.sql_queries import models as sql_queries_models


class CancelQueryPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not cancel the Query."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    queryId: sql_queries_models.QueryId
    """The id of a query."""


@dataclass
class CancelQueryPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["CancelQueryPermissionDenied"]
    parameters: CancelQueryPermissionDeniedParameters
    error_instance_id: str


class ExecuteQueryPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not execute the Query."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class ExecuteQueryPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["ExecuteQueryPermissionDenied"]
    parameters: ExecuteQueryPermissionDeniedParameters
    error_instance_id: str


class GetResultsPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not getResults the Query."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    queryId: sql_queries_models.QueryId
    """The id of a query."""


@dataclass
class GetResultsPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["GetResultsPermissionDenied"]
    parameters: GetResultsPermissionDeniedParameters
    error_instance_id: str


class GetStatusPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not getStatus the Query."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    queryId: sql_queries_models.QueryId
    """The id of a query."""


@dataclass
class GetStatusPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["GetStatusPermissionDenied"]
    parameters: GetStatusPermissionDeniedParameters
    error_instance_id: str


class QueryCanceledParameters(typing_extensions.TypedDict):
    """The query was canceled."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    queryId: sql_queries_models.QueryId


@dataclass
class QueryCanceled(errors.BadRequestError):
    name: typing.Literal["QueryCanceled"]
    parameters: QueryCanceledParameters
    error_instance_id: str


class QueryFailedParameters(typing_extensions.TypedDict):
    """The query failed."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    queryId: sql_queries_models.QueryId
    errorMessage: str


@dataclass
class QueryFailed(errors.InternalServerError):
    name: typing.Literal["QueryFailed"]
    parameters: QueryFailedParameters
    error_instance_id: str


class QueryParseErrorParameters(typing_extensions.TypedDict):
    """The query cannot be parsed."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    errorMessage: str


@dataclass
class QueryParseError(errors.BadRequestError):
    name: typing.Literal["QueryParseError"]
    parameters: QueryParseErrorParameters
    error_instance_id: str


class QueryPermissionDeniedParameters(typing_extensions.TypedDict):
    """The provided token does not have permission to access the given query."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    queryId: sql_queries_models.QueryId


@dataclass
class QueryPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["QueryPermissionDenied"]
    parameters: QueryPermissionDeniedParameters
    error_instance_id: str


class QueryRunningParameters(typing_extensions.TypedDict):
    """The query is running."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    queryId: sql_queries_models.QueryId


@dataclass
class QueryRunning(errors.BadRequestError):
    name: typing.Literal["QueryRunning"]
    parameters: QueryRunningParameters
    error_instance_id: str


class ReadQueryInputsPermissionDeniedParameters(typing_extensions.TypedDict):
    """The provided token does not have permission to access the inputs to the query."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    rids: typing.List[core.RID]
    """The RIDs of the inputs to the query that the user does not have permission to query."""


@dataclass
class ReadQueryInputsPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["ReadQueryInputsPermissionDenied"]
    parameters: ReadQueryInputsPermissionDeniedParameters
    error_instance_id: str


__all__ = [
    "CancelQueryPermissionDenied",
    "ExecuteQueryPermissionDenied",
    "GetResultsPermissionDenied",
    "GetStatusPermissionDenied",
    "QueryCanceled",
    "QueryFailed",
    "QueryParseError",
    "QueryPermissionDenied",
    "QueryRunning",
    "ReadQueryInputsPermissionDenied",
]
