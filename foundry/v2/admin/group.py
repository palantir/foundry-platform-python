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
from pydantic import StrictStr
from pydantic import validate_call
from typing_extensions import Annotated
from typing_extensions import TypedDict

from foundry._core import ApiClient
from foundry._core import Auth
from foundry._core import RequestInfo
from foundry._core import ResourceIterator
from foundry._errors import handle_unexpected
from foundry.v2.admin.group_member import GroupMemberClient
from foundry.v2.admin.models._attribute_name import AttributeName
from foundry.v2.admin.models._attribute_values import AttributeValues
from foundry.v2.admin.models._get_groups_batch_request_element_dict import (
    GetGroupsBatchRequestElementDict,
)  # NOQA
from foundry.v2.admin.models._get_groups_batch_response import GetGroupsBatchResponse
from foundry.v2.admin.models._group import Group
from foundry.v2.admin.models._group_name import GroupName
from foundry.v2.admin.models._group_search_filter_dict import GroupSearchFilterDict
from foundry.v2.admin.models._list_groups_response import ListGroupsResponse
from foundry.v2.admin.models._search_groups_response import SearchGroupsResponse
from foundry.v2.core.models._organization_rid import OrganizationRid
from foundry.v2.core.models._page_size import PageSize
from foundry.v2.core.models._page_token import PageToken
from foundry.v2.core.models._preview_mode import PreviewMode
from foundry.v2.core.models._principal_id import PrincipalId


class GroupClient:
    def __init__(self, auth: Auth, hostname: str) -> None:
        self._api_client = ApiClient(auth=auth, hostname=hostname)

        self.GroupMember = GroupMemberClient(auth=auth, hostname=hostname)

    @validate_call
    @handle_unexpected
    def create(
        self,
        *,
        attributes: Dict[AttributeName, AttributeValues],
        name: GroupName,
        organizations: List[OrganizationRid],
        description: Optional[StrictStr] = None,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> Group:
        """
        Creates a new Group.
        :param attributes: A map of the Group's attributes. Attributes prefixed with "multipass:" are reserved for internal use by Foundry and are subject to change.
        :type attributes: Dict[AttributeName, AttributeValues]
        :param name: The name of the Group.
        :type name: GroupName
        :param organizations: The RIDs of the Organizations whose members can see this group. At least one Organization RID must be listed.
        :type organizations: List[OrganizationRid]
        :param description: A description of the Group.
        :type description: Optional[StrictStr]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: Group
        """

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/admin/groups",
                query_params={
                    "preview": preview,
                },
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
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "name": GroupName,
                        "organizations": List[OrganizationRid],
                        "description": Optional[StrictStr],
                        "attributes": Dict[AttributeName, AttributeValues],
                    },
                ),
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
        Delete the Group with the specified id.
        :param group_id: groupId
        :type group_id: PrincipalId
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
                resource_path="/v2/admin/groups/{groupId}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "groupId": group_id,
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
        group_id: PrincipalId,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> Group:
        """
        Get the Group with the specified id.
        :param group_id: groupId
        :type group_id: PrincipalId
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: Group
        """

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/admin/groups/{groupId}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "groupId": group_id,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=Group,
                request_timeout=request_timeout,
            ),
        )

    @validate_call
    @handle_unexpected
    def get_batch(
        self,
        body: Annotated[List[GetGroupsBatchRequestElementDict], Len(min_length=1, max_length=500)],
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> GetGroupsBatchResponse:
        """
        Execute multiple get requests on Group.

        The maximum batch size for this endpoint is 500.
        :param body: Body of the request
        :type body: Annotated[List[GetGroupsBatchRequestElementDict], Len(min_length=1, max_length=500)]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: GetGroupsBatchResponse
        """

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/admin/groups/getBatch",
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
                    List[GetGroupsBatchRequestElementDict], Len(min_length=1, max_length=500)
                ],
                response_type=GetGroupsBatchResponse,
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
        Lists all Groups.

        This is a paged endpoint. Each page may be smaller or larger than the requested page size. However, it is guaranteed that if there are more results available, the `nextPageToken` field will be populated. To get the next page, make the same request again, but set the value of the `pageToken` query parameter to be value of the `nextPageToken` value of the previous response. If there is no `nextPageToken` field in the response, you are on the last page.
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ResourceIterator[Group]
        """

        return self._api_client.iterate_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/admin/groups",
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
        Lists all Groups.

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
        :rtype: ListGroupsResponse
        """

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/admin/groups",
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
                response_type=ListGroupsResponse,
                request_timeout=request_timeout,
            ),
        )

    @validate_call
    @handle_unexpected
    def search(
        self,
        *,
        where: GroupSearchFilterDict,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> SearchGroupsResponse:
        """

        :param where:
        :type where: GroupSearchFilterDict
        :param page_size:
        :type page_size: Optional[PageSize]
        :param page_token:
        :type page_token: Optional[PageToken]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: SearchGroupsResponse
        """

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/admin/groups/search",
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
                        "where": GroupSearchFilterDict,
                        "pageSize": Optional[PageSize],
                        "pageToken": Optional[PageToken],
                    },
                ),
                response_type=SearchGroupsResponse,
                request_timeout=request_timeout,
            ),
        )
