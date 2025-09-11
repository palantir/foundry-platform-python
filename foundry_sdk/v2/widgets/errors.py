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
from foundry_sdk.v2.widgets import models as widgets_models


class DeleteReleasePermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not delete the Release."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    widgetSetRid: widgets_models.WidgetSetRid
    """A Resource Identifier (RID) identifying a widget set."""

    releaseVersion: widgets_models.ReleaseVersion
    """The semantic version of the widget set."""


@dataclass
class DeleteReleasePermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["DeleteReleasePermissionDenied"]
    parameters: DeleteReleasePermissionDeniedParameters
    error_instance_id: str


class DevModeSettingsNotFoundParameters(typing_extensions.TypedDict):
    """The given DevModeSettings could not be found."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class DevModeSettingsNotFound(errors.NotFoundError):
    name: typing.Literal["DevModeSettingsNotFound"]
    parameters: DevModeSettingsNotFoundParameters
    error_instance_id: str


class DisableDevModeSettingsPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not disable the DevModeSettings."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class DisableDevModeSettingsPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["DisableDevModeSettingsPermissionDenied"]
    parameters: DisableDevModeSettingsPermissionDeniedParameters
    error_instance_id: str


class EnableDevModeSettingsPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not enable the DevModeSettings."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class EnableDevModeSettingsPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["EnableDevModeSettingsPermissionDenied"]
    parameters: EnableDevModeSettingsPermissionDeniedParameters
    error_instance_id: str


class FileCountLimitExceededParameters(typing_extensions.TypedDict):
    """The .zip archive contains too many files."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    fileCountLimit: int


@dataclass
class FileCountLimitExceeded(errors.BadRequestError):
    name: typing.Literal["FileCountLimitExceeded"]
    parameters: FileCountLimitExceededParameters
    error_instance_id: str


class FileSizeLimitExceededParameters(typing_extensions.TypedDict):
    """
    A file inside the .zip archive is too big. You must ensure that all files inside
    the .zip archive are within the limit.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    fileSizeBytesLimit: core.Long
    currentFileSizeBytes: core.Long
    currentFilePath: str


@dataclass
class FileSizeLimitExceeded(errors.BadRequestError):
    name: typing.Literal["FileSizeLimitExceeded"]
    parameters: FileSizeLimitExceededParameters
    error_instance_id: str


class GetDevModeSettingsPermissionDeniedParameters(typing_extensions.TypedDict):
    """The provided token does not have permission to access dev mode settings."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class GetDevModeSettingsPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["GetDevModeSettingsPermissionDenied"]
    parameters: GetDevModeSettingsPermissionDeniedParameters
    error_instance_id: str


class InvalidDevModeBaseHrefParameters(typing_extensions.TypedDict):
    """
    The base href in the dev mode settings is invalid. It must be a valid localhost URL
    with an optional port.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    baseHref: str


@dataclass
class InvalidDevModeBaseHref(errors.BadRequestError):
    name: typing.Literal["InvalidDevModeBaseHref"]
    parameters: InvalidDevModeBaseHrefParameters
    error_instance_id: str


class InvalidDevModeEntrypointCssCountParameters(typing_extensions.TypedDict):
    """
    The dev mode settings contains too many CSS entrypoints. You must limit the number
    of CSS entrypoints to the maximum allowed.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    reason: str
    entrypointCssCount: int


@dataclass
class InvalidDevModeEntrypointCssCount(errors.BadRequestError):
    name: typing.Literal["InvalidDevModeEntrypointCssCount"]
    parameters: InvalidDevModeEntrypointCssCountParameters
    error_instance_id: str


class InvalidDevModeEntrypointJsCountParameters(typing_extensions.TypedDict):
    """
    The dev mode settings contains too many JavaScript entrypoints. You must limit the number
    of JavaScript entrypoints to the maximum allowed.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    reason: str
    entrypointJsCount: int


@dataclass
class InvalidDevModeEntrypointJsCount(errors.BadRequestError):
    name: typing.Literal["InvalidDevModeEntrypointJsCount"]
    parameters: InvalidDevModeEntrypointJsCountParameters
    error_instance_id: str


class InvalidDevModeFilePathParameters(typing_extensions.TypedDict):
    """
    The dev mode settings contains an invalid entrypoint file path. The file path must be a
    valid localhost URL with an optional port and a file path.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    reason: str
    filePath: str


@dataclass
class InvalidDevModeFilePath(errors.BadRequestError):
    name: typing.Literal["InvalidDevModeFilePath"]
    parameters: InvalidDevModeFilePathParameters
    error_instance_id: str


