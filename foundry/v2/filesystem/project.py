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


from __future__ import annotations

import warnings
from functools import cached_property
from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import Union

import pydantic
from typing_extensions import Annotated
from typing_extensions import TypedDict

from foundry._core import ApiClient
from foundry._core import ApiResponse
from foundry._core import Auth
from foundry._core import Config
from foundry._core import RequestInfo
from foundry._core import ResourceIterator
from foundry._core import StreamingContextManager
from foundry._core.utils import maybe_ignore_preview
from foundry._errors import handle_unexpected
from foundry.v2.core.models._organization_rid import OrganizationRid
from foundry.v2.core.models._page_size import PageSize
from foundry.v2.core.models._page_token import PageToken
from foundry.v2.core.models._preview_mode import PreviewMode
from foundry.v2.core.models._role_id import RoleId
from foundry.v2.filesystem import errors as filesystem_errors
from foundry.v2.filesystem.models._list_organizations_of_project_response import (
    ListOrganizationsOfProjectResponse,
)  # NOQA
from foundry.v2.filesystem.models._principal_with_id import PrincipalWithId
from foundry.v2.filesystem.models._principal_with_id_dict import PrincipalWithIdDict
from foundry.v2.filesystem.models._project import Project
from foundry.v2.filesystem.models._project_rid import ProjectRid
from foundry.v2.filesystem.models._project_template_rid import ProjectTemplateRid
from foundry.v2.filesystem.models._project_template_variable_id import (
    ProjectTemplateVariableId,
)  # NOQA
from foundry.v2.filesystem.models._project_template_variable_value import (
    ProjectTemplateVariableValue,
)  # NOQA
from foundry.v2.filesystem.models._resource_display_name import ResourceDisplayName
from foundry.v2.filesystem.models._space_rid import SpaceRid


