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
from typing import Optional

import pydantic
from typing_extensions import Annotated

from foundry._core import ApiClient
from foundry._core import ApiResponse
from foundry._core import Auth
from foundry._core import Config
from foundry._core import RequestInfo
from foundry._core import ResourceIterator
from foundry._core import StreamingContextManager
from foundry._core.utils import maybe_ignore_preview
from foundry._errors import handle_unexpected
from foundry.v2.admin.models._group_membership import GroupMembership
from foundry.v2.admin.models._list_group_memberships_response import (
    ListGroupMembershipsResponse,
)  # NOQA
from foundry.v2.core.models._page_size import PageSize
from foundry.v2.core.models._page_token import PageToken
from foundry.v2.core.models._principal_id import PrincipalId


class GroupMembershipClient:
    """
    The API client for the GroupMembership Resource.

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
        self.with_streaming_response = _GroupMembershipClientStreaming(
            auth=auth, hostname=hostname, config=config
        )
        self.with_raw_response = _GroupMembershipClientRaw(
            auth=auth, hostname=hostname, config=config
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def list(
        self,
        user_id: PrincipalId,
        *,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        transitive: Optional[bool] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ResourceIterator[GroupMembership]:
        """
        Lists all Groups a given User is a member of.

        This is a paged endpoint. Each page may be smaller or larger than the requested page size. However,
        it is guaranteed that if there are more results available, the `nextPageToken` field will be populated.
        To get the next page, make the same request again, but set the value of the `pageToken` query parameter
        to be value of the `nextPageToken` value of the previous response. If there is no `nextPageToken` field
        in the response, you are on the last page.

        :param user_id: userId
        :type user_id: PrincipalId
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param page_token: pageToken
        :type page_token: Optional[PageToken]
        :param transitive: transitive
        :type transitive: Optional[bool]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ResourceIterator[GroupMembership]
        """

        return self._api_client.iterate_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/admin/users/{userId}/groupMemberships",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
                    "transitive": transitive,
                },
                path_params={
                    "userId": user_id,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ListGroupMembershipsResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def page(
        self,
        user_id: PrincipalId,
        *,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        transitive: Optional[bool] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ListGroupMembershipsResponse:
        """
        Lists all Groups a given User is a member of.

        This is a paged endpoint. Each page may be smaller or larger than the requested page size. However,
        it is guaranteed that if there are more results available, the `nextPageToken` field will be populated.
        To get the next page, make the same request again, but set the value of the `pageToken` query parameter
        to be value of the `nextPageToken` value of the previous response. If there is no `nextPageToken` field
        in the response, you are on the last page.

        :param user_id: userId
        :type user_id: PrincipalId
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param page_token: pageToken
        :type page_token: Optional[PageToken]
        :param transitive: transitive
        :type transitive: Optional[bool]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ListGroupMembershipsResponse
        """

        warnings.warn(
            "The client.admin.GroupMembership.page(...) method has been deprecated. Please use client.admin.GroupMembership.list(...) instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/admin/users/{userId}/groupMemberships",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
                    "transitive": transitive,
                },
                path_params={
                    "userId": user_id,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ListGroupMembershipsResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        ).decode()


class _GroupMembershipClientRaw:
    """
    The API client for the GroupMembership Resource.

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
    def list(
        self,
        user_id: PrincipalId,
        *,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        transitive: Optional[bool] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[ListGroupMembershipsResponse]:
        """
        Lists all Groups a given User is a member of.

        This is a paged endpoint. Each page may be smaller or larger than the requested page size. However,
        it is guaranteed that if there are more results available, the `nextPageToken` field will be populated.
        To get the next page, make the same request again, but set the value of the `pageToken` query parameter
        to be value of the `nextPageToken` value of the previous response. If there is no `nextPageToken` field
        in the response, you are on the last page.

        :param user_id: userId
        :type user_id: PrincipalId
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param page_token: pageToken
        :type page_token: Optional[PageToken]
        :param transitive: transitive
        :type transitive: Optional[bool]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[ListGroupMembershipsResponse]
        """

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/admin/users/{userId}/groupMemberships",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
                    "transitive": transitive,
                },
                path_params={
                    "userId": user_id,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ListGroupMembershipsResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def page(
        self,
        user_id: PrincipalId,
        *,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        transitive: Optional[bool] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[ListGroupMembershipsResponse]:
        """
        Lists all Groups a given User is a member of.

        This is a paged endpoint. Each page may be smaller or larger than the requested page size. However,
        it is guaranteed that if there are more results available, the `nextPageToken` field will be populated.
        To get the next page, make the same request again, but set the value of the `pageToken` query parameter
        to be value of the `nextPageToken` value of the previous response. If there is no `nextPageToken` field
        in the response, you are on the last page.

        :param user_id: userId
        :type user_id: PrincipalId
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param page_token: pageToken
        :type page_token: Optional[PageToken]
        :param transitive: transitive
        :type transitive: Optional[bool]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[ListGroupMembershipsResponse]
        """

        warnings.warn(
            "The client.admin.GroupMembership.page(...) method has been deprecated. Please use client.admin.GroupMembership.list(...) instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/admin/users/{userId}/groupMemberships",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
                    "transitive": transitive,
                },
                path_params={
                    "userId": user_id,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ListGroupMembershipsResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )


class _GroupMembershipClientStreaming:
    """
    The API client for the GroupMembership Resource.

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
    def list(
        self,
        user_id: PrincipalId,
        *,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        transitive: Optional[bool] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[ListGroupMembershipsResponse]:
        """
        Lists all Groups a given User is a member of.

        This is a paged endpoint. Each page may be smaller or larger than the requested page size. However,
        it is guaranteed that if there are more results available, the `nextPageToken` field will be populated.
        To get the next page, make the same request again, but set the value of the `pageToken` query parameter
        to be value of the `nextPageToken` value of the previous response. If there is no `nextPageToken` field
        in the response, you are on the last page.

        :param user_id: userId
        :type user_id: PrincipalId
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param page_token: pageToken
        :type page_token: Optional[PageToken]
        :param transitive: transitive
        :type transitive: Optional[bool]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[ListGroupMembershipsResponse]
        """

        return self._api_client.stream_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/admin/users/{userId}/groupMemberships",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
                    "transitive": transitive,
                },
                path_params={
                    "userId": user_id,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ListGroupMembershipsResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def page(
        self,
        user_id: PrincipalId,
        *,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        transitive: Optional[bool] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[ListGroupMembershipsResponse]:
        """
        Lists all Groups a given User is a member of.

        This is a paged endpoint. Each page may be smaller or larger than the requested page size. However,
        it is guaranteed that if there are more results available, the `nextPageToken` field will be populated.
        To get the next page, make the same request again, but set the value of the `pageToken` query parameter
        to be value of the `nextPageToken` value of the previous response. If there is no `nextPageToken` field
        in the response, you are on the last page.

        :param user_id: userId
        :type user_id: PrincipalId
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param page_token: pageToken
        :type page_token: Optional[PageToken]
        :param transitive: transitive
        :type transitive: Optional[bool]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[ListGroupMembershipsResponse]
        """

        warnings.warn(
            "The client.admin.GroupMembership.page(...) method has been deprecated. Please use client.admin.GroupMembership.list(...) instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        return self._api_client.stream_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/admin/users/{userId}/groupMemberships",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
                    "transitive": transitive,
                },
                path_params={
                    "userId": user_id,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ListGroupMembershipsResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )
