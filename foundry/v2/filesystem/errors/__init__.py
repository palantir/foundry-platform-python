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


from foundry.v2.filesystem.errors._add_group_to_parent_group_permission_denied import (
    AddGroupToParentGroupPermissionDenied,
)  # NOQA
from foundry.v2.filesystem.errors._add_markings_permission_denied import (
    AddMarkingsPermissionDenied,
)  # NOQA
from foundry.v2.filesystem.errors._add_organizations_permission_denied import (
    AddOrganizationsPermissionDenied,
)  # NOQA
from foundry.v2.filesystem.errors._add_resource_roles_permission_denied import (
    AddResourceRolesPermissionDenied,
)  # NOQA
from foundry.v2.filesystem.errors._create_folder_outside_project_not_supported import (
    CreateFolderOutsideProjectNotSupported,
)  # NOQA
from foundry.v2.filesystem.errors._create_folder_permission_denied import (
    CreateFolderPermissionDenied,
)  # NOQA
from foundry.v2.filesystem.errors._create_group_permission_denied import (
    CreateGroupPermissionDenied,
)  # NOQA
from foundry.v2.filesystem.errors._create_project_from_template_permission_denied import (
    CreateProjectFromTemplatePermissionDenied,
)  # NOQA
from foundry.v2.filesystem.errors._create_project_no_owner_like_role_grant import (
    CreateProjectNoOwnerLikeRoleGrant,
)  # NOQA
from foundry.v2.filesystem.errors._create_project_permission_denied import (
    CreateProjectPermissionDenied,
)  # NOQA
from foundry.v2.filesystem.errors._default_roles_not_in_space_role_set import (
    DefaultRolesNotInSpaceRoleSet,
)  # NOQA
from foundry.v2.filesystem.errors._delete_resource_permission_denied import (
    DeleteResourcePermissionDenied,
)  # NOQA
from foundry.v2.filesystem.errors._folder_not_found import FolderNotFound
from foundry.v2.filesystem.errors._forbidden_operation_on_autosaved_resource import (
    ForbiddenOperationOnAutosavedResource,
)  # NOQA
from foundry.v2.filesystem.errors._forbidden_operation_on_hidden_resource import (
    ForbiddenOperationOnHiddenResource,
)  # NOQA
from foundry.v2.filesystem.errors._get_access_requirements_permission_denied import (
    GetAccessRequirementsPermissionDenied,
)  # NOQA
from foundry.v2.filesystem.errors._get_by_path_permission_denied import (
    GetByPathPermissionDenied,
)  # NOQA
from foundry.v2.filesystem.errors._get_root_folder_not_supported import (
    GetRootFolderNotSupported,
)  # NOQA
from foundry.v2.filesystem.errors._get_space_resource_not_supported import (
    GetSpaceResourceNotSupported,
)  # NOQA
from foundry.v2.filesystem.errors._invalid_default_roles import InvalidDefaultRoles
from foundry.v2.filesystem.errors._invalid_description import InvalidDescription
from foundry.v2.filesystem.errors._invalid_display_name import InvalidDisplayName
from foundry.v2.filesystem.errors._invalid_folder import InvalidFolder
from foundry.v2.filesystem.errors._invalid_organization_hierarchy import (
    InvalidOrganizationHierarchy,
)  # NOQA
from foundry.v2.filesystem.errors._invalid_organizations import InvalidOrganizations
from foundry.v2.filesystem.errors._invalid_path import InvalidPath
from foundry.v2.filesystem.errors._invalid_principal_ids_for_group_template import (
    InvalidPrincipalIdsForGroupTemplate,
)  # NOQA
from foundry.v2.filesystem.errors._invalid_role_ids import InvalidRoleIds
from foundry.v2.filesystem.errors._invalid_variable import InvalidVariable
from foundry.v2.filesystem.errors._invalid_variable_enum_option import (
    InvalidVariableEnumOption,
)  # NOQA
from foundry.v2.filesystem.errors._marking_not_found import MarkingNotFound
from foundry.v2.filesystem.errors._missing_display_name import MissingDisplayName
from foundry.v2.filesystem.errors._missing_variable_value import MissingVariableValue
from foundry.v2.filesystem.errors._not_authorized_to_apply_organization import (
    NotAuthorizedToApplyOrganization,
)  # NOQA
from foundry.v2.filesystem.errors._organization_cannot_be_removed import (
    OrganizationCannotBeRemoved,
)  # NOQA
from foundry.v2.filesystem.errors._organization_marking_not_on_space import (
    OrganizationMarkingNotOnSpace,
)  # NOQA
from foundry.v2.filesystem.errors._organization_marking_not_supported import (
    OrganizationMarkingNotSupported,
)  # NOQA
from foundry.v2.filesystem.errors._organizations_not_found import OrganizationsNotFound
from foundry.v2.filesystem.errors._path_not_found import PathNotFound
from foundry.v2.filesystem.errors._permanently_delete_resource_permission_denied import (
    PermanentlyDeleteResourcePermissionDenied,
)  # NOQA
from foundry.v2.filesystem.errors._project_creation_not_supported import (
    ProjectCreationNotSupported,
)  # NOQA
from foundry.v2.filesystem.errors._project_name_already_exists import (
    ProjectNameAlreadyExists,
)  # NOQA
from foundry.v2.filesystem.errors._project_not_found import ProjectNotFound
from foundry.v2.filesystem.errors._project_template_not_found import ProjectTemplateNotFound  # NOQA
from foundry.v2.filesystem.errors._remove_markings_permission_denied import (
    RemoveMarkingsPermissionDenied,
)  # NOQA
from foundry.v2.filesystem.errors._remove_organizations_permission_denied import (
    RemoveOrganizationsPermissionDenied,
)  # NOQA
from foundry.v2.filesystem.errors._remove_resource_roles_permission_denied import (
    RemoveResourceRolesPermissionDenied,
)  # NOQA
from foundry.v2.filesystem.errors._resource_name_already_exists import (
    ResourceNameAlreadyExists,
)  # NOQA
from foundry.v2.filesystem.errors._resource_not_directly_trashed import (
    ResourceNotDirectlyTrashed,
)  # NOQA
from foundry.v2.filesystem.errors._resource_not_found import ResourceNotFound
from foundry.v2.filesystem.errors._resource_not_trashed import ResourceNotTrashed
from foundry.v2.filesystem.errors._restore_resource_permission_denied import (
    RestoreResourcePermissionDenied,
)  # NOQA
from foundry.v2.filesystem.errors._space_not_found import SpaceNotFound
from foundry.v2.filesystem.errors._template_group_name_conflict import (
    TemplateGroupNameConflict,
)  # NOQA
from foundry.v2.filesystem.errors._template_marking_name_conflict import (
    TemplateMarkingNameConflict,
)  # NOQA
from foundry.v2.filesystem.errors._trashing_autosaved_resources_not_supported import (
    TrashingAutosavedResourcesNotSupported,
)  # NOQA
from foundry.v2.filesystem.errors._trashing_hidden_resources_not_supported import (
    TrashingHiddenResourcesNotSupported,
)  # NOQA
from foundry.v2.filesystem.errors._trashing_space_not_supported import (
    TrashingSpaceNotSupported,
)  # NOQA

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