class ProjectClient:
    """
    The API client for the Project Resource.

    :param auth: Your auth configuration.
    :param hostname: Your Foundry hostname (for example, "myfoundry.palantirfoundry.com"). This can also include your API gateway service URI.
    :param config: Optionally specify the configuration for the HTTP session.
    """

    def __init__(
        self,
        auth: Auth,
        hostname: str,
        config: Optional[Config] = None,
    ):
        self._auth = auth
        self._hostname = hostname
        self._config = config
        self._api_client = ApiClient(auth=auth, hostname=hostname, config=config)
        self.with_streaming_response = _ProjectClientStreaming(
            auth=auth, hostname=hostname, config=config
        )
        self.with_raw_response = _ProjectClientRaw(auth=auth, hostname=hostname, config=config)

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def add_organizations(
        self,
        project_rid: ProjectRid,
        *,
        organization_rids: List[OrganizationRid],
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> None:
        """
        Adds a list of Organizations to a Project.
        :param project_rid: projectRid
        :type project_rid: ProjectRid
        :param organization_rids:
        :type organization_rids: List[OrganizationRid]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: None

        :raises AddOrganizationsPermissionDenied: Could not addOrganizations the Project.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/filesystem/projects/{projectRid}/addOrganizations",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "projectRid": project_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                },
                body={
                    "organizationRids": organization_rids,
                },
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "organizationRids": List[OrganizationRid],
                    },
                ),
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "AddOrganizationsPermissionDenied": filesystem_errors.AddOrganizationsPermissionDenied,
                },
            ),
        ).decode()

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def create(
        self,
        *,
        default_roles: List[RoleId],
        display_name: ResourceDisplayName,
        organization_rids: List[OrganizationRid],
        role_grants: Dict[RoleId, List[Union[PrincipalWithId, PrincipalWithIdDict]]],
        space_rid: SpaceRid,
        description: Optional[str] = None,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> Project:
        """
        Creates a new Project.

        Note that third-party applications using this endpoint via OAuth2 cannot be associated with an
        Ontology SDK as this will reduce the scope of operations to only those within specified projects.
        When creating the application, select "No, I won't use an Ontology SDK" on the Resources page.

        :param default_roles:
        :type default_roles: List[RoleId]
        :param display_name:
        :type display_name: ResourceDisplayName
        :param organization_rids:
        :type organization_rids: List[OrganizationRid]
        :param role_grants:
        :type role_grants: Dict[RoleId, List[Union[PrincipalWithId, PrincipalWithIdDict]]]
        :param space_rid:
        :type space_rid: SpaceRid
        :param description:
        :type description: Optional[str]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: Project

        :raises CreateProjectNoOwnerLikeRoleGrant: The create project request would create a project with no principal being granted an owner-like role. As a result, there would be no user with administrative privileges over the project. A role is defined to be owner-like if it has the `compass:edit-project` operation. In the common case of the default role-set, this is just the `compass:manage` role.
        :raises CreateProjectPermissionDenied: Could not create the Project.
        :raises InvalidDisplayName: The display name of a Resource should not be exactly `.` or `..`, contain a forward slash `/` or be too long.
        :raises InvalidRoleIds: A roleId referenced in either default roles or role grants does not exist in the project role set for the space.
        :raises OrganizationsNotFound: At least one organization RID could not be found.
        :raises ProjectCreationNotSupported: Project creation is not supported in the current user's space.
        :raises ProjectNameAlreadyExists: The requested display name for the created project is already being used in the space.
        :raises SpaceNotFound: The referenced space cannot be found.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/filesystem/projects/create",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "displayName": display_name,
                    "description": description,
                    "spaceRid": space_rid,
                    "roleGrants": role_grants,
                    "defaultRoles": default_roles,
                    "organizationRids": organization_rids,
                },
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "displayName": ResourceDisplayName,
                        "description": Optional[str],
                        "spaceRid": SpaceRid,
                        "roleGrants": Dict[
                            RoleId, List[Union[PrincipalWithId, PrincipalWithIdDict]]
                        ],
                        "defaultRoles": List[RoleId],
                        "organizationRids": List[OrganizationRid],
                    },
                ),
                response_type=Project,
                request_timeout=request_timeout,
                throwable_errors={
                    "CreateProjectNoOwnerLikeRoleGrant": filesystem_errors.CreateProjectNoOwnerLikeRoleGrant,
                    "CreateProjectPermissionDenied": filesystem_errors.CreateProjectPermissionDenied,
                    "InvalidDisplayName": filesystem_errors.InvalidDisplayName,
                    "InvalidRoleIds": filesystem_errors.InvalidRoleIds,
                    "OrganizationsNotFound": filesystem_errors.OrganizationsNotFound,
                    "ProjectCreationNotSupported": filesystem_errors.ProjectCreationNotSupported,
                    "ProjectNameAlreadyExists": filesystem_errors.ProjectNameAlreadyExists,
                    "SpaceNotFound": filesystem_errors.SpaceNotFound,
                },
            ),
        ).decode()

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def create_from_template(
        self,
        *,
        template_rid: ProjectTemplateRid,
        variable_values: Dict[ProjectTemplateVariableId, ProjectTemplateVariableValue],
        default_roles: Optional[List[RoleId]] = None,
        organization_rids: Optional[List[OrganizationRid]] = None,
        preview: Optional[PreviewMode] = None,
        project_description: Optional[str] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> Project:
        """
        Creates a project from a project template.
        :param template_rid:
        :type template_rid: ProjectTemplateRid
        :param variable_values:
        :type variable_values: Dict[ProjectTemplateVariableId, ProjectTemplateVariableValue]
        :param default_roles:
        :type default_roles: Optional[List[RoleId]]
        :param organization_rids:
        :type organization_rids: Optional[List[OrganizationRid]]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param project_description:
        :type project_description: Optional[str]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: Project

        :raises AddGroupToParentGroupPermissionDenied: The user is not authorized to add a a group to the parent group required to create the project from template.
        :raises CreateGroupPermissionDenied: The user is not authorized to create the group in the organization required to create the project from template.
        :raises CreateProjectFromTemplatePermissionDenied: Could not createFromTemplate the Project.
        :raises CreateProjectNoOwnerLikeRoleGrant: The create project request would create a project with no principal being granted an owner-like role. As a result, there would be no user with administrative privileges over the project. A role is defined to be owner-like if it has the `compass:edit-project` operation. In the common case of the default role-set, this is just the `compass:manage` role.
        :raises DefaultRolesNotInSpaceRoleSet: The requested default roles are not in the role set of the space for the project template.
        :raises InvalidDescription: Either the user has not passed a value for a template with unset project description, or has passed a value for a template with fixed project description.
        :raises InvalidOrganizationHierarchy: Organizations on a project must also exist on the parent space. This error is thrown if the configuration  of a project's organizations (on creation or subsequently) results in the project being marked with either  no organizations in a marked space, or with an organization that is not present on the parent space.
        :raises InvalidOrganizations: Either the user has not passed organizations for a template with suggested organizations, or has passed organization for a template with fixed organizations.
        :raises InvalidPrincipalIdsForGroupTemplate: The template requested for project creation contains principal IDs that do not exist.
        :raises InvalidVariable: A variable referenced in the request to create project from template is not defined on the template.
        :raises InvalidVariableEnumOption: The value passed in the request to create project from template for an enum type variable is not a valid option.
        :raises MissingVariableValue: A variable defined on the template requested for project creation does not have a value set in the request.
        :raises NotAuthorizedToApplyOrganization: The user is not authorized to apply at least one of the organization markings required to create the project from template.
        :raises ProjectTemplateNotFound: The project template RID referenced cannot be found.
        :raises TemplateGroupNameConflict: Creating the project from template would attempt to create new groups with names conflicting either with other new groups, or existing groups.
        :raises TemplateMarkingNameConflict: Creating the project from template would attempt to create new markings with names conflicting either with other new markings, or existing markings.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/filesystem/projects/createFromTemplate",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "templateRid": template_rid,
                    "variableValues": variable_values,
                    "defaultRoles": default_roles,
                    "organizationRids": organization_rids,
                    "projectDescription": project_description,
                },
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "templateRid": ProjectTemplateRid,
                        "variableValues": Dict[
                            ProjectTemplateVariableId, ProjectTemplateVariableValue
                        ],
                        "defaultRoles": Optional[List[RoleId]],
                        "organizationRids": Optional[List[OrganizationRid]],
                        "projectDescription": Optional[str],
                    },
                ),
                response_type=Project,
                request_timeout=request_timeout,
                throwable_errors={
                    "AddGroupToParentGroupPermissionDenied": filesystem_errors.AddGroupToParentGroupPermissionDenied,
                    "CreateGroupPermissionDenied": filesystem_errors.CreateGroupPermissionDenied,
                    "CreateProjectFromTemplatePermissionDenied": filesystem_errors.CreateProjectFromTemplatePermissionDenied,
                    "CreateProjectNoOwnerLikeRoleGrant": filesystem_errors.CreateProjectNoOwnerLikeRoleGrant,
                    "DefaultRolesNotInSpaceRoleSet": filesystem_errors.DefaultRolesNotInSpaceRoleSet,
                    "InvalidDescription": filesystem_errors.InvalidDescription,
                    "InvalidOrganizationHierarchy": filesystem_errors.InvalidOrganizationHierarchy,
                    "InvalidOrganizations": filesystem_errors.InvalidOrganizations,
                    "InvalidPrincipalIdsForGroupTemplate": filesystem_errors.InvalidPrincipalIdsForGroupTemplate,
                    "InvalidVariable": filesystem_errors.InvalidVariable,
                    "InvalidVariableEnumOption": filesystem_errors.InvalidVariableEnumOption,
                    "MissingVariableValue": filesystem_errors.MissingVariableValue,
                    "NotAuthorizedToApplyOrganization": filesystem_errors.NotAuthorizedToApplyOrganization,
                    "ProjectTemplateNotFound": filesystem_errors.ProjectTemplateNotFound,
                    "TemplateGroupNameConflict": filesystem_errors.TemplateGroupNameConflict,
                    "TemplateMarkingNameConflict": filesystem_errors.TemplateMarkingNameConflict,
                },
            ),
        ).decode()

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def get(
        self,
        project_rid: ProjectRid,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> Project:
        """
        Get the Project with the specified rid.
        :param project_rid: projectRid
        :type project_rid: ProjectRid
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: Project

        :raises ProjectNotFound: The given Project could not be found.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/filesystem/projects/{projectRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "projectRid": project_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=Project,
                request_timeout=request_timeout,
                throwable_errors={
                    "ProjectNotFound": filesystem_errors.ProjectNotFound,
                },
            ),
        ).decode()

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def organizations(
        self,
        project_rid: ProjectRid,
        *,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ResourceIterator[OrganizationRid]:
        """
        List of Organizations directly applied to a Project. The number of Organizations on a Project is
        typically small so the `pageSize` and `pageToken` parameters are not required.

        :param project_rid: projectRid
        :type project_rid: ProjectRid
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param page_token: pageToken
        :type page_token: Optional[PageToken]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ResourceIterator[OrganizationRid]
        """

        return self._api_client.iterate_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/filesystem/projects/{projectRid}/organizations",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
                    "preview": preview,
                },
                path_params={
                    "projectRid": project_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ListOrganizationsOfProjectResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def organizations_page(
        self,
        project_rid: ProjectRid,
        *,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ListOrganizationsOfProjectResponse:
        """
        List of Organizations directly applied to a Project. The number of Organizations on a Project is
        typically small so the `pageSize` and `pageToken` parameters are not required.

        :param project_rid: projectRid
        :type project_rid: ProjectRid
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param page_token: pageToken
        :type page_token: Optional[PageToken]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ListOrganizationsOfProjectResponse
        """

        warnings.warn(
            "The client.filesystem.Project.organizations_page(...) method has been deprecated. Please use client.filesystem.Project.organizations(...) instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/filesystem/projects/{projectRid}/organizations",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
                    "preview": preview,
                },
                path_params={
                    "projectRid": project_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ListOrganizationsOfProjectResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        ).decode()

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def remove_organizations(
        self,
        project_rid: ProjectRid,
        *,
        organization_rids: List[OrganizationRid],
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> None:
        """
        Removes Organizations from a Project.
        :param project_rid: projectRid
        :type project_rid: ProjectRid
        :param organization_rids:
        :type organization_rids: List[OrganizationRid]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: None

        :raises RemoveOrganizationsPermissionDenied: Could not removeOrganizations the Project.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/filesystem/projects/{projectRid}/removeOrganizations",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "projectRid": project_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                },
                body={
                    "organizationRids": organization_rids,
                },
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "organizationRids": List[OrganizationRid],
                    },
                ),
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "RemoveOrganizationsPermissionDenied": filesystem_errors.RemoveOrganizationsPermissionDenied,
                },
            ),
        ).decode()


class _ProjectClientRaw:
    """
    The API client for the Project Resource.

    :param auth: Your auth configuration.
    :param hostname: Your Foundry hostname (for example, "myfoundry.palantirfoundry.com"). This can also include your API gateway service URI.
    :param config: Optionally specify the configuration for the HTTP session.
    """

    def __init__(
        self,
        auth: Auth,
        hostname: str,
        config: Optional[Config] = None,
    ):
        self._auth = auth
        self._hostname = hostname
        self._config = config
        self._api_client = ApiClient(auth=auth, hostname=hostname, config=config)

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def add_organizations(
        self,
        project_rid: ProjectRid,
        *,
        organization_rids: List[OrganizationRid],
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[None]:
        """
        Adds a list of Organizations to a Project.
        :param project_rid: projectRid
        :type project_rid: ProjectRid
        :param organization_rids:
        :type organization_rids: List[OrganizationRid]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[None]

        :raises AddOrganizationsPermissionDenied: Could not addOrganizations the Project.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/filesystem/projects/{projectRid}/addOrganizations",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "projectRid": project_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                },
                body={
                    "organizationRids": organization_rids,
                },
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "organizationRids": List[OrganizationRid],
                    },
                ),
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "AddOrganizationsPermissionDenied": filesystem_errors.AddOrganizationsPermissionDenied,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def create(
        self,
        *,
        default_roles: List[RoleId],
        display_name: ResourceDisplayName,
        organization_rids: List[OrganizationRid],
        role_grants: Dict[RoleId, List[Union[PrincipalWithId, PrincipalWithIdDict]]],
        space_rid: SpaceRid,
        description: Optional[str] = None,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[Project]:
        """
        Creates a new Project.

        Note that third-party applications using this endpoint via OAuth2 cannot be associated with an
        Ontology SDK as this will reduce the scope of operations to only those within specified projects.
        When creating the application, select "No, I won't use an Ontology SDK" on the Resources page.

        :param default_roles:
        :type default_roles: List[RoleId]
        :param display_name:
        :type display_name: ResourceDisplayName
        :param organization_rids:
        :type organization_rids: List[OrganizationRid]
        :param role_grants:
        :type role_grants: Dict[RoleId, List[Union[PrincipalWithId, PrincipalWithIdDict]]]
        :param space_rid:
        :type space_rid: SpaceRid
        :param description:
        :type description: Optional[str]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[Project]

        :raises CreateProjectNoOwnerLikeRoleGrant: The create project request would create a project with no principal being granted an owner-like role. As a result, there would be no user with administrative privileges over the project. A role is defined to be owner-like if it has the `compass:edit-project` operation. In the common case of the default role-set, this is just the `compass:manage` role.
        :raises CreateProjectPermissionDenied: Could not create the Project.
        :raises InvalidDisplayName: The display name of a Resource should not be exactly `.` or `..`, contain a forward slash `/` or be too long.
        :raises InvalidRoleIds: A roleId referenced in either default roles or role grants does not exist in the project role set for the space.
        :raises OrganizationsNotFound: At least one organization RID could not be found.
        :raises ProjectCreationNotSupported: Project creation is not supported in the current user's space.
        :raises ProjectNameAlreadyExists: The requested display name for the created project is already being used in the space.
        :raises SpaceNotFound: The referenced space cannot be found.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/filesystem/projects/create",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "displayName": display_name,
                    "description": description,
                    "spaceRid": space_rid,
                    "roleGrants": role_grants,
                    "defaultRoles": default_roles,
                    "organizationRids": organization_rids,
                },
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "displayName": ResourceDisplayName,
                        "description": Optional[str],
                        "spaceRid": SpaceRid,
                        "roleGrants": Dict[
                            RoleId, List[Union[PrincipalWithId, PrincipalWithIdDict]]
                        ],
                        "defaultRoles": List[RoleId],
                        "organizationRids": List[OrganizationRid],
                    },
                ),
                response_type=Project,
                request_timeout=request_timeout,
                throwable_errors={
                    "CreateProjectNoOwnerLikeRoleGrant": filesystem_errors.CreateProjectNoOwnerLikeRoleGrant,
                    "CreateProjectPermissionDenied": filesystem_errors.CreateProjectPermissionDenied,
                    "InvalidDisplayName": filesystem_errors.InvalidDisplayName,
                    "InvalidRoleIds": filesystem_errors.InvalidRoleIds,
                    "OrganizationsNotFound": filesystem_errors.OrganizationsNotFound,
                    "ProjectCreationNotSupported": filesystem_errors.ProjectCreationNotSupported,
                    "ProjectNameAlreadyExists": filesystem_errors.ProjectNameAlreadyExists,
                    "SpaceNotFound": filesystem_errors.SpaceNotFound,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def create_from_template(
        self,
        *,
        template_rid: ProjectTemplateRid,
        variable_values: Dict[ProjectTemplateVariableId, ProjectTemplateVariableValue],
        default_roles: Optional[List[RoleId]] = None,
        organization_rids: Optional[List[OrganizationRid]] = None,
        preview: Optional[PreviewMode] = None,
        project_description: Optional[str] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[Project]:
        """
        Creates a project from a project template.
        :param template_rid:
        :type template_rid: ProjectTemplateRid
        :param variable_values:
        :type variable_values: Dict[ProjectTemplateVariableId, ProjectTemplateVariableValue]
        :param default_roles:
        :type default_roles: Optional[List[RoleId]]
        :param organization_rids:
        :type organization_rids: Optional[List[OrganizationRid]]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param project_description:
        :type project_description: Optional[str]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[Project]

        :raises AddGroupToParentGroupPermissionDenied: The user is not authorized to add a a group to the parent group required to create the project from template.
        :raises CreateGroupPermissionDenied: The user is not authorized to create the group in the organization required to create the project from template.
        :raises CreateProjectFromTemplatePermissionDenied: Could not createFromTemplate the Project.
        :raises CreateProjectNoOwnerLikeRoleGrant: The create project request would create a project with no principal being granted an owner-like role. As a result, there would be no user with administrative privileges over the project. A role is defined to be owner-like if it has the `compass:edit-project` operation. In the common case of the default role-set, this is just the `compass:manage` role.
        :raises DefaultRolesNotInSpaceRoleSet: The requested default roles are not in the role set of the space for the project template.
        :raises InvalidDescription: Either the user has not passed a value for a template with unset project description, or has passed a value for a template with fixed project description.
        :raises InvalidOrganizationHierarchy: Organizations on a project must also exist on the parent space. This error is thrown if the configuration  of a project's organizations (on creation or subsequently) results in the project being marked with either  no organizations in a marked space, or with an organization that is not present on the parent space.
        :raises InvalidOrganizations: Either the user has not passed organizations for a template with suggested organizations, or has passed organization for a template with fixed organizations.
        :raises InvalidPrincipalIdsForGroupTemplate: The template requested for project creation contains principal IDs that do not exist.
        :raises InvalidVariable: A variable referenced in the request to create project from template is not defined on the template.
        :raises InvalidVariableEnumOption: The value passed in the request to create project from template for an enum type variable is not a valid option.
        :raises MissingVariableValue: A variable defined on the template requested for project creation does not have a value set in the request.
        :raises NotAuthorizedToApplyOrganization: The user is not authorized to apply at least one of the organization markings required to create the project from template.
        :raises ProjectTemplateNotFound: The project template RID referenced cannot be found.
        :raises TemplateGroupNameConflict: Creating the project from template would attempt to create new groups with names conflicting either with other new groups, or existing groups.
        :raises TemplateMarkingNameConflict: Creating the project from template would attempt to create new markings with names conflicting either with other new markings, or existing markings.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/filesystem/projects/createFromTemplate",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "templateRid": template_rid,
                    "variableValues": variable_values,
                    "defaultRoles": default_roles,
                    "organizationRids": organization_rids,
                    "projectDescription": project_description,
                },
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "templateRid": ProjectTemplateRid,
                        "variableValues": Dict[
                            ProjectTemplateVariableId, ProjectTemplateVariableValue
                        ],
                        "defaultRoles": Optional[List[RoleId]],
                        "organizationRids": Optional[List[OrganizationRid]],
                        "projectDescription": Optional[str],
                    },
                ),
                response_type=Project,
                request_timeout=request_timeout,
                throwable_errors={
                    "AddGroupToParentGroupPermissionDenied": filesystem_errors.AddGroupToParentGroupPermissionDenied,
                    "CreateGroupPermissionDenied": filesystem_errors.CreateGroupPermissionDenied,
                    "CreateProjectFromTemplatePermissionDenied": filesystem_errors.CreateProjectFromTemplatePermissionDenied,
                    "CreateProjectNoOwnerLikeRoleGrant": filesystem_errors.CreateProjectNoOwnerLikeRoleGrant,
                    "DefaultRolesNotInSpaceRoleSet": filesystem_errors.DefaultRolesNotInSpaceRoleSet,
                    "InvalidDescription": filesystem_errors.InvalidDescription,
                    "InvalidOrganizationHierarchy": filesystem_errors.InvalidOrganizationHierarchy,
                    "InvalidOrganizations": filesystem_errors.InvalidOrganizations,
                    "InvalidPrincipalIdsForGroupTemplate": filesystem_errors.InvalidPrincipalIdsForGroupTemplate,
                    "InvalidVariable": filesystem_errors.InvalidVariable,
                    "InvalidVariableEnumOption": filesystem_errors.InvalidVariableEnumOption,
                    "MissingVariableValue": filesystem_errors.MissingVariableValue,
                    "NotAuthorizedToApplyOrganization": filesystem_errors.NotAuthorizedToApplyOrganization,
                    "ProjectTemplateNotFound": filesystem_errors.ProjectTemplateNotFound,
                    "TemplateGroupNameConflict": filesystem_errors.TemplateGroupNameConflict,
                    "TemplateMarkingNameConflict": filesystem_errors.TemplateMarkingNameConflict,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def get(
        self,
        project_rid: ProjectRid,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[Project]:
        """
        Get the Project with the specified rid.
        :param project_rid: projectRid
        :type project_rid: ProjectRid
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[Project]

        :raises ProjectNotFound: The given Project could not be found.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/filesystem/projects/{projectRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "projectRid": project_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=Project,
                request_timeout=request_timeout,
                throwable_errors={
                    "ProjectNotFound": filesystem_errors.ProjectNotFound,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def organizations(
        self,
        project_rid: ProjectRid,
        *,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[ListOrganizationsOfProjectResponse]:
        """
        List of Organizations directly applied to a Project. The number of Organizations on a Project is
        typically small so the `pageSize` and `pageToken` parameters are not required.

        :param project_rid: projectRid
        :type project_rid: ProjectRid
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param page_token: pageToken
        :type page_token: Optional[PageToken]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[ListOrganizationsOfProjectResponse]
        """

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/filesystem/projects/{projectRid}/organizations",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
                    "preview": preview,
                },
                path_params={
                    "projectRid": project_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ListOrganizationsOfProjectResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def organizations_page(
        self,
        project_rid: ProjectRid,
        *,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[ListOrganizationsOfProjectResponse]:
        """
        List of Organizations directly applied to a Project. The number of Organizations on a Project is
        typically small so the `pageSize` and `pageToken` parameters are not required.

        :param project_rid: projectRid
        :type project_rid: ProjectRid
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param page_token: pageToken
        :type page_token: Optional[PageToken]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[ListOrganizationsOfProjectResponse]
        """

        warnings.warn(
            "The client.filesystem.Project.organizations_page(...) method has been deprecated. Please use client.filesystem.Project.organizations(...) instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/filesystem/projects/{projectRid}/organizations",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
                    "preview": preview,
                },
                path_params={
                    "projectRid": project_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ListOrganizationsOfProjectResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def remove_organizations(
        self,
        project_rid: ProjectRid,
        *,
        organization_rids: List[OrganizationRid],
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[None]:
        """
        Removes Organizations from a Project.
        :param project_rid: projectRid
        :type project_rid: ProjectRid
        :param organization_rids:
        :type organization_rids: List[OrganizationRid]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[None]

        :raises RemoveOrganizationsPermissionDenied: Could not removeOrganizations the Project.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/filesystem/projects/{projectRid}/removeOrganizations",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "projectRid": project_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                },
                body={
                    "organizationRids": organization_rids,
                },
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "organizationRids": List[OrganizationRid],
                    },
                ),
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "RemoveOrganizationsPermissionDenied": filesystem_errors.RemoveOrganizationsPermissionDenied,
                },
            ),
        )


