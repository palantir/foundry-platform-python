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
from foundry_sdk.v2.data_health import models as data_health_models


class CheckAlreadyExistsParameters(typing_extensions.TypedDict):
    """
    A check of the given type for the given subject(s) already exists. The conflicting check will be returned
    if the provided token has permission to view it.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    conflictingCheck: typing_extensions.NotRequired[data_health_models.Check]


@dataclass
class CheckAlreadyExists(errors.ConflictError):
    name: typing.Literal["CheckAlreadyExists"]
    parameters: CheckAlreadyExistsParameters
    error_instance_id: str


class CheckNotFoundParameters(typing_extensions.TypedDict):
    """The given Check could not be found."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    checkRid: core_models.CheckRid


@dataclass
class CheckNotFound(errors.NotFoundError):
    name: typing.Literal["CheckNotFound"]
    parameters: CheckNotFoundParameters
    error_instance_id: str


class CheckReportNotFoundParameters(typing_extensions.TypedDict):
    """The given CheckReport could not be found."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    checkReportRid: core_models.CheckReportRid


@dataclass
class CheckReportNotFound(errors.NotFoundError):
    name: typing.Literal["CheckReportNotFound"]
    parameters: CheckReportNotFoundParameters
    error_instance_id: str


class CheckTypeNotSupportedParameters(typing_extensions.TypedDict):
    """The type of the requested check is not yet supported in the Platform API."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    checkType: str


@dataclass
class CheckTypeNotSupported(errors.BadRequestError):
    name: typing.Literal["CheckTypeNotSupported"]
    parameters: CheckTypeNotSupportedParameters
    error_instance_id: str


class CreateCheckPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not create the Check."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class CreateCheckPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["CreateCheckPermissionDenied"]
    parameters: CreateCheckPermissionDeniedParameters
    error_instance_id: str


class DeleteCheckPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not delete the Check."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    checkRid: core_models.CheckRid


@dataclass
class DeleteCheckPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["DeleteCheckPermissionDenied"]
    parameters: DeleteCheckPermissionDeniedParameters
    error_instance_id: str


class InvalidNumericColumnCheckConfigParameters(typing_extensions.TypedDict):
    """The NumericColumnCheckConfig is invalid. It must contain at least one of numericBounds or trend."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class InvalidNumericColumnCheckConfig(errors.BadRequestError):
    name: typing.Literal["InvalidNumericColumnCheckConfig"]
    parameters: InvalidNumericColumnCheckConfigParameters
    error_instance_id: str


class InvalidPercentageCheckConfigParameters(typing_extensions.TypedDict):
    """The PercentageCheckConfig is invalid. It must contain at least one of percentageBounds or medianDeviation."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class InvalidPercentageCheckConfig(errors.BadRequestError):
    name: typing.Literal["InvalidPercentageCheckConfig"]
    parameters: InvalidPercentageCheckConfigParameters
    error_instance_id: str


class InvalidTimeCheckConfigParameters(typing_extensions.TypedDict):
    """The TimeCheckConfig is invalid. It must contain at least one of timeBounds or medianDeviation."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class InvalidTimeCheckConfig(errors.BadRequestError):
    name: typing.Literal["InvalidTimeCheckConfig"]
    parameters: InvalidTimeCheckConfigParameters
    error_instance_id: str


class InvalidTrendConfigParameters(typing_extensions.TypedDict):
    """The TrendConfig is invalid. It must contain at least one of trendType or differenceBounds."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class InvalidTrendConfig(errors.BadRequestError):
    name: typing.Literal["InvalidTrendConfig"]
    parameters: InvalidTrendConfigParameters
    error_instance_id: str


class ModifyingCheckTypeNotSupportedParameters(typing_extensions.TypedDict):
    """Changing the type of a check after it has been created is not supported."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    originalCheckType: str
    newCheckType: str


@dataclass
class ModifyingCheckTypeNotSupported(errors.BadRequestError):
    name: typing.Literal["ModifyingCheckTypeNotSupported"]
    parameters: ModifyingCheckTypeNotSupportedParameters
    error_instance_id: str


class PercentageValueAboveMaximumParameters(typing_extensions.TypedDict):
    """PercentageValue must be less than or equal to 100.0"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    value: float
    """The value that was provided."""

    maxInclusive: float
    """The maximum value allowed."""


@dataclass
class PercentageValueAboveMaximum(errors.BadRequestError):
    name: typing.Literal["PercentageValueAboveMaximum"]
    parameters: PercentageValueAboveMaximumParameters
    error_instance_id: str


class PercentageValueBelowMinimumParameters(typing_extensions.TypedDict):
    """PercentageValue must be greater than or equal to 0.0"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    value: float
    """The value that was provided."""

    minInclusive: float
    """The minimum value allowed."""


@dataclass
class PercentageValueBelowMinimum(errors.BadRequestError):
    name: typing.Literal["PercentageValueBelowMinimum"]
    parameters: PercentageValueBelowMinimumParameters
    error_instance_id: str


class ReplaceCheckPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not replace the Check."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    checkRid: core_models.CheckRid


@dataclass
class ReplaceCheckPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["ReplaceCheckPermissionDenied"]
    parameters: ReplaceCheckPermissionDeniedParameters
    error_instance_id: str


__all__ = [
    "CheckAlreadyExists",
    "CheckNotFound",
    "CheckReportNotFound",
    "CheckTypeNotSupported",
    "CreateCheckPermissionDenied",
    "DeleteCheckPermissionDenied",
    "InvalidNumericColumnCheckConfig",
    "InvalidPercentageCheckConfig",
    "InvalidTimeCheckConfig",
    "InvalidTrendConfig",
    "ModifyingCheckTypeNotSupported",
    "PercentageValueAboveMaximum",
    "PercentageValueBelowMinimum",
    "ReplaceCheckPermissionDenied",
]
