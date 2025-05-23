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
from foundry_sdk.v2.core import errors as core_errors
from foundry_sdk.v2.core import models as core_models


class GroupMemberClient:
    """
    The API client for the GroupMember Resource.

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

        self.with_streaming_response = _GroupMemberClientStreaming(self)
        self.with_raw_response = _GroupMemberClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def add(
        self,
        group_id: core_models.PrincipalId,
        *,
        principal_ids: typing.List[core_models.PrincipalId],
        expiration: typing.Optional[admin_models.GroupMembershipExpiration] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> None:
        """

        :param group_id:
        :type group_id: PrincipalId
        :param principal_ids:
        :type principal_ids: List[PrincipalId]
        :param expiration:
        :type expiration: Optional[GroupMembershipExpiration]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: None

        :raises AddGroupMembersPermissionDenied: Could not add the GroupMember.
        :raises AddGroupMembersPermissionDenied: Could not add the GroupMember.
        :raises GroupNotFound: The given Group could not be found.
        :raises PrincipalNotFound: A principal (User or Group) with the given PrincipalId could not be found
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/admin/groups/{groupId}/groupMembers/add",
                query_params={},
                path_params={
                    "groupId": group_id,
                },
                header_params={
                    "Content-Type": "application/json",
                },
                body={
                    "principalIds": principal_ids,
                    "expiration": expiration,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "principalIds": typing.List[core_models.PrincipalId],
                        "expiration": typing.Optional[admin_models.GroupMembershipExpiration],
                    },
                ),
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "AddGroupMembersPermissionDenied": admin_errors.AddGroupMembersPermissionDenied,
                    "AddGroupMembersPermissionDenied": admin_errors.AddGroupMembersPermissionDenied,
                    "GroupNotFound": admin_errors.GroupNotFound,
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
        group_id: core_models.PrincipalId,
        *,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        transitive: typing.Optional[bool] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> core.ResourceIterator[admin_models.GroupMember]:
        """
        Lists all members (which can be a User or a Group) of a given Group.

        This is a paged endpoint. Each page may be smaller or larger than the requested page size. However,
        it is guaranteed that if there are more results available, the `nextPageToken` field will be populated.
        To get the next page, make the same request again, but set the value of the `pageToken` query parameter
        to be value of the `nextPageToken` value of the previous response. If there is no `nextPageToken` field
        in the response, you are on the last page.

        :param group_id:
        :type group_id: PrincipalId
        :param page_size: The page size to use for the endpoint.
        :type page_size: Optional[PageSize]
        :param page_token: The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
        :type page_token: Optional[PageToken]
        :param transitive: When true, includes the transitive members of groups contained within this group. For example, say the Group has member Group A, and Group A has member User B. If `transitive=false` only Group A will be returned, but if `transitive=true` then Group A and User B will be returned. This will recursively resolve Groups through all layers of nesting.  Defaults to false.
        :type transitive: Optional[bool]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ResourceIterator[admin_models.GroupMember]

        :raises GroupNotFound: The given Group could not be found.
        :raises InvalidPageSize: The provided page size was zero or negative. Page sizes must be greater than zero.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/admin/groups/{groupId}/groupMembers",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
                    "transitive": transitive,
                },
                path_params={
                    "groupId": group_id,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=admin_models.ListGroupMembersResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "GroupNotFound": admin_errors.GroupNotFound,
                    "InvalidPageSize": core_errors.InvalidPageSize,
                },
                response_mode=_sdk_internal.get("response_mode", "ITERATOR"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def remove(
        self,
        group_id: core_models.PrincipalId,
        *,
        principal_ids: typing.List[core_models.PrincipalId],
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> None:
        """

        :param group_id:
        :type group_id: PrincipalId
        :param principal_ids:
        :type principal_ids: List[PrincipalId]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: None

        :raises GroupNotFound: The given Group could not be found.
        :raises PrincipalNotFound: A principal (User or Group) with the given PrincipalId could not be found
        :raises RemoveGroupMembersPermissionDenied: Could not remove the GroupMember.
        :raises RemoveGroupMembersPermissionDenied: Could not remove the GroupMember.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/admin/groups/{groupId}/groupMembers/remove",
                query_params={},
                path_params={
                    "groupId": group_id,
                },
                header_params={
                    "Content-Type": "application/json",
                },
                body={
                    "principalIds": principal_ids,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "principalIds": typing.List[core_models.PrincipalId],
                    },
                ),
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "GroupNotFound": admin_errors.GroupNotFound,
                    "PrincipalNotFound": admin_errors.PrincipalNotFound,
                    "RemoveGroupMembersPermissionDenied": admin_errors.RemoveGroupMembersPermissionDenied,
                    "RemoveGroupMembersPermissionDenied": admin_errors.RemoveGroupMembersPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _GroupMemberClientRaw:
    def __init__(self, client: GroupMemberClient) -> None:
        def add(_: None): ...
        def list(_: admin_models.ListGroupMembersResponse): ...
        def remove(_: None): ...

        self.add = core.with_raw_response(add, client.add)
        self.list = core.with_raw_response(list, client.list)
        self.remove = core.with_raw_response(remove, client.remove)


class _GroupMemberClientStreaming:
    def __init__(self, client: GroupMemberClient) -> None:
        def list(_: admin_models.ListGroupMembersResponse): ...

        self.list = core.with_streaming_response(list, client.list)


