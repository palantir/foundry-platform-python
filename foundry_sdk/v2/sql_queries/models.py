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

import decimal
import typing
from datetime import date

import pydantic
import typing_extensions

from foundry_sdk import _core as core
from foundry_sdk.v2.core import models as core_models


class AnyColumnType(core.ModelBase):
    """AnyColumnType"""

    type: typing.Literal["any"] = "any"


class CanceledQueryStatus(core.ModelBase):
    """CanceledQueryStatus"""

    type: typing.Literal["canceled"] = "canceled"


ColumnType: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union[
        core_models.DateType,
        "StructColumnType",
        core_models.StringType,
        core_models.DoubleType,
        core_models.IntegerType,
        core_models.FloatType,
        "ListColumnType",
        "AnyColumnType",
        core_models.LongType,
        core_models.BooleanType,
        core_models.BinaryType,
        core_models.ShortType,
        "DecimalColumnType",
        "MapColumnType",
        core_models.TimestampType,
    ],
    pydantic.Field(discriminator="type"),
]
"""The type of a column in a SQL query result or parameter."""


class DecimalColumnType(core.ModelBase):
    """DecimalColumnType"""

    precision: int
    scale: int
    type: typing.Literal["decimal"] = "decimal"


class ExecuteOntologySqlQueryRequest(core.ModelBase):
    """ExecuteOntologySqlQueryRequest"""

    query: str
    """The SQL query to execute."""

    parameters: typing.Optional[Parameters] = None
    """
    Parameters for the SQL query. Can be either unnamed positional parameters
    or a named parameter mapping.
    """

    row_limit: typing.Optional[int] = pydantic.Field(alias=str("rowLimit"), default=None)  # type: ignore[literal-required]
    """Maximum number of rows to return."""

    dry_run: typing.Optional[bool] = pydantic.Field(alias=str("dryRun"), default=None)  # type: ignore[literal-required]
    """If true, parse and validate the query without executing it. Defaults to false."""


class ExecuteSqlQueryRequest(core.ModelBase):
    """ExecuteSqlQueryRequest"""

    query: str
    """
    The SQL query to execute. Queries should conform to the
    [Spark SQL dialect](https://spark.apache.org/docs/latest/sql-ref.html). This supports SELECT
    queries only. Datasets can be referenced in SQL queries by path or by RID. See the 
    [documentation](https://www.palantir.com/docs/foundry/analytics-connectivity/odbc-jdbc-drivers/#use-sql-to-query-foundry-datasets)
    for more details.
    """

    fallback_branch_ids: typing.Optional[typing.List[core_models.BranchName]] = pydantic.Field(alias=str("fallbackBranchIds"), default=None)  # type: ignore[literal-required]
    """
    The list of branch ids to use as fallbacks if the query fails to execute on the primary branch. If a
    is not explicitly provided in the SQL query, the resource will be queried on the first fallback branch
    provided that exists. If no fallback branches are provided the default branch is used. This is
    `master` for most enrollments.
    """

    serialization_format: typing.Optional[SerializationFormat] = pydantic.Field(alias=str("serializationFormat"), default=None)  # type: ignore[literal-required]
    """The format used to serialize query results. If not specified, defaults to `ARROW`."""


class FailedQueryStatus(core.ModelBase):
    """FailedQueryStatus"""

    error_message: str = pydantic.Field(alias=str("errorMessage"))  # type: ignore[literal-required]
    """An error message describing why the query failed."""

    type: typing.Literal["failed"] = "failed"


class ListColumnType(core.ModelBase):
    """ListColumnType"""

    element_type: ColumnType = pydantic.Field(alias=str("elementType"))  # type: ignore[literal-required]
    type: typing.Literal["list"] = "list"


class MapColumnType(core.ModelBase):
    """MapColumnType"""

    key_type: ColumnType = pydantic.Field(alias=str("keyType"))  # type: ignore[literal-required]
    value_type: ColumnType = pydantic.Field(alias=str("valueType"))  # type: ignore[literal-required]
    type: typing.Literal["map"] = "map"


