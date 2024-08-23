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
from typing import Optional
from typing import Union

from pydantic import Field
from pydantic import StrictBool
from pydantic import StrictInt
from pydantic import validate_call

from foundry._core import ResourceIterator
from foundry._errors import handle_unexpected
from foundry.api_client import ApiClient
from foundry.api_client import RequestInfo
from foundry.v2.models._add_group_members_request import AddGroupMembersRequest
from foundry.v2.models._add_group_members_request_dict import AddGroupMembersRequestDict
from foundry.v2.models._group_member import GroupMember
from foundry.v2.models._list_group_members_response import ListGroupMembersResponse
from foundry.v2.models._page_size import PageSize
from foundry.v2.models._page_token import PageToken
from foundry.v2.models._preview_mode import PreviewMode
from foundry.v2.models._principal_id import PrincipalId
from foundry.v2.models._remove_group_members_request import RemoveGroupMembersRequest
from foundry.v2.models._remove_group_members_request_dict import (
    RemoveGroupMembersRequestDict,
)  # NOQA


class GroupMemberResource:
    def __init__(self, api_client: ApiClient) -> None:
        self._api_client = api_client

    @validate_call
    @handle_unexpected
    def add(
        self,
        group_id: PrincipalId,
        add_group_members_request: Union[AddGroupMembersRequest, AddGroupMembersRequestDict],
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> None:
        """

        :param group_id: groupId
        :type group_id: PrincipalId
        :param add_group_members_request: Body of the request
        :type add_group_members_request: Union[AddGroupMembersRequest, AddGroupMembersRequestDict]
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
        _body_params: Any = add_group_members_request
        _query_params["preview"] = preview

        _path_params["groupId"] = group_id

        _header_params["Content-Type"] = "application/json"

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/admin/groups/{groupId}/groupMembers/add",
                query_params=_query_params,
                path_params=_path_params,
                header_params=_header_params,
                body=_body_params,
                body_type=Union[AddGroupMembersRequest, AddGroupMembersRequestDict],
                response_type=None,
                request_timeout=request_timeout,
            ),
        )

    @validate_call
    @handle_unexpected
    def list(
        self,
        group_id: PrincipalId,
        *,
        page_size: Optional[PageSize] = None,
        preview: Optional[PreviewMode] = None,
        transitive: Optional[StrictBool] = None,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> ResourceIterator[GroupMember]:
        """
        Lists all GroupMembers.

        This is a paged endpoint. Each page may be smaller or larger than the requested page size. However, it is guaranteed that if there are more results available, the `nextPageToken` field will be populated. To get the next page, make the same request again, but set the value of the `pageToken` query parameter to be value of the `nextPageToken` value of the previous response. If there is no `nextPageToken` field in the response, you are on the last page.
        :param group_id: groupId
        :type group_id: PrincipalId
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param transitive: transitive
        :type transitive: Optional[StrictBool]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ResourceIterator[GroupMember]
        """

        _path_params: Dict[str, Any] = {}
        _query_params: Dict[str, Any] = {}
        _header_params: Dict[str, Any] = {}
        _body_params: Any = None
        _query_params["pageSize"] = page_size

        _query_params["preview"] = preview

        _query_params["transitive"] = transitive

        _path_params["groupId"] = group_id

        _header_params["Accept"] = "application/json"

        return self._api_client.iterate_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/admin/groups/{groupId}/groupMembers",
                query_params=_query_params,
                path_params=_path_params,
                header_params=_header_params,
                body=_body_params,
                body_type=None,
                response_type=ListGroupMembersResponse,
                request_timeout=request_timeout,
            ),
        )

    @validate_call
    @handle_unexpected
    def page(
        self,
        group_id: PrincipalId,
        *,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        preview: Optional[PreviewMode] = None,
        transitive: Optional[StrictBool] = None,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> ListGroupMembersResponse:
        """
        Lists all GroupMembers.

        This is a paged endpoint. Each page may be smaller or larger than the requested page size. However, it is guaranteed that if there are more results available, the `nextPageToken` field will be populated. To get the next page, make the same request again, but set the value of the `pageToken` query parameter to be value of the `nextPageToken` value of the previous response. If there is no `nextPageToken` field in the response, you are on the last page.
        :param group_id: groupId
        :type group_id: PrincipalId
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param page_token: pageToken
        :type page_token: Optional[PageToken]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param transitive: transitive
        :type transitive: Optional[StrictBool]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ListGroupMembersResponse
        """

        _path_params: Dict[str, Any] = {}
        _query_params: Dict[str, Any] = {}
        _header_params: Dict[str, Any] = {}
        _body_params: Any = None
        _query_params["pageSize"] = page_size

        _query_params["pageToken"] = page_token

        _query_params["preview"] = preview

        _query_params["transitive"] = transitive

        _path_params["groupId"] = group_id

        _header_params["Accept"] = "application/json"

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/admin/groups/{groupId}/groupMembers",
                query_params=_query_params,
                path_params=_path_params,
                header_params=_header_params,
                body=_body_params,
                body_type=None,
                response_type=ListGroupMembersResponse,
                request_timeout=request_timeout,
            ),
        )

    @validate_call
    @handle_unexpected
    def remove(
        self,
        group_id: PrincipalId,
        remove_group_members_request: Union[
            RemoveGroupMembersRequest, RemoveGroupMembersRequestDict
        ],
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> None:
        """

        :param group_id: groupId
        :type group_id: PrincipalId
        :param remove_group_members_request: Body of the request
        :type remove_group_members_request: Union[RemoveGroupMembersRequest, RemoveGroupMembersRequestDict]
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
        _body_params: Any = remove_group_members_request
        _query_params["preview"] = preview

        _path_params["groupId"] = group_id

        _header_params["Content-Type"] = "application/json"

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/admin/groups/{groupId}/groupMembers/remove",
                query_params=_query_params,
                path_params=_path_params,
                header_params=_header_params,
                body=_body_params,
                body_type=Union[RemoveGroupMembersRequest, RemoveGroupMembersRequestDict],
                response_type=None,
                request_timeout=request_timeout,
            ),
        )
