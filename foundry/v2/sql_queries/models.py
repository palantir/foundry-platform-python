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


class CanceledQueryStatus(pydantic.BaseModel):
    """CanceledQueryStatus"""

    type: typing.Literal["canceled"] = "canceled"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "CanceledQueryStatusDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            CanceledQueryStatusDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class CanceledQueryStatusDict(typing_extensions.TypedDict):
    """CanceledQueryStatus"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    type: typing.Literal["canceled"]


class FailedQueryStatus(pydantic.BaseModel):
    """FailedQueryStatus"""

    error_message: str = pydantic.Field(alias=str("errorMessage"))  # type: ignore[literal-required]
    """An error message describing why the query failed."""

    type: typing.Literal["failed"] = "failed"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "FailedQueryStatusDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(FailedQueryStatusDict, self.model_dump(by_alias=True, exclude_none=True))


class FailedQueryStatusDict(typing_extensions.TypedDict):
    """FailedQueryStatus"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    errorMessage: str
    """An error message describing why the query failed."""

    type: typing.Literal["failed"]


QueryId = str
"""The identifier of a Query."""


QueryStatus = typing_extensions.Annotated[
    typing.Union[
        "RunningQueryStatus", "CanceledQueryStatus", "FailedQueryStatus", "SucceededQueryStatus"
    ],
    pydantic.Field(discriminator="type"),
]
"""QueryStatus"""


QueryStatusDict = typing_extensions.Annotated[
    typing.Union[
        "RunningQueryStatusDict",
        "CanceledQueryStatusDict",
        "FailedQueryStatusDict",
        "SucceededQueryStatusDict",
    ],
    pydantic.Field(discriminator="type"),
]
"""QueryStatus"""


class RunningQueryStatus(pydantic.BaseModel):
    """RunningQueryStatus"""

    query_id: QueryId = pydantic.Field(alias=str("queryId"))  # type: ignore[literal-required]
    type: typing.Literal["running"] = "running"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "RunningQueryStatusDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            RunningQueryStatusDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class RunningQueryStatusDict(typing_extensions.TypedDict):
    """RunningQueryStatus"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    queryId: QueryId
    type: typing.Literal["running"]


class SucceededQueryStatus(pydantic.BaseModel):
    """SucceededQueryStatus"""

    query_id: QueryId = pydantic.Field(alias=str("queryId"))  # type: ignore[literal-required]
    type: typing.Literal["succeeded"] = "succeeded"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "SucceededQueryStatusDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            SucceededQueryStatusDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class SucceededQueryStatusDict(typing_extensions.TypedDict):
    """SucceededQueryStatus"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    queryId: QueryId
    type: typing.Literal["succeeded"]


__all__ = [
    "CanceledQueryStatus",
    "CanceledQueryStatusDict",
    "FailedQueryStatus",
    "FailedQueryStatusDict",
    "QueryId",
    "QueryStatus",
    "QueryStatusDict",
    "RunningQueryStatus",
    "RunningQueryStatusDict",
    "SucceededQueryStatus",
    "SucceededQueryStatusDict",
]
