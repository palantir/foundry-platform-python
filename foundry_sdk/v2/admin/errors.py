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
from foundry_sdk.v2.admin import models as admin_models
from foundry_sdk.v2.core import models as core_models


class AddGroupMembersPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not add the GroupMember."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    groupId: core_models.PrincipalId


@dataclass
class AddGroupMembersPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["AddGroupMembersPermissionDenied"]
    parameters: AddGroupMembersPermissionDeniedParameters
    error_instance_id: str


class AddMarkingMembersPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not add the MarkingMember."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    markingId: core_models.MarkingId


@dataclass
class AddMarkingMembersPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["AddMarkingMembersPermissionDenied"]
    parameters: AddMarkingMembersPermissionDeniedParameters
    error_instance_id: str


class AddMarkingRoleAssignmentsPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not add the MarkingRoleAssignment."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    markingId: core_models.MarkingId


@dataclass
class AddMarkingRoleAssignmentsPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["AddMarkingRoleAssignmentsPermissionDenied"]
    parameters: AddMarkingRoleAssignmentsPermissionDeniedParameters
    error_instance_id: str


class AddOrganizationRoleAssignmentsPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not add the OrganizationRoleAssignment."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    organizationRid: core_models.OrganizationRid


@dataclass
class AddOrganizationRoleAssignmentsPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["AddOrganizationRoleAssignmentsPermissionDenied"]
    parameters: AddOrganizationRoleAssignmentsPermissionDeniedParameters
    error_instance_id: str


class AuthenticationProviderNotFoundParameters(typing_extensions.TypedDict):
    """The given AuthenticationProvider could not be found."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    enrollmentRid: core_models.EnrollmentRid
    authenticationProviderRid: admin_models.AuthenticationProviderRid


@dataclass
class AuthenticationProviderNotFound(errors.NotFoundError):
    name: typing.Literal["AuthenticationProviderNotFound"]
    parameters: AuthenticationProviderNotFoundParameters
    error_instance_id: str


class CannotReplaceProviderInfoForPrincipalInProtectedRealmParameters(typing_extensions.TypedDict):
    """Provider information for Principals in this Realm cannot be replaced."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    principalId: core_models.PrincipalId
    realm: core_models.Realm


@dataclass
class CannotReplaceProviderInfoForPrincipalInProtectedRealm(errors.BadRequestError):
    name: typing.Literal["CannotReplaceProviderInfoForPrincipalInProtectedRealm"]
    parameters: CannotReplaceProviderInfoForPrincipalInProtectedRealmParameters
    error_instance_id: str


class CreateGroupPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not create the Group."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class CreateGroupPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["CreateGroupPermissionDenied"]
    parameters: CreateGroupPermissionDeniedParameters
    error_instance_id: str


class CreateMarkingMissingInitialAdminRoleParameters(typing_extensions.TypedDict):
    """At least one ADMIN role assignment must be provided when creating a marking."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class CreateMarkingMissingInitialAdminRole(errors.BadRequestError):
    name: typing.Literal["CreateMarkingMissingInitialAdminRole"]
    parameters: CreateMarkingMissingInitialAdminRoleParameters
    error_instance_id: str


class CreateMarkingNameInCategoryAlreadyExistsParameters(typing_extensions.TypedDict):
    """A marking with the same name already exists in the category."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    displayName: str
    categoryId: admin_models.MarkingCategoryId


@dataclass
class CreateMarkingNameInCategoryAlreadyExists(errors.BadRequestError):
    name: typing.Literal["CreateMarkingNameInCategoryAlreadyExists"]
    parameters: CreateMarkingNameInCategoryAlreadyExistsParameters
    error_instance_id: str


class CreateMarkingPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not create the Marking."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class CreateMarkingPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["CreateMarkingPermissionDenied"]
    parameters: CreateMarkingPermissionDeniedParameters
    error_instance_id: str


class DeleteGroupPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not delete the Group."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    groupId: core_models.PrincipalId


@dataclass
class DeleteGroupPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["DeleteGroupPermissionDenied"]
    parameters: DeleteGroupPermissionDeniedParameters
    error_instance_id: str


class DeleteUserPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not delete the User."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    userId: core_models.PrincipalId


@dataclass
class DeleteUserPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["DeleteUserPermissionDenied"]
    parameters: DeleteUserPermissionDeniedParameters
    error_instance_id: str


