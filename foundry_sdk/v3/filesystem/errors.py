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
from foundry_sdk.v3.filesystem import models as filesystem_models


class CreateFolderOutsideProjectNotSupportedParameters(typing_extensions.TypedDict):
    """Folders can only be created within a project."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    parentFolderRid: core_models.FolderRid


@dataclass
class CreateFolderOutsideProjectNotSupported(errors.BadRequestError):
    name: typing.Literal["CreateFolderOutsideProjectNotSupported"]
    parameters: CreateFolderOutsideProjectNotSupportedParameters
    error_instance_id: str


class CreateFolderPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not create the folder due to insufficient permissions."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    parentFolderRid: core_models.FolderRid


@dataclass
class CreateFolderPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["CreateFolderPermissionDenied"]
    parameters: CreateFolderPermissionDeniedParameters
    error_instance_id: str


class DeleteFolderPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not delete the folder due to insufficient permissions."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    folderRid: core_models.FolderRid


@dataclass
class DeleteFolderPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["DeleteFolderPermissionDenied"]
    parameters: DeleteFolderPermissionDeniedParameters
    error_instance_id: str


class DeleteOntologyResourcePermissionDeniedParameters(typing_extensions.TypedDict):
    """
    The resource, or one of its descendants, backs an ontology entity. Trashing such a resource through the
    filesystem would leave the ontology in an inconsistent state, so it must be deleted through the ontology APIs
    instead.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    resourceRids: typing.List[filesystem_models.ResourceRid]
    """The RIDs of the ontology-backed resources that prevent the request from being fulfilled."""


@dataclass
class DeleteOntologyResourcePermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["DeleteOntologyResourcePermissionDenied"]
    parameters: DeleteOntologyResourcePermissionDeniedParameters
    error_instance_id: str


class DeleteProjectPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not delete the project due to insufficient permissions."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    projectRid: filesystem_models.ProjectRid


@dataclass
class DeleteProjectPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["DeleteProjectPermissionDenied"]
    parameters: DeleteProjectPermissionDeniedParameters
    error_instance_id: str


class DeleteResourcePermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not delete the resource due to insufficient permissions."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    resourceRid: filesystem_models.ResourceRid


@dataclass
class DeleteResourcePermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["DeleteResourcePermissionDenied"]
    parameters: DeleteResourcePermissionDeniedParameters
    error_instance_id: str


class DeleteServiceSpaceNotSupportedParameters(typing_extensions.TypedDict):
    """The service's space cannot be deleted."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class DeleteServiceSpaceNotSupported(errors.BadRequestError):
    name: typing.Literal["DeleteServiceSpaceNotSupported"]
    parameters: DeleteServiceSpaceNotSupportedParameters
    error_instance_id: str


class DeleteSpacePermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not delete the space due to insufficient permissions."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    spaceRid: filesystem_models.SpaceRid


@dataclass
class DeleteSpacePermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["DeleteSpacePermissionDenied"]
    parameters: DeleteSpacePermissionDeniedParameters
    error_instance_id: str


class DeleteUserSpaceNotSupportedParameters(typing_extensions.TypedDict):
    """The user's space cannot be deleted."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class DeleteUserSpaceNotSupported(errors.BadRequestError):
    name: typing.Literal["DeleteUserSpaceNotSupported"]
    parameters: DeleteUserSpaceNotSupportedParameters
    error_instance_id: str


class FolderNotFoundParameters(typing_extensions.TypedDict):

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    folderRid: core_models.FolderRid


@dataclass
class FolderNotFound(errors.NotFoundError):
    name: typing.Literal["FolderNotFound"]
    parameters: FolderNotFoundParameters
    error_instance_id: str


class FoldersNotFoundParameters(typing_extensions.TypedDict):
    """The specified folders could not be found."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    folderRids: typing.List[core_models.FolderRid]


@dataclass
class FoldersNotFound(errors.NotFoundError):
    name: typing.Literal["FoldersNotFound"]
    parameters: FoldersNotFoundParameters
    error_instance_id: str


class GetResourceTimedOutParameters(typing_extensions.TypedDict):
    """The request to retrieve resource information timed out."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class GetResourceTimedOut(errors.InternalServerError):
    name: typing.Literal["GetResourceTimedOut"]
    parameters: GetResourceTimedOutParameters
    error_instance_id: str


