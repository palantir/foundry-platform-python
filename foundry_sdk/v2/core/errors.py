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
from foundry_sdk.v2.core import models as core_models


class ApiFeaturePreviewUsageOnlyParameters(typing_extensions.TypedDict):
    """
    This feature is only supported in preview mode. Please use `preview=true` in the query
    parameters to call this endpoint.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class ApiFeaturePreviewUsageOnly(errors.BadRequestError):
    name: typing.Literal["ApiFeaturePreviewUsageOnly"]
    parameters: ApiFeaturePreviewUsageOnlyParameters
    error_instance_id: str


class ApiUsageDeniedParameters(typing_extensions.TypedDict):
    """You are not allowed to use Palantir APIs."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    missingScope: typing_extensions.NotRequired[core_models.OperationScope]


@dataclass
class ApiUsageDenied(errors.PermissionDeniedError):
    name: typing.Literal["ApiUsageDenied"]
    parameters: ApiUsageDeniedParameters
    error_instance_id: str


class BatchRequestSizeExceededLimitParameters(typing_extensions.TypedDict):
    """The submitted batch request was too large."""

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


class FolderNotFoundParameters(typing_extensions.TypedDict):
    """The requested folder could not be found, or the client token does not have access to it."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    folderRid: core_models.FolderRid


@dataclass
class FolderNotFound(errors.NotFoundError):
    name: typing.Literal["FolderNotFound"]
    parameters: FolderNotFoundParameters
    error_instance_id: str


class FoundryBranchNotFoundParameters(typing_extensions.TypedDict):
    """The requested foundry branch could not be found, or the client token does not have access to it."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    branch: core_models.FoundryBranch


@dataclass
class FoundryBranchNotFound(errors.NotFoundError):
    name: typing.Literal["FoundryBranchNotFound"]
    parameters: FoundryBranchNotFoundParameters
    error_instance_id: str


class InvalidAndFilterParameters(typing_extensions.TypedDict):
    """The provided AND filter should have at least one sub-filter."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class InvalidAndFilter(errors.BadRequestError):
    name: typing.Literal["InvalidAndFilter"]
    parameters: InvalidAndFilterParameters
    error_instance_id: str


class InvalidChangeDataCaptureConfigurationParameters(typing_extensions.TypedDict):
    """The change data capture configuration is invalid."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class InvalidChangeDataCaptureConfiguration(errors.BadRequestError):
    name: typing.Literal["InvalidChangeDataCaptureConfiguration"]
    parameters: InvalidChangeDataCaptureConfigurationParameters
    error_instance_id: str


class InvalidFieldSchemaParameters(typing_extensions.TypedDict):
    """The field schema failed validations"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    fieldName: typing_extensions.NotRequired[core_models.FieldName]
    message: str


@dataclass
class InvalidFieldSchema(errors.BadRequestError):
    name: typing.Literal["InvalidFieldSchema"]
    parameters: InvalidFieldSchemaParameters
    error_instance_id: str


class InvalidFilterValueParameters(typing_extensions.TypedDict):
    """The provided filter value is invalid."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    field: str
    value: typing.Any
    expectedType: core_models.FilterType


@dataclass
class InvalidFilterValue(errors.BadRequestError):
    name: typing.Literal["InvalidFilterValue"]
    parameters: InvalidFilterValueParameters
    error_instance_id: str


class InvalidOrFilterParameters(typing_extensions.TypedDict):
    """The provided OR filter should have at least one sub-filter."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class InvalidOrFilter(errors.BadRequestError):
    name: typing.Literal["InvalidOrFilter"]
    parameters: InvalidOrFilterParameters
    error_instance_id: str


class InvalidPageSizeParameters(typing_extensions.TypedDict):
    """The provided page size was zero or negative. Page sizes must be greater than zero."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    pageSize: core_models.PageSize
    """The page size to use for the endpoint."""


@dataclass
class InvalidPageSize(errors.BadRequestError):
    name: typing.Literal["InvalidPageSize"]
    parameters: InvalidPageSizeParameters
    error_instance_id: str


