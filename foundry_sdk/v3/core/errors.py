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
from foundry_sdk.v3.core import models as core_models


class BatchRequestSizeExceededLimitParameters(typing_extensions.TypedDict):
    """Thrown when a batch request exceeds the endpoint's maximum batch size."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    maximumBatchSize: int
    """The maximum size of batch requests that can be sent to this endpoint."""

    providedBatchSize: int
    """The size of the batch request that was sent to this endpoint."""


@dataclass
class BatchRequestSizeExceededLimit(errors.BadRequestError):
    name: typing.Literal["BatchRequestSizeExceededLimit"]
    parameters: BatchRequestSizeExceededLimitParameters
    error_instance_id: str


class InvalidPageSizeParameters(typing_extensions.TypedDict):
    """The provided page size was negative. Page sizes must be greater than or equal to zero."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    pageSize: core_models.PageSize


@dataclass
class InvalidPageSize(errors.BadRequestError):
    name: typing.Literal["InvalidPageSize"]
    parameters: InvalidPageSizeParameters
    error_instance_id: str


class MissingBatchRequestParameters(typing_extensions.TypedDict):
    """Thrown when a batch request contains no elements."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class MissingBatchRequest(errors.BadRequestError):
    name: typing.Literal["MissingBatchRequest"]
    parameters: MissingBatchRequestParameters
    error_instance_id: str


__all__ = [
    "BatchRequestSizeExceededLimit",
    "InvalidPageSize",
    "MissingBatchRequest",
]
