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

import annotated_types
import pydantic
import typing_extensions

from foundry_sdk import _core as core
from foundry_sdk import _errors as errors
from foundry_sdk.v2.admin import errors as admin_errors
from foundry_sdk.v2.admin import models as admin_models
from foundry_sdk.v2.core import errors as core_errors
from foundry_sdk.v2.core import models as core_models


class GroupClient:
    """
    The API client for the Group Resource.

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

        self.with_streaming_response = _GroupClientStreaming(self)
        self.with_raw_response = _GroupClientRaw(self)

    @cached_property
    def ProviderInfo(self):
        from foundry_sdk.v2.admin.group_provider_info import GroupProviderInfoClient

        return GroupProviderInfoClient(
            auth=self._auth,
            hostname=self._hostname_supplier,
            config=self._config,
        )

    @cached_property
    def GroupMember(self):
        from foundry_sdk.v2.admin.group_member import GroupMemberClient

        return GroupMemberClient(
            auth=self._auth,
            hostname=self._hostname_supplier,
            config=self._config,
        )

    @cached_property
    def MembershipExpirationPolicy(self):
        from foundry_sdk.v2.admin.group_membership_expiration_policy import (
            GroupMembershipExpirationPolicyClient,
        )

        return GroupMembershipExpirationPolicyClient(
            auth=self._auth,
            hostname=self._hostname_supplier,
            config=self._config,
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def create(
        self,
        *,
        attributes: typing.Dict[admin_models.AttributeName, admin_models.AttributeValues],
        name: admin_models.GroupName,
        organizations: typing.List[core_models.OrganizationRid],
        description: typing.Optional[str] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> admin_models.Group:
        """
        Creates a new Group.
        :param attributes: A map of the Group's attributes. Attributes prefixed with "multipass:" are reserved for internal use by Foundry and are subject to change.
        :type attributes: Dict[AttributeName, AttributeValues]
        :param name: The name of the Group.
        :type name: GroupName
        :param organizations: The RIDs of the Organizations whose members can see this group. At least one Organization RID must be listed.
        :type organizations: List[OrganizationRid]
        :param description: A description of the Group.
        :type description: Optional[str]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: admin_models.Group

        :raises CreateGroupPermissionDenied: Could not create the Group.
        :raises GroupNameAlreadyExists: A group with this name already exists
        :raises InvalidGroupOrganizations: At least one Organization RID must be provided for a group
        :raises OrganizationNotFound: The given Organization could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/admin/groups",
                query_params={},
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body=admin_models.CreateGroupRequest(
                    name=name,
                    organizations=organizations,
                    description=description,
                    attributes=attributes,
                ),
                response_type=admin_models.Group,
                request_timeout=request_timeout,
                throwable_errors={
                    "CreateGroupPermissionDenied": admin_errors.CreateGroupPermissionDenied,
                    "GroupNameAlreadyExists": admin_errors.GroupNameAlreadyExists,
                    "InvalidGroupOrganizations": admin_errors.InvalidGroupOrganizations,
                    "OrganizationNotFound": admin_errors.OrganizationNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def delete(
        self,
        group_id: core_models.GroupId,
        *,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> None:
        """
        Delete the Group with the specified id.
        :param group_id:
        :type group_id: GroupId
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: None

        :raises DeleteGroupPermissionDenied: Could not delete the Group.
        :raises GroupNotFound: The given Group could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="DELETE",
                resource_path="/v2/admin/groups/{groupId}",
                query_params={},
                path_params={
                    "groupId": group_id,
                },
                header_params={},
                body=None,
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "DeleteGroupPermissionDenied": admin_errors.DeleteGroupPermissionDenied,
                    "GroupNotFound": admin_errors.GroupNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        group_id: core_models.GroupId,
        *,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> admin_models.Group:
        """
        Get the Group with the specified id.
        :param group_id:
        :type group_id: GroupId
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: admin_models.Group

        :raises GroupNotFound: The given Group could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/admin/groups/{groupId}",
                query_params={},
                path_params={
                    "groupId": group_id,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=admin_models.Group,
                request_timeout=request_timeout,
                throwable_errors={
                    "GroupNotFound": admin_errors.GroupNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get_batch(
        self,
        body: typing_extensions.Annotated[
            typing.List[admin_models.GetGroupsBatchRequestElement],
            annotated_types.Len(min_length=1, max_length=500),
        ],
        *,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> admin_models.GetGroupsBatchResponse:
        """
        Execute multiple get requests on Group.

        The maximum batch size for this endpoint is 500.
        :param body: Body of the request
        :type body: List[GetGroupsBatchRequestElement]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: admin_models.GetGroupsBatchResponse
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/admin/groups/getBatch",
                query_params={},
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body=body,
                response_type=admin_models.GetGroupsBatchResponse,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def list(
        self,
        *,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> core.ResourceIterator[admin_models.Group]:
        """
        Lists all Groups.

        This is a paged endpoint. Each page may be smaller or larger than the requested page size. However, it is guaranteed that if there are more results available, the `nextPageToken` field will be populated. To get the next page, make the same request again, but set the value of the `pageToken` query parameter to be value of the `nextPageToken` value of the previous response. If there is no `nextPageToken` field in the response, you are on the last page.
        :param page_size: The page size to use for the endpoint.
        :type page_size: Optional[PageSize]
        :param page_token: The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
        :type page_token: Optional[PageToken]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ResourceIterator[admin_models.Group]

        :raises InvalidPageSize: The provided page size was zero or negative. Page sizes must be greater than zero.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/admin/groups",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
                },
                path_params={},
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=admin_models.ListGroupsResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "InvalidPageSize": core_errors.InvalidPageSize,
                },
                response_mode=_sdk_internal.get("response_mode", "ITERATOR"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def list_current(
        self,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> admin_models.ListCurrentGroupsResponse:
        """
        Returns all Groups which contain the current user as a direct or transitive member. For example if the current user is a member of Group A and Group A is a member of Group B, this endpoint will return Group A and Group B.

        Unlike the list Group Memberships endpoint which requires the `api:admin-read` scope, this endpoint
        does not require any particular scopes and can be used by any authenticated user to retrieve their own
        group memberships.

        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: admin_models.ListCurrentGroupsResponse

        :raises ListCurrentGroupsPermissionDenied: Could not listCurrent the Group.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/admin/groups/listCurrent",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=admin_models.ListCurrentGroupsResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "ListCurrentGroupsPermissionDenied": admin_errors.ListCurrentGroupsPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def replace(
        self,
        group_id: core_models.GroupId,
        *,
        attributes: typing.Dict[admin_models.AttributeName, admin_models.AttributeValues],
        name: admin_models.GroupName,
        organizations: typing.List[core_models.OrganizationRid],
        description: typing.Optional[str] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> admin_models.Group:
        """
        When replacing groups, you must send all attributes that begin with `multipass:` exactly as they appear when calling the Get Group endpoint.
        :param group_id:
        :type group_id: GroupId
        :param attributes: A map of the Group's attributes. Attributes prefixed with "multipass:" are reserved for internal use by Foundry and are subject to change.
        :type attributes: Dict[AttributeName, AttributeValues]
        :param name: The name of the Group.
        :type name: GroupName
        :param organizations: The RIDs of the Organizations whose members can see this group. At least one Organization RID must be listed.
        :type organizations: List[OrganizationRid]
        :param description: A description of the Group.
        :type description: Optional[str]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: admin_models.Group

        :raises AttributesNotEditable: One or more attributes are not editable. Attributes prefixed with "multipass:" are reserved for internal use by Foundry and are not editable.
        :raises GroupNameAlreadyExists: A group with this name already exists
        :raises GroupNotFound: The given Group could not be found.
        :raises InvalidGroupOrganizations: At least one Organization RID must be provided for a group
        :raises ReplaceGroupPermissionDenied: Could not replace the Group.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="PUT",
                resource_path="/v2/admin/groups/{groupId}",
                query_params={},
                path_params={
                    "groupId": group_id,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body=admin_models.ReplaceGroupRequest(
                    name=name,
                    organizations=organizations,
                    description=description,
                    attributes=attributes,
                ),
                response_type=admin_models.Group,
                request_timeout=request_timeout,
                throwable_errors={
                    "AttributesNotEditable": admin_errors.AttributesNotEditable,
                    "GroupNameAlreadyExists": admin_errors.GroupNameAlreadyExists,
                    "GroupNotFound": admin_errors.GroupNotFound,
                    "InvalidGroupOrganizations": admin_errors.InvalidGroupOrganizations,
                    "ReplaceGroupPermissionDenied": admin_errors.ReplaceGroupPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def search(
        self,
        *,
        where: admin_models.GroupSearchFilter,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> admin_models.SearchGroupsResponse:
        """
        Perform a case-insensitive prefix search for groups based on group name.

        :param where:
        :type where: GroupSearchFilter
        :param page_size:
        :type page_size: Optional[PageSize]
        :param page_token:
        :type page_token: Optional[PageToken]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: admin_models.SearchGroupsResponse

        :raises InvalidPageSize: The provided page size was zero or negative. Page sizes must be greater than zero.
        :raises SearchGroupsPermissionDenied: Could not search the Group.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/admin/groups/search",
                query_params={},
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body=admin_models.SearchGroupsRequest(
                    where=where,
                    page_size=page_size,
                    page_token=page_token,
                ),
                response_type=admin_models.SearchGroupsResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "InvalidPageSize": core_errors.InvalidPageSize,
                    "SearchGroupsPermissionDenied": admin_errors.SearchGroupsPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _GroupClientRaw:
    def __init__(self, client: GroupClient) -> None:
        def create(_: admin_models.Group): ...
        def delete(_: None): ...
        def get(_: admin_models.Group): ...
        def get_batch(_: admin_models.GetGroupsBatchResponse): ...
        def list(_: admin_models.ListGroupsResponse): ...
        def list_current(_: admin_models.ListCurrentGroupsResponse): ...
        def replace(_: admin_models.Group): ...
        def search(_: admin_models.SearchGroupsResponse): ...

        self.create = core.with_raw_response(create, client.create)
        self.delete = core.with_raw_response(delete, client.delete)
        self.get = core.with_raw_response(get, client.get)
        self.get_batch = core.with_raw_response(get_batch, client.get_batch)
        self.list = core.with_raw_response(list, client.list)
        self.list_current = core.with_raw_response(list_current, client.list_current)
        self.replace = core.with_raw_response(replace, client.replace)
        self.search = core.with_raw_response(search, client.search)


class _GroupClientStreaming:
    def __init__(self, client: GroupClient) -> None:
        def create(_: admin_models.Group): ...
        def get(_: admin_models.Group): ...
        def get_batch(_: admin_models.GetGroupsBatchResponse): ...
        def list(_: admin_models.ListGroupsResponse): ...
        def list_current(_: admin_models.ListCurrentGroupsResponse): ...
        def replace(_: admin_models.Group): ...
        def search(_: admin_models.SearchGroupsResponse): ...

        self.create = core.with_streaming_response(create, client.create)
        self.get = core.with_streaming_response(get, client.get)
        self.get_batch = core.with_streaming_response(get_batch, client.get_batch)
        self.list = core.with_streaming_response(list, client.list)
        self.list_current = core.with_streaming_response(list_current, client.list_current)
        self.replace = core.with_streaming_response(replace, client.replace)
        self.search = core.with_streaming_response(search, client.search)


class AsyncGroupClient:
    """
    The API client for the Group Resource.

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

        self.with_streaming_response = _AsyncGroupClientStreaming(self)
        self.with_raw_response = _AsyncGroupClientRaw(self)

    @cached_property
    def ProviderInfo(self):
        from foundry_sdk.v2.admin.group_provider_info import (
            AsyncGroupProviderInfoClient,
        )

        return AsyncGroupProviderInfoClient(
            auth=self._auth,
            hostname=self._hostname_supplier,
            config=self._config,
        )

    @cached_property
    def GroupMember(self):
        from foundry_sdk.v2.admin.group_member import AsyncGroupMemberClient

        return AsyncGroupMemberClient(
            auth=self._auth,
            hostname=self._hostname_supplier,
            config=self._config,
        )

    @cached_property
    def MembershipExpirationPolicy(self):
        from foundry_sdk.v2.admin.group_membership_expiration_policy import (
            AsyncGroupMembershipExpirationPolicyClient,
        )

        return AsyncGroupMembershipExpirationPolicyClient(
            auth=self._auth,
            hostname=self._hostname_supplier,
            config=self._config,
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def create(
        self,
        *,
        attributes: typing.Dict[admin_models.AttributeName, admin_models.AttributeValues],
        name: admin_models.GroupName,
        organizations: typing.List[core_models.OrganizationRid],
        description: typing.Optional[str] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[admin_models.Group]:
        """
        Creates a new Group.
        :param attributes: A map of the Group's attributes. Attributes prefixed with "multipass:" are reserved for internal use by Foundry and are subject to change.
        :type attributes: Dict[AttributeName, AttributeValues]
        :param name: The name of the Group.
        :type name: GroupName
        :param organizations: The RIDs of the Organizations whose members can see this group. At least one Organization RID must be listed.
        :type organizations: List[OrganizationRid]
        :param description: A description of the Group.
        :type description: Optional[str]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[admin_models.Group]

        :raises CreateGroupPermissionDenied: Could not create the Group.
        :raises GroupNameAlreadyExists: A group with this name already exists
        :raises InvalidGroupOrganizations: At least one Organization RID must be provided for a group
        :raises OrganizationNotFound: The given Organization could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/admin/groups",
                query_params={},
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body=admin_models.CreateGroupRequest(
                    name=name,
                    organizations=organizations,
                    description=description,
                    attributes=attributes,
                ),
                response_type=admin_models.Group,
                request_timeout=request_timeout,
                throwable_errors={
                    "CreateGroupPermissionDenied": admin_errors.CreateGroupPermissionDenied,
                    "GroupNameAlreadyExists": admin_errors.GroupNameAlreadyExists,
                    "InvalidGroupOrganizations": admin_errors.InvalidGroupOrganizations,
                    "OrganizationNotFound": admin_errors.OrganizationNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def delete(
        self,
        group_id: core_models.GroupId,
        *,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[None]:
        """
        Delete the Group with the specified id.
        :param group_id:
        :type group_id: GroupId
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[None]

        :raises DeleteGroupPermissionDenied: Could not delete the Group.
        :raises GroupNotFound: The given Group could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="DELETE",
                resource_path="/v2/admin/groups/{groupId}",
                query_params={},
                path_params={
                    "groupId": group_id,
                },
                header_params={},
                body=None,
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "DeleteGroupPermissionDenied": admin_errors.DeleteGroupPermissionDenied,
                    "GroupNotFound": admin_errors.GroupNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        group_id: core_models.GroupId,
        *,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[admin_models.Group]:
        """
        Get the Group with the specified id.
        :param group_id:
        :type group_id: GroupId
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[admin_models.Group]

        :raises GroupNotFound: The given Group could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/admin/groups/{groupId}",
                query_params={},
                path_params={
                    "groupId": group_id,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=admin_models.Group,
                request_timeout=request_timeout,
                throwable_errors={
                    "GroupNotFound": admin_errors.GroupNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get_batch(
        self,
        body: typing_extensions.Annotated[
            typing.List[admin_models.GetGroupsBatchRequestElement],
            annotated_types.Len(min_length=1, max_length=500),
        ],
        *,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[admin_models.GetGroupsBatchResponse]:
        """
        Execute multiple get requests on Group.

        The maximum batch size for this endpoint is 500.
        :param body: Body of the request
        :type body: List[GetGroupsBatchRequestElement]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[admin_models.GetGroupsBatchResponse]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/admin/groups/getBatch",
                query_params={},
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body=body,
                response_type=admin_models.GetGroupsBatchResponse,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def list(
        self,
        *,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> core.AsyncResourceIterator[admin_models.Group]:
        """
        Lists all Groups.

        This is a paged endpoint. Each page may be smaller or larger than the requested page size. However, it is guaranteed that if there are more results available, the `nextPageToken` field will be populated. To get the next page, make the same request again, but set the value of the `pageToken` query parameter to be value of the `nextPageToken` value of the previous response. If there is no `nextPageToken` field in the response, you are on the last page.
        :param page_size: The page size to use for the endpoint.
        :type page_size: Optional[PageSize]
        :param page_token: The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
        :type page_token: Optional[PageToken]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.AsyncResourceIterator[admin_models.Group]

        :raises InvalidPageSize: The provided page size was zero or negative. Page sizes must be greater than zero.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/admin/groups",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
                },
                path_params={},
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=admin_models.ListGroupsResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "InvalidPageSize": core_errors.InvalidPageSize,
                },
                response_mode=_sdk_internal.get("response_mode", "ITERATOR"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def list_current(
        self,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[admin_models.ListCurrentGroupsResponse]:
        """
        Returns all Groups which contain the current user as a direct or transitive member. For example if the current user is a member of Group A and Group A is a member of Group B, this endpoint will return Group A and Group B.

        Unlike the list Group Memberships endpoint which requires the `api:admin-read` scope, this endpoint
        does not require any particular scopes and can be used by any authenticated user to retrieve their own
        group memberships.

        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[admin_models.ListCurrentGroupsResponse]

        :raises ListCurrentGroupsPermissionDenied: Could not listCurrent the Group.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/admin/groups/listCurrent",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=admin_models.ListCurrentGroupsResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "ListCurrentGroupsPermissionDenied": admin_errors.ListCurrentGroupsPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def replace(
        self,
        group_id: core_models.GroupId,
        *,
        attributes: typing.Dict[admin_models.AttributeName, admin_models.AttributeValues],
        name: admin_models.GroupName,
        organizations: typing.List[core_models.OrganizationRid],
        description: typing.Optional[str] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[admin_models.Group]:
        """
        When replacing groups, you must send all attributes that begin with `multipass:` exactly as they appear when calling the Get Group endpoint.
        :param group_id:
        :type group_id: GroupId
        :param attributes: A map of the Group's attributes. Attributes prefixed with "multipass:" are reserved for internal use by Foundry and are subject to change.
        :type attributes: Dict[AttributeName, AttributeValues]
        :param name: The name of the Group.
        :type name: GroupName
        :param organizations: The RIDs of the Organizations whose members can see this group. At least one Organization RID must be listed.
        :type organizations: List[OrganizationRid]
        :param description: A description of the Group.
        :type description: Optional[str]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[admin_models.Group]

        :raises AttributesNotEditable: One or more attributes are not editable. Attributes prefixed with "multipass:" are reserved for internal use by Foundry and are not editable.
        :raises GroupNameAlreadyExists: A group with this name already exists
        :raises GroupNotFound: The given Group could not be found.
        :raises InvalidGroupOrganizations: At least one Organization RID must be provided for a group
        :raises ReplaceGroupPermissionDenied: Could not replace the Group.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="PUT",
                resource_path="/v2/admin/groups/{groupId}",
                query_params={},
                path_params={
                    "groupId": group_id,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body=admin_models.ReplaceGroupRequest(
                    name=name,
                    organizations=organizations,
                    description=description,
                    attributes=attributes,
                ),
                response_type=admin_models.Group,
                request_timeout=request_timeout,
                throwable_errors={
                    "AttributesNotEditable": admin_errors.AttributesNotEditable,
                    "GroupNameAlreadyExists": admin_errors.GroupNameAlreadyExists,
                    "GroupNotFound": admin_errors.GroupNotFound,
                    "InvalidGroupOrganizations": admin_errors.InvalidGroupOrganizations,
                    "ReplaceGroupPermissionDenied": admin_errors.ReplaceGroupPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def search(
        self,
        *,
        where: admin_models.GroupSearchFilter,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[admin_models.SearchGroupsResponse]:
        """
        Perform a case-insensitive prefix search for groups based on group name.

        :param where:
        :type where: GroupSearchFilter
        :param page_size:
        :type page_size: Optional[PageSize]
        :param page_token:
        :type page_token: Optional[PageToken]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[admin_models.SearchGroupsResponse]

        :raises InvalidPageSize: The provided page size was zero or negative. Page sizes must be greater than zero.
        :raises SearchGroupsPermissionDenied: Could not search the Group.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/admin/groups/search",
                query_params={},
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body=admin_models.SearchGroupsRequest(
                    where=where,
                    page_size=page_size,
                    page_token=page_token,
                ),
                response_type=admin_models.SearchGroupsResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "InvalidPageSize": core_errors.InvalidPageSize,
                    "SearchGroupsPermissionDenied": admin_errors.SearchGroupsPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _AsyncGroupClientRaw:
    def __init__(self, client: AsyncGroupClient) -> None:
        def create(_: admin_models.Group): ...
        def delete(_: None): ...
        def get(_: admin_models.Group): ...
        def get_batch(_: admin_models.GetGroupsBatchResponse): ...
        def list(_: admin_models.ListGroupsResponse): ...
        def list_current(_: admin_models.ListCurrentGroupsResponse): ...
        def replace(_: admin_models.Group): ...
        def search(_: admin_models.SearchGroupsResponse): ...

        self.create = core.async_with_raw_response(create, client.create)
        self.delete = core.async_with_raw_response(delete, client.delete)
        self.get = core.async_with_raw_response(get, client.get)
        self.get_batch = core.async_with_raw_response(get_batch, client.get_batch)
        self.list = core.async_with_raw_response(list, client.list)
        self.list_current = core.async_with_raw_response(list_current, client.list_current)
        self.replace = core.async_with_raw_response(replace, client.replace)
        self.search = core.async_with_raw_response(search, client.search)


class _AsyncGroupClientStreaming:
    def __init__(self, client: AsyncGroupClient) -> None:
        def create(_: admin_models.Group): ...
        def get(_: admin_models.Group): ...
        def get_batch(_: admin_models.GetGroupsBatchResponse): ...
        def list(_: admin_models.ListGroupsResponse): ...
        def list_current(_: admin_models.ListCurrentGroupsResponse): ...
        def replace(_: admin_models.Group): ...
        def search(_: admin_models.SearchGroupsResponse): ...

        self.create = core.async_with_streaming_response(create, client.create)
        self.get = core.async_with_streaming_response(get, client.get)
        self.get_batch = core.async_with_streaming_response(get_batch, client.get_batch)
        self.list = core.async_with_streaming_response(list, client.list)
        self.list_current = core.async_with_streaming_response(list_current, client.list_current)
        self.replace = core.async_with_streaming_response(replace, client.replace)
        self.search = core.async_with_streaming_response(search, client.search)