class InvalidPageTokenParameters(typing_extensions.TypedDict):
    """The provided page token is invalid."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    pageToken: core_models.PageToken
    """
    The page token indicates where to start paging. This should be omitted from the first page's request.
    To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response
    and use it to populate the `pageToken` field of the next request.
    """


@dataclass
class InvalidPageToken(errors.BadRequestError):
    name: typing.Literal["InvalidPageToken"]
    parameters: InvalidPageTokenParameters
    error_instance_id: str


class InvalidParameterCombinationParameters(typing_extensions.TypedDict):
    """The given parameters are individually valid but cannot be used in the given combination."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    validCombinations: typing.List[typing.List[str]]
    providedParameters: typing.List[str]


@dataclass
class InvalidParameterCombination(errors.BadRequestError):
    name: typing.Literal["InvalidParameterCombination"]
    parameters: InvalidParameterCombinationParameters
    error_instance_id: str


class InvalidSchemaParameters(typing_extensions.TypedDict):
    """The schema failed validations"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    errorType: str
    message: str


@dataclass
class InvalidSchema(errors.BadRequestError):
    name: typing.Literal["InvalidSchema"]
    parameters: InvalidSchemaParameters
    error_instance_id: str


class InvalidTimeZoneParameters(typing_extensions.TypedDict):
    """The time zone is invalid."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    timeZone: core_models.ZoneId


@dataclass
class InvalidTimeZone(errors.BadRequestError):
    name: typing.Literal["InvalidTimeZone"]
    parameters: InvalidTimeZoneParameters
    error_instance_id: str


class MissingBatchRequestParameters(typing_extensions.TypedDict):
    """Batch requests must contain at least one element."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class MissingBatchRequest(errors.BadRequestError):
    name: typing.Literal["MissingBatchRequest"]
    parameters: MissingBatchRequestParameters
    error_instance_id: str


class MissingPostBodyParameters(typing_extensions.TypedDict):
    """A post body is required for this endpoint, but was not found in the request."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class MissingPostBody(errors.BadRequestError):
    name: typing.Literal["MissingPostBody"]
    parameters: MissingPostBodyParameters
    error_instance_id: str


class ResourceNameAlreadyExistsParameters(typing_extensions.TypedDict):
    """The provided resource name is already in use by another resource in the same folder."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    parentFolderRid: core_models.FolderRid
    resourceName: str


@dataclass
class ResourceNameAlreadyExists(errors.ConflictError):
    name: typing.Literal["ResourceNameAlreadyExists"]
    parameters: ResourceNameAlreadyExistsParameters
    error_instance_id: str


class SchemaIsNotStreamSchemaParameters(typing_extensions.TypedDict):
    """The requested schema could not be converted into a stream schema."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class SchemaIsNotStreamSchema(errors.BadRequestError):
    name: typing.Literal["SchemaIsNotStreamSchema"]
    parameters: SchemaIsNotStreamSchemaParameters
    error_instance_id: str


class UnknownDistanceUnitParameters(typing_extensions.TypedDict):
    """An unknown distance unit was provided."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    unknownUnit: str
    knownUnits: typing.List[core_models.DistanceUnit]


@dataclass
class UnknownDistanceUnit(errors.BadRequestError):
    name: typing.Literal["UnknownDistanceUnit"]
    parameters: UnknownDistanceUnitParameters
    error_instance_id: str


__all__ = [
    "ApiFeaturePreviewUsageOnly",
    "ApiUsageDenied",
    "BatchRequestSizeExceededLimit",
    "FolderNotFound",
    "FoundryBranchNotFound",
    "InvalidAndFilter",
    "InvalidChangeDataCaptureConfiguration",
    "InvalidFieldSchema",
    "InvalidFilterValue",
    "InvalidOrFilter",
    "InvalidPageSize",
    "InvalidPageToken",
    "InvalidParameterCombination",
    "InvalidSchema",
    "InvalidTimeZone",
    "MissingBatchRequest",
    "MissingPostBody",
    "ResourceNameAlreadyExists",
    "SchemaIsNotStreamSchema",
    "UnknownDistanceUnit",
]
