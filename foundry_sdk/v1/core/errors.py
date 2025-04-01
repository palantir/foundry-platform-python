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
from foundry_sdk.v1.core import models as core_models


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


class FolderNotFoundParameters(typing_extensions.TypedDict):
    """The requested folder could not be found, or the client token does not have access to it."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    folderRid: core_models.FolderRid


@dataclass
class FolderNotFound(errors.NotFoundError):
    name: typing.Literal["FolderNotFound"]
    parameters: FolderNotFoundParameters
    error_instance_id: str


class InvalidPageSizeParameters(typing_extensions.TypedDict):
    """The provided page size was zero or negative. Page sizes must be greater than zero."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    pageSize: core_models.PageSize


@dataclass
class InvalidPageSize(errors.BadRequestError):
    name: typing.Literal["InvalidPageSize"]
    parameters: InvalidPageSizeParameters
    error_instance_id: str


class InvalidPageTokenParameters(typing_extensions.TypedDict):
    """The provided page token could not be used to retrieve the next page of results."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    pageToken: core_models.PageToken


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
    "FolderNotFound",
    "InvalidPageSize",
    "InvalidPageToken",
    "InvalidParameterCombination",
    "MissingPostBody",
    "ResourceNameAlreadyExists",
    "UnknownDistanceUnit",
]