class InvalidDevModeWidgetSettingsCountParameters(typing_extensions.TypedDict):
    """
    The dev mode settings contains too many widget settings. You must limit the number of
    widget settings to the maximum allowed.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    reason: str
    widgetSettingsCount: int


@dataclass
class InvalidDevModeWidgetSettingsCount(errors.BadRequestError):
    name: typing.Literal["InvalidDevModeWidgetSettingsCount"]
    parameters: InvalidDevModeWidgetSettingsCountParameters
    error_instance_id: str


class InvalidEntrypointCssCountParameters(typing_extensions.TypedDict):
    """
    The widget declares too many CSS entrypoints. You must limit the number
    of CSS entrypoints to the maximum allowed.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    reason: str
    entrypointCssCount: int


@dataclass
class InvalidEntrypointCssCount(errors.BadRequestError):
    name: typing.Literal["InvalidEntrypointCssCount"]
    parameters: InvalidEntrypointCssCountParameters
    error_instance_id: str


class InvalidEntrypointJsCountParameters(typing_extensions.TypedDict):
    """
    The widget declares too many JavaScript entrypoints. You must limit the number
    of JavaScript entrypoints to the maximum allowed.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    reason: str
    entrypointJsCount: int


@dataclass
class InvalidEntrypointJsCount(errors.BadRequestError):
    name: typing.Literal["InvalidEntrypointJsCount"]
    parameters: InvalidEntrypointJsCountParameters
    error_instance_id: str


class InvalidEventCountParameters(typing_extensions.TypedDict):
    """The widget config contains too many events."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    reason: str
    eventCount: int


@dataclass
class InvalidEventCount(errors.BadRequestError):
    name: typing.Literal["InvalidEventCount"]
    parameters: InvalidEventCountParameters
    error_instance_id: str


class InvalidEventDisplayNameParameters(typing_extensions.TypedDict):
    """The event display name is invalid."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    reason: str
    eventDisplayName: str


@dataclass
class InvalidEventDisplayName(errors.BadRequestError):
    name: typing.Literal["InvalidEventDisplayName"]
    parameters: InvalidEventDisplayNameParameters
    error_instance_id: str


class InvalidEventIdParameters(typing_extensions.TypedDict):
    """The event id is invalid."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    reason: str
    eventId: str


@dataclass
class InvalidEventId(errors.BadRequestError):
    name: typing.Literal["InvalidEventId"]
    parameters: InvalidEventIdParameters
    error_instance_id: str


class InvalidEventParameterUpdateIdParameters(typing_extensions.TypedDict):
    """The event references an invalid parameter id."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    reason: str
    parameterUpdateId: str


@dataclass
class InvalidEventParameterUpdateId(errors.BadRequestError):
    name: typing.Literal["InvalidEventParameterUpdateId"]
    parameters: InvalidEventParameterUpdateIdParameters
    error_instance_id: str


class InvalidFilePathParameters(typing_extensions.TypedDict):
    """The widget declares an invalid production entrypoint file path."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    reason: str
    filePath: str


@dataclass
class InvalidFilePath(errors.BadRequestError):
    name: typing.Literal["InvalidFilePath"]
    parameters: InvalidFilePathParameters
    error_instance_id: str


class InvalidManifestParameters(typing_extensions.TypedDict):
    """
    The manifest file in the .zip archive at the path `.palantir/widgets.config.json`
    could not be found or is not well formed.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    reason: str


@dataclass
class InvalidManifest(errors.BadRequestError):
    name: typing.Literal["InvalidManifest"]
    parameters: InvalidManifestParameters
    error_instance_id: str


class InvalidParameterCountParameters(typing_extensions.TypedDict):
    """The widget config contains too many parameters."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    reason: str
    parameterCount: int


@dataclass
class InvalidParameterCount(errors.BadRequestError):
    name: typing.Literal["InvalidParameterCount"]
    parameters: InvalidParameterCountParameters
    error_instance_id: str


class InvalidParameterDisplayNameParameters(typing_extensions.TypedDict):
    """The parameter display name is invalid."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    reason: str
    parameterDisplayName: str


@dataclass
class InvalidParameterDisplayName(errors.BadRequestError):
    name: typing.Literal["InvalidParameterDisplayName"]
    parameters: InvalidParameterDisplayNameParameters
    error_instance_id: str


class InvalidParameterIdParameters(typing_extensions.TypedDict):
    """The parameter id is invalid."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    reason: str
    parameterId: str


