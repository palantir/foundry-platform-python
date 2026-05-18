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


class OrganizationGuestMemberClient:
    """
    The API client for the OrganizationGuestMember Resource.

    :param auth: Your auth configuration.
    :param hostname: The hostname supplier for resolving base URLs.
    :param config: Optionally specify the configuration for the HTTP session.
    """

    def __init__(
        self,
        auth: core.Auth,
        hostname: typing.Union[str, core.HostnameSupplier],
        config: typing.Optional[core.Config] = None,
    ):
        self._auth = auth
        if isinstance(hostname, core.HostnameSupplier):
            self._hostname_supplier = hostname
        else:
            self._hostname_supplier = core.create_hostname_supplier(hostname, config)
        self._hostname = self._hostname_supplier.get_hostname()
        self._config = config
        self._api_client = core.ApiClient(
            auth=auth, hostname=self._hostname_supplier, config=config
        )

        self.with_streaming_response = _OrganizationGuestMemberClientStreaming(self)
        self.with_raw_response = _OrganizationGuestMemberClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def add(
        self,
        organization_rid: core_models.OrganizationRid,
        *,
        principal_ids: typing.List[core_models.PrincipalId],
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> None:
        """
        Adds principals as guest members of an Organization. Attempting to add a primary member through this endpoint will not add the principal as a guest, but will still return a successful response.

        :param organization_rid:
        :type organization_rid: OrganizationRid
        :param principal_ids:
        :type principal_ids: List[PrincipalId]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: None

        :raises AddOrganizationGuestMembersPermissionDenied: Could not add the OrganizationGuestMember.
        :raises OrganizationNotFound: The given Organization could not be found.
        :raises PrincipalNotFound: A principal (User or Group) with the given PrincipalId could not be found
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/admin/organizations/{organizationRid}/guestMembers/add",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "organizationRid": organization_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                },
                body=admin_models.AddOrganizationGuestMembersRequest(
                    principal_ids=principal_ids,
                ),
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "AddOrganizationGuestMembersPermissionDenied": admin_errors.AddOrganizationGuestMembersPermissionDenied,
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
    ) -> admin_models.ListOrganizationGuestMembersResponse:
        """
        Lists all guest members of an Organization.

        :param organization_rid:
        :type organization_rid: OrganizationRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: admin_models.ListOrganizationGuestMembersResponse

        :raises ListOrganizationGuestMembersPermissionDenied: The provided token does not have permission to list guest members for this organization.
        :raises OrganizationNotFound: The given Organization could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/admin/organizations/{organizationRid}/guestMembers",
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
                response_type=admin_models.ListOrganizationGuestMembersResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "ListOrganizationGuestMembersPermissionDenied": admin_errors.ListOrganizationGuestMembersPermissionDenied,
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
        principal_ids: typing.List[core_models.PrincipalId],
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> None:
        """
        Removes principals from being guest members of an Organization. Attempting to remove a primary member through this endpoint will not remove the primary member, but will still return a successful response.

        :param organization_rid:
        :type organization_rid: OrganizationRid
        :param principal_ids:
        :type principal_ids: List[PrincipalId]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: None

        :raises OrganizationNotFound: The given Organization could not be found.
        :raises PrincipalNotFound: A principal (User or Group) with the given PrincipalId could not be found
        :raises RemoveOrganizationGuestMembersPermissionDenied: Could not remove the OrganizationGuestMember.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/admin/organizations/{organizationRid}/guestMembers/remove",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "organizationRid": organization_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                },
                body=admin_models.RemoveOrganizationGuestMembersRequest(
                    principal_ids=principal_ids,
                ),
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "OrganizationNotFound": admin_errors.OrganizationNotFound,
                    "PrincipalNotFound": admin_errors.PrincipalNotFound,
                    "RemoveOrganizationGuestMembersPermissionDenied": admin_errors.RemoveOrganizationGuestMembersPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _OrganizationGuestMemberClientRaw:
    def __init__(self, client: OrganizationGuestMemberClient) -> None:
        def add(_: None): ...
        def list(_: admin_models.ListOrganizationGuestMembersResponse): ...
        def remove(_: None): ...

        self.add = core.with_raw_response(add, client.add)
        self.list = core.with_raw_response(list, client.list)
        self.remove = core.with_raw_response(remove, client.remove)


class _OrganizationGuestMemberClientStreaming:
    def __init__(self, client: OrganizationGuestMemberClient) -> None:
        def list(_: admin_models.ListOrganizationGuestMembersResponse): ...

        self.list = core.with_streaming_response(list, client.list)


class AsyncOrganizationGuestMemberClient:
    """
    The API client for the OrganizationGuestMember Resource.

    :param auth: Your auth configuration.
    :param hostname: The hostname supplier for resolving base URLs.
    :param config: Optionally specify the configuration for the HTTP session.
    """

    def __init__(
        self,
        auth: core.Auth,
        hostname: typing.Union[str, core.HostnameSupplier],
        config: typing.Optional[core.Config] = None,
    ):
        self._auth = auth
        if isinstance(hostname, core.HostnameSupplier):
            self._hostname_supplier = hostname
        else:
            self._hostname_supplier = core.create_hostname_supplier(hostname, config)
        self._hostname = self._hostname_supplier.get_hostname()
        self._config = config
        self._api_client = core.AsyncApiClient(
            auth=auth, hostname=self._hostname_supplier, config=config
        )

        self.with_streaming_response = _AsyncOrganizationGuestMemberClientStreaming(self)
        self.with_raw_response = _AsyncOrganizationGuestMemberClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def add(
        self,
        organization_rid: core_models.OrganizationRid,
        *,
        principal_ids: typing.List[core_models.PrincipalId],
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[None]:
        """
        Adds principals as guest members of an Organization. Attempting to add a primary member through this endpoint will not add the principal as a guest, but will still return a successful response.

        :param organization_rid:
        :type organization_rid: OrganizationRid
        :param principal_ids:
        :type principal_ids: List[PrincipalId]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[None]

        :raises AddOrganizationGuestMembersPermissionDenied: Could not add the OrganizationGuestMember.
        :raises OrganizationNotFound: The given Organization could not be found.
        :raises PrincipalNotFound: A principal (User or Group) with the given PrincipalId could not be found
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/admin/organizations/{organizationRid}/guestMembers/add",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "organizationRid": organization_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                },
                body=admin_models.AddOrganizationGuestMembersRequest(
                    principal_ids=principal_ids,
                ),
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "AddOrganizationGuestMembersPermissionDenied": admin_errors.AddOrganizationGuestMembersPermissionDenied,
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
    ) -> typing.Awaitable[admin_models.ListOrganizationGuestMembersResponse]:
        """
        Lists all guest members of an Organization.

        :param organization_rid:
        :type organization_rid: OrganizationRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[admin_models.ListOrganizationGuestMembersResponse]

        :raises ListOrganizationGuestMembersPermissionDenied: The provided token does not have permission to list guest members for this organization.
        :raises OrganizationNotFound: The given Organization could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/admin/organizations/{organizationRid}/guestMembers",
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
                response_type=admin_models.ListOrganizationGuestMembersResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "ListOrganizationGuestMembersPermissionDenied": admin_errors.ListOrganizationGuestMembersPermissionDenied,
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
        principal_ids: typing.List[core_models.PrincipalId],
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[None]:
        """
        Removes principals from being guest members of an Organization. Attempting to remove a primary member through this endpoint will not remove the primary member, but will still return a successful response.

        :param organization_rid:
        :type organization_rid: OrganizationRid
        :param principal_ids:
        :type principal_ids: List[PrincipalId]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[None]

        :raises OrganizationNotFound: The given Organization could not be found.
        :raises PrincipalNotFound: A principal (User or Group) with the given PrincipalId could not be found
        :raises RemoveOrganizationGuestMembersPermissionDenied: Could not remove the OrganizationGuestMember.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/admin/organizations/{organizationRid}/guestMembers/remove",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "organizationRid": organization_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                },
                body=admin_models.RemoveOrganizationGuestMembersRequest(
                    principal_ids=principal_ids,
                ),
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "OrganizationNotFound": admin_errors.OrganizationNotFound,
                    "PrincipalNotFound": admin_errors.PrincipalNotFound,
                    "RemoveOrganizationGuestMembersPermissionDenied": admin_errors.RemoveOrganizationGuestMembersPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _AsyncOrganizationGuestMemberClientRaw:
    def __init__(self, client: AsyncOrganizationGuestMemberClient) -> None:
        def add(_: None): ...
        def list(_: admin_models.ListOrganizationGuestMembersResponse): ...
        def remove(_: None): ...

        self.add = core.async_with_raw_response(add, client.add)
        self.list = core.async_with_raw_response(list, client.list)
        self.remove = core.async_with_raw_response(remove, client.remove)


class _AsyncOrganizationGuestMemberClientStreaming:
    def __init__(self, client: AsyncOrganizationGuestMemberClient) -> None:
        def list(_: admin_models.ListOrganizationGuestMembersResponse): ...

        self.list = core.async_with_streaming_response(list, client.list)