class GetRootFolderNotSupportedParameters(typing_extensions.TypedDict):
    """The root folder cannot be retrieved."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class GetRootFolderNotSupported(errors.BadRequestError):
    name: typing.Literal["GetRootFolderNotSupported"]
    parameters: GetRootFolderNotSupportedParameters
    error_instance_id: str


class InvalidDisplayNameParameters(typing_extensions.TypedDict):
    """
    A display name must not be empty, must not be exactly `.` or `..`, must not contain a forward slash (`/`), and
    must not exceed 700 characters.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    displayName: filesystem_models.DisplayName
    maxLength: int
    """The maximum number of characters allowed in a display name."""


@dataclass
class InvalidDisplayName(errors.BadRequestError):
    name: typing.Literal["InvalidDisplayName"]
    parameters: InvalidDisplayNameParameters
    error_instance_id: str


class InvalidDisplayNameOnRestoreParameters(typing_extensions.TypedDict):
    """
    Cannot restore resource because restoring it would produce an invalid display name. While the resource is
    still in trash, rename it to a valid name that does not contain the reserved text ' (trashed)', then retry the
    restore.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    displayName: filesystem_models.DisplayName
    """The name that the resource would receive after being restored."""


@dataclass
class InvalidDisplayNameOnRestore(errors.BadRequestError):
    name: typing.Literal["InvalidDisplayNameOnRestore"]
    parameters: InvalidDisplayNameOnRestoreParameters
    error_instance_id: str


class InvalidFoldersParameters(typing_extensions.TypedDict):
    """The given resources are not folders."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    resourceRids: typing.List[filesystem_models.ResourceRid]


@dataclass
class InvalidFolders(errors.BadRequestError):
    name: typing.Literal["InvalidFolders"]
    parameters: InvalidFoldersParameters
    error_instance_id: str


class InvalidParentFolderParameters(typing_extensions.TypedDict):
    """The specified parent resource is not a folder."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    parentFolderRid: core_models.FolderRid


@dataclass
class InvalidParentFolder(errors.BadRequestError):
    name: typing.Literal["InvalidParentFolder"]
    parameters: InvalidParentFolderParameters
    error_instance_id: str


class InvalidPathParameters(typing_extensions.TypedDict):
    """
    The given path is invalid.

    A valid path has all components separated by a single `/`.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    path: filesystem_models.ResourcePath


@dataclass
class InvalidPath(errors.BadRequestError):
    name: typing.Literal["InvalidPath"]
    parameters: InvalidPathParameters
    error_instance_id: str


class InvalidProjectsParameters(typing_extensions.TypedDict):
    """The given resources are not projects."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    resourceRids: typing.List[filesystem_models.ResourceRid]


@dataclass
class InvalidProjects(errors.BadRequestError):
    name: typing.Literal["InvalidProjects"]
    parameters: InvalidProjectsParameters
    error_instance_id: str


class InvalidSpacesParameters(typing_extensions.TypedDict):
    """The given resources are not spaces."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    resourceRids: typing.List[filesystem_models.ResourceRid]


@dataclass
class InvalidSpaces(errors.BadRequestError):
    name: typing.Literal["InvalidSpaces"]
    parameters: InvalidSpacesParameters
    error_instance_id: str


class ListSpacesTimedOutParameters(typing_extensions.TypedDict):
    """The request to list spaces timed out."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class ListSpacesTimedOut(errors.InternalServerError):
    name: typing.Literal["ListSpacesTimedOut"]
    parameters: ListSpacesTimedOutParameters
    error_instance_id: str


class MissingDisplayNameParameters(typing_extensions.TypedDict):
    """A display name must be provided."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class MissingDisplayName(errors.BadRequestError):
    name: typing.Literal["MissingDisplayName"]
    parameters: MissingDisplayNameParameters
    error_instance_id: str


class ParentFolderNotFoundParameters(typing_extensions.TypedDict):
    """The specified parent folder could not be found."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    parentFolderRid: core_models.FolderRid


@dataclass
class ParentFolderNotFound(errors.NotFoundError):
    name: typing.Literal["ParentFolderNotFound"]
    parameters: ParentFolderNotFoundParameters
    error_instance_id: str


class PathNotFoundParameters(typing_extensions.TypedDict):
    """The given path could not be found."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    path: filesystem_models.ResourcePath


