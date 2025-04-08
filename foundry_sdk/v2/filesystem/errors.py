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
from foundry_sdk.v2.filesystem import models as filesystem_models


class AddGroupToParentGroupPermissionDeniedParameters(typing_extensions.TypedDict):
    """The user is not authorized to add a a group to the parent group required to create the project from template."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    parentGroupsWithoutPermission: typing.List[core_models.GroupRid]


@dataclass
class AddGroupToParentGroupPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["AddGroupToParentGroupPermissionDenied"]
    parameters: AddGroupToParentGroupPermissionDeniedParameters
    error_instance_id: str


class AddMarkingsPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not addMarkings the Resource."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    resourceRid: filesystem_models.ResourceRid


@dataclass
class AddMarkingsPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["AddMarkingsPermissionDenied"]
    parameters: AddMarkingsPermissionDeniedParameters
    error_instance_id: str


class AddOrganizationsPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not addOrganizations the Project."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    projectRid: filesystem_models.ProjectRid


@dataclass
class AddOrganizationsPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["AddOrganizationsPermissionDenied"]
    parameters: AddOrganizationsPermissionDeniedParameters
    error_instance_id: str


class AddResourceRolesPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not add the ResourceRole."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    resourceRid: filesystem_models.ResourceRid


@dataclass
class AddResourceRolesPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["AddResourceRolesPermissionDenied"]
    parameters: AddResourceRolesPermissionDeniedParameters
    error_instance_id: str


class CreateFolderOutsideProjectNotSupportedParameters(typing_extensions.TypedDict):
    """The given Resource is not a folder."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    parentFolderRid: filesystem_models.FolderRid


@dataclass
class CreateFolderOutsideProjectNotSupported(errors.BadRequestError):
    name: typing.Literal["CreateFolderOutsideProjectNotSupported"]
    parameters: CreateFolderOutsideProjectNotSupportedParameters
    error_instance_id: str


class CreateFolderPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not create the Folder."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class CreateFolderPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["CreateFolderPermissionDenied"]
    parameters: CreateFolderPermissionDeniedParameters
    error_instance_id: str


class CreateGroupPermissionDeniedParameters(typing_extensions.TypedDict):
    """The user is not authorized to create the group in the organization required to create the project from template."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    organizationsWithoutPermission: typing.List[core_models.OrganizationRid]


@dataclass
class CreateGroupPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["CreateGroupPermissionDenied"]
    parameters: CreateGroupPermissionDeniedParameters
    error_instance_id: str


class CreateProjectFromTemplatePermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not createFromTemplate the Project."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class CreateProjectFromTemplatePermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["CreateProjectFromTemplatePermissionDenied"]
    parameters: CreateProjectFromTemplatePermissionDeniedParameters
    error_instance_id: str


class CreateProjectNoOwnerLikeRoleGrantParameters(typing_extensions.TypedDict):
    """The create project request would create a project with no principal being granted an owner-like role. As a result, there would be no user with administrative privileges over the project. A role is defined to be owner-like if it has the `compass:edit-project` operation. In the common case of the default role-set, this is just the `compass:manage` role."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    grantedRoleIds: typing.List[core_models.RoleId]
    roleSetOwnerLikeRoleIds: typing.List[core_models.RoleId]


@dataclass
class CreateProjectNoOwnerLikeRoleGrant(errors.BadRequestError):
    name: typing.Literal["CreateProjectNoOwnerLikeRoleGrant"]
    parameters: CreateProjectNoOwnerLikeRoleGrantParameters
    error_instance_id: str


class CreateProjectPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not create the Project."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class CreateProjectPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["CreateProjectPermissionDenied"]
    parameters: CreateProjectPermissionDeniedParameters
    error_instance_id: str


