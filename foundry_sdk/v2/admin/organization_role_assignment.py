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
from foundry_sdk.v2.admin import errors as admin_errors
from foundry_sdk.v2.admin import models as admin_models
from foundry_sdk.v2.core import models as core_models


class OrganizationRoleAssignmentClient:
    """
    The API client for the OrganizationRoleAssignment Resource.

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

        self.with_streaming_response = _OrganizationRoleAssignmentClientStreaming(self)
        self.with_raw_response = _OrganizationRoleAssignmentClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def add(
        self,
        organization_rid: core_models.OrganizationRid,
        *,
        role_assignments: typing.List[core_models.RoleAssignmentUpdate],
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> None:
        """
        Assign roles to principals for the given Organization. At most 100 role assignments can be added in a single request.

        :param organization_rid:
        :type organization_rid: OrganizationRid
        :param role_assignments:
        :type role_assignments: List[RoleAssignmentUpdate]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: None

        :raises AddOrganizationRoleAssignmentsPermissionDenied: Could not add the OrganizationRoleAssignment.
        :raises OrganizationNotFound: The given Organization could not be found.
        :raises PrincipalNotFound: A principal (User or Group) with the given PrincipalId could not be found
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/admin/organizations/{organizationRid}/roleAssignments/add",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "organizationRid": organization_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                },
                body={
                    "roleAssignments": role_assignments,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "roleAssignments": typing.List[core_models.RoleAssignmentUpdate],
                    },
                ),
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "AddOrganizationRoleAssignmentsPermissionDenied": admin_errors.AddOrganizationRoleAssignmentsPermissionDenied,
                    "OrganizationNotFound": admin_errors.OrganizationNotFound,
                    "PrincipalNotFound": admin_errors.PrincipalNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def list(
        self,
        organization_rid: core_models.OrganizationRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> admin_models.ListOrganizationRoleAssignmentsResponse:
        """
        List all principals who are assigned a role for the given Organization.

        :param organization_rid:
        :type organization_rid: OrganizationRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: admin_models.ListOrganizationRoleAssignmentsResponse

        :raises ListOrganizationRoleAssignmentsPermissionDenied: The provided token does not have permission to list assigned roles for this organization.
        :raises OrganizationNotFound: The given Organization could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/admin/organizations/{organizationRid}/roleAssignments",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "organizationRid": organization_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=admin_models.ListOrganizationRoleAssignmentsResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "ListOrganizationRoleAssignmentsPermissionDenied": admin_errors.ListOrganizationRoleAssignmentsPermissionDenied,
                    "OrganizationNotFound": admin_errors.OrganizationNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def remove(
        self,
        organization_rid: core_models.OrganizationRid,
        *,
        role_assignments: typing.List[core_models.RoleAssignmentUpdate],
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> None:
        """
        Remove roles from principals for the given Organization. At most 100 role assignments can be removed in a single request.

        :param organization_rid:
        :type organization_rid: OrganizationRid
        :param role_assignments:
        :type role_assignments: List[RoleAssignmentUpdate]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: None

        :raises OrganizationNotFound: The given Organization could not be found.
        :raises PrincipalNotFound: A principal (User or Group) with the given PrincipalId could not be found
        :raises RemoveOrganizationRoleAssignmentsPermissionDenied: Could not remove the OrganizationRoleAssignment.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/admin/organizations/{organizationRid}/roleAssignments/remove",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "organizationRid": organization_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                },
                body={
                    "roleAssignments": role_assignments,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "roleAssignments": typing.List[core_models.RoleAssignmentUpdate],
                    },
                ),
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "OrganizationNotFound": admin_errors.OrganizationNotFound,
                    "PrincipalNotFound": admin_errors.PrincipalNotFound,
                    "RemoveOrganizationRoleAssignmentsPermissionDenied": admin_errors.RemoveOrganizationRoleAssignmentsPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _OrganizationRoleAssignmentClientRaw:
    def __init__(self, client: OrganizationRoleAssignmentClient) -> None:
        def add(_: None): ...
        def list(_: admin_models.ListOrganizationRoleAssignmentsResponse): ...
        def remove(_: None): ...

        self.add = core.with_raw_response(add, client.add)
        self.list = core.with_raw_response(list, client.list)
        self.remove = core.with_raw_response(remove, client.remove)


class _OrganizationRoleAssignmentClientStreaming:
    def __init__(self, client: OrganizationRoleAssignmentClient) -> None:
        def list(_: admin_models.ListOrganizationRoleAssignmentsResponse): ...

        self.list = core.with_streaming_response(list, client.list)


