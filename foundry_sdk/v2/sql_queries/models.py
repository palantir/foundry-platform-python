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


class CanceledQueryStatus(pydantic.BaseModel):
    """CanceledQueryStatus"""

    type: typing.Literal["canceled"] = "canceled"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class FailedQueryStatus(pydantic.BaseModel):
    """FailedQueryStatus"""

    error_message: str = pydantic.Field(alias=str("errorMessage"))  # type: ignore[literal-required]
    """An error message describing why the query failed."""

    type: typing.Literal["failed"] = "failed"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


QueryStatus = typing_extensions.Annotated[
    typing.Union[
        "RunningQueryStatus", CanceledQueryStatus, FailedQueryStatus, "SucceededQueryStatus"
    ],
    pydantic.Field(discriminator="type"),
]
"""QueryStatus"""


class RunningQueryStatus(pydantic.BaseModel):
    """RunningQueryStatus"""

    query_id: SqlQueryId = pydantic.Field(alias=str("queryId"))  # type: ignore[literal-required]
    type: typing.Literal["running"] = "running"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


SqlQueryId = str
"""The identifier of a SQL Query."""


class SucceededQueryStatus(pydantic.BaseModel):
    """SucceededQueryStatus"""

    query_id: SqlQueryId = pydantic.Field(alias=str("queryId"))  # type: ignore[literal-required]
    type: typing.Literal["succeeded"] = "succeeded"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


core.resolve_forward_references(QueryStatus, globalns=globals(), localns=locals())

__all__ = [
    "CanceledQueryStatus",
    "FailedQueryStatus",
    "QueryStatus",
    "RunningQueryStatus",
    "SqlQueryId",
    "SucceededQueryStatus",
]