class DefaultRolesNotInSpaceRoleSetParameters(typing_extensions.TypedDict):
    """The requested default roles are not in the role set of the space for the project template."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class DefaultRolesNotInSpaceRoleSet(errors.BadRequestError):
    name: typing.Literal["DefaultRolesNotInSpaceRoleSet"]
    parameters: DefaultRolesNotInSpaceRoleSetParameters
    error_instance_id: str


class DeleteResourcePermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not delete the Resource."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    resourceRid: filesystem_models.ResourceRid


@dataclass
class DeleteResourcePermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["DeleteResourcePermissionDenied"]
    parameters: DeleteResourcePermissionDeniedParameters
    error_instance_id: str


class FolderNotFoundParameters(typing_extensions.TypedDict):
    """The given Folder could not be found."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    folderRid: filesystem_models.FolderRid


@dataclass
class FolderNotFound(errors.NotFoundError):
    name: typing.Literal["FolderNotFound"]
    parameters: FolderNotFoundParameters
    error_instance_id: str


class ForbiddenOperationOnAutosavedResourceParameters(typing_extensions.TypedDict):
    """Performing this operation on an autosaved resource is not supported."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    resourceRid: filesystem_models.ResourceRid


@dataclass
class ForbiddenOperationOnAutosavedResource(errors.BadRequestError):
    name: typing.Literal["ForbiddenOperationOnAutosavedResource"]
    parameters: ForbiddenOperationOnAutosavedResourceParameters
    error_instance_id: str


class ForbiddenOperationOnHiddenResourceParameters(typing_extensions.TypedDict):
    """Performing this operation on a hidden resource is not supported."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    resourceRid: filesystem_models.ResourceRid


@dataclass
class ForbiddenOperationOnHiddenResource(errors.BadRequestError):
    name: typing.Literal["ForbiddenOperationOnHiddenResource"]
    parameters: ForbiddenOperationOnHiddenResourceParameters
    error_instance_id: str


class GetAccessRequirementsPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not getAccessRequirements the Resource."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    resourceRid: filesystem_models.ResourceRid


@dataclass
class GetAccessRequirementsPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["GetAccessRequirementsPermissionDenied"]
    parameters: GetAccessRequirementsPermissionDeniedParameters
    error_instance_id: str


class GetByPathPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not getByPath the Resource."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class GetByPathPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["GetByPathPermissionDenied"]
    parameters: GetByPathPermissionDeniedParameters
    error_instance_id: str


class GetRootFolderNotSupportedParameters(typing_extensions.TypedDict):
    """Getting the root folder as a resource is not supported."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class GetRootFolderNotSupported(errors.BadRequestError):
    name: typing.Literal["GetRootFolderNotSupported"]
    parameters: GetRootFolderNotSupportedParameters
    error_instance_id: str


class GetSpaceResourceNotSupportedParameters(typing_extensions.TypedDict):
    """Getting a space as a resource is not supported."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    spaceRid: filesystem_models.SpaceRid


@dataclass
class GetSpaceResourceNotSupported(errors.BadRequestError):
    name: typing.Literal["GetSpaceResourceNotSupported"]
    parameters: GetSpaceResourceNotSupportedParameters
    error_instance_id: str


class InvalidDefaultRolesParameters(typing_extensions.TypedDict):
    """Either the user has not passed default roles for a template with suggested default roles, or has passed default roles for a template with fixed default roles."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class InvalidDefaultRoles(errors.BadRequestError):
    name: typing.Literal["InvalidDefaultRoles"]
    parameters: InvalidDefaultRolesParameters
    error_instance_id: str


class InvalidDescriptionParameters(typing_extensions.TypedDict):
    """Either the user has not passed a value for a template with unset project description, or has passed a value for a template with fixed project description."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class InvalidDescription(errors.BadRequestError):
    name: typing.Literal["InvalidDescription"]
    parameters: InvalidDescriptionParameters
    error_instance_id: str


class InvalidDisplayNameParameters(typing_extensions.TypedDict):
    """
    The display name of a Resource should not be exactly `.` or `..`, contain a forward slash `/` or be
    too long.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    displayName: filesystem_models.ResourceDisplayName


@dataclass
class InvalidDisplayName(errors.BadRequestError):
    name: typing.Literal["InvalidDisplayName"]
    parameters: InvalidDisplayNameParameters
    error_instance_id: str


class InvalidFolderParameters(typing_extensions.TypedDict):
    """The given Resource is not a Folder."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    resourceRid: filesystem_models.ResourceRid


