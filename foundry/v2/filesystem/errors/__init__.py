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


from foundry.v2.filesystem.errors._access_requirements_not_found import (
    AccessRequirementsNotFound,
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
from foundry.v2.filesystem.errors._get_by_path_permission_denied import (
    GetByPathPermissionDenied,
)  # NOQA
from foundry.v2.filesystem.errors._invalid_display_name import InvalidDisplayName
from foundry.v2.filesystem.errors._invalid_folder import InvalidFolder
from foundry.v2.filesystem.errors._invalid_path import InvalidPath
from foundry.v2.filesystem.errors._marking_not_found import MarkingNotFound
from foundry.v2.filesystem.errors._missing_display_name import MissingDisplayName
from foundry.v2.filesystem.errors._organization_marking_not_supported import (
    OrganizationMarkingNotSupported,
)  # NOQA
from foundry.v2.filesystem.errors._organization_not_found import OrganizationNotFound
from foundry.v2.filesystem.errors._path_not_found import PathNotFound
from foundry.v2.filesystem.errors._permanently_delete_resource_permission_denied import (
    PermanentlyDeleteResourcePermissionDenied,
)  # NOQA
from foundry.v2.filesystem.errors._project_not_found import ProjectNotFound
from foundry.v2.filesystem.errors._remove_markings_permission_denied import (
    RemoveMarkingsPermissionDenied,
)  # NOQA
from foundry.v2.filesystem.errors._remove_organizations_permission_denied import (
    RemoveOrganizationsPermissionDenied,
)  # NOQA
from foundry.v2.filesystem.errors._remove_resource_roles_permission_denied import (
    RemoveResourceRolesPermissionDenied,
)  # NOQA
from foundry.v2.filesystem.errors._resource_not_directly_trashed import (
    ResourceNotDirectlyTrashed,
)  # NOQA
from foundry.v2.filesystem.errors._resource_not_found import ResourceNotFound
from foundry.v2.filesystem.errors._resource_not_trashed import ResourceNotTrashed
from foundry.v2.filesystem.errors._restore_resource_permission_denied import (
    RestoreResourcePermissionDenied,
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
    "AccessRequirementsNotFound",
    "AddMarkingsPermissionDenied",
    "AddOrganizationsPermissionDenied",
    "AddResourceRolesPermissionDenied",
    "CreateFolderOutsideProjectNotSupported",
    "CreateFolderPermissionDenied",
    "DeleteResourcePermissionDenied",
    "FolderNotFound",
    "ForbiddenOperationOnAutosavedResource",
    "ForbiddenOperationOnHiddenResource",
    "GetByPathPermissionDenied",
    "InvalidDisplayName",
    "InvalidFolder",
    "InvalidPath",
    "MarkingNotFound",
    "MissingDisplayName",
    "OrganizationMarkingNotSupported",
    "OrganizationNotFound",
    "PathNotFound",
    "PermanentlyDeleteResourcePermissionDenied",
    "ProjectNotFound",
    "RemoveMarkingsPermissionDenied",
    "RemoveOrganizationsPermissionDenied",
    "RemoveResourceRolesPermissionDenied",
    "ResourceNotDirectlyTrashed",
    "ResourceNotFound",
    "ResourceNotTrashed",
    "RestoreResourcePermissionDenied",
    "TrashingAutosavedResourcesNotSupported",
    "TrashingHiddenResourcesNotSupported",
    "TrashingSpaceNotSupported",
]