@dataclass
class InvalidParameterId(errors.BadRequestError):
    name: typing.Literal["InvalidParameterId"]
    parameters: InvalidParameterIdParameters
    error_instance_id: str


class InvalidPublishRepositoryParameters(typing_extensions.TypedDict):
    """The manifest file targets a widget set that has not linked the repository to publish."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class InvalidPublishRepository(errors.BadRequestError):
    name: typing.Literal["InvalidPublishRepository"]
    parameters: InvalidPublishRepositoryParameters
    error_instance_id: str


class InvalidReleaseDescriptionParameters(typing_extensions.TypedDict):
    """The release description is invalid."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    reason: str
    releaseDescription: str


@dataclass
class InvalidReleaseDescription(errors.BadRequestError):
    name: typing.Literal["InvalidReleaseDescription"]
    parameters: InvalidReleaseDescriptionParameters
    error_instance_id: str


class InvalidReleaseWidgetsCountParameters(typing_extensions.TypedDict):
    """The release contains zero widgets or too many widgets."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    reason: str
    widgetsCount: int


@dataclass
class InvalidReleaseWidgetsCount(errors.BadRequestError):
    name: typing.Literal["InvalidReleaseWidgetsCount"]
    parameters: InvalidReleaseWidgetsCountParameters
    error_instance_id: str


class InvalidVersionParameters(typing_extensions.TypedDict):
    """
    The given version is invalid. Versions must follow semantic versioning with major, minor,
    and patch versions separate by periods, e.g. `0.1.0` or `1.2.3`.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    version: str


@dataclass
class InvalidVersion(errors.BadRequestError):
    name: typing.Literal["InvalidVersion"]
    parameters: InvalidVersionParameters
    error_instance_id: str


class InvalidWidgetDescriptionParameters(typing_extensions.TypedDict):
    """The widget description is invalid."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    reason: str
    widgetDescription: str


@dataclass
class InvalidWidgetDescription(errors.BadRequestError):
    name: typing.Literal["InvalidWidgetDescription"]
    parameters: InvalidWidgetDescriptionParameters
    error_instance_id: str


class InvalidWidgetIdParameters(typing_extensions.TypedDict):
    """The widget id is invalid."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    reason: str
    widgetId: str


@dataclass
class InvalidWidgetId(errors.BadRequestError):
    name: typing.Literal["InvalidWidgetId"]
    parameters: InvalidWidgetIdParameters
    error_instance_id: str


class InvalidWidgetNameParameters(typing_extensions.TypedDict):
    """The widget name is invalid."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    reason: str
    widgetName: str


@dataclass
class InvalidWidgetName(errors.BadRequestError):
    name: typing.Literal["InvalidWidgetName"]
    parameters: InvalidWidgetNameParameters
    error_instance_id: str


class OntologySdkNotFoundParameters(typing_extensions.TypedDict):
    """A referenced Ontology SDK package could not be found."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    sdkPackageRid: core.RID
    sdkVersion: str


@dataclass
class OntologySdkNotFound(errors.NotFoundError):
    name: typing.Literal["OntologySdkNotFound"]
    parameters: OntologySdkNotFoundParameters
    error_instance_id: str


class PauseDevModeSettingsPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not pause the DevModeSettings."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class PauseDevModeSettingsPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["PauseDevModeSettingsPermissionDenied"]
    parameters: PauseDevModeSettingsPermissionDeniedParameters
    error_instance_id: str


class PublishReleasePermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not publish the Repository."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    repositoryRid: widgets_models.RepositoryRid
    """A Resource Identifier (RID) identifying a repository."""


@dataclass
class PublishReleasePermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["PublishReleasePermissionDenied"]
    parameters: PublishReleasePermissionDeniedParameters
    error_instance_id: str


class ReleaseNotFoundParameters(typing_extensions.TypedDict):
    """The given Release could not be found."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    widgetSetRid: widgets_models.WidgetSetRid
    """A Resource Identifier (RID) identifying a widget set."""

    releaseVersion: widgets_models.ReleaseVersion
    """The semantic version of the widget set."""


@dataclass
class ReleaseNotFound(errors.NotFoundError):
    name: typing.Literal["ReleaseNotFound"]
    parameters: ReleaseNotFoundParameters
    error_instance_id: str


class RepositoryNotFoundParameters(typing_extensions.TypedDict):
    """The given Repository could not be found."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    repositoryRid: widgets_models.RepositoryRid
    """A Resource Identifier (RID) identifying a repository."""