@dataclass
class InvalidFolder(errors.BadRequestError):
    name: typing.Literal["InvalidFolder"]
    parameters: InvalidFolderParameters
    error_instance_id: str


class InvalidOrganizationHierarchyParameters(typing_extensions.TypedDict):
    """
    Organizations on a project must also exist on the parent space. This error is thrown if the configuration
    of a project's organizations (on creation or subsequently) results in the project being marked with either
    no organizations in a marked space, or with an organization that is not present on the parent space.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    organizationRids: typing.List[core_models.OrganizationRid]


@dataclass
class InvalidOrganizationHierarchy(errors.BadRequestError):
    name: typing.Literal["InvalidOrganizationHierarchy"]
    parameters: InvalidOrganizationHierarchyParameters
    error_instance_id: str


class InvalidOrganizationsParameters(typing_extensions.TypedDict):
    """Either the user has not passed organizations for a template with suggested organizations, or has passed organization for a template with fixed organizations."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class InvalidOrganizations(errors.BadRequestError):
    name: typing.Literal["InvalidOrganizations"]
    parameters: InvalidOrganizationsParameters
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


class InvalidPrincipalIdsForGroupTemplateParameters(typing_extensions.TypedDict):
    """The template requested for project creation contains principal IDs that do not exist."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    invalidPrincipalIds: typing.List[core_models.PrincipalId]


@dataclass
class InvalidPrincipalIdsForGroupTemplate(errors.BadRequestError):
    name: typing.Literal["InvalidPrincipalIdsForGroupTemplate"]
    parameters: InvalidPrincipalIdsForGroupTemplateParameters
    error_instance_id: str


class InvalidRoleIdsParameters(typing_extensions.TypedDict):
    """A roleId referenced in either default roles or role grants does not exist in the project role set for the space."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    requestedRoleIds: typing.List[core_models.RoleId]
    """All referenced role ids in the create project request."""


@dataclass
class InvalidRoleIds(errors.BadRequestError):
    name: typing.Literal["InvalidRoleIds"]
    parameters: InvalidRoleIdsParameters
    error_instance_id: str


class InvalidVariableParameters(typing_extensions.TypedDict):
    """A variable referenced in the request to create project from template is not defined on the template."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    templateVariableId: str


@dataclass
class InvalidVariable(errors.BadRequestError):
    name: typing.Literal["InvalidVariable"]
    parameters: InvalidVariableParameters
    error_instance_id: str


class InvalidVariableEnumOptionParameters(typing_extensions.TypedDict):
    """The value passed in the request to create project from template for an enum type variable is not a valid option."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    variableId: str
    invalidOption: str
    validOptions: typing.List[str]


@dataclass
class InvalidVariableEnumOption(errors.BadRequestError):
    name: typing.Literal["InvalidVariableEnumOption"]
    parameters: InvalidVariableEnumOptionParameters
    error_instance_id: str


class MarkingNotFoundParameters(typing_extensions.TypedDict):
    """A provided marking ID cannot be found."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    markingIds: typing.List[core_models.MarkingId]


@dataclass
class MarkingNotFound(errors.NotFoundError):
    name: typing.Literal["MarkingNotFound"]
    parameters: MarkingNotFoundParameters
    error_instance_id: str


class MissingDisplayNameParameters(typing_extensions.TypedDict):
    """A Display Name must be provided."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class MissingDisplayName(errors.BadRequestError):
    name: typing.Literal["MissingDisplayName"]
    parameters: MissingDisplayNameParameters
    error_instance_id: str


class MissingVariableValueParameters(typing_extensions.TypedDict):
    """A variable defined on the template requested for project creation does not have a value set in the request."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    templateVariableId: str


@dataclass
class MissingVariableValue(errors.BadRequestError):
    name: typing.Literal["MissingVariableValue"]
    parameters: MissingVariableValueParameters
    error_instance_id: str


class NotAuthorizedToApplyOrganizationParameters(typing_extensions.TypedDict):
    """The user is not authorized to apply at least one of the organization markings required to create the project from template."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    organizationRids: typing.List[core_models.OrganizationRid]


