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


from foundry.v2.admin.errors._add_group_members_permission_denied import (
    AddGroupMembersPermissionDenied,
)  # NOQA
from foundry.v2.admin.errors._add_marking_members_permission_denied import (
    AddMarkingMembersPermissionDenied,
)  # NOQA
from foundry.v2.admin.errors._add_marking_role_assignments_permission_denied import (
    AddMarkingRoleAssignmentsPermissionDenied,
)  # NOQA
from foundry.v2.admin.errors._authentication_provider_not_found import (
    AuthenticationProviderNotFound,
)  # NOQA
from foundry.v2.admin.errors._cannot_replace_provider_info_for_principal_in_protected_realm import (
    CannotReplaceProviderInfoForPrincipalInProtectedRealm,
)  # NOQA
from foundry.v2.admin.errors._create_group_permission_denied import (
    CreateGroupPermissionDenied,
)  # NOQA
from foundry.v2.admin.errors._create_marking_missing_initial_admin_role import (
    CreateMarkingMissingInitialAdminRole,
)  # NOQA
from foundry.v2.admin.errors._create_marking_name_in_category_already_exists import (
    CreateMarkingNameInCategoryAlreadyExists,
)  # NOQA
from foundry.v2.admin.errors._create_marking_permission_denied import (
    CreateMarkingPermissionDenied,
)  # NOQA
from foundry.v2.admin.errors._delete_group_permission_denied import (
    DeleteGroupPermissionDenied,
)  # NOQA
from foundry.v2.admin.errors._delete_user_permission_denied import (
    DeleteUserPermissionDenied,
)  # NOQA
from foundry.v2.admin.errors._enrollment_not_found import EnrollmentNotFound
from foundry.v2.admin.errors._get_current_enrollment_permission_denied import (
    GetCurrentEnrollmentPermissionDenied,
)  # NOQA
from foundry.v2.admin.errors._get_current_user_permission_denied import (
    GetCurrentUserPermissionDenied,
)  # NOQA
from foundry.v2.admin.errors._get_group_provider_info_permission_denied import (
    GetGroupProviderInfoPermissionDenied,
)  # NOQA
from foundry.v2.admin.errors._get_marking_category_permission_denied import (
    GetMarkingCategoryPermissionDenied,
)  # NOQA
from foundry.v2.admin.errors._get_marking_permission_denied import (
    GetMarkingPermissionDenied,
)  # NOQA
from foundry.v2.admin.errors._get_markings_user_permission_denied import (
    GetMarkingsUserPermissionDenied,
)  # NOQA
from foundry.v2.admin.errors._get_profile_picture_of_user_permission_denied import (
    GetProfilePictureOfUserPermissionDenied,
)  # NOQA
from foundry.v2.admin.errors._get_user_provider_info_permission_denied import (
    GetUserProviderInfoPermissionDenied,
)  # NOQA
from foundry.v2.admin.errors._group_name_already_exists import GroupNameAlreadyExists
from foundry.v2.admin.errors._group_not_found import GroupNotFound
from foundry.v2.admin.errors._group_provider_info_not_found import GroupProviderInfoNotFound  # NOQA
from foundry.v2.admin.errors._invalid_group_membership_expiration import (
    InvalidGroupMembershipExpiration,
)  # NOQA
from foundry.v2.admin.errors._invalid_group_organizations import InvalidGroupOrganizations  # NOQA
from foundry.v2.admin.errors._invalid_host_name import InvalidHostName
from foundry.v2.admin.errors._invalid_profile_picture import InvalidProfilePicture
from foundry.v2.admin.errors._list_hosts_permission_denied import ListHostsPermissionDenied  # NOQA
from foundry.v2.admin.errors._list_marking_members_permission_denied import (
    ListMarkingMembersPermissionDenied,
)  # NOQA
from foundry.v2.admin.errors._list_marking_role_assignments_permission_denied import (
    ListMarkingRoleAssignmentsPermissionDenied,
)  # NOQA
from foundry.v2.admin.errors._marking_category_not_found import MarkingCategoryNotFound
from foundry.v2.admin.errors._marking_not_found import MarkingNotFound
from foundry.v2.admin.errors._organization_not_found import OrganizationNotFound
from foundry.v2.admin.errors._preregister_group_permission_denied import (
    PreregisterGroupPermissionDenied,
)  # NOQA
from foundry.v2.admin.errors._preregister_user_permission_denied import (
    PreregisterUserPermissionDenied,
)  # NOQA
from foundry.v2.admin.errors._principal_not_found import PrincipalNotFound
from foundry.v2.admin.errors._profile_picture_not_found import ProfilePictureNotFound
from foundry.v2.admin.errors._remove_group_members_permission_denied import (
    RemoveGroupMembersPermissionDenied,
)  # NOQA
from foundry.v2.admin.errors._remove_marking_members_permission_denied import (
    RemoveMarkingMembersPermissionDenied,
)  # NOQA
from foundry.v2.admin.errors._remove_marking_role_assignments_permission_denied import (
    RemoveMarkingRoleAssignmentsPermissionDenied,
)  # NOQA
from foundry.v2.admin.errors._remove_marking_role_assignments_remove_all_administrators_not_allowed import (
    RemoveMarkingRoleAssignmentsRemoveAllAdministratorsNotAllowed,
)  # NOQA
from foundry.v2.admin.errors._replace_group_provider_info_permission_denied import (
    ReplaceGroupProviderInfoPermissionDenied,
)  # NOQA
from foundry.v2.admin.errors._replace_organization_permission_denied import (
    ReplaceOrganizationPermissionDenied,
)  # NOQA
from foundry.v2.admin.errors._replace_user_provider_info_permission_denied import (
    ReplaceUserProviderInfoPermissionDenied,
)  # NOQA
from foundry.v2.admin.errors._search_groups_permission_denied import (
    SearchGroupsPermissionDenied,
)  # NOQA
from foundry.v2.admin.errors._search_users_permission_denied import (
    SearchUsersPermissionDenied,
)  # NOQA
from foundry.v2.admin.errors._user_not_found import UserNotFound
from foundry.v2.admin.errors._user_provider_info_not_found import UserProviderInfoNotFound  # NOQA

__all__ = [
    "AddGroupMembersPermissionDenied",
    "AddMarkingMembersPermissionDenied",
    "AddMarkingRoleAssignmentsPermissionDenied",
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
    "ListHostsPermissionDenied",
    "ListMarkingMembersPermissionDenied",
    "ListMarkingRoleAssignmentsPermissionDenied",
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
    "ReplaceGroupProviderInfoPermissionDenied",
    "ReplaceOrganizationPermissionDenied",
    "ReplaceUserProviderInfoPermissionDenied",
    "SearchGroupsPermissionDenied",
    "SearchUsersPermissionDenied",
    "UserNotFound",
    "UserProviderInfoNotFound",
]
