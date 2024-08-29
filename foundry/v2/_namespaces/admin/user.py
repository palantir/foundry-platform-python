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

from typing import Annotated
from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import Union

from pydantic import Field
from pydantic import StrictInt
from pydantic import validate_call

from foundry._core import ResourceIterator
from foundry._errors import handle_unexpected
from foundry.api_client import ApiClient
from foundry.api_client import RequestInfo
from foundry.v2._namespaces.admin.group_membership import GroupMembershipResource
from foundry.v2.models._get_users_batch_request_element import GetUsersBatchRequestElement  # NOQA
from foundry.v2.models._get_users_batch_request_element_dict import (
    GetUsersBatchRequestElementDict,
)  # NOQA
from foundry.v2.models._get_users_batch_response import GetUsersBatchResponse
from foundry.v2.models._list_users_response import ListUsersResponse
from foundry.v2.models._page_size import PageSize
from foundry.v2.models._page_token import PageToken
from foundry.v2.models._preview_mode import PreviewMode
from foundry.v2.models._principal_id import PrincipalId
from foundry.v2.models._search_users_request import SearchUsersRequest
from foundry.v2.models._search_users_request_dict import SearchUsersRequestDict
from foundry.v2.models._search_users_response import SearchUsersResponse
from foundry.v2.models._user import User


class UserResource:
    def __init__(self, api_client: ApiClient) -> None:
        self._api_client = api_client

        self.GroupMembership = GroupMembershipResource(api_client=api_client)

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

        _path_params: Dict[str, Any] = {}
        _query_params: Dict[str, Any] = {}
        _header_params: Dict[str, Any] = {}
        _body_params: Any = None
        _query_params["preview"] = preview

        _path_params["userId"] = user_id

        return self._api_client.call_api(
            RequestInfo(
                method="DELETE",
                resource_path="/v2/admin/users/{userId}",
                query_params=_query_params,
                path_params=_path_params,
                header_params=_header_params,
                body=_body_params,
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

        _path_params: Dict[str, Any] = {}
        _query_params: Dict[str, Any] = {}
        _header_params: Dict[str, Any] = {}
        _body_params: Any = None
        _query_params["preview"] = preview

        _path_params["userId"] = user_id

        _header_params["Accept"] = "application/json"

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/admin/users/{userId}",
                query_params=_query_params,
                path_params=_path_params,
                header_params=_header_params,
                body=_body_params,
                body_type=None,
                response_type=User,
                request_timeout=request_timeout,
            ),
        )

    @validate_call
    @handle_unexpected
    def get_batch(
        self,
        body: Union[List[GetUsersBatchRequestElement], List[GetUsersBatchRequestElementDict]],
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> GetUsersBatchResponse:
        """
        Execute multiple get requests on User.

        The maximum batch size for this endpoint is 500.
        :param body: Body of the request
        :type body: Union[List[GetUsersBatchRequestElement], List[GetUsersBatchRequestElementDict]]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: GetUsersBatchResponse
        """

        _path_params: Dict[str, Any] = {}
        _query_params: Dict[str, Any] = {}
        _header_params: Dict[str, Any] = {}
        _body_params: Any = body
        _query_params["preview"] = preview

        _header_params["Content-Type"] = "application/json"

        _header_params["Accept"] = "application/json"

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/admin/users/getBatch",
                query_params=_query_params,
                path_params=_path_params,
                header_params=_header_params,
                body=_body_params,
                body_type=Union[
                    List[GetUsersBatchRequestElement], List[GetUsersBatchRequestElementDict]
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

        _path_params: Dict[str, Any] = {}
        _query_params: Dict[str, Any] = {}
        _header_params: Dict[str, Any] = {}
        _body_params: Any = None
        _query_params["preview"] = preview

        _header_params["Accept"] = "application/json"

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/admin/users/getCurrent",
                query_params=_query_params,
                path_params=_path_params,
                header_params=_header_params,
                body=_body_params,
                body_type=None,
                response_type=User,
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

        _path_params: Dict[str, Any] = {}
        _query_params: Dict[str, Any] = {}
        _header_params: Dict[str, Any] = {}
        _body_params: Any = None
        _query_params["pageSize"] = page_size

        _query_params["preview"] = preview

        _header_params["Accept"] = "application/json"

        return self._api_client.iterate_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/admin/users",
                query_params=_query_params,
                path_params=_path_params,
                header_params=_header_params,
                body=_body_params,
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

        _path_params: Dict[str, Any] = {}
        _query_params: Dict[str, Any] = {}
        _header_params: Dict[str, Any] = {}
        _body_params: Any = None
        _query_params["pageSize"] = page_size

        _query_params["pageToken"] = page_token

        _query_params["preview"] = preview

        _header_params["Accept"] = "application/json"

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/admin/users",
                query_params=_query_params,
                path_params=_path_params,
                header_params=_header_params,
                body=_body_params,
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

        _path_params: Dict[str, Any] = {}
        _query_params: Dict[str, Any] = {}
        _header_params: Dict[str, Any] = {}
        _body_params: Any = None
        _query_params["preview"] = preview

        _path_params["userId"] = user_id

        _header_params["Accept"] = "application/octet-stream"

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/admin/users/{userId}/profilePicture",
                query_params=_query_params,
                path_params=_path_params,
                header_params=_header_params,
                body=_body_params,
                body_type=None,
                response_type=bytes,
                request_timeout=request_timeout,
            ),
        )

    @validate_call
    @handle_unexpected
    def search(
        self,
        search_users_request: Union[SearchUsersRequest, SearchUsersRequestDict],
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> SearchUsersResponse:
        """

        :param search_users_request: Body of the request
        :type search_users_request: Union[SearchUsersRequest, SearchUsersRequestDict]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: SearchUsersResponse
        """

        _path_params: Dict[str, Any] = {}
        _query_params: Dict[str, Any] = {}
        _header_params: Dict[str, Any] = {}
        _body_params: Any = search_users_request
        _query_params["preview"] = preview

        _header_params["Content-Type"] = "application/json"

        _header_params["Accept"] = "application/json"

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/admin/users/search",
                query_params=_query_params,
                path_params=_path_params,
                header_params=_header_params,
                body=_body_params,
                body_type=Union[SearchUsersRequest, SearchUsersRequestDict],
                response_type=SearchUsersResponse,
                request_timeout=request_timeout,
            ),
        )