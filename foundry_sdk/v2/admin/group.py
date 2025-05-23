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

        self.with_streaming_response = _GroupClientStreaming(self)
        self.with_raw_response = _GroupClientRaw(self)

    @cached_property
    def ProviderInfo(self):
        from foundry_sdk.v2.admin.group_provider_info import GroupProviderInfoClient

        return GroupProviderInfoClient(
            auth=self._auth,
            hostname=self._hostname,
            config=self._config,
        )

    @cached_property
    def GroupMember(self):
        from foundry_sdk.v2.admin.group_member import GroupMemberClient

        return GroupMemberClient(
            auth=self._auth,
            hostname=self._hostname,
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
                body={
                    "name": name,
                    "organizations": organizations,
                    "description": description,
                    "attributes": attributes,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "name": admin_models.GroupName,
                        "organizations": typing.List[core_models.OrganizationRid],
                        "description": typing.Optional[str],
                        "attributes": typing.Dict[
                            admin_models.AttributeName, admin_models.AttributeValues
                        ],
                    },
                ),
                response_type=admin_models.Group,
                request_timeout=request_timeout,
                throwable_errors={
                    "CreateGroupPermissionDenied": admin_errors.CreateGroupPermissionDenied,
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
        group_id: core_models.PrincipalId,
        *,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> None:
        """
        Delete the Group with the specified id.
        :param group_id:
        :type group_id: PrincipalId
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: None

        :raises DeleteGroupPermissionDenied: Could not delete the Group.
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
                body_type=None,
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "DeleteGroupPermissionDenied": admin_errors.DeleteGroupPermissionDenied,
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
        group_id: core_models.PrincipalId,
        *,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> admin_models.Group:
        """
        Get the Group with the specified id.
        :param group_id:
        :type group_id: PrincipalId
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
                body_type=None,
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
                body_type=typing_extensions.Annotated[
                    typing.List[admin_models.GetGroupsBatchRequestElement],
                    annotated_types.Len(min_length=1, max_length=500),
                ],
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
                body_type=None,
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
                body={
                    "where": where,
                    "pageSize": page_size,
                    "pageToken": page_token,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "where": admin_models.GroupSearchFilter,
                        "pageSize": typing.Optional[core_models.PageSize],
                        "pageToken": typing.Optional[core_models.PageToken],
                    },
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
        def search(_: admin_models.SearchGroupsResponse): ...

        self.create = core.with_raw_response(create, client.create)
        self.delete = core.with_raw_response(delete, client.delete)
        self.get = core.with_raw_response(get, client.get)
        self.get_batch = core.with_raw_response(get_batch, client.get_batch)
        self.list = core.with_raw_response(list, client.list)
        self.search = core.with_raw_response(search, client.search)


class _GroupClientStreaming:
    def __init__(self, client: GroupClient) -> None:
        def create(_: admin_models.Group): ...
        def get(_: admin_models.Group): ...
        def get_batch(_: admin_models.GetGroupsBatchResponse): ...
        def list(_: admin_models.ListGroupsResponse): ...
        def search(_: admin_models.SearchGroupsResponse): ...

        self.create = core.with_streaming_response(create, client.create)
        self.get = core.with_streaming_response(get, client.get)
        self.get_batch = core.with_streaming_response(get_batch, client.get_batch)
        self.list = core.with_streaming_response(list, client.list)
        self.search = core.with_streaming_response(search, client.search)


class AsyncGroupClient:
    """
    The API client for the Group Resource.

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

        self.with_streaming_response = _AsyncGroupClientStreaming(self)
        self.with_raw_response = _AsyncGroupClientRaw(self)

    @cached_property
    def ProviderInfo(self):
        from foundry_sdk.v2.admin.group_provider_info import AsyncGroupProviderInfoClient  # NOQA

        return AsyncGroupProviderInfoClient(
            auth=self._auth,
            hostname=self._hostname,
            config=self._config,
        )

    @cached_property
    def GroupMember(self):
        from foundry_sdk.v2.admin.group_member import AsyncGroupMemberClient

        return AsyncGroupMemberClient(
            auth=self._auth,
            hostname=self._hostname,
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
                body={
                    "name": name,
                    "organizations": organizations,
                    "description": description,
                    "attributes": attributes,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "name": admin_models.GroupName,
                        "organizations": typing.List[core_models.OrganizationRid],
                        "description": typing.Optional[str],
                        "attributes": typing.Dict[
                            admin_models.AttributeName, admin_models.AttributeValues
                        ],
                    },
                ),
                response_type=admin_models.Group,
                request_timeout=request_timeout,
                throwable_errors={
                    "CreateGroupPermissionDenied": admin_errors.CreateGroupPermissionDenied,
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
        group_id: core_models.PrincipalId,
        *,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[None]:
        """
        Delete the Group with the specified id.
        :param group_id:
        :type group_id: PrincipalId
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[None]

        :raises DeleteGroupPermissionDenied: Could not delete the Group.
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
                body_type=None,
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "DeleteGroupPermissionDenied": admin_errors.DeleteGroupPermissionDenied,
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
        group_id: core_models.PrincipalId,
        *,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[admin_models.Group]:
        """
        Get the Group with the specified id.
        :param group_id:
        :type group_id: PrincipalId
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
                body_type=None,
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
                body_type=typing_extensions.Annotated[
                    typing.List[admin_models.GetGroupsBatchRequestElement],
                    annotated_types.Len(min_length=1, max_length=500),
                ],
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
                body_type=None,
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
                body={
                    "where": where,
                    "pageSize": page_size,
                    "pageToken": page_token,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "where": admin_models.GroupSearchFilter,
                        "pageSize": typing.Optional[core_models.PageSize],
                        "pageToken": typing.Optional[core_models.PageToken],
                    },
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
        def search(_: admin_models.SearchGroupsResponse): ...

        self.create = core.async_with_raw_response(create, client.create)
        self.delete = core.async_with_raw_response(delete, client.delete)
        self.get = core.async_with_raw_response(get, client.get)
        self.get_batch = core.async_with_raw_response(get_batch, client.get_batch)
        self.list = core.async_with_raw_response(list, client.list)
        self.search = core.async_with_raw_response(search, client.search)


class _AsyncGroupClientStreaming:
    def __init__(self, client: AsyncGroupClient) -> None:
        def create(_: admin_models.Group): ...
        def get(_: admin_models.Group): ...
        def get_batch(_: admin_models.GetGroupsBatchResponse): ...
        def list(_: admin_models.ListGroupsResponse): ...
        def search(_: admin_models.SearchGroupsResponse): ...

        self.create = core.async_with_streaming_response(create, client.create)
        self.get = core.async_with_streaming_response(get, client.get)
        self.get_batch = core.async_with_streaming_response(get_batch, client.get_batch)
        self.list = core.async_with_streaming_response(list, client.list)
        self.search = core.async_with_streaming_response(search, client.search)