@dataclass
class NotAuthorizedToApplyOrganization(errors.BadRequestError):
    name: typing.Literal["NotAuthorizedToApplyOrganization"]
    parameters: NotAuthorizedToApplyOrganizationParameters
    error_instance_id: str


class OrganizationCannotBeRemovedParameters(typing_extensions.TypedDict):
    """
    An organization cannot be removed from a project if it would result in a project with no organizations
    under a space marked with an organization.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    organizationRids: typing.List[core_models.OrganizationRid]


@dataclass
class OrganizationCannotBeRemoved(errors.BadRequestError):
    name: typing.Literal["OrganizationCannotBeRemoved"]
    parameters: OrganizationCannotBeRemovedParameters
    error_instance_id: str


class OrganizationMarkingNotOnSpaceParameters(typing_extensions.TypedDict):
    """At least one of the organization markings associated with a passed organization is not applied on the requested space."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    spaceRid: filesystem_models.SpaceRid
    organizationRids: typing.List[core_models.OrganizationRid]


@dataclass
class OrganizationMarkingNotOnSpace(errors.BadRequestError):
    name: typing.Literal["OrganizationMarkingNotOnSpace"]
    parameters: OrganizationMarkingNotOnSpaceParameters
    error_instance_id: str


class OrganizationMarkingNotSupportedParameters(typing_extensions.TypedDict):
    """
    Adding an organization marking as a regular marking is not supported. Use the organization endpoints on a
    project resource instead.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    markingIds: typing.List[core_models.MarkingId]


@dataclass
class OrganizationMarkingNotSupported(errors.BadRequestError):
    name: typing.Literal["OrganizationMarkingNotSupported"]
    parameters: OrganizationMarkingNotSupportedParameters
    error_instance_id: str


class OrganizationsNotFoundParameters(typing_extensions.TypedDict):
    """At least one organization RID could not be found."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    organizationRids: typing.List[core_models.OrganizationRid]


@dataclass
class OrganizationsNotFound(errors.NotFoundError):
    name: typing.Literal["OrganizationsNotFound"]
    parameters: OrganizationsNotFoundParameters
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


class PermanentlyDeleteResourcePermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not permanentlyDelete the Resource."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    resourceRid: filesystem_models.ResourceRid


@dataclass
class PermanentlyDeleteResourcePermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["PermanentlyDeleteResourcePermissionDenied"]
    parameters: PermanentlyDeleteResourcePermissionDeniedParameters
    error_instance_id: str


class ProjectCreationNotSupportedParameters(typing_extensions.TypedDict):
    """Project creation is not supported in the current user's space."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    spaceRid: filesystem_models.SpaceRid


@dataclass
class ProjectCreationNotSupported(errors.BadRequestError):
    name: typing.Literal["ProjectCreationNotSupported"]
    parameters: ProjectCreationNotSupportedParameters
    error_instance_id: str


class ProjectNameAlreadyExistsParameters(typing_extensions.TypedDict):
    """The requested display name for the created project is already being used in the space."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    displayName: filesystem_models.ResourceDisplayName
    spaceRid: filesystem_models.SpaceRid


@dataclass
class ProjectNameAlreadyExists(errors.ConflictError):
    name: typing.Literal["ProjectNameAlreadyExists"]
    parameters: ProjectNameAlreadyExistsParameters
    error_instance_id: str


class ProjectNotFoundParameters(typing_extensions.TypedDict):
    """The given Project could not be found."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    projectRid: filesystem_models.ProjectRid


@dataclass
class ProjectNotFound(errors.NotFoundError):
    name: typing.Literal["ProjectNotFound"]
    parameters: ProjectNotFoundParameters
    error_instance_id: str


class ProjectTemplateNotFoundParameters(typing_extensions.TypedDict):
    """The project template RID referenced cannot be found."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    projectTemplateRid: filesystem_models.ProjectTemplateRid