class AsyncGroupMemberClient:
    """
    The API client for the GroupMember Resource.

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

        self.with_streaming_response = _AsyncGroupMemberClientStreaming(self)
        self.with_raw_response = _AsyncGroupMemberClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def add(
        self,
        group_id: core_models.PrincipalId,
        *,
        principal_ids: typing.List[core_models.PrincipalId],
        expiration: typing.Optional[admin_models.GroupMembershipExpiration] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[None]:
        """

        :param group_id:
        :type group_id: PrincipalId
        :param principal_ids:
        :type principal_ids: List[PrincipalId]
        :param expiration:
        :type expiration: Optional[GroupMembershipExpiration]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[None]

        :raises AddGroupMembersPermissionDenied: Could not add the GroupMember.
        :raises AddGroupMembersPermissionDenied: Could not add the GroupMember.
        :raises GroupNotFound: The given Group could not be found.
        :raises PrincipalNotFound: A principal (User or Group) with the given PrincipalId could not be found
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/admin/groups/{groupId}/groupMembers/add",
                query_params={},
                path_params={
                    "groupId": group_id,
                },
                header_params={
                    "Content-Type": "application/json",
                },
                body={
                    "principalIds": principal_ids,
                    "expiration": expiration,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "principalIds": typing.List[core_models.PrincipalId],
                        "expiration": typing.Optional[admin_models.GroupMembershipExpiration],
                    },
                ),
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "AddGroupMembersPermissionDenied": admin_errors.AddGroupMembersPermissionDenied,
                    "AddGroupMembersPermissionDenied": admin_errors.AddGroupMembersPermissionDenied,
                    "GroupNotFound": admin_errors.GroupNotFound,
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
        group_id: core_models.PrincipalId,
        *,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        transitive: typing.Optional[bool] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> core.AsyncResourceIterator[admin_models.GroupMember]:
        """
        Lists all members (which can be a User or a Group) of a given Group.

        This is a paged endpoint. Each page may be smaller or larger than the requested page size. However,
        it is guaranteed that if there are more results available, the `nextPageToken` field will be populated.
        To get the next page, make the same request again, but set the value of the `pageToken` query parameter
        to be value of the `nextPageToken` value of the previous response. If there is no `nextPageToken` field
        in the response, you are on the last page.

        :param group_id:
        :type group_id: PrincipalId
        :param page_size: The page size to use for the endpoint.
        :type page_size: Optional[PageSize]
        :param page_token: The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
        :type page_token: Optional[PageToken]
        :param transitive: When true, includes the transitive members of groups contained within this group. For example, say the Group has member Group A, and Group A has member User B. If `transitive=false` only Group A will be returned, but if `transitive=true` then Group A and User B will be returned. This will recursively resolve Groups through all layers of nesting.  Defaults to false.
        :type transitive: Optional[bool]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.AsyncResourceIterator[admin_models.GroupMember]

        :raises GroupNotFound: The given Group could not be found.
        :raises InvalidPageSize: The provided page size was zero or negative. Page sizes must be greater than zero.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/admin/groups/{groupId}/groupMembers",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
                    "transitive": transitive,
                },
                path_params={
                    "groupId": group_id,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=admin_models.ListGroupMembersResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "GroupNotFound": admin_errors.GroupNotFound,
                    "InvalidPageSize": core_errors.InvalidPageSize,
                },
                response_mode=_sdk_internal.get("response_mode", "ITERATOR"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def remove(
        self,
        group_id: core_models.PrincipalId,
        *,
        principal_ids: typing.List[core_models.PrincipalId],
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[None]:
        """

        :param group_id:
        :type group_id: PrincipalId
        :param principal_ids:
        :type principal_ids: List[PrincipalId]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[None]

        :raises GroupNotFound: The given Group could not be found.
        :raises PrincipalNotFound: A principal (User or Group) with the given PrincipalId could not be found
        :raises RemoveGroupMembersPermissionDenied: Could not remove the GroupMember.
        :raises RemoveGroupMembersPermissionDenied: Could not remove the GroupMember.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/admin/groups/{groupId}/groupMembers/remove",
                query_params={},
                path_params={
                    "groupId": group_id,
                },
                header_params={
                    "Content-Type": "application/json",
                },
                body={
                    "principalIds": principal_ids,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "principalIds": typing.List[core_models.PrincipalId],
                    },
                ),
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "GroupNotFound": admin_errors.GroupNotFound,
                    "PrincipalNotFound": admin_errors.PrincipalNotFound,
                    "RemoveGroupMembersPermissionDenied": admin_errors.RemoveGroupMembersPermissionDenied,
                    "RemoveGroupMembersPermissionDenied": admin_errors.RemoveGroupMembersPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _AsyncGroupMemberClientRaw:
    def __init__(self, client: AsyncGroupMemberClient) -> None:
        def add(_: None): ...
        def list(_: admin_models.ListGroupMembersResponse): ...
        def remove(_: None): ...

        self.add = core.async_with_raw_response(add, client.add)
        self.list = core.async_with_raw_response(list, client.list)
        self.remove = core.async_with_raw_response(remove, client.remove)


class _AsyncGroupMemberClientStreaming:
    def __init__(self, client: AsyncGroupMemberClient) -> None:
        def list(_: admin_models.ListGroupMembersResponse): ...

        self.list = core.async_with_streaming_response(list, client.list)