class _ProjectClientStreaming:
    """
    The API client for the Project Resource.

    :param auth: Your auth configuration.
    :param hostname: Your Foundry hostname (for example, "myfoundry.palantirfoundry.com"). This can also include your API gateway service URI.
    :param config: Optionally specify the configuration for the HTTP session.
    """

    def __init__(
        self,
        auth: Auth,
        hostname: str,
        config: Optional[Config] = None,
    ):
        self._auth = auth
        self._hostname = hostname
        self._config = config
        self._api_client = ApiClient(auth=auth, hostname=hostname, config=config)

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def add_organizations(
        self,
        project_rid: ProjectRid,
        *,
        organization_rids: List[OrganizationRid],
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[None]:
        """
        Adds a list of Organizations to a Project.
        :param project_rid: projectRid
        :type project_rid: ProjectRid
        :param organization_rids:
        :type organization_rids: List[OrganizationRid]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[None]

        :raises AddOrganizationsPermissionDenied: Could not addOrganizations the Project.
        """

        return self._api_client.stream_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/filesystem/projects/{projectRid}/addOrganizations",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "projectRid": project_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                },
                body={
                    "organizationRids": organization_rids,
                },
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "organizationRids": List[OrganizationRid],
                    },
                ),
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "AddOrganizationsPermissionDenied": filesystem_errors.AddOrganizationsPermissionDenied,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def create(
        self,
        *,
        default_roles: List[RoleId],
        display_name: ResourceDisplayName,
        organization_rids: List[OrganizationRid],
        role_grants: Dict[RoleId, List[Union[PrincipalWithId, PrincipalWithIdDict]]],
        space_rid: SpaceRid,
        description: Optional[str] = None,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[Project]:
        """
        Creates a new Project.

        Note that third-party applications using this endpoint via OAuth2 cannot be associated with an
        Ontology SDK as this will reduce the scope of operations to only those within specified projects.
        When creating the application, select "No, I won't use an Ontology SDK" on the Resources page.

        :param default_roles:
        :type default_roles: List[RoleId]
        :param display_name:
        :type display_name: ResourceDisplayName
        :param organization_rids:
        :type organization_rids: List[OrganizationRid]
        :param role_grants:
        :type role_grants: Dict[RoleId, List[Union[PrincipalWithId, PrincipalWithIdDict]]]
        :param space_rid:
        :type space_rid: SpaceRid
        :param description:
        :type description: Optional[str]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[Project]

        :raises CreateProjectNoOwnerLikeRoleGrant: The create project request would create a project with no principal being granted an owner-like role. As a result, there would be no user with administrative privileges over the project. A role is defined to be owner-like if it has the `compass:edit-project` operation. In the common case of the default role-set, this is just the `compass:manage` role.
        :raises CreateProjectPermissionDenied: Could not create the Project.
        :raises InvalidDisplayName: The display name of a Resource should not be exactly `.` or `..`, contain a forward slash `/` or be too long.
        :raises InvalidRoleIds: A roleId referenced in either default roles or role grants does not exist in the project role set for the space.
        :raises OrganizationsNotFound: At least one organization RID could not be found.
        :raises ProjectCreationNotSupported: Project creation is not supported in the current user's space.
        :raises ProjectNameAlreadyExists: The requested display name for the created project is already being used in the space.
        :raises SpaceNotFound: The referenced space cannot be found.
        """

        return self._api_client.stream_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/filesystem/projects/create",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "displayName": display_name,
                    "description": description,
                    "spaceRid": space_rid,
                    "roleGrants": role_grants,
                    "defaultRoles": default_roles,
                    "organizationRids": organization_rids,
                },
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "displayName": ResourceDisplayName,
                        "description": Optional[str],
                        "spaceRid": SpaceRid,
                        "roleGrants": Dict[
                            RoleId, List[Union[PrincipalWithId, PrincipalWithIdDict]]
                        ],
                        "defaultRoles": List[RoleId],
                        "organizationRids": List[OrganizationRid],
                    },
                ),
                response_type=Project,
                request_timeout=request_timeout,
                throwable_errors={
                    "CreateProjectNoOwnerLikeRoleGrant": filesystem_errors.CreateProjectNoOwnerLikeRoleGrant,
                    "CreateProjectPermissionDenied": filesystem_errors.CreateProjectPermissionDenied,
                    "InvalidDisplayName": filesystem_errors.InvalidDisplayName,
                    "InvalidRoleIds": filesystem_errors.InvalidRoleIds,
                    "OrganizationsNotFound": filesystem_errors.OrganizationsNotFound,
                    "ProjectCreationNotSupported": filesystem_errors.ProjectCreationNotSupported,
                    "ProjectNameAlreadyExists": filesystem_errors.ProjectNameAlreadyExists,
                    "SpaceNotFound": filesystem_errors.SpaceNotFound,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def create_from_template(
        self,
        *,
        template_rid: ProjectTemplateRid,
        variable_values: Dict[ProjectTemplateVariableId, ProjectTemplateVariableValue],
        default_roles: Optional[List[RoleId]] = None,
        organization_rids: Optional[List[OrganizationRid]] = None,
        preview: Optional[PreviewMode] = None,
        project_description: Optional[str] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[Project]:
        """
        Creates a project from a project template.
        :param template_rid:
        :type template_rid: ProjectTemplateRid
        :param variable_values:
        :type variable_values: Dict[ProjectTemplateVariableId, ProjectTemplateVariableValue]
        :param default_roles:
        :type default_roles: Optional[List[RoleId]]
        :param organization_rids:
        :type organization_rids: Optional[List[OrganizationRid]]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param project_description:
        :type project_description: Optional[str]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[Project]

        :raises AddGroupToParentGroupPermissionDenied: The user is not authorized to add a a group to the parent group required to create the project from template.
        :raises CreateGroupPermissionDenied: The user is not authorized to create the group in the organization required to create the project from template.
        :raises CreateProjectFromTemplatePermissionDenied: Could not createFromTemplate the Project.
        :raises CreateProjectNoOwnerLikeRoleGrant: The create project request would create a project with no principal being granted an owner-like role. As a result, there would be no user with administrative privileges over the project. A role is defined to be owner-like if it has the `compass:edit-project` operation. In the common case of the default role-set, this is just the `compass:manage` role.
        :raises DefaultRolesNotInSpaceRoleSet: The requested default roles are not in the role set of the space for the project template.
        :raises InvalidDescription: Either the user has not passed a value for a template with unset project description, or has passed a value for a template with fixed project description.
        :raises InvalidOrganizationHierarchy: Organizations on a project must also exist on the parent space. This error is thrown if the configuration  of a project's organizations (on creation or subsequently) results in the project being marked with either  no organizations in a marked space, or with an organization that is not present on the parent space.
        :raises InvalidOrganizations: Either the user has not passed organizations for a template with suggested organizations, or has passed organization for a template with fixed organizations.
        :raises InvalidPrincipalIdsForGroupTemplate: The template requested for project creation contains principal IDs that do not exist.
        :raises InvalidVariable: A variable referenced in the request to create project from template is not defined on the template.
        :raises InvalidVariableEnumOption: The value passed in the request to create project from template for an enum type variable is not a valid option.
        :raises MissingVariableValue: A variable defined on the template requested for project creation does not have a value set in the request.
        :raises NotAuthorizedToApplyOrganization: The user is not authorized to apply at least one of the organization markings required to create the project from template.
        :raises ProjectTemplateNotFound: The project template RID referenced cannot be found.
        :raises TemplateGroupNameConflict: Creating the project from template would attempt to create new groups with names conflicting either with other new groups, or existing groups.
        :raises TemplateMarkingNameConflict: Creating the project from template would attempt to create new markings with names conflicting either with other new markings, or existing markings.
        """

        return self._api_client.stream_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/filesystem/projects/createFromTemplate",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "templateRid": template_rid,
                    "variableValues": variable_values,
                    "defaultRoles": default_roles,
                    "organizationRids": organization_rids,
                    "projectDescription": project_description,
                },
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "templateRid": ProjectTemplateRid,
                        "variableValues": Dict[
                            ProjectTemplateVariableId, ProjectTemplateVariableValue
                        ],
                        "defaultRoles": Optional[List[RoleId]],
                        "organizationRids": Optional[List[OrganizationRid]],
                        "projectDescription": Optional[str],
                    },
                ),
                response_type=Project,
                request_timeout=request_timeout,
                throwable_errors={
                    "AddGroupToParentGroupPermissionDenied": filesystem_errors.AddGroupToParentGroupPermissionDenied,
                    "CreateGroupPermissionDenied": filesystem_errors.CreateGroupPermissionDenied,
                    "CreateProjectFromTemplatePermissionDenied": filesystem_errors.CreateProjectFromTemplatePermissionDenied,
                    "CreateProjectNoOwnerLikeRoleGrant": filesystem_errors.CreateProjectNoOwnerLikeRoleGrant,
                    "DefaultRolesNotInSpaceRoleSet": filesystem_errors.DefaultRolesNotInSpaceRoleSet,
                    "InvalidDescription": filesystem_errors.InvalidDescription,
                    "InvalidOrganizationHierarchy": filesystem_errors.InvalidOrganizationHierarchy,
                    "InvalidOrganizations": filesystem_errors.InvalidOrganizations,
                    "InvalidPrincipalIdsForGroupTemplate": filesystem_errors.InvalidPrincipalIdsForGroupTemplate,
                    "InvalidVariable": filesystem_errors.InvalidVariable,
                    "InvalidVariableEnumOption": filesystem_errors.InvalidVariableEnumOption,
                    "MissingVariableValue": filesystem_errors.MissingVariableValue,
                    "NotAuthorizedToApplyOrganization": filesystem_errors.NotAuthorizedToApplyOrganization,
                    "ProjectTemplateNotFound": filesystem_errors.ProjectTemplateNotFound,
                    "TemplateGroupNameConflict": filesystem_errors.TemplateGroupNameConflict,
                    "TemplateMarkingNameConflict": filesystem_errors.TemplateMarkingNameConflict,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def get(
        self,
        project_rid: ProjectRid,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[Project]:
        """
        Get the Project with the specified rid.
        :param project_rid: projectRid
        :type project_rid: ProjectRid
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[Project]

        :raises ProjectNotFound: The given Project could not be found.
        """

        return self._api_client.stream_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/filesystem/projects/{projectRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "projectRid": project_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=Project,
                request_timeout=request_timeout,
                throwable_errors={
                    "ProjectNotFound": filesystem_errors.ProjectNotFound,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def organizations(
        self,
        project_rid: ProjectRid,
        *,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[ListOrganizationsOfProjectResponse]:
        """
        List of Organizations directly applied to a Project. The number of Organizations on a Project is
        typically small so the `pageSize` and `pageToken` parameters are not required.

        :param project_rid: projectRid
        :type project_rid: ProjectRid
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param page_token: pageToken
        :type page_token: Optional[PageToken]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[ListOrganizationsOfProjectResponse]
        """

        return self._api_client.stream_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/filesystem/projects/{projectRid}/organizations",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
                    "preview": preview,
                },
                path_params={
                    "projectRid": project_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ListOrganizationsOfProjectResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def organizations_page(
        self,
        project_rid: ProjectRid,
        *,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[ListOrganizationsOfProjectResponse]:
        """
        List of Organizations directly applied to a Project. The number of Organizations on a Project is
        typically small so the `pageSize` and `pageToken` parameters are not required.

        :param project_rid: projectRid
        :type project_rid: ProjectRid
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param page_token: pageToken
        :type page_token: Optional[PageToken]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[ListOrganizationsOfProjectResponse]
        """

        warnings.warn(
            "The client.filesystem.Project.organizations_page(...) method has been deprecated. Please use client.filesystem.Project.organizations(...) instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        return self._api_client.stream_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/filesystem/projects/{projectRid}/organizations",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
                    "preview": preview,
                },
                path_params={
                    "projectRid": project_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ListOrganizationsOfProjectResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def remove_organizations(
        self,
        project_rid: ProjectRid,
        *,
        organization_rids: List[OrganizationRid],
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[None]:
        """
        Removes Organizations from a Project.
        :param project_rid: projectRid
        :type project_rid: ProjectRid
        :param organization_rids:
        :type organization_rids: List[OrganizationRid]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[None]

        :raises RemoveOrganizationsPermissionDenied: Could not removeOrganizations the Project.
        """

        return self._api_client.stream_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/filesystem/projects/{projectRid}/removeOrganizations",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "projectRid": project_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                },
                body={
                    "organizationRids": organization_rids,
                },
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "organizationRids": List[OrganizationRid],
                    },
                ),
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "RemoveOrganizationsPermissionDenied": filesystem_errors.RemoveOrganizationsPermissionDenied,
                },
            ),
        )
