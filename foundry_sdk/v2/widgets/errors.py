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


class InvalidDevModeFilePathParameters(typing_extensions.TypedDict):
    """
    The dev mode settings contains an invalid entrypoint file path. The file path must be a
    valid localhost URL with an optional port and a file path.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

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
    The dev mode settings contains too many CSS entrypoints. You must limit the number
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
    The dev mode settings contains too many JavaScript entrypoints. You must limit the number
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


class InvalidPublishRepositoryParameters(typing_extensions.TypedDict):
    """The manifest file targets a widget set that has not linked the repository to publish."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class InvalidPublishRepository(errors.BadRequestError):
    name: typing.Literal["InvalidPublishRepository"]
    parameters: InvalidPublishRepositoryParameters
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
    "InvalidDevModeFilePath",
    "InvalidDevModeWidgetSettingsCount",
    "InvalidEntrypointCssCount",
    "InvalidEntrypointJsCount",
    "InvalidManifest",
    "InvalidPublishRepository",
    "InvalidVersion",
    "PauseDevModeSettingsPermissionDenied",
    "PublishReleasePermissionDenied",
    "ReleaseNotFound",
    "RepositoryNotFound",
    "SetWidgetSetDevModeSettingsByIdPermissionDenied",
    "SetWidgetSetDevModeSettingsPermissionDenied",
    "VersionAlreadyExists",
    "VersionLimitExceeded",
    "WidgetSetNotFound",
]