class EnrollmentNotFoundParameters(typing_extensions.TypedDict):
    """The given Enrollment could not be found."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    enrollmentRid: core_models.EnrollmentRid


@dataclass
class EnrollmentNotFound(errors.NotFoundError):
    name: typing.Literal["EnrollmentNotFound"]
    parameters: EnrollmentNotFoundParameters
    error_instance_id: str


class GetCurrentEnrollmentPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not getCurrent the Enrollment."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class GetCurrentEnrollmentPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["GetCurrentEnrollmentPermissionDenied"]
    parameters: GetCurrentEnrollmentPermissionDeniedParameters
    error_instance_id: str


class GetCurrentUserPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not getCurrent the User."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class GetCurrentUserPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["GetCurrentUserPermissionDenied"]
    parameters: GetCurrentUserPermissionDeniedParameters
    error_instance_id: str


class GetGroupProviderInfoPermissionDeniedParameters(typing_extensions.TypedDict):
    """The provided token does not have permission to view the provider information for the given group."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    groupId: core_models.PrincipalId


@dataclass
class GetGroupProviderInfoPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["GetGroupProviderInfoPermissionDenied"]
    parameters: GetGroupProviderInfoPermissionDeniedParameters
    error_instance_id: str


class GetMarkingCategoryPermissionDeniedParameters(typing_extensions.TypedDict):
    """The provided token does not have permission to view the marking category."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    markingCategoryId: admin_models.MarkingCategoryId


@dataclass
class GetMarkingCategoryPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["GetMarkingCategoryPermissionDenied"]
    parameters: GetMarkingCategoryPermissionDeniedParameters
    error_instance_id: str


class GetMarkingPermissionDeniedParameters(typing_extensions.TypedDict):
    """The provided token does not have permission to view the marking."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    markingId: core_models.MarkingId


@dataclass
class GetMarkingPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["GetMarkingPermissionDenied"]
    parameters: GetMarkingPermissionDeniedParameters
    error_instance_id: str


class GetMarkingsUserPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not getMarkings the User."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    userId: core_models.PrincipalId


@dataclass
class GetMarkingsUserPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["GetMarkingsUserPermissionDenied"]
    parameters: GetMarkingsUserPermissionDeniedParameters
    error_instance_id: str


class GetProfilePictureOfUserPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not profilePicture the User."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    userId: core_models.PrincipalId


@dataclass
class GetProfilePictureOfUserPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["GetProfilePictureOfUserPermissionDenied"]
    parameters: GetProfilePictureOfUserPermissionDeniedParameters
    error_instance_id: str


class GetUserProviderInfoPermissionDeniedParameters(typing_extensions.TypedDict):
    """The provided token does not have permission to view the provider information for the given user."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    userId: core_models.PrincipalId


@dataclass
class GetUserProviderInfoPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["GetUserProviderInfoPermissionDenied"]
    parameters: GetUserProviderInfoPermissionDeniedParameters
    error_instance_id: str


class GroupNameAlreadyExistsParameters(typing_extensions.TypedDict):
    """A group with this name already exists"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    groupName: str


@dataclass
class GroupNameAlreadyExists(errors.BadRequestError):
    name: typing.Literal["GroupNameAlreadyExists"]
    parameters: GroupNameAlreadyExistsParameters
    error_instance_id: str


class GroupNotFoundParameters(typing_extensions.TypedDict):
    """The given Group could not be found."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    groupId: core_models.PrincipalId


@dataclass
class GroupNotFound(errors.NotFoundError):
    name: typing.Literal["GroupNotFound"]
    parameters: GroupNotFoundParameters
    error_instance_id: str


class GroupProviderInfoNotFoundParameters(typing_extensions.TypedDict):
    """The given GroupProviderInfo could not be found."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    groupId: core_models.PrincipalId


@dataclass
class GroupProviderInfoNotFound(errors.NotFoundError):
    name: typing.Literal["GroupProviderInfoNotFound"]
    parameters: GroupProviderInfoNotFoundParameters
    error_instance_id: str