@dataclass
class ProjectTemplateNotFound(errors.NotFoundError):
    name: typing.Literal["ProjectTemplateNotFound"]
    parameters: ProjectTemplateNotFoundParameters
    error_instance_id: str


class RemoveMarkingsPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not removeMarkings the Resource."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    resourceRid: filesystem_models.ResourceRid


@dataclass
class RemoveMarkingsPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["RemoveMarkingsPermissionDenied"]
    parameters: RemoveMarkingsPermissionDeniedParameters
    error_instance_id: str


class RemoveOrganizationsPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not removeOrganizations the Project."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    projectRid: filesystem_models.ProjectRid


@dataclass
class RemoveOrganizationsPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["RemoveOrganizationsPermissionDenied"]
    parameters: RemoveOrganizationsPermissionDeniedParameters
    error_instance_id: str


class RemoveResourceRolesPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not remove the ResourceRole."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    resourceRid: filesystem_models.ResourceRid


@dataclass
class RemoveResourceRolesPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["RemoveResourceRolesPermissionDenied"]
    parameters: RemoveResourceRolesPermissionDeniedParameters
    error_instance_id: str


class ResourceNameAlreadyExistsParameters(typing_extensions.TypedDict):
    """The provided resource name is already in use by another resource in the same folder."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    parentFolderRid: filesystem_models.FolderRid
    displayName: str


@dataclass
class ResourceNameAlreadyExists(errors.ConflictError):
    name: typing.Literal["ResourceNameAlreadyExists"]
    parameters: ResourceNameAlreadyExistsParameters
    error_instance_id: str


class ResourceNotDirectlyTrashedParameters(typing_extensions.TypedDict):
    """The Resource is not directly trashed."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    resourceRid: filesystem_models.ResourceRid


@dataclass
class ResourceNotDirectlyTrashed(errors.BadRequestError):
    name: typing.Literal["ResourceNotDirectlyTrashed"]
    parameters: ResourceNotDirectlyTrashedParameters
    error_instance_id: str


class ResourceNotFoundParameters(typing_extensions.TypedDict):
    """The given Resource could not be found."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    resourceRid: filesystem_models.ResourceRid


@dataclass
class ResourceNotFound(errors.NotFoundError):
    name: typing.Literal["ResourceNotFound"]
    parameters: ResourceNotFoundParameters
    error_instance_id: str


class ResourceNotTrashedParameters(typing_extensions.TypedDict):
    """The Resource should be directly trashed before being permanently deleted."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    resourceRid: filesystem_models.ResourceRid


@dataclass
class ResourceNotTrashed(errors.BadRequestError):
    name: typing.Literal["ResourceNotTrashed"]
    parameters: ResourceNotTrashedParameters
    error_instance_id: str


class RestoreResourcePermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not restore the Resource."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    resourceRid: filesystem_models.ResourceRid


@dataclass
class RestoreResourcePermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["RestoreResourcePermissionDenied"]
    parameters: RestoreResourcePermissionDeniedParameters
    error_instance_id: str


class SpaceNotFoundParameters(typing_extensions.TypedDict):
    """The referenced space cannot be found."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    spaceRid: filesystem_models.SpaceRid


@dataclass
class SpaceNotFound(errors.NotFoundError):
    name: typing.Literal["SpaceNotFound"]
    parameters: SpaceNotFoundParameters
    error_instance_id: str


class TemplateGroupNameConflictParameters(typing_extensions.TypedDict):
    """Creating the project from template would attempt to create new groups with names conflicting either with other new groups, or existing groups."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    conflictingGroupNames: typing.List[core_models.GroupName]


@dataclass
class TemplateGroupNameConflict(errors.ConflictError):
    name: typing.Literal["TemplateGroupNameConflict"]
    parameters: TemplateGroupNameConflictParameters
    error_instance_id: str