class AsyncOrganizationRoleAssignmentClient:
    """
    The API client for the OrganizationRoleAssignment Resource.

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

        self.with_streaming_response = _AsyncOrganizationRoleAssignmentClientStreaming(self)
        self.with_raw_response = _AsyncOrganizationRoleAssignmentClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def add(
        self,
        organization_rid: core_models.OrganizationRid,
        *,
        role_assignments: typing.List[core_models.RoleAssignmentUpdate],
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[None]:
        """
        Assign roles to principals for the given Organization. At most 100 role assignments can be added in a single request.

        :param organization_rid:
        :type organization_rid: OrganizationRid
        :param role_assignments:
        :type role_assignments: List[RoleAssignmentUpdate]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[None]

        :raises AddOrganizationRoleAssignmentsPermissionDenied: Could not add the OrganizationRoleAssignment.
        :raises OrganizationNotFound: The given Organization could not be found.
        :raises PrincipalNotFound: A principal (User or Group) with the given PrincipalId could not be found
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/admin/organizations/{organizationRid}/roleAssignments/add",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "organizationRid": organization_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                },
                body={
                    "roleAssignments": role_assignments,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "roleAssignments": typing.List[core_models.RoleAssignmentUpdate],
                    },
                ),
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "AddOrganizationRoleAssignmentsPermissionDenied": admin_errors.AddOrganizationRoleAssignmentsPermissionDenied,
                    "OrganizationNotFound": admin_errors.OrganizationNotFound,
                    "PrincipalNotFound": admin_errors.PrincipalNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def list(
        self,
        organization_rid: core_models.OrganizationRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[admin_models.ListOrganizationRoleAssignmentsResponse]:
        """
        List all principals who are assigned a role for the given Organization.

        :param organization_rid:
        :type organization_rid: OrganizationRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[admin_models.ListOrganizationRoleAssignmentsResponse]

        :raises ListOrganizationRoleAssignmentsPermissionDenied: The provided token does not have permission to list assigned roles for this organization.
        :raises OrganizationNotFound: The given Organization could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/admin/organizations/{organizationRid}/roleAssignments",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "organizationRid": organization_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=admin_models.ListOrganizationRoleAssignmentsResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "ListOrganizationRoleAssignmentsPermissionDenied": admin_errors.ListOrganizationRoleAssignmentsPermissionDenied,
                    "OrganizationNotFound": admin_errors.OrganizationNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def remove(
        self,
        organization_rid: core_models.OrganizationRid,
        *,
        role_assignments: typing.List[core_models.RoleAssignmentUpdate],
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[None]:
        """
        Remove roles from principals for the given Organization. At most 100 role assignments can be removed in a single request.

        :param organization_rid:
        :type organization_rid: OrganizationRid
        :param role_assignments:
        :type role_assignments: List[RoleAssignmentUpdate]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[None]

        :raises OrganizationNotFound: The given Organization could not be found.
        :raises PrincipalNotFound: A principal (User or Group) with the given PrincipalId could not be found
        :raises RemoveOrganizationRoleAssignmentsPermissionDenied: Could not remove the OrganizationRoleAssignment.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/admin/organizations/{organizationRid}/roleAssignments/remove",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "organizationRid": organization_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                },
                body={
                    "roleAssignments": role_assignments,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "roleAssignments": typing.List[core_models.RoleAssignmentUpdate],
                    },
                ),
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "OrganizationNotFound": admin_errors.OrganizationNotFound,
                    "PrincipalNotFound": admin_errors.PrincipalNotFound,
                    "RemoveOrganizationRoleAssignmentsPermissionDenied": admin_errors.RemoveOrganizationRoleAssignmentsPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _AsyncOrganizationRoleAssignmentClientRaw:
    def __init__(self, client: AsyncOrganizationRoleAssignmentClient) -> None:
        def add(_: None): ...
        def list(_: admin_models.ListOrganizationRoleAssignmentsResponse): ...
        def remove(_: None): ...

        self.add = core.async_with_raw_response(add, client.add)
        self.list = core.async_with_raw_response(list, client.list)
        self.remove = core.async_with_raw_response(remove, client.remove)


class _AsyncOrganizationRoleAssignmentClientStreaming:
    def __init__(self, client: AsyncOrganizationRoleAssignmentClient) -> None:
        def list(_: admin_models.ListOrganizationRoleAssignmentsResponse): ...

        self.list = core.async_with_streaming_response(list, client.list)