class InvalidGroupMembershipExpirationParameters(typing_extensions.TypedDict):
    """The member expiration you provided does not conform to the Group's requirements for member expirations."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    groupId: core_models.PrincipalId
    expirationProvided: typing_extensions.NotRequired[admin_models.GroupMembershipExpiration]
    maximumDuration: typing_extensions.NotRequired[str]
    latestExpiration: typing_extensions.NotRequired[core.AwareDatetime]


@dataclass
class InvalidGroupMembershipExpiration(errors.BadRequestError):
    name: typing.Literal["InvalidGroupMembershipExpiration"]
    parameters: InvalidGroupMembershipExpirationParameters
    error_instance_id: str


class InvalidGroupOrganizationsParameters(typing_extensions.TypedDict):
    """At least one Organization RID must be provided for a group"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class InvalidGroupOrganizations(errors.BadRequestError):
    name: typing.Literal["InvalidGroupOrganizations"]
    parameters: InvalidGroupOrganizationsParameters
    error_instance_id: str


class InvalidHostNameParameters(typing_extensions.TypedDict):
    """The provided hostname must be a valid domain name. The only allowed characters are letters, numbers, periods, and hyphens."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    invalidHostName: str


@dataclass
class InvalidHostName(errors.BadRequestError):
    name: typing.Literal["InvalidHostName"]
    parameters: InvalidHostNameParameters
    error_instance_id: str


class InvalidProfilePictureParameters(typing_extensions.TypedDict):
    """The user's profile picture is not a valid image"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    userId: core_models.PrincipalId


@dataclass
class InvalidProfilePicture(errors.BadRequestError):
    name: typing.Literal["InvalidProfilePicture"]
    parameters: InvalidProfilePictureParameters
    error_instance_id: str


class ListAvailableRolesOrganizationPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not listAvailableRoles the Organization."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    organizationRid: core_models.OrganizationRid


@dataclass
class ListAvailableRolesOrganizationPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["ListAvailableRolesOrganizationPermissionDenied"]
    parameters: ListAvailableRolesOrganizationPermissionDeniedParameters
    error_instance_id: str


class ListHostsPermissionDeniedParameters(typing_extensions.TypedDict):
    """You do not have permission to list hosts for this enrollment"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    enrollmentRid: core_models.EnrollmentRid


@dataclass
class ListHostsPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["ListHostsPermissionDenied"]
    parameters: ListHostsPermissionDeniedParameters
    error_instance_id: str


class ListMarkingMembersPermissionDeniedParameters(typing_extensions.TypedDict):
    """The provided token does not have permission to list the members of this marking."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    markingId: core_models.MarkingId


@dataclass
class ListMarkingMembersPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["ListMarkingMembersPermissionDenied"]
    parameters: ListMarkingMembersPermissionDeniedParameters
    error_instance_id: str


class ListMarkingRoleAssignmentsPermissionDeniedParameters(typing_extensions.TypedDict):
    """The provided token does not have permission to list assigned roles for this marking."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    markingId: core_models.MarkingId


@dataclass
class ListMarkingRoleAssignmentsPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["ListMarkingRoleAssignmentsPermissionDenied"]
    parameters: ListMarkingRoleAssignmentsPermissionDeniedParameters
    error_instance_id: str


class ListOrganizationRoleAssignmentsPermissionDeniedParameters(typing_extensions.TypedDict):
    """The provided token does not have permission to list assigned roles for this organization."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    organizationRid: core_models.OrganizationRid


@dataclass
class ListOrganizationRoleAssignmentsPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["ListOrganizationRoleAssignmentsPermissionDenied"]
    parameters: ListOrganizationRoleAssignmentsPermissionDeniedParameters
    error_instance_id: str


class MarkingCategoryNotFoundParameters(typing_extensions.TypedDict):
    """The given MarkingCategory could not be found."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    markingCategoryId: admin_models.MarkingCategoryId


@dataclass
class MarkingCategoryNotFound(errors.NotFoundError):
    name: typing.Literal["MarkingCategoryNotFound"]
    parameters: MarkingCategoryNotFoundParameters
    error_instance_id: str


class MarkingNotFoundParameters(typing_extensions.TypedDict):
    """The given Marking could not be found."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    markingId: core_models.MarkingId


@dataclass
class MarkingNotFound(errors.NotFoundError):
    name: typing.Literal["MarkingNotFound"]
    parameters: MarkingNotFoundParameters
    error_instance_id: str


