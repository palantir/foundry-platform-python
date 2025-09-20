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
from foundry_sdk.v2.datasets import models as datasets_models


class CanceledQueryStatus(core.ModelBase):
    """CanceledQueryStatus"""

    type: typing.Literal["canceled"] = "canceled"


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

    fallback_branch_ids: typing.Optional[typing.List[datasets_models.BranchName]] = pydantic.Field(alias=str("fallbackBranchIds"), default=None)  # type: ignore[literal-required]
    """
    The list of branch ids to use as fallbacks if the query fails to execute on the primary branch. If a
    is not explicitly provided in the SQL query, the resource will be queried on the first fallback branch
    provided that exists. If no fallback branches are provided the default branch is used. This is
    `master` for most enrollments.
    """


class FailedQueryStatus(core.ModelBase):
    """FailedQueryStatus"""

    error_message: str = pydantic.Field(alias=str("errorMessage"))  # type: ignore[literal-required]
    """An error message describing why the query failed."""

    type: typing.Literal["failed"] = "failed"


QueryStatus = typing_extensions.Annotated[
    typing.Union[
        "RunningQueryStatus", CanceledQueryStatus, FailedQueryStatus, "SucceededQueryStatus"
    ],
    pydantic.Field(discriminator="type"),
]
"""QueryStatus"""


class RunningQueryStatus(core.ModelBase):
    """RunningQueryStatus"""

    query_id: SqlQueryId = pydantic.Field(alias=str("queryId"))  # type: ignore[literal-required]
    type: typing.Literal["running"] = "running"


SqlQueryId = str
"""The identifier of a SQL Query."""


class SucceededQueryStatus(core.ModelBase):
    """SucceededQueryStatus"""

    query_id: SqlQueryId = pydantic.Field(alias=str("queryId"))  # type: ignore[literal-required]
    type: typing.Literal["succeeded"] = "succeeded"


core.resolve_forward_references(QueryStatus, globalns=globals(), localns=locals())

__all__ = [
    "CanceledQueryStatus",
    "ExecuteSqlQueryRequest",
    "FailedQueryStatus",
    "QueryStatus",
    "RunningQueryStatus",
    "SqlQueryId",
    "SucceededQueryStatus",
]
