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
from functools import cached_property

import pydantic
import typing_extensions

from foundry_sdk import _core as core
from foundry_sdk import _errors as errors
from foundry_sdk.v2.admin import errors as admin_errors
from foundry_sdk.v2.admin import models as admin_models
from foundry_sdk.v2.core import models as core_models


class OrganizationClient:
    """
    The API client for the Organization Resource.

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

        self.with_streaming_response = _OrganizationClientStreaming(self)
        self.with_raw_response = _OrganizationClientRaw(self)

    @cached_property
    def OrganizationRoleAssignment(self):
        from foundry_sdk.v2.admin.organization_role_assignment import (
            OrganizationRoleAssignmentClient,
        )  # NOQA

        return OrganizationRoleAssignmentClient(
            auth=self._auth,
            hostname=self._hostname,
            config=self._config,
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        organization_rid: core_models.OrganizationRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> admin_models.Organization:
        """
        Get the Organization with the specified rid.
        :param organization_rid:
        :type organization_rid: OrganizationRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: admin_models.Organization

        :raises OrganizationNotFound: The given Organization could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/admin/organizations/{organizationRid}",
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
                response_type=admin_models.Organization,
                request_timeout=request_timeout,
                throwable_errors={
                    "OrganizationNotFound": admin_errors.OrganizationNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def list_available_roles(
        self,
        organization_rid: core_models.OrganizationRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> admin_models.ListAvailableOrganizationRolesResponse:
        """
        List all roles that can be assigned to a principal for the given Organization.

        :param organization_rid:
        :type organization_rid: OrganizationRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: admin_models.ListAvailableOrganizationRolesResponse

        :raises ListAvailableRolesOrganizationPermissionDenied: Could not listAvailableRoles the Organization.
        :raises OrganizationNotFound: The given Organization could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/admin/organizations/{organizationRid}/listAvailableRoles",
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
                response_type=admin_models.ListAvailableOrganizationRolesResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "ListAvailableRolesOrganizationPermissionDenied": admin_errors.ListAvailableRolesOrganizationPermissionDenied,
                    "OrganizationNotFound": admin_errors.OrganizationNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def replace(
        self,
        organization_rid: core_models.OrganizationRid,
        *,
        name: admin_models.OrganizationName,
        description: typing.Optional[str] = None,
        host: typing.Optional[admin_models.HostName] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> admin_models.Organization:
        """
        Replace the Organization with the specified rid.
        :param organization_rid:
        :type organization_rid: OrganizationRid
        :param name:
        :type name: OrganizationName
        :param description:
        :type description: Optional[str]
        :param host: The primary host name of the Organization. This should be used when constructing URLs for users of this Organization.
        :type host: Optional[HostName]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: admin_models.Organization

        :raises InvalidHostName: The provided hostname must be a valid domain name. The only allowed characters are letters, numbers, periods, and hyphens.
        :raises OrganizationNotFound: The given Organization could not be found.
        :raises ReplaceOrganizationPermissionDenied: Could not replace the Organization.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="PUT",
                resource_path="/v2/admin/organizations/{organizationRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "organizationRid": organization_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "name": name,
                    "host": host,
                    "description": description,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "name": admin_models.OrganizationName,
                        "host": typing.Optional[admin_models.HostName],
                        "description": typing.Optional[str],
                    },
                ),
                response_type=admin_models.Organization,
                request_timeout=request_timeout,
                throwable_errors={
                    "InvalidHostName": admin_errors.InvalidHostName,
                    "OrganizationNotFound": admin_errors.OrganizationNotFound,
                    "ReplaceOrganizationPermissionDenied": admin_errors.ReplaceOrganizationPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _OrganizationClientRaw:
    def __init__(self, client: OrganizationClient) -> None:
        def get(_: admin_models.Organization): ...
        def list_available_roles(_: admin_models.ListAvailableOrganizationRolesResponse): ...
        def replace(_: admin_models.Organization): ...

        self.get = core.with_raw_response(get, client.get)
        self.list_available_roles = core.with_raw_response(
            list_available_roles, client.list_available_roles
        )
        self.replace = core.with_raw_response(replace, client.replace)


class _OrganizationClientStreaming:
    def __init__(self, client: OrganizationClient) -> None:
        def get(_: admin_models.Organization): ...
        def list_available_roles(_: admin_models.ListAvailableOrganizationRolesResponse): ...
        def replace(_: admin_models.Organization): ...

        self.get = core.with_streaming_response(get, client.get)
        self.list_available_roles = core.with_streaming_response(
            list_available_roles, client.list_available_roles
        )
        self.replace = core.with_streaming_response(replace, client.replace)


class AsyncOrganizationClient:
    """
    The API client for the Organization Resource.

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

        self.with_streaming_response = _AsyncOrganizationClientStreaming(self)
        self.with_raw_response = _AsyncOrganizationClientRaw(self)

    @cached_property
    def OrganizationRoleAssignment(self):
        from foundry_sdk.v2.admin.organization_role_assignment import (
            AsyncOrganizationRoleAssignmentClient,
        )  # NOQA

        return AsyncOrganizationRoleAssignmentClient(
            auth=self._auth,
            hostname=self._hostname,
            config=self._config,
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        organization_rid: core_models.OrganizationRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[admin_models.Organization]:
        """
        Get the Organization with the specified rid.
        :param organization_rid:
        :type organization_rid: OrganizationRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[admin_models.Organization]

        :raises OrganizationNotFound: The given Organization could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/admin/organizations/{organizationRid}",
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
                response_type=admin_models.Organization,
                request_timeout=request_timeout,
                throwable_errors={
                    "OrganizationNotFound": admin_errors.OrganizationNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def list_available_roles(
        self,
        organization_rid: core_models.OrganizationRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[admin_models.ListAvailableOrganizationRolesResponse]:
        """
        List all roles that can be assigned to a principal for the given Organization.

        :param organization_rid:
        :type organization_rid: OrganizationRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[admin_models.ListAvailableOrganizationRolesResponse]

        :raises ListAvailableRolesOrganizationPermissionDenied: Could not listAvailableRoles the Organization.
        :raises OrganizationNotFound: The given Organization could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/admin/organizations/{organizationRid}/listAvailableRoles",
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
                response_type=admin_models.ListAvailableOrganizationRolesResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "ListAvailableRolesOrganizationPermissionDenied": admin_errors.ListAvailableRolesOrganizationPermissionDenied,
                    "OrganizationNotFound": admin_errors.OrganizationNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def replace(
        self,
        organization_rid: core_models.OrganizationRid,
        *,
        name: admin_models.OrganizationName,
        description: typing.Optional[str] = None,
        host: typing.Optional[admin_models.HostName] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[admin_models.Organization]:
        """
        Replace the Organization with the specified rid.
        :param organization_rid:
        :type organization_rid: OrganizationRid
        :param name:
        :type name: OrganizationName
        :param description:
        :type description: Optional[str]
        :param host: The primary host name of the Organization. This should be used when constructing URLs for users of this Organization.
        :type host: Optional[HostName]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[admin_models.Organization]

        :raises InvalidHostName: The provided hostname must be a valid domain name. The only allowed characters are letters, numbers, periods, and hyphens.
        :raises OrganizationNotFound: The given Organization could not be found.
        :raises ReplaceOrganizationPermissionDenied: Could not replace the Organization.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="PUT",
                resource_path="/v2/admin/organizations/{organizationRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "organizationRid": organization_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "name": name,
                    "host": host,
                    "description": description,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "name": admin_models.OrganizationName,
                        "host": typing.Optional[admin_models.HostName],
                        "description": typing.Optional[str],
                    },
                ),
                response_type=admin_models.Organization,
                request_timeout=request_timeout,
                throwable_errors={
                    "InvalidHostName": admin_errors.InvalidHostName,
                    "OrganizationNotFound": admin_errors.OrganizationNotFound,
                    "ReplaceOrganizationPermissionDenied": admin_errors.ReplaceOrganizationPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _AsyncOrganizationClientRaw:
    def __init__(self, client: AsyncOrganizationClient) -> None:
        def get(_: admin_models.Organization): ...
        def list_available_roles(_: admin_models.ListAvailableOrganizationRolesResponse): ...
        def replace(_: admin_models.Organization): ...

        self.get = core.async_with_raw_response(get, client.get)
        self.list_available_roles = core.async_with_raw_response(
            list_available_roles, client.list_available_roles
        )
        self.replace = core.async_with_raw_response(replace, client.replace)


class _AsyncOrganizationClientStreaming:
    def __init__(self, client: AsyncOrganizationClient) -> None:
        def get(_: admin_models.Organization): ...
        def list_available_roles(_: admin_models.ListAvailableOrganizationRolesResponse): ...
        def replace(_: admin_models.Organization): ...

        self.get = core.async_with_streaming_response(get, client.get)
        self.list_available_roles = core.async_with_streaming_response(
            list_available_roles, client.list_available_roles
        )
        self.replace = core.async_with_streaming_response(replace, client.replace)
