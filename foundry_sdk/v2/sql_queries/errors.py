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


class CancelSqlQueryPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not cancel the SqlQuery."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class CancelSqlQueryPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["CancelSqlQueryPermissionDenied"]
    parameters: CancelSqlQueryPermissionDeniedParameters
    error_instance_id: str


class ColumnTypesNotSupportedParameters(typing_extensions.TypedDict):
    """The query result contains column types that are not supported by the requested serialization format."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class ColumnTypesNotSupported(errors.BadRequestError):
    name: typing.Literal["ColumnTypesNotSupported"]
    parameters: ColumnTypesNotSupportedParameters
    error_instance_id: str


class ExecuteOntologySqlQueryPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not executeOntology the SqlQuery."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class ExecuteOntologySqlQueryPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["ExecuteOntologySqlQueryPermissionDenied"]
    parameters: ExecuteOntologySqlQueryPermissionDeniedParameters
    error_instance_id: str


class ExecuteSqlQueryPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not execute the SqlQuery."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class ExecuteSqlQueryPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["ExecuteSqlQueryPermissionDenied"]
    parameters: ExecuteSqlQueryPermissionDeniedParameters
    error_instance_id: str


class GetResultsSqlQueryPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not getResults the SqlQuery."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class GetResultsSqlQueryPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["GetResultsSqlQueryPermissionDenied"]
    parameters: GetResultsSqlQueryPermissionDeniedParameters
    error_instance_id: str


class GetStatusSqlQueryPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not getStatus the SqlQuery."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class GetStatusSqlQueryPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["GetStatusSqlQueryPermissionDenied"]
    parameters: GetStatusSqlQueryPermissionDeniedParameters
    error_instance_id: str


class OntologyObjectTypeNotFoundParameters(typing_extensions.TypedDict):
    """
    The ontology query referenced an object type RID that does not exist or
    is not visible to the requesting user. Verify the RID (e.g. via
    list-object-types or get-object-type-details) and retry.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    objectTypeRid: core.RID


@dataclass
class OntologyObjectTypeNotFound(errors.NotFoundError):
    name: typing.Literal["OntologyObjectTypeNotFound"]
    parameters: OntologyObjectTypeNotFoundParameters
    error_instance_id: str


class OntologyQueryFailedParameters(typing_extensions.TypedDict):
    """The Ontology query failed."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    errorMessage: str


@dataclass
class OntologyQueryFailed(errors.InternalServerError):
    name: typing.Literal["OntologyQueryFailed"]
    parameters: OntologyQueryFailedParameters
    error_instance_id: str


class OntologyQueryInvalidObjectBackendParameters(typing_extensions.TypedDict):
    """
    The ontology query references object types or link types indexed in Object
    Storage V1, which is incompatible with Ontology SQL. Migrate the entities
    to Object Storage V2 or remove them from the query.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    objectTypeRids: typing.List[core.RID]
    linkTypeRids: typing.List[core.RID]


@dataclass
class OntologyQueryInvalidObjectBackend(errors.BadRequestError):
    name: typing.Literal["OntologyQueryInvalidObjectBackend"]
    parameters: OntologyQueryInvalidObjectBackendParameters
    error_instance_id: str


class OntologyQueryNestedObjectSetTooLargeParameters(typing_extensions.TypedDict):
    """
    The query references too many objects across joins, link lookups, or
    sub-queries. Narrow the scope (add filters, reduce joins, restrict
    object types) and retry. The actual and maximum object counts are
    returned as parameters.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    nestedObjectSetSize: core.Long
    maxAllowedNestedObjectSetSize: core.Long


@dataclass
class OntologyQueryNestedObjectSetTooLarge(errors.BadRequestError):
    name: typing.Literal["OntologyQueryNestedObjectSetTooLarge"]
    parameters: OntologyQueryNestedObjectSetTooLargeParameters
    error_instance_id: str


class OntologyQueryStringColumnTooLongParameters(typing_extensions.TypedDict):
    """
    A string column in the query result contains a value larger than
    the platform's per-cell size limit. Exclude or filter the column,
    or scope the query to skip the oversized rows.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    columnName: str


@dataclass
class OntologyQueryStringColumnTooLong(errors.BadRequestError):
    name: typing.Literal["OntologyQueryStringColumnTooLong"]
    parameters: OntologyQueryStringColumnTooLongParameters
    error_instance_id: str


class QueryCanceledParameters(typing_extensions.TypedDict):
    """The query was canceled."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class QueryCanceled(errors.BadRequestError):
    name: typing.Literal["QueryCanceled"]
    parameters: QueryCanceledParameters
    error_instance_id: str


class QueryFailedParameters(typing_extensions.TypedDict):
    """The query failed."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

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


@dataclass
class QueryPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["QueryPermissionDenied"]
    parameters: QueryPermissionDeniedParameters
    error_instance_id: str


class QueryRunningParameters(typing_extensions.TypedDict):
    """The query is running."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


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
    "CancelSqlQueryPermissionDenied",
    "ColumnTypesNotSupported",
    "ExecuteOntologySqlQueryPermissionDenied",
    "ExecuteSqlQueryPermissionDenied",
    "GetResultsSqlQueryPermissionDenied",
    "GetStatusSqlQueryPermissionDenied",
    "OntologyObjectTypeNotFound",
    "OntologyQueryFailed",
    "OntologyQueryInvalidObjectBackend",
    "OntologyQueryNestedObjectSetTooLarge",
    "OntologyQueryStringColumnTooLong",
    "QueryCanceled",
    "QueryFailed",
    "QueryParseError",
    "QueryPermissionDenied",
    "QueryRunning",
    "ReadQueryInputsPermissionDenied",
]