@dataclass
class PathNotFound(errors.NotFoundError):
    name: typing.Literal["PathNotFound"]
    parameters: PathNotFoundParameters
    error_instance_id: str


class ProjectNotFoundParameters(typing_extensions.TypedDict):

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    projectRid: filesystem_models.ProjectRid


@dataclass
class ProjectNotFound(errors.NotFoundError):
    name: typing.Literal["ProjectNotFound"]
    parameters: ProjectNotFoundParameters
    error_instance_id: str


class ProjectsNotFoundParameters(typing_extensions.TypedDict):
    """The specified projects could not be found."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    projectRids: typing.List[filesystem_models.ProjectRid]


@dataclass
class ProjectsNotFound(errors.NotFoundError):
    name: typing.Literal["ProjectsNotFound"]
    parameters: ProjectsNotFoundParameters
    error_instance_id: str


class ResourceDisplayNameAlreadyExistsParameters(typing_extensions.TypedDict):
    """The provided resource display name is already in use by another resource in the same folder."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    parentFolderRid: core_models.FolderRid
    displayName: filesystem_models.DisplayName


@dataclass
class ResourceDisplayNameAlreadyExists(errors.ConflictError):
    name: typing.Literal["ResourceDisplayNameAlreadyExists"]
    parameters: ResourceDisplayNameAlreadyExistsParameters
    error_instance_id: str


class ResourceNotDirectlyTrashedParameters(typing_extensions.TypedDict):
    """The resource is not directly trashed."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    resourceRid: filesystem_models.ResourceRid


@dataclass
class ResourceNotDirectlyTrashed(errors.BadRequestError):
    name: typing.Literal["ResourceNotDirectlyTrashed"]
    parameters: ResourceNotDirectlyTrashedParameters
    error_instance_id: str


class ResourceNotFoundParameters(typing_extensions.TypedDict):

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    resourceRid: filesystem_models.ResourceRid


@dataclass
class ResourceNotFound(errors.NotFoundError):
    name: typing.Literal["ResourceNotFound"]
    parameters: ResourceNotFoundParameters
    error_instance_id: str


class ResourceRegisteredForDeletionParameters(typing_extensions.TypedDict):
    """
    The resource, or one of its ancestors, is registered for deletion. Resources cannot be created within, or
    restored within, a project or space that is registered for deletion.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    resourceRid: filesystem_models.ResourceRid
    """
    The RID of the resource that is registered for deletion. This may be an ancestor, such as the containing
    project or space, rather than the resource named in the request.
    """


@dataclass
class ResourceRegisteredForDeletion(errors.BadRequestError):
    name: typing.Literal["ResourceRegisteredForDeletion"]
    parameters: ResourceRegisteredForDeletionParameters
    error_instance_id: str


class RestoreOntologyResourcePermissionDeniedParameters(typing_extensions.TypedDict):
    """
    The resource, or one of the trashed ancestors that would be restored alongside it, backs an ontology entity.
    Restoring such a resource through the filesystem would leave the ontology in an inconsistent state, so it must be
    restored through the ontology APIs instead.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    resourceRids: typing.List[filesystem_models.ResourceRid]
    """The RIDs of the ontology-backed resources that prevent the request from being fulfilled."""


@dataclass
class RestoreOntologyResourcePermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["RestoreOntologyResourcePermissionDenied"]
    parameters: RestoreOntologyResourcePermissionDeniedParameters
    error_instance_id: str


class RestoreResourcePermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not restore the resource due to insufficient permissions."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    resourceRid: filesystem_models.ResourceRid


@dataclass
class RestoreResourcePermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["RestoreResourcePermissionDenied"]
    parameters: RestoreResourcePermissionDeniedParameters
    error_instance_id: str


class SpaceNotFoundParameters(typing_extensions.TypedDict):

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    spaceRid: filesystem_models.SpaceRid


@dataclass
class SpaceNotFound(errors.NotFoundError):
    name: typing.Literal["SpaceNotFound"]
    parameters: SpaceNotFoundParameters
    error_instance_id: str


class SpacesNotFoundParameters(typing_extensions.TypedDict):
    """The specified spaces could not be found."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    spaceRids: typing.List[filesystem_models.SpaceRid]