class OrganizationNotFoundParameters(typing_extensions.TypedDict):
    """The given Organization could not be found."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    organizationRid: core_models.OrganizationRid


@dataclass
class OrganizationNotFound(errors.NotFoundError):
    name: typing.Literal["OrganizationNotFound"]
    parameters: OrganizationNotFoundParameters
    error_instance_id: str


class PreregisterGroupPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not preregisterGroup the AuthenticationProvider."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    enrollmentRid: core_models.EnrollmentRid
    authenticationProviderRid: admin_models.AuthenticationProviderRid


@dataclass
class PreregisterGroupPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["PreregisterGroupPermissionDenied"]
    parameters: PreregisterGroupPermissionDeniedParameters
    error_instance_id: str


class PreregisterUserPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not preregisterUser the AuthenticationProvider."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    enrollmentRid: core_models.EnrollmentRid
    authenticationProviderRid: admin_models.AuthenticationProviderRid


@dataclass
class PreregisterUserPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["PreregisterUserPermissionDenied"]
    parameters: PreregisterUserPermissionDeniedParameters
    error_instance_id: str


class PrincipalNotFoundParameters(typing_extensions.TypedDict):
    """A principal (User or Group) with the given PrincipalId could not be found"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    principalId: core_models.PrincipalId


@dataclass
class PrincipalNotFound(errors.NotFoundError):
    name: typing.Literal["PrincipalNotFound"]
    parameters: PrincipalNotFoundParameters
    error_instance_id: str


class ProfilePictureNotFoundParameters(typing_extensions.TypedDict):
    """The user has not set a profile picture"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    userId: core_models.PrincipalId


@dataclass
class ProfilePictureNotFound(errors.NotFoundError):
    name: typing.Literal["ProfilePictureNotFound"]
    parameters: ProfilePictureNotFoundParameters
    error_instance_id: str


class RemoveGroupMembersPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not remove the GroupMember."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    groupId: core_models.PrincipalId


@dataclass
class RemoveGroupMembersPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["RemoveGroupMembersPermissionDenied"]
    parameters: RemoveGroupMembersPermissionDeniedParameters
    error_instance_id: str


class RemoveMarkingMembersPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not remove the MarkingMember."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    markingId: core_models.MarkingId


@dataclass
class RemoveMarkingMembersPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["RemoveMarkingMembersPermissionDenied"]
    parameters: RemoveMarkingMembersPermissionDeniedParameters
    error_instance_id: str


class RemoveMarkingRoleAssignmentsPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not remove the MarkingRoleAssignment."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    markingId: core_models.MarkingId


@dataclass
class RemoveMarkingRoleAssignmentsPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["RemoveMarkingRoleAssignmentsPermissionDenied"]
    parameters: RemoveMarkingRoleAssignmentsPermissionDeniedParameters
    error_instance_id: str


class RemoveMarkingRoleAssignmentsRemoveAllAdministratorsNotAllowedParameters(
    typing_extensions.TypedDict
):
    """You cannot remove all administrators from a marking."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    markingId: core_models.MarkingId
    currentAdministrators: typing.List[core_models.PrincipalId]


@dataclass
class RemoveMarkingRoleAssignmentsRemoveAllAdministratorsNotAllowed(errors.BadRequestError):
    name: typing.Literal["RemoveMarkingRoleAssignmentsRemoveAllAdministratorsNotAllowed"]
    parameters: RemoveMarkingRoleAssignmentsRemoveAllAdministratorsNotAllowedParameters
    error_instance_id: str


class RemoveOrganizationRoleAssignmentsPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not remove the OrganizationRoleAssignment."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    organizationRid: core_models.OrganizationRid


@dataclass
class RemoveOrganizationRoleAssignmentsPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["RemoveOrganizationRoleAssignmentsPermissionDenied"]
    parameters: RemoveOrganizationRoleAssignmentsPermissionDeniedParameters
    error_instance_id: str


class ReplaceGroupProviderInfoPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not replace the GroupProviderInfo."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    groupId: core_models.PrincipalId


@dataclass
class ReplaceGroupProviderInfoPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["ReplaceGroupProviderInfoPermissionDenied"]
    parameters: ReplaceGroupProviderInfoPermissionDeniedParameters
    error_instance_id: str


class ReplaceOrganizationPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not replace the Organization."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    organizationRid: core_models.OrganizationRid


@dataclass
class ReplaceOrganizationPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["ReplaceOrganizationPermissionDenied"]
    parameters: ReplaceOrganizationPermissionDeniedParameters
    error_instance_id: str


class ReplaceUserProviderInfoPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not replace the UserProviderInfo."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    userId: core_models.PrincipalId


@dataclass
class ReplaceUserProviderInfoPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["ReplaceUserProviderInfoPermissionDenied"]
    parameters: ReplaceUserProviderInfoPermissionDeniedParameters
    error_instance_id: str


class RevokeAllTokensUserPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not revokeAllTokens the User."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    userId: core_models.PrincipalId


@dataclass
class RevokeAllTokensUserPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["RevokeAllTokensUserPermissionDenied"]
    parameters: RevokeAllTokensUserPermissionDeniedParameters
    error_instance_id: str


class RoleNotFoundParameters(typing_extensions.TypedDict):
    """The given Role could not be found."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    roleId: core_models.RoleId


@dataclass
class RoleNotFound(errors.NotFoundError):
    name: typing.Literal["RoleNotFound"]
    parameters: RoleNotFoundParameters
    error_instance_id: str


class SearchGroupsPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not search the Group."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class SearchGroupsPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["SearchGroupsPermissionDenied"]
    parameters: SearchGroupsPermissionDeniedParameters
    error_instance_id: str


class SearchUsersPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not search the User."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class SearchUsersPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["SearchUsersPermissionDenied"]
    parameters: SearchUsersPermissionDeniedParameters
    error_instance_id: str


class UserNotFoundParameters(typing_extensions.TypedDict):
    """The given User could not be found."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    userId: core_models.PrincipalId


@dataclass
class UserNotFound(errors.NotFoundError):
    name: typing.Literal["UserNotFound"]
    parameters: UserNotFoundParameters
    error_instance_id: str


class UserProviderInfoNotFoundParameters(typing_extensions.TypedDict):
    """The given UserProviderInfo could not be found."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    userId: core_models.PrincipalId


@dataclass
class UserProviderInfoNotFound(errors.NotFoundError):
    name: typing.Literal["UserProviderInfoNotFound"]
    parameters: UserProviderInfoNotFoundParameters
    error_instance_id: str


__all__ = [
    "AddGroupMembersPermissionDenied",
    "AddMarkingMembersPermissionDenied",
    "AddMarkingRoleAssignmentsPermissionDenied",
    "AddOrganizationRoleAssignmentsPermissionDenied",
    "AuthenticationProviderNotFound",
    "CannotReplaceProviderInfoForPrincipalInProtectedRealm",
    "CreateGroupPermissionDenied",
    "CreateMarkingMissingInitialAdminRole",
    "CreateMarkingNameInCategoryAlreadyExists",
    "CreateMarkingPermissionDenied",
    "DeleteGroupPermissionDenied",
    "DeleteUserPermissionDenied",
    "EnrollmentNotFound",
    "GetCurrentEnrollmentPermissionDenied",
    "GetCurrentUserPermissionDenied",
    "GetGroupProviderInfoPermissionDenied",
    "GetMarkingCategoryPermissionDenied",
    "GetMarkingPermissionDenied",
    "GetMarkingsUserPermissionDenied",
    "GetProfilePictureOfUserPermissionDenied",
    "GetUserProviderInfoPermissionDenied",
    "GroupNameAlreadyExists",
    "GroupNotFound",
    "GroupProviderInfoNotFound",
    "InvalidGroupMembershipExpiration",
    "InvalidGroupOrganizations",
    "InvalidHostName",
    "InvalidProfilePicture",
    "ListAvailableRolesOrganizationPermissionDenied",
    "ListHostsPermissionDenied",
    "ListMarkingMembersPermissionDenied",
    "ListMarkingRoleAssignmentsPermissionDenied",
    "ListOrganizationRoleAssignmentsPermissionDenied",
    "MarkingCategoryNotFound",
    "MarkingNotFound",
    "OrganizationNotFound",
    "PreregisterGroupPermissionDenied",
    "PreregisterUserPermissionDenied",
    "PrincipalNotFound",
    "ProfilePictureNotFound",
    "RemoveGroupMembersPermissionDenied",
    "RemoveMarkingMembersPermissionDenied",
    "RemoveMarkingRoleAssignmentsPermissionDenied",
    "RemoveMarkingRoleAssignmentsRemoveAllAdministratorsNotAllowed",
    "RemoveOrganizationRoleAssignmentsPermissionDenied",
    "ReplaceGroupProviderInfoPermissionDenied",
    "ReplaceOrganizationPermissionDenied",
    "ReplaceUserProviderInfoPermissionDenied",
    "RevokeAllTokensUserPermissionDenied",
    "RoleNotFound",
    "SearchGroupsPermissionDenied",
    "SearchUsersPermissionDenied",
    "UserNotFound",
    "UserProviderInfoNotFound",
]
