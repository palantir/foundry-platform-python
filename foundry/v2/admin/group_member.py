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
from foundry.v2.admin import errors as admin_errors
from foundry.v2.admin.models._group_member import GroupMember
from foundry.v2.admin.models._group_membership_expiration import GroupMembershipExpiration  # NOQA
from foundry.v2.admin.models._list_group_members_response import ListGroupMembersResponse  # NOQA
from foundry.v2.core.models._page_size import PageSize
from foundry.v2.core.models._page_token import PageToken
from foundry.v2.core.models._principal_id import PrincipalId


class GroupMemberClient:
    """
    The API client for the GroupMember Resource.

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
        self.with_streaming_response = _GroupMemberClientStreaming(
            auth=auth, hostname=hostname, config=config
        )
        self.with_raw_response = _GroupMemberClientRaw(auth=auth, hostname=hostname, config=config)

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def add(
        self,
        group_id: PrincipalId,
        *,
        principal_ids: List[PrincipalId],
        expiration: Optional[GroupMembershipExpiration] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> None:
        """

        :param group_id: groupId
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
        :raises PrincipalNotFound: A principal (User or Group) with the given PrincipalId could not be found
        """

        return self._api_client.call_api(
            RequestInfo(
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
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "principalIds": List[PrincipalId],
                        "expiration": Optional[GroupMembershipExpiration],
                    },
                ),
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "AddGroupMembersPermissionDenied": admin_errors.AddGroupMembersPermissionDenied,
                    "PrincipalNotFound": admin_errors.PrincipalNotFound,
                },
            ),
        ).decode()

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def list(
        self,
        group_id: PrincipalId,
        *,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        transitive: Optional[bool] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ResourceIterator[GroupMember]:
        """
        Lists all members (which can be a User or a Group) of a given Group.

        This is a paged endpoint. Each page may be smaller or larger than the requested page size. However,
        it is guaranteed that if there are more results available, the `nextPageToken` field will be populated.
        To get the next page, make the same request again, but set the value of the `pageToken` query parameter
        to be value of the `nextPageToken` value of the previous response. If there is no `nextPageToken` field
        in the response, you are on the last page.

        :param group_id: groupId
        :type group_id: PrincipalId
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param page_token: pageToken
        :type page_token: Optional[PageToken]
        :param transitive: transitive
        :type transitive: Optional[bool]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ResourceIterator[GroupMember]
        """

        return self._api_client.iterate_api(
            RequestInfo(
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
                response_type=ListGroupMembersResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def page(
        self,
        group_id: PrincipalId,
        *,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        transitive: Optional[bool] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ListGroupMembersResponse:
        """
        Lists all members (which can be a User or a Group) of a given Group.

        This is a paged endpoint. Each page may be smaller or larger than the requested page size. However,
        it is guaranteed that if there are more results available, the `nextPageToken` field will be populated.
        To get the next page, make the same request again, but set the value of the `pageToken` query parameter
        to be value of the `nextPageToken` value of the previous response. If there is no `nextPageToken` field
        in the response, you are on the last page.

        :param group_id: groupId
        :type group_id: PrincipalId
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param page_token: pageToken
        :type page_token: Optional[PageToken]
        :param transitive: transitive
        :type transitive: Optional[bool]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ListGroupMembersResponse
        """

        warnings.warn(
            "The client.admin.GroupMember.page(...) method has been deprecated. Please use client.admin.GroupMember.list(...) instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        return self._api_client.call_api(
            RequestInfo(
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
                response_type=ListGroupMembersResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        ).decode()

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def remove(
        self,
        group_id: PrincipalId,
        *,
        principal_ids: List[PrincipalId],
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> None:
        """

        :param group_id: groupId
        :type group_id: PrincipalId
        :param principal_ids:
        :type principal_ids: List[PrincipalId]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: None

        :raises PrincipalNotFound: A principal (User or Group) with the given PrincipalId could not be found
        :raises RemoveGroupMembersPermissionDenied: Could not remove the GroupMember.
        """

        return self._api_client.call_api(
            RequestInfo(
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
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "principalIds": List[PrincipalId],
                    },
                ),
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "PrincipalNotFound": admin_errors.PrincipalNotFound,
                    "RemoveGroupMembersPermissionDenied": admin_errors.RemoveGroupMembersPermissionDenied,
                },
            ),
        ).decode()


class _GroupMemberClientRaw:
    """
    The API client for the GroupMember Resource.

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
    def add(
        self,
        group_id: PrincipalId,
        *,
        principal_ids: List[PrincipalId],
        expiration: Optional[GroupMembershipExpiration] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[None]:
        """

        :param group_id: groupId
        :type group_id: PrincipalId
        :param principal_ids:
        :type principal_ids: List[PrincipalId]
        :param expiration:
        :type expiration: Optional[GroupMembershipExpiration]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[None]

        :raises AddGroupMembersPermissionDenied: Could not add the GroupMember.
        :raises PrincipalNotFound: A principal (User or Group) with the given PrincipalId could not be found
        """

        return self._api_client.call_api(
            RequestInfo(
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
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "principalIds": List[PrincipalId],
                        "expiration": Optional[GroupMembershipExpiration],
                    },
                ),
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "AddGroupMembersPermissionDenied": admin_errors.AddGroupMembersPermissionDenied,
                    "PrincipalNotFound": admin_errors.PrincipalNotFound,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def list(
        self,
        group_id: PrincipalId,
        *,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        transitive: Optional[bool] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[ListGroupMembersResponse]:
        """
        Lists all members (which can be a User or a Group) of a given Group.

        This is a paged endpoint. Each page may be smaller or larger than the requested page size. However,
        it is guaranteed that if there are more results available, the `nextPageToken` field will be populated.
        To get the next page, make the same request again, but set the value of the `pageToken` query parameter
        to be value of the `nextPageToken` value of the previous response. If there is no `nextPageToken` field
        in the response, you are on the last page.

        :param group_id: groupId
        :type group_id: PrincipalId
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param page_token: pageToken
        :type page_token: Optional[PageToken]
        :param transitive: transitive
        :type transitive: Optional[bool]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[ListGroupMembersResponse]
        """

        return self._api_client.call_api(
            RequestInfo(
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
                response_type=ListGroupMembersResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def page(
        self,
        group_id: PrincipalId,
        *,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        transitive: Optional[bool] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[ListGroupMembersResponse]:
        """
        Lists all members (which can be a User or a Group) of a given Group.

        This is a paged endpoint. Each page may be smaller or larger than the requested page size. However,
        it is guaranteed that if there are more results available, the `nextPageToken` field will be populated.
        To get the next page, make the same request again, but set the value of the `pageToken` query parameter
        to be value of the `nextPageToken` value of the previous response. If there is no `nextPageToken` field
        in the response, you are on the last page.

        :param group_id: groupId
        :type group_id: PrincipalId
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param page_token: pageToken
        :type page_token: Optional[PageToken]
        :param transitive: transitive
        :type transitive: Optional[bool]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[ListGroupMembersResponse]
        """

        warnings.warn(
            "The client.admin.GroupMember.page(...) method has been deprecated. Please use client.admin.GroupMember.list(...) instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        return self._api_client.call_api(
            RequestInfo(
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
                response_type=ListGroupMembersResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def remove(
        self,
        group_id: PrincipalId,
        *,
        principal_ids: List[PrincipalId],
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[None]:
        """

        :param group_id: groupId
        :type group_id: PrincipalId
        :param principal_ids:
        :type principal_ids: List[PrincipalId]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[None]

        :raises PrincipalNotFound: A principal (User or Group) with the given PrincipalId could not be found
        :raises RemoveGroupMembersPermissionDenied: Could not remove the GroupMember.
        """

        return self._api_client.call_api(
            RequestInfo(
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
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "principalIds": List[PrincipalId],
                    },
                ),
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "PrincipalNotFound": admin_errors.PrincipalNotFound,
                    "RemoveGroupMembersPermissionDenied": admin_errors.RemoveGroupMembersPermissionDenied,
                },
            ),
        )


class _GroupMemberClientStreaming:
    """
    The API client for the GroupMember Resource.

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
    def add(
        self,
        group_id: PrincipalId,
        *,
        principal_ids: List[PrincipalId],
        expiration: Optional[GroupMembershipExpiration] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[None]:
        """

        :param group_id: groupId
        :type group_id: PrincipalId
        :param principal_ids:
        :type principal_ids: List[PrincipalId]
        :param expiration:
        :type expiration: Optional[GroupMembershipExpiration]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[None]

        :raises AddGroupMembersPermissionDenied: Could not add the GroupMember.
        :raises PrincipalNotFound: A principal (User or Group) with the given PrincipalId could not be found
        """

        return self._api_client.stream_api(
            RequestInfo(
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
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "principalIds": List[PrincipalId],
                        "expiration": Optional[GroupMembershipExpiration],
                    },
                ),
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "AddGroupMembersPermissionDenied": admin_errors.AddGroupMembersPermissionDenied,
                    "PrincipalNotFound": admin_errors.PrincipalNotFound,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def list(
        self,
        group_id: PrincipalId,
        *,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        transitive: Optional[bool] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[ListGroupMembersResponse]:
        """
        Lists all members (which can be a User or a Group) of a given Group.

        This is a paged endpoint. Each page may be smaller or larger than the requested page size. However,
        it is guaranteed that if there are more results available, the `nextPageToken` field will be populated.
        To get the next page, make the same request again, but set the value of the `pageToken` query parameter
        to be value of the `nextPageToken` value of the previous response. If there is no `nextPageToken` field
        in the response, you are on the last page.

        :param group_id: groupId
        :type group_id: PrincipalId
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param page_token: pageToken
        :type page_token: Optional[PageToken]
        :param transitive: transitive
        :type transitive: Optional[bool]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[ListGroupMembersResponse]
        """

        return self._api_client.stream_api(
            RequestInfo(
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
                response_type=ListGroupMembersResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def page(
        self,
        group_id: PrincipalId,
        *,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        transitive: Optional[bool] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[ListGroupMembersResponse]:
        """
        Lists all members (which can be a User or a Group) of a given Group.

        This is a paged endpoint. Each page may be smaller or larger than the requested page size. However,
        it is guaranteed that if there are more results available, the `nextPageToken` field will be populated.
        To get the next page, make the same request again, but set the value of the `pageToken` query parameter
        to be value of the `nextPageToken` value of the previous response. If there is no `nextPageToken` field
        in the response, you are on the last page.

        :param group_id: groupId
        :type group_id: PrincipalId
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param page_token: pageToken
        :type page_token: Optional[PageToken]
        :param transitive: transitive
        :type transitive: Optional[bool]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[ListGroupMembersResponse]
        """

        warnings.warn(
            "The client.admin.GroupMember.page(...) method has been deprecated. Please use client.admin.GroupMember.list(...) instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        return self._api_client.stream_api(
            RequestInfo(
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
                response_type=ListGroupMembersResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def remove(
        self,
        group_id: PrincipalId,
        *,
        principal_ids: List[PrincipalId],
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[None]:
        """

        :param group_id: groupId
        :type group_id: PrincipalId
        :param principal_ids:
        :type principal_ids: List[PrincipalId]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[None]

        :raises PrincipalNotFound: A principal (User or Group) with the given PrincipalId could not be found
        :raises RemoveGroupMembersPermissionDenied: Could not remove the GroupMember.
        """

        return self._api_client.stream_api(
            RequestInfo(
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
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "principalIds": List[PrincipalId],
                    },
                ),
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "PrincipalNotFound": admin_errors.PrincipalNotFound,
                    "RemoveGroupMembersPermissionDenied": admin_errors.RemoveGroupMembersPermissionDenied,
                },
            ),
        )