@dataclass
class SpacesNotFound(errors.NotFoundError):
    name: typing.Literal["SpacesNotFound"]
    parameters: SpacesNotFoundParameters
    error_instance_id: str


class TrashingAutosavedResourcesNotSupportedParameters(typing_extensions.TypedDict):
    """Auto-saved resources cannot be trashed."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    resourceRids: typing.List[filesystem_models.ResourceRid]
    """The RIDs of the auto-saved resources that cannot be trashed."""


@dataclass
class TrashingAutosavedResourcesNotSupported(errors.BadRequestError):
    name: typing.Literal["TrashingAutosavedResourcesNotSupported"]
    parameters: TrashingAutosavedResourcesNotSupportedParameters
    error_instance_id: str


class TrashingHiddenResourcesNotSupportedParameters(typing_extensions.TypedDict):
    """Hidden resources cannot be trashed."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    resourceRids: typing.List[filesystem_models.ResourceRid]
    """The RIDs of the hidden resources that cannot be trashed."""


@dataclass
class TrashingHiddenResourcesNotSupported(errors.BadRequestError):
    name: typing.Literal["TrashingHiddenResourcesNotSupported"]
    parameters: TrashingHiddenResourcesNotSupportedParameters
    error_instance_id: str


class TrashingHomeFoldersNotSupportedParameters(typing_extensions.TypedDict):
    """Home folders cannot be trashed. Home folders are created and managed by the platform."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    resourceRids: typing.List[filesystem_models.ResourceRid]
    """The RIDs of the home folders that cannot be trashed."""


@dataclass
class TrashingHomeFoldersNotSupported(errors.BadRequestError):
    name: typing.Literal["TrashingHomeFoldersNotSupported"]
    parameters: TrashingHomeFoldersNotSupportedParameters
    error_instance_id: str


class TrashingRootFolderNotSupportedParameters(typing_extensions.TypedDict):
    """The root folder cannot be trashed."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class TrashingRootFolderNotSupported(errors.BadRequestError):
    name: typing.Literal["TrashingRootFolderNotSupported"]
    parameters: TrashingRootFolderNotSupportedParameters
    error_instance_id: str


class TrashingSpacesNotSupportedParameters(typing_extensions.TypedDict):
    """Space trashing has been disabled."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    spaceRids: typing.List[filesystem_models.SpaceRid]
    """The RIDs of the spaces that cannot be trashed."""


@dataclass
class TrashingSpacesNotSupported(errors.BadRequestError):
    name: typing.Literal["TrashingSpacesNotSupported"]
    parameters: TrashingSpacesNotSupportedParameters
    error_instance_id: str


__all__ = [
    "CreateFolderOutsideProjectNotSupported",
    "CreateFolderPermissionDenied",
    "DeleteFolderPermissionDenied",
    "DeleteOntologyResourcePermissionDenied",
    "DeleteProjectPermissionDenied",
    "DeleteResourcePermissionDenied",
    "DeleteServiceSpaceNotSupported",
    "DeleteSpacePermissionDenied",
    "DeleteUserSpaceNotSupported",
    "FolderNotFound",
    "FoldersNotFound",
    "GetResourceTimedOut",
    "GetRootFolderNotSupported",
    "InvalidDisplayName",
    "InvalidDisplayNameOnRestore",
    "InvalidFolders",
    "InvalidParentFolder",
    "InvalidPath",
    "InvalidProjects",
    "InvalidSpaces",
    "ListSpacesTimedOut",
    "MissingDisplayName",
    "ParentFolderNotFound",
    "PathNotFound",
    "ProjectNotFound",
    "ProjectsNotFound",
    "ResourceDisplayNameAlreadyExists",
    "ResourceNotDirectlyTrashed",
    "ResourceNotFound",
    "ResourceRegisteredForDeletion",
    "RestoreOntologyResourcePermissionDenied",
    "RestoreResourcePermissionDenied",
    "SpaceNotFound",
    "SpacesNotFound",
    "TrashingAutosavedResourcesNotSupported",
    "TrashingHiddenResourcesNotSupported",
    "TrashingHomeFoldersNotSupported",
    "TrashingRootFolderNotSupported",
    "TrashingSpacesNotSupported",
]
