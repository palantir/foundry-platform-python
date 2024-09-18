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

from typing import Any
from typing import Dict
from typing import List
from typing import Optional

from annotated_types import Len
from pydantic import Field
from pydantic import StrictInt
from pydantic import validate_call
from typing_extensions import Annotated
from typing_extensions import TypedDict

from foundry._core import ApiClient
from foundry._core import Auth
from foundry._core import RequestInfo
from foundry._core import ResourceIterator
from foundry._errors import handle_unexpected
from foundry.v2.admin.group_membership import GroupMembershipClient
from foundry.v2.admin.models._get_user_markings_response import GetUserMarkingsResponse
from foundry.v2.admin.models._get_users_batch_request_element_dict import (
    GetUsersBatchRequestElementDict,
)  # NOQA
from foundry.v2.admin.models._get_users_batch_response import GetUsersBatchResponse
from foundry.v2.admin.models._list_users_response import ListUsersResponse
from foundry.v2.admin.models._search_users_response import SearchUsersResponse
from foundry.v2.admin.models._user import User
from foundry.v2.admin.models._user_search_filter_dict import UserSearchFilterDict
from foundry.v2.core.models._page_size import PageSize
from foundry.v2.core.models._page_token import PageToken
from foundry.v2.core.models._preview_mode import PreviewMode
from foundry.v2.core.models._principal_id import PrincipalId


class UserClient:
    def __init__(self, auth: Auth, hostname: str) -> None:
        self._api_client = ApiClient(auth=auth, hostname=hostname)

        self.GroupMembership = GroupMembershipClient(auth=auth, hostname=hostname)

    @validate_call
    @handle_unexpected
    def delete(
        self,
        user_id: PrincipalId,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> None:
        """
        Delete the User with the specified id.
        :param user_id: userId
        :type user_id: PrincipalId
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: None
        """

        return self._api_client.call_api(
            RequestInfo(
                method="DELETE",
                resource_path="/v2/admin/users/{userId}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "userId": user_id,
                },
                header_params={},
                body=None,
                body_type=None,
                response_type=None,
                request_timeout=request_timeout,
            ),
        )

    @validate_call
    @handle_unexpected
    def get(
        self,
        user_id: PrincipalId,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> User:
        """
        Get the User with the specified id.
        :param user_id: userId
        :type user_id: PrincipalId
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: User
        """

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/admin/users/{userId}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "userId": user_id,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=User,
                request_timeout=request_timeout,
            ),
        )

    @validate_call
    @handle_unexpected
    def get_batch(
        self,
        body: Annotated[List[GetUsersBatchRequestElementDict], Len(min_length=1, max_length=500)],
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> GetUsersBatchResponse:
        """
        Execute multiple get requests on User.

        The maximum batch size for this endpoint is 500.
        :param body: Body of the request
        :type body: Annotated[List[GetUsersBatchRequestElementDict], Len(min_length=1, max_length=500)]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: GetUsersBatchResponse
        """

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/admin/users/getBatch",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body=body,
                body_type=Annotated[
                    List[GetUsersBatchRequestElementDict], Len(min_length=1, max_length=500)
                ],
                response_type=GetUsersBatchResponse,
                request_timeout=request_timeout,
            ),
        )

    @validate_call
    @handle_unexpected
    def get_current(
        self,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> User:
        """

        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: User
        """

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/admin/users/getCurrent",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=User,
                request_timeout=request_timeout,
            ),
        )

    @validate_call
    @handle_unexpected
    def get_markings(
        self,
        user_id: PrincipalId,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> GetUserMarkingsResponse:
        """
        Retrieve Markings that the user is currently a member of.
        :param user_id: userId
        :type user_id: PrincipalId
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: GetUserMarkingsResponse
        """

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/admin/users/{userId}/getMarkings",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "userId": user_id,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=GetUserMarkingsResponse,
                request_timeout=request_timeout,
            ),
        )

    @validate_call
    @handle_unexpected
    def list(
        self,
        *,
        page_size: Optional[PageSize] = None,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> ResourceIterator[User]:
        """
        Lists all Users.

        This is a paged endpoint. Each page may be smaller or larger than the requested page size. However, it is guaranteed that if there are more results available, the `nextPageToken` field will be populated. To get the next page, make the same request again, but set the value of the `pageToken` query parameter to be value of the `nextPageToken` value of the previous response. If there is no `nextPageToken` field in the response, you are on the last page.
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ResourceIterator[User]
        """

        return self._api_client.iterate_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/admin/users",
                query_params={
                    "pageSize": page_size,
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ListUsersResponse,
                request_timeout=request_timeout,
            ),
        )

    @validate_call
    @handle_unexpected
    def page(
        self,
        *,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> ListUsersResponse:
        """
        Lists all Users.

        This is a paged endpoint. Each page may be smaller or larger than the requested page size. However, it is guaranteed that if there are more results available, the `nextPageToken` field will be populated. To get the next page, make the same request again, but set the value of the `pageToken` query parameter to be value of the `nextPageToken` value of the previous response. If there is no `nextPageToken` field in the response, you are on the last page.
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param page_token: pageToken
        :type page_token: Optional[PageToken]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ListUsersResponse
        """

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/admin/users",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ListUsersResponse,
                request_timeout=request_timeout,
            ),
        )

    @validate_call
    @handle_unexpected
    def profile_picture(
        self,
        user_id: PrincipalId,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> bytes:
        """

        :param user_id: userId
        :type user_id: PrincipalId
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: bytes
        """

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/admin/users/{userId}/profilePicture",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "userId": user_id,
                },
                header_params={
                    "Accept": "application/octet-stream",
                },
                body=None,
                body_type=None,
                response_type=bytes,
                request_timeout=request_timeout,
            ),
        )

    @validate_call
    @handle_unexpected
    def search(
        self,
        *,
        where: UserSearchFilterDict,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> SearchUsersResponse:
        """

        :param where:
        :type where: UserSearchFilterDict
        :param page_size:
        :type page_size: Optional[PageSize]
        :param page_token:
        :type page_token: Optional[PageToken]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: SearchUsersResponse
        """

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/admin/users/search",
                query_params={
                    "preview": preview,
                },
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
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "where": UserSearchFilterDict,
                        "pageSize": Optional[PageSize],
                        "pageToken": Optional[PageToken],
                    },
                ),
                response_type=SearchUsersResponse,
                request_timeout=request_timeout,
            ),
        )
