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
from pydantic import StrictInt
from pydantic import validate_call

from foundry._core import ResourceIterator
from foundry._errors import handle_unexpected
from foundry._namespaces.admin.group_member import GroupMemberResource
from foundry.api_client import ApiClient
from foundry.api_client import RequestInfo
from foundry.models._create_group_request import CreateGroupRequest
from foundry.models._create_group_request_dict import CreateGroupRequestDict
from foundry.models._group import Group
from foundry.models._list_groups_response import ListGroupsResponse
from foundry.models._page_size import PageSize
from foundry.models._page_token import PageToken
from foundry.models._preview_mode import PreviewMode
from foundry.models._principal_id import PrincipalId
from foundry.models._search_groups_request import SearchGroupsRequest
from foundry.models._search_groups_request_dict import SearchGroupsRequestDict
from foundry.models._search_groups_response import SearchGroupsResponse


class GroupResource:
    def __init__(self, api_client: ApiClient) -> None:
        self._api_client = api_client

        self.GroupMember = GroupMemberResource(api_client=api_client)

    @validate_call
    @handle_unexpected
    def create(
        self,
        create_group_request: Union[CreateGroupRequest, CreateGroupRequestDict],
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> Group:
        """
        Creates a new Group
        :param create_group_request: Body of the request
        :type create_group_request: Union[CreateGroupRequest, CreateGroupRequestDict]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: Group
        """

        _path_params: Dict[str, Any] = {}
        _query_params: Dict[str, Any] = {}
        _header_params: Dict[str, Any] = {}
        _body_params: Any = create_group_request
        _query_params["preview"] = preview

        _header_params["Content-Type"] = "application/json"

        _header_params["Accept"] = "application/json"

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/admin/groups",
                query_params=_query_params,
                path_params=_path_params,
                header_params=_header_params,
                body=_body_params,
                body_type=Union[CreateGroupRequest, CreateGroupRequestDict],
                response_type=Group,
                request_timeout=request_timeout,
            ),
        )

    @validate_call
    @handle_unexpected
    def delete(
        self,
        group_id: PrincipalId,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> None:
        """
        Deletes the given Group
        :param group_id: groupId
        :type group_id: PrincipalId
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

        _path_params["groupId"] = group_id

        return self._api_client.call_api(
            RequestInfo(
                method="DELETE",
                resource_path="/v2/admin/groups/{groupId}",
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
        group_id: PrincipalId,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> Group:
        """
        Get the Group
        :param group_id: groupId
        :type group_id: PrincipalId
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: Group
        """

        _path_params: Dict[str, Any] = {}
        _query_params: Dict[str, Any] = {}
        _header_params: Dict[str, Any] = {}
        _body_params: Any = None
        _query_params["preview"] = preview

        _path_params["groupId"] = group_id

        _header_params["Accept"] = "application/json"

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/admin/groups/{groupId}",
                query_params=_query_params,
                path_params=_path_params,
                header_params=_header_params,
                body=_body_params,
                body_type=None,
                response_type=Group,
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
    ) -> ResourceIterator[Group]:
        """
        Lists all Groups
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ResourceIterator[Group]
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
                resource_path="/v2/admin/groups",
                query_params=_query_params,
                path_params=_path_params,
                header_params=_header_params,
                body=_body_params,
                body_type=None,
                response_type=ListGroupsResponse,
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
    ) -> ListGroupsResponse:
        """
        Lists all Groups
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param page_token: pageToken
        :type page_token: Optional[PageToken]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ListGroupsResponse
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
                resource_path="/v2/admin/groups",
                query_params=_query_params,
                path_params=_path_params,
                header_params=_header_params,
                body=_body_params,
                body_type=None,
                response_type=ListGroupsResponse,
                request_timeout=request_timeout,
            ),
        )

    @validate_call
    @handle_unexpected
    def search(
        self,
        search_groups_request: Union[SearchGroupsRequest, SearchGroupsRequestDict],
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> SearchGroupsResponse:
        """

        :param search_groups_request: Body of the request
        :type search_groups_request: Union[SearchGroupsRequest, SearchGroupsRequestDict]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: SearchGroupsResponse
        """

        _path_params: Dict[str, Any] = {}
        _query_params: Dict[str, Any] = {}
        _header_params: Dict[str, Any] = {}
        _body_params: Any = search_groups_request
        _query_params["preview"] = preview

        _header_params["Content-Type"] = "application/json"

        _header_params["Accept"] = "application/json"

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/admin/groups/search",
                query_params=_query_params,
                path_params=_path_params,
                header_params=_header_params,
                body=_body_params,
                body_type=Union[SearchGroupsRequest, SearchGroupsRequestDict],
                response_type=SearchGroupsResponse,
                request_timeout=request_timeout,
            ),
        )