@dataclass
class RepositoryNotFound(errors.NotFoundError):
    name: typing.Literal["RepositoryNotFound"]
    parameters: RepositoryNotFoundParameters
    error_instance_id: str


class SetWidgetSetDevModeSettingsByIdPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not setWidgetSetById the DevModeSettings."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class SetWidgetSetDevModeSettingsByIdPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["SetWidgetSetDevModeSettingsByIdPermissionDenied"]
    parameters: SetWidgetSetDevModeSettingsByIdPermissionDeniedParameters
    error_instance_id: str


class SetWidgetSetDevModeSettingsPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not setWidgetSet the DevModeSettings."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class SetWidgetSetDevModeSettingsPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["SetWidgetSetDevModeSettingsPermissionDenied"]
    parameters: SetWidgetSetDevModeSettingsPermissionDeniedParameters
    error_instance_id: str


class VersionAlreadyExistsParameters(typing_extensions.TypedDict):
    """The given version already exists."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    version: str


@dataclass
class VersionAlreadyExists(errors.ConflictError):
    name: typing.Literal["VersionAlreadyExists"]
    parameters: VersionAlreadyExistsParameters
    error_instance_id: str


class VersionLimitExceededParameters(typing_extensions.TypedDict):
    """
    The widget set contains too many versions. You must delete an old version before
    uploading a new one.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    versionLimit: int


@dataclass
class VersionLimitExceeded(errors.BadRequestError):
    name: typing.Literal["VersionLimitExceeded"]
    parameters: VersionLimitExceededParameters
    error_instance_id: str


class WidgetIdNotFoundParameters(typing_extensions.TypedDict):
    """
    A non-existent widget id was provided. If creating a new widget, you must first publish your changes before
    previewing with developer mode.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    widgetSetRid: widgets_models.WidgetSetRid
    widgetId: str


@dataclass
class WidgetIdNotFound(errors.NotFoundError):
    name: typing.Literal["WidgetIdNotFound"]
    parameters: WidgetIdNotFoundParameters
    error_instance_id: str


class WidgetLimitExceededParameters(typing_extensions.TypedDict):
    """
    The widget set contains too many widgets. You must delete another widget before
    creating a new one.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    widgetLimit: int


@dataclass
class WidgetLimitExceeded(errors.BadRequestError):
    name: typing.Literal["WidgetLimitExceeded"]
    parameters: WidgetLimitExceededParameters
    error_instance_id: str


class WidgetSetNotFoundParameters(typing_extensions.TypedDict):
    """The given WidgetSet could not be found."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    widgetSetRid: widgets_models.WidgetSetRid
    """A Resource Identifier (RID) identifying a widget set."""


@dataclass
class WidgetSetNotFound(errors.NotFoundError):
    name: typing.Literal["WidgetSetNotFound"]
    parameters: WidgetSetNotFoundParameters
    error_instance_id: str


__all__ = [
    "DeleteReleasePermissionDenied",
    "DevModeSettingsNotFound",
    "DisableDevModeSettingsPermissionDenied",
    "EnableDevModeSettingsPermissionDenied",
    "FileCountLimitExceeded",
    "FileSizeLimitExceeded",
    "GetDevModeSettingsPermissionDenied",
    "InvalidDevModeBaseHref",
    "InvalidDevModeEntrypointCssCount",
    "InvalidDevModeEntrypointJsCount",
    "InvalidDevModeFilePath",
    "InvalidDevModeWidgetSettingsCount",
    "InvalidEntrypointCssCount",
    "InvalidEntrypointJsCount",
    "InvalidEventCount",
    "InvalidEventDisplayName",
    "InvalidEventId",
    "InvalidEventParameterUpdateId",
    "InvalidFilePath",
    "InvalidManifest",
    "InvalidParameterCount",
    "InvalidParameterDisplayName",
    "InvalidParameterId",
    "InvalidPublishRepository",
    "InvalidReleaseDescription",
    "InvalidReleaseWidgetsCount",
    "InvalidVersion",
    "InvalidWidgetDescription",
    "InvalidWidgetId",
    "InvalidWidgetName",
    "OntologySdkNotFound",
    "PauseDevModeSettingsPermissionDenied",
    "PublishReleasePermissionDenied",
    "ReleaseNotFound",
    "RepositoryNotFound",
    "SetWidgetSetDevModeSettingsByIdPermissionDenied",
    "SetWidgetSetDevModeSettingsPermissionDenied",
    "VersionAlreadyExists",
    "VersionLimitExceeded",
    "WidgetIdNotFound",
    "WidgetLimitExceeded",
    "WidgetSetNotFound",
]
