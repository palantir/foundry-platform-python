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
from foundry_sdk.v2.third_party_applications import (
    models as third_party_applications_models,
)  # NOQA


class CannotDeleteDeployedVersionParameters(typing_extensions.TypedDict):
    """The given website version is deployed. You must un-deploy it before deleting it."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    version: third_party_applications_models.VersionVersion


@dataclass
class CannotDeleteDeployedVersion(errors.BadRequestError):
    name: typing.Literal["CannotDeleteDeployedVersion"]
    parameters: CannotDeleteDeployedVersionParameters
    error_instance_id: str


class DeleteVersionPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not delete the Version."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    thirdPartyApplicationRid: third_party_applications_models.ThirdPartyApplicationRid
    """An RID identifying a third-party application created in Developer Console."""

    versionVersion: third_party_applications_models.VersionVersion
    """The semantic version of the Website."""


@dataclass
class DeleteVersionPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["DeleteVersionPermissionDenied"]
    parameters: DeleteVersionPermissionDeniedParameters
    error_instance_id: str


class DeployWebsitePermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not deploy the Website."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    thirdPartyApplicationRid: third_party_applications_models.ThirdPartyApplicationRid
    """An RID identifying a third-party application created in Developer Console."""


@dataclass
class DeployWebsitePermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["DeployWebsitePermissionDenied"]
    parameters: DeployWebsitePermissionDeniedParameters
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


class InvalidVersionParameters(typing_extensions.TypedDict):
    """The given website version is invalid. Versions must follow semantic versioning with major, minor, and patch versions separate by periods, e.g. `0.1.0` or `1.2.3`."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    version: str


@dataclass
class InvalidVersion(errors.BadRequestError):
    name: typing.Literal["InvalidVersion"]
    parameters: InvalidVersionParameters
    error_instance_id: str


class ThirdPartyApplicationNotFoundParameters(typing_extensions.TypedDict):
    """The given ThirdPartyApplication could not be found."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    thirdPartyApplicationRid: third_party_applications_models.ThirdPartyApplicationRid
    """An RID identifying a third-party application created in Developer Console."""


@dataclass
class ThirdPartyApplicationNotFound(errors.NotFoundError):
    name: typing.Literal["ThirdPartyApplicationNotFound"]
    parameters: ThirdPartyApplicationNotFoundParameters
    error_instance_id: str


class UndeployWebsitePermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not undeploy the Website."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    thirdPartyApplicationRid: third_party_applications_models.ThirdPartyApplicationRid
    """An RID identifying a third-party application created in Developer Console."""


@dataclass
class UndeployWebsitePermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["UndeployWebsitePermissionDenied"]
    parameters: UndeployWebsitePermissionDeniedParameters
    error_instance_id: str


class UploadSnapshotVersionPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not uploadSnapshot the Version."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    thirdPartyApplicationRid: third_party_applications_models.ThirdPartyApplicationRid
    """An RID identifying a third-party application created in Developer Console."""


@dataclass
class UploadSnapshotVersionPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["UploadSnapshotVersionPermissionDenied"]
    parameters: UploadSnapshotVersionPermissionDeniedParameters
    error_instance_id: str


class UploadVersionPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not upload the Version."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    thirdPartyApplicationRid: third_party_applications_models.ThirdPartyApplicationRid
    """An RID identifying a third-party application created in Developer Console."""


@dataclass
class UploadVersionPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["UploadVersionPermissionDenied"]
    parameters: UploadVersionPermissionDeniedParameters
    error_instance_id: str


class VersionAlreadyExistsParameters(typing_extensions.TypedDict):
    """The given website version already exists."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    version: third_party_applications_models.VersionVersion


@dataclass
class VersionAlreadyExists(errors.ConflictError):
    name: typing.Literal["VersionAlreadyExists"]
    parameters: VersionAlreadyExistsParameters
    error_instance_id: str


class VersionLimitExceededParameters(typing_extensions.TypedDict):
    """
    The website contains too many versions. You must delete an old version before
    uploading a new one.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    versionLimit: int


@dataclass
class VersionLimitExceeded(errors.BadRequestError):
    name: typing.Literal["VersionLimitExceeded"]
    parameters: VersionLimitExceededParameters
    error_instance_id: str


class VersionNotFoundParameters(typing_extensions.TypedDict):
    """The given Version could not be found."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    thirdPartyApplicationRid: third_party_applications_models.ThirdPartyApplicationRid
    """An RID identifying a third-party application created in Developer Console."""

    versionVersion: third_party_applications_models.VersionVersion
    """The semantic version of the Website."""


@dataclass
class VersionNotFound(errors.NotFoundError):
    name: typing.Literal["VersionNotFound"]
    parameters: VersionNotFoundParameters
    error_instance_id: str


class WebsiteNotFoundParameters(typing_extensions.TypedDict):
    """The given Website could not be found."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    thirdPartyApplicationRid: third_party_applications_models.ThirdPartyApplicationRid
    """An RID identifying a third-party application created in Developer Console."""


@dataclass
class WebsiteNotFound(errors.NotFoundError):
    name: typing.Literal["WebsiteNotFound"]
    parameters: WebsiteNotFoundParameters
    error_instance_id: str


__all__ = [
    "CannotDeleteDeployedVersion",
    "DeleteVersionPermissionDenied",
    "DeployWebsitePermissionDenied",
    "FileCountLimitExceeded",
    "FileSizeLimitExceeded",
    "InvalidVersion",
    "ThirdPartyApplicationNotFound",
    "UndeployWebsitePermissionDenied",
    "UploadSnapshotVersionPermissionDenied",
    "UploadVersionPermissionDenied",
    "VersionAlreadyExists",
    "VersionLimitExceeded",
    "VersionNotFound",
    "WebsiteNotFound",
]