MapParameterKey: typing_extensions.TypeAlias = str
"""A key for a map parameter value."""


class NamedParameterMapping(core.ModelBase):
    """A named mapping of parameter names to values."""

    mapping: ParameterMapping
    type: typing.Literal["namedParameterMapping"] = "namedParameterMapping"


class ParameterAnyValue(core.ModelBase):
    """An untyped parameter value."""

    value: typing.Any
    type: typing.Literal["any"] = "any"


class ParameterBooleanValue(core.ModelBase):
    """A boolean parameter value."""

    value: bool
    type: typing.Literal["boolean"] = "boolean"


class ParameterDateValue(core.ModelBase):
    """A date parameter value."""

    value: date
    type: typing.Literal["date"] = "date"


class ParameterDecimalValue(core.ModelBase):
    """A decimal parameter value."""

    value: decimal.Decimal
    type: typing.Literal["decimal"] = "decimal"


class ParameterDoubleValue(core.ModelBase):
    """A double parameter value."""

    value: float
    type: typing.Literal["double"] = "double"


class ParameterFloatValue(core.ModelBase):
    """A float parameter value."""

    value: float
    type: typing.Literal["float"] = "float"


class ParameterIntegerValue(core.ModelBase):
    """An integer parameter value."""

    value: int
    type: typing.Literal["integer"] = "integer"


class ParameterListValue(core.ModelBase):
    """A parameter value that is a list of other parameter values. All values in the list must be of the same type."""

    values: typing.List[ParameterValue]
    element_type: ColumnType = pydantic.Field(alias=str("elementType"))  # type: ignore[literal-required]
    type: typing.Literal["list"] = "list"


class ParameterLongValue(core.ModelBase):
    """A long integer parameter value."""

    value: core.Long
    type: typing.Literal["long"] = "long"


class ParameterMapValue(core.ModelBase):
    """A map parameter value."""

    values: typing.Dict[MapParameterKey, ParameterValue]
    type: typing.Literal["map"] = "map"


ParameterMapping: typing_extensions.TypeAlias = typing.Dict["ParameterName", "ParameterValue"]
"""A mapping of named parameters to their values."""


ParameterName: typing_extensions.TypeAlias = str
"""The name of a SQL query parameter."""


class ParameterNullValue(core.ModelBase):
    """A null parameter value."""

    type: typing.Literal["null"] = "null"


class ParameterShortValue(core.ModelBase):
    """A short integer parameter value."""

    value: int
    type: typing.Literal["short"] = "short"


class ParameterStringValue(core.ModelBase):
    """A string parameter value."""

    value: str
    type: typing.Literal["string"] = "string"


class ParameterStructValue(core.ModelBase):
    """A struct composed of ordered elements, each with a name and value."""

    struct_elements: typing.List[StructElement] = pydantic.Field(alias=str("structElements"))  # type: ignore[literal-required]
    type: typing.Literal["struct"] = "struct"


class ParameterTimestampValue(core.ModelBase):
    """A timestamp parameter value."""

    value: core.AwareDatetime
    type: typing.Literal["timestamp"] = "timestamp"


ParameterValue: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union[
        "ParameterDateValue",
        "ParameterStructValue",
        "ParameterStringValue",
        "ParameterDoubleValue",
        "ParameterIntegerValue",
        "ParameterFloatValue",
        "ParameterListValue",
        "ParameterAnyValue",
        "ParameterLongValue",
        "ParameterBooleanValue",
        "ParameterNullValue",
        "ParameterShortValue",
        "ParameterDecimalValue",
        "ParameterMapValue",
        "ParameterTimestampValue",
    ],
    pydantic.Field(discriminator="type"),
]
"""A typed parameter value for SQL query execution."""


