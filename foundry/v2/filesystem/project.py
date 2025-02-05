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
        Creates a project.
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
        Creates a project.
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
        Creates a project.
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
            ),
        )
