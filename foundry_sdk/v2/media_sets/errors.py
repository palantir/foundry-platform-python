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
from foundry_sdk.v2.media_sets import models as media_sets_models


class ConflictingMediaSetIdentifiersParameters(typing_extensions.TypedDict):
    """Client provided more than one of branch name, branch rid, or view rid as arguments.  Only one may be specified."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class ConflictingMediaSetIdentifiers(errors.BadRequestError):
    name: typing.Literal["ConflictingMediaSetIdentifiers"]
    parameters: ConflictingMediaSetIdentifiersParameters
    error_instance_id: str


class GetMediaItemRidByPathPermissionDeniedParameters(typing_extensions.TypedDict):
    """The token does not have permission to view paths in this media set."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    mediaSetRid: core_models.MediaSetRid


@dataclass
class GetMediaItemRidByPathPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["GetMediaItemRidByPathPermissionDenied"]
    parameters: GetMediaItemRidByPathPermissionDeniedParameters
    error_instance_id: str


class InvalidMediaItemSchemaParameters(typing_extensions.TypedDict):
    """The media item does not match the schema of the media set."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    mediaSetRid: core_models.MediaSetRid
    path: typing_extensions.NotRequired[core_models.MediaItemPath]


@dataclass
class InvalidMediaItemSchema(errors.BadRequestError):
    name: typing.Literal["InvalidMediaItemSchema"]
    parameters: InvalidMediaItemSchemaParameters
    error_instance_id: str


class MediaItemHasUnsupportedSecuritySettingsParameters(typing_extensions.TypedDict):
    """The file cannot be read because it contains unsupported security settings (for example, public-key security handlers in a PDF)."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    mediaSetRid: core_models.MediaSetRid
    path: typing_extensions.NotRequired[core_models.MediaItemPath]


@dataclass
class MediaItemHasUnsupportedSecuritySettings(errors.BadRequestError):
    name: typing.Literal["MediaItemHasUnsupportedSecuritySettings"]
    parameters: MediaItemHasUnsupportedSecuritySettingsParameters
    error_instance_id: str


class MediaItemImageUnparsableParameters(typing_extensions.TypedDict):
    """The file cannot be parsed as an image."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    mediaSetRid: core_models.MediaSetRid
    path: typing_extensions.NotRequired[core_models.MediaItemPath]


@dataclass
class MediaItemImageUnparsable(errors.BadRequestError):
    name: typing.Literal["MediaItemImageUnparsable"]
    parameters: MediaItemImageUnparsableParameters
    error_instance_id: str


class MediaItemIsPasswordProtectedParameters(typing_extensions.TypedDict):
    """The file cannot be read because it is password protected."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    mediaSetRid: core_models.MediaSetRid
    path: typing_extensions.NotRequired[core_models.MediaItemPath]


@dataclass
class MediaItemIsPasswordProtected(errors.BadRequestError):
    name: typing.Literal["MediaItemIsPasswordProtected"]
    parameters: MediaItemIsPasswordProtectedParameters
    error_instance_id: str


class MediaItemNotFoundParameters(typing_extensions.TypedDict):
    """The requested media item could not be found, or the client token does not have access to it."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    mediaSetRid: core_models.MediaSetRid
    mediaItemRid: core_models.MediaItemRid


@dataclass
class MediaItemNotFound(errors.NotFoundError):
    name: typing.Literal["MediaItemNotFound"]
    parameters: MediaItemNotFoundParameters
    error_instance_id: str


class MediaItemXmlUnparsableParameters(typing_extensions.TypedDict):
    """The document cannot be parsed due to an unrecognized XML structure."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    mediaItemXmlFormat: media_sets_models.MediaItemXmlFormat
    mediaSetRid: core_models.MediaSetRid
    path: typing_extensions.NotRequired[core_models.MediaItemPath]


@dataclass
class MediaItemXmlUnparsable(errors.BadRequestError):
    name: typing.Literal["MediaItemXmlUnparsable"]
    parameters: MediaItemXmlUnparsableParameters
    error_instance_id: str


class MediaSetNotFoundParameters(typing_extensions.TypedDict):
    """The requested media set could not be found, or the client token does not have access to it."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    mediaSetRid: core_models.MediaSetRid


@dataclass
class MediaSetNotFound(errors.NotFoundError):
    name: typing.Literal["MediaSetNotFound"]
    parameters: MediaSetNotFoundParameters
    error_instance_id: str


class MissingMediaItemContentParameters(typing_extensions.TypedDict):
    """The file has no bytes."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    mediaSetRid: core_models.MediaSetRid
    path: typing_extensions.NotRequired[core_models.MediaItemPath]


@dataclass
class MissingMediaItemContent(errors.BadRequestError):
    name: typing.Literal["MissingMediaItemContent"]
    parameters: MissingMediaItemContentParameters
    error_instance_id: str


class MissingMediaItemPathParameters(typing_extensions.TypedDict):
    """The given media set requires paths but no path was provided."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    mediaSetRid: core_models.MediaSetRid


@dataclass
class MissingMediaItemPath(errors.BadRequestError):
    name: typing.Literal["MissingMediaItemPath"]
    parameters: MissingMediaItemPathParameters
    error_instance_id: str


class TransformedMediaItemNotFoundParameters(typing_extensions.TypedDict):
    """The requested media item could not be found, or the client token does not have access to it."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    mediaSetRid: core_models.MediaSetRid
    mediaItemRid: core_models.MediaItemRid


@dataclass
class TransformedMediaItemNotFound(errors.NotFoundError):
    name: typing.Literal["TransformedMediaItemNotFound"]
    parameters: TransformedMediaItemNotFoundParameters
    error_instance_id: str


__all__ = [
    "ConflictingMediaSetIdentifiers",
    "GetMediaItemRidByPathPermissionDenied",
    "InvalidMediaItemSchema",
    "MediaItemHasUnsupportedSecuritySettings",
    "MediaItemImageUnparsable",
    "MediaItemIsPasswordProtected",
    "MediaItemNotFound",
    "MediaItemXmlUnparsable",
    "MediaSetNotFound",
    "MissingMediaItemContent",
    "MissingMediaItemPath",
    "TransformedMediaItemNotFound",
]