class TemplateMarkingNameConflictParameters(typing_extensions.TypedDict):
    """Creating the project from template would attempt to create new markings with names conflicting either with other new markings, or existing markings."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    conflictingMarkingNames: typing.List[str]


@dataclass
class TemplateMarkingNameConflict(errors.ConflictError):
    name: typing.Literal["TemplateMarkingNameConflict"]
    parameters: TemplateMarkingNameConflictParameters
    error_instance_id: str


class TrashingAutosavedResourcesNotSupportedParameters(typing_extensions.TypedDict):
    """Auto-saved Resources cannot be trashed."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    resourceRid: filesystem_models.ResourceRid


@dataclass
class TrashingAutosavedResourcesNotSupported(errors.BadRequestError):
    name: typing.Literal["TrashingAutosavedResourcesNotSupported"]
    parameters: TrashingAutosavedResourcesNotSupportedParameters
    error_instance_id: str


class TrashingHiddenResourcesNotSupportedParameters(typing_extensions.TypedDict):
    """Hidden Resources cannot be trashed."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    resourceRid: filesystem_models.ResourceRid


@dataclass
class TrashingHiddenResourcesNotSupported(errors.BadRequestError):
    name: typing.Literal["TrashingHiddenResourcesNotSupported"]
    parameters: TrashingHiddenResourcesNotSupportedParameters
    error_instance_id: str


class TrashingSpaceNotSupportedParameters(typing_extensions.TypedDict):
    """Spaces cannot be trashed."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    resourceRid: filesystem_models.ResourceRid


@dataclass
class TrashingSpaceNotSupported(errors.BadRequestError):
    name: typing.Literal["TrashingSpaceNotSupported"]
    parameters: TrashingSpaceNotSupportedParameters
    error_instance_id: str


__all__ = [
    "AddGroupToParentGroupPermissionDenied",
    "AddMarkingsPermissionDenied",
    "AddOrganizationsPermissionDenied",
    "AddResourceRolesPermissionDenied",
    "CreateFolderOutsideProjectNotSupported",
    "CreateFolderPermissionDenied",
    "CreateGroupPermissionDenied",
    "CreateProjectFromTemplatePermissionDenied",
    "CreateProjectNoOwnerLikeRoleGrant",
    "CreateProjectPermissionDenied",
    "DefaultRolesNotInSpaceRoleSet",
    "DeleteResourcePermissionDenied",
    "FolderNotFound",
    "ForbiddenOperationOnAutosavedResource",
    "ForbiddenOperationOnHiddenResource",
    "GetAccessRequirementsPermissionDenied",
    "GetByPathPermissionDenied",
    "GetRootFolderNotSupported",
    "GetSpaceResourceNotSupported",
    "InvalidDefaultRoles",
    "InvalidDescription",
    "InvalidDisplayName",
    "InvalidFolder",
    "InvalidOrganizationHierarchy",
    "InvalidOrganizations",
    "InvalidPath",
    "InvalidPrincipalIdsForGroupTemplate",
    "InvalidRoleIds",
    "InvalidVariable",
    "InvalidVariableEnumOption",
    "MarkingNotFound",
    "MissingDisplayName",
    "MissingVariableValue",
    "NotAuthorizedToApplyOrganization",
    "OrganizationCannotBeRemoved",
    "OrganizationMarkingNotOnSpace",
    "OrganizationMarkingNotSupported",
    "OrganizationsNotFound",
    "PathNotFound",
    "PermanentlyDeleteResourcePermissionDenied",
    "ProjectCreationNotSupported",
    "ProjectNameAlreadyExists",
    "ProjectNotFound",
    "ProjectTemplateNotFound",
    "RemoveMarkingsPermissionDenied",
    "RemoveOrganizationsPermissionDenied",
    "RemoveResourceRolesPermissionDenied",
    "ResourceNameAlreadyExists",
    "ResourceNotDirectlyTrashed",
    "ResourceNotFound",
    "ResourceNotTrashed",
    "RestoreResourcePermissionDenied",
    "SpaceNotFound",
    "TemplateGroupNameConflict",
    "TemplateMarkingNameConflict",
    "TrashingAutosavedResourcesNotSupported",
    "TrashingHiddenResourcesNotSupported",
    "TrashingSpaceNotSupported",
]
