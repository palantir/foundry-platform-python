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

import pydantic
import typing_extensions

from foundry_sdk import _core as core
from foundry_sdk import _errors as errors
from foundry_sdk.v2.core import models as core_models
from foundry_sdk.v2.filesystem import errors as filesystem_errors
from foundry_sdk.v2.filesystem import models as filesystem_models


class ProjectClient:
    """
    The API client for the Project Resource.

    :param auth: Your auth configuration.
    :param hostname: Your Foundry hostname (for example, "myfoundry.palantirfoundry.com"). This can also include your API gateway service URI.
    :param config: Optionally specify the configuration for the HTTP session.
    """

    def __init__(
        self,
        auth: core.Auth,
        hostname: str,
        config: typing.Optional[core.Config] = None,
    ):
        self._auth = auth
        self._hostname = hostname
        self._config = config
        self._api_client = core.ApiClient(auth=auth, hostname=hostname, config=config)

        self.with_streaming_response = _ProjectClientStreaming(self)
        self.with_raw_response = _ProjectClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def add_organizations(
        self,
        project_rid: filesystem_models.ProjectRid,
        *,
        organization_rids: typing.List[core_models.OrganizationRid],
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> None:
        """
        Adds a list of Organizations to a Project.
        :param project_rid:
        :type project_rid: ProjectRid
        :param organization_rids:
        :type organization_rids: List[OrganizationRid]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: None

        :raises AddOrganizationsPermissionDenied: Could not addOrganizations the Project.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "organizationRids": typing.List[core_models.OrganizationRid],
                    },
                ),
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "AddOrganizationsPermissionDenied": filesystem_errors.AddOrganizationsPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def create(
        self,
        *,
        default_roles: typing.List[core_models.RoleId],
        display_name: filesystem_models.ResourceDisplayName,
        organization_rids: typing.List[core_models.OrganizationRid],
        role_grants: typing.Dict[
            core_models.RoleId, typing.List[filesystem_models.PrincipalWithId]
        ],
        space_rid: filesystem_models.SpaceRid,
        description: typing.Optional[str] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> filesystem_models.Project:
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
        :type role_grants: Dict[RoleId, List[PrincipalWithId]]
        :param space_rid:
        :type space_rid: SpaceRid
        :param description:
        :type description: Optional[str]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: filesystem_models.Project

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
            core.RequestInfo(
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
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "displayName": filesystem_models.ResourceDisplayName,
                        "description": typing.Optional[str],
                        "spaceRid": filesystem_models.SpaceRid,
                        "roleGrants": typing.Dict[
                            core_models.RoleId, typing.List[filesystem_models.PrincipalWithId]
                        ],
                        "defaultRoles": typing.List[core_models.RoleId],
                        "organizationRids": typing.List[core_models.OrganizationRid],
                    },
                ),
                response_type=filesystem_models.Project,
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
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def create_from_template(
        self,
        *,
        template_rid: filesystem_models.ProjectTemplateRid,
        variable_values: typing.Dict[
            filesystem_models.ProjectTemplateVariableId,
            filesystem_models.ProjectTemplateVariableValue,
        ],
        default_roles: typing.Optional[typing.List[core_models.RoleId]] = None,
        organization_rids: typing.Optional[typing.List[core_models.OrganizationRid]] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        project_description: typing.Optional[str] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> filesystem_models.Project:
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
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param project_description:
        :type project_description: Optional[str]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: filesystem_models.Project

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
            core.RequestInfo(
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
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "templateRid": filesystem_models.ProjectTemplateRid,
                        "variableValues": typing.Dict[
                            filesystem_models.ProjectTemplateVariableId,
                            filesystem_models.ProjectTemplateVariableValue,
                        ],
                        "defaultRoles": typing.Optional[typing.List[core_models.RoleId]],
                        "organizationRids": typing.Optional[
                            typing.List[core_models.OrganizationRid]
                        ],
                        "projectDescription": typing.Optional[str],
                    },
                ),
                response_type=filesystem_models.Project,
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
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        project_rid: filesystem_models.ProjectRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> filesystem_models.Project:
        """
        Get the Project with the specified rid.
        :param project_rid:
        :type project_rid: ProjectRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: filesystem_models.Project

        :raises ProjectNotFound: The given Project could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                response_type=filesystem_models.Project,
                request_timeout=request_timeout,
                throwable_errors={
                    "ProjectNotFound": filesystem_errors.ProjectNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def organizations(
        self,
        project_rid: filesystem_models.ProjectRid,
        *,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> core.ResourceIterator[core_models.OrganizationRid]:
        """
        List of Organizations directly applied to a Project. The number of Organizations on a Project is
        typically small so the `pageSize` and `pageToken` parameters are not required.

        :param project_rid:
        :type project_rid: ProjectRid
        :param page_size: The page size to use for the endpoint.
        :type page_size: Optional[PageSize]
        :param page_token: The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
        :type page_token: Optional[PageToken]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ResourceIterator[core_models.OrganizationRid]
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                response_type=filesystem_models.ListOrganizationsOfProjectResponse,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode", "ITERATOR"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def remove_organizations(
        self,
        project_rid: filesystem_models.ProjectRid,
        *,
        organization_rids: typing.List[core_models.OrganizationRid],
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> None:
        """
        Removes Organizations from a Project.
        :param project_rid:
        :type project_rid: ProjectRid
        :param organization_rids:
        :type organization_rids: List[OrganizationRid]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: None

        :raises RemoveOrganizationsPermissionDenied: Could not removeOrganizations the Project.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "organizationRids": typing.List[core_models.OrganizationRid],
                    },
                ),
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "RemoveOrganizationsPermissionDenied": filesystem_errors.RemoveOrganizationsPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _ProjectClientRaw:
    def __init__(self, client: ProjectClient) -> None:
        def add_organizations(_: None): ...
        def create(_: filesystem_models.Project): ...
        def create_from_template(_: filesystem_models.Project): ...
        def get(_: filesystem_models.Project): ...
        def organizations(_: filesystem_models.ListOrganizationsOfProjectResponse): ...
        def remove_organizations(_: None): ...

        self.add_organizations = core.with_raw_response(add_organizations, client.add_organizations)
        self.create = core.with_raw_response(create, client.create)
        self.create_from_template = core.with_raw_response(
            create_from_template, client.create_from_template
        )
        self.get = core.with_raw_response(get, client.get)
        self.organizations = core.with_raw_response(organizations, client.organizations)
        self.remove_organizations = core.with_raw_response(
            remove_organizations, client.remove_organizations
        )


class _ProjectClientStreaming:
    def __init__(self, client: ProjectClient) -> None:
        def create(_: filesystem_models.Project): ...
        def create_from_template(_: filesystem_models.Project): ...
        def get(_: filesystem_models.Project): ...
        def organizations(_: filesystem_models.ListOrganizationsOfProjectResponse): ...

        self.create = core.with_streaming_response(create, client.create)
        self.create_from_template = core.with_streaming_response(
            create_from_template, client.create_from_template
        )
        self.get = core.with_streaming_response(get, client.get)
        self.organizations = core.with_streaming_response(organizations, client.organizations)


class AsyncProjectClient:
    """
    The API client for the Project Resource.

    :param auth: Your auth configuration.
    :param hostname: Your Foundry hostname (for example, "myfoundry.palantirfoundry.com"). This can also include your API gateway service URI.
    :param config: Optionally specify the configuration for the HTTP session.
    """

    def __init__(
        self,
        auth: core.Auth,
        hostname: str,
        config: typing.Optional[core.Config] = None,
    ):
        self._auth = auth
        self._hostname = hostname
        self._config = config
        self._api_client = core.AsyncApiClient(auth=auth, hostname=hostname, config=config)

        self.with_streaming_response = _AsyncProjectClientStreaming(self)
        self.with_raw_response = _AsyncProjectClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def add_organizations(
        self,
        project_rid: filesystem_models.ProjectRid,
        *,
        organization_rids: typing.List[core_models.OrganizationRid],
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[None]:
        """
        Adds a list of Organizations to a Project.
        :param project_rid:
        :type project_rid: ProjectRid
        :param organization_rids:
        :type organization_rids: List[OrganizationRid]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[None]

        :raises AddOrganizationsPermissionDenied: Could not addOrganizations the Project.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "organizationRids": typing.List[core_models.OrganizationRid],
                    },
                ),
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "AddOrganizationsPermissionDenied": filesystem_errors.AddOrganizationsPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def create(
        self,
        *,
        default_roles: typing.List[core_models.RoleId],
        display_name: filesystem_models.ResourceDisplayName,
        organization_rids: typing.List[core_models.OrganizationRid],
        role_grants: typing.Dict[
            core_models.RoleId, typing.List[filesystem_models.PrincipalWithId]
        ],
        space_rid: filesystem_models.SpaceRid,
        description: typing.Optional[str] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[filesystem_models.Project]:
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
        :type role_grants: Dict[RoleId, List[PrincipalWithId]]
        :param space_rid:
        :type space_rid: SpaceRid
        :param description:
        :type description: Optional[str]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[filesystem_models.Project]

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
            core.RequestInfo(
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
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "displayName": filesystem_models.ResourceDisplayName,
                        "description": typing.Optional[str],
                        "spaceRid": filesystem_models.SpaceRid,
                        "roleGrants": typing.Dict[
                            core_models.RoleId, typing.List[filesystem_models.PrincipalWithId]
                        ],
                        "defaultRoles": typing.List[core_models.RoleId],
                        "organizationRids": typing.List[core_models.OrganizationRid],
                    },
                ),
                response_type=filesystem_models.Project,
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
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def create_from_template(
        self,
        *,
        template_rid: filesystem_models.ProjectTemplateRid,
        variable_values: typing.Dict[
            filesystem_models.ProjectTemplateVariableId,
            filesystem_models.ProjectTemplateVariableValue,
        ],
        default_roles: typing.Optional[typing.List[core_models.RoleId]] = None,
        organization_rids: typing.Optional[typing.List[core_models.OrganizationRid]] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        project_description: typing.Optional[str] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[filesystem_models.Project]:
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
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param project_description:
        :type project_description: Optional[str]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[filesystem_models.Project]

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
            core.RequestInfo(
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
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "templateRid": filesystem_models.ProjectTemplateRid,
                        "variableValues": typing.Dict[
                            filesystem_models.ProjectTemplateVariableId,
                            filesystem_models.ProjectTemplateVariableValue,
                        ],
                        "defaultRoles": typing.Optional[typing.List[core_models.RoleId]],
                        "organizationRids": typing.Optional[
                            typing.List[core_models.OrganizationRid]
                        ],
                        "projectDescription": typing.Optional[str],
                    },
                ),
                response_type=filesystem_models.Project,
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
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        project_rid: filesystem_models.ProjectRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[filesystem_models.Project]:
        """
        Get the Project with the specified rid.
        :param project_rid:
        :type project_rid: ProjectRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[filesystem_models.Project]

        :raises ProjectNotFound: The given Project could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                response_type=filesystem_models.Project,
                request_timeout=request_timeout,
                throwable_errors={
                    "ProjectNotFound": filesystem_errors.ProjectNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def organizations(
        self,
        project_rid: filesystem_models.ProjectRid,
        *,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> core.AsyncResourceIterator[core_models.OrganizationRid]:
        """
        List of Organizations directly applied to a Project. The number of Organizations on a Project is
        typically small so the `pageSize` and `pageToken` parameters are not required.

        :param project_rid:
        :type project_rid: ProjectRid
        :param page_size: The page size to use for the endpoint.
        :type page_size: Optional[PageSize]
        :param page_token: The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
        :type page_token: Optional[PageToken]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.AsyncResourceIterator[core_models.OrganizationRid]
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                response_type=filesystem_models.ListOrganizationsOfProjectResponse,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode", "ITERATOR"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def remove_organizations(
        self,
        project_rid: filesystem_models.ProjectRid,
        *,
        organization_rids: typing.List[core_models.OrganizationRid],
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[None]:
        """
        Removes Organizations from a Project.
        :param project_rid:
        :type project_rid: ProjectRid
        :param organization_rids:
        :type organization_rids: List[OrganizationRid]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[None]

        :raises RemoveOrganizationsPermissionDenied: Could not removeOrganizations the Project.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "organizationRids": typing.List[core_models.OrganizationRid],
                    },
                ),
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "RemoveOrganizationsPermissionDenied": filesystem_errors.RemoveOrganizationsPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _AsyncProjectClientRaw:
    def __init__(self, client: AsyncProjectClient) -> None:
        def add_organizations(_: None): ...
        def create(_: filesystem_models.Project): ...
        def create_from_template(_: filesystem_models.Project): ...
        def get(_: filesystem_models.Project): ...
        def organizations(_: filesystem_models.ListOrganizationsOfProjectResponse): ...
        def remove_organizations(_: None): ...

        self.add_organizations = core.async_with_raw_response(
            add_organizations, client.add_organizations
        )
        self.create = core.async_with_raw_response(create, client.create)
        self.create_from_template = core.async_with_raw_response(
            create_from_template, client.create_from_template
        )
        self.get = core.async_with_raw_response(get, client.get)
        self.organizations = core.async_with_raw_response(organizations, client.organizations)
        self.remove_organizations = core.async_with_raw_response(
            remove_organizations, client.remove_organizations
        )


class _AsyncProjectClientStreaming:
    def __init__(self, client: AsyncProjectClient) -> None:
        def create(_: filesystem_models.Project): ...
        def create_from_template(_: filesystem_models.Project): ...
        def get(_: filesystem_models.Project): ...
        def organizations(_: filesystem_models.ListOrganizationsOfProjectResponse): ...

        self.create = core.async_with_streaming_response(create, client.create)
        self.create_from_template = core.async_with_streaming_response(
            create_from_template, client.create_from_template
        )
        self.get = core.async_with_streaming_response(get, client.get)
        self.organizations = core.async_with_streaming_response(organizations, client.organizations)