Parameters: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union["UnnamedParameterValues", "NamedParameterMapping"],
    pydantic.Field(discriminator="type"),
]
"""
Parameters for SQL query execution. Can be either unnamed positional parameters
or named parameter mappings.
"""


QueryStatus: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union[
        "RunningQueryStatus", "CanceledQueryStatus", "FailedQueryStatus", "SucceededQueryStatus"
    ],
    pydantic.Field(discriminator="type"),
]
"""QueryStatus"""


class RunningQueryStatus(core.ModelBase):
    """RunningQueryStatus"""

    query_id: SqlQueryId = pydantic.Field(alias=str("queryId"))  # type: ignore[literal-required]
    type: typing.Literal["running"] = "running"


SerializationFormat: typing_extensions.TypeAlias = typing.Literal["ARROW", "CSV"]
"""Format for SQL query result serialization."""


SqlQueryId: typing_extensions.TypeAlias = str
"""The identifier of a SQL Query."""


class StructColumnFieldType(core.ModelBase):
    """StructColumnFieldType"""

    name: str
    type: ColumnType


class StructColumnType(core.ModelBase):
    """StructColumnType"""

    fields: typing.List[StructColumnFieldType]
    type: typing.Literal["struct"] = "struct"


class StructElement(core.ModelBase):
    """Represents an entry in a struct."""

    struct_element_name: StructElementName = pydantic.Field(alias=str("structElementName"))  # type: ignore[literal-required]
    struct_element_value: ParameterValue = pydantic.Field(alias=str("structElementValue"))  # type: ignore[literal-required]


StructElementName: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union["StructFieldRid", "StructFieldKeyValue"], pydantic.Field(discriminator="type")
]
"""The name of a struct element."""


class StructFieldKeyValue(core.ModelBase):
    """A string key for a struct field."""

    value: str
    type: typing.Literal["structFieldKey"] = "structFieldKey"


class StructFieldRid(core.ModelBase):
    """A unique identifier for a field of a struct property type."""

    value: core.RID
    type: typing.Literal["structFieldRid"] = "structFieldRid"


class SucceededQueryStatus(core.ModelBase):
    """SucceededQueryStatus"""

    query_id: SqlQueryId = pydantic.Field(alias=str("queryId"))  # type: ignore[literal-required]
    type: typing.Literal["succeeded"] = "succeeded"


class UnnamedParameterValues(core.ModelBase):
    """An ordered list of unnamed positional parameter values."""

    values: typing.List[ParameterValue]
    type: typing.Literal["unnamedParameterValues"] = "unnamedParameterValues"


core.resolve_forward_references_in_module(__name__)

__all__ = [
    "AnyColumnType",
    "CanceledQueryStatus",
    "ColumnType",
    "DecimalColumnType",
    "ExecuteOntologySqlQueryRequest",
    "ExecuteSqlQueryRequest",
    "FailedQueryStatus",
    "ListColumnType",
    "MapColumnType",
    "MapParameterKey",
    "NamedParameterMapping",
    "ParameterAnyValue",
    "ParameterBooleanValue",
    "ParameterDateValue",
    "ParameterDecimalValue",
    "ParameterDoubleValue",
    "ParameterFloatValue",
    "ParameterIntegerValue",
    "ParameterListValue",
    "ParameterLongValue",
    "ParameterMapValue",
    "ParameterMapping",
    "ParameterName",
    "ParameterNullValue",
    "ParameterShortValue",
    "ParameterStringValue",
    "ParameterStructValue",
    "ParameterTimestampValue",
    "ParameterValue",
    "Parameters",
    "QueryStatus",
    "RunningQueryStatus",
    "SerializationFormat",
    "SqlQueryId",
    "StructColumnFieldType",
    "StructColumnType",
    "StructElement",
    "StructElementName",
    "StructFieldKeyValue",
    "StructFieldRid",
    "SucceededQueryStatus",
    "UnnamedParameterValues",
]
