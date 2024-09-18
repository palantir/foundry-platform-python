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

from pydantic import Field
from pydantic import StrictBool
from pydantic import StrictInt
from pydantic import validate_call
from typing_extensions import Annotated
from typing_extensions import TypedDict

from foundry._core import ApiClient
from foundry._core import Auth
from foundry._core import RequestInfo
from foundry._core import ResourceIterator
from foundry._errors import handle_unexpected
from foundry.v2.admin.models._group_member import GroupMember
from foundry.v2.admin.models._group_membership_expiration import GroupMembershipExpiration  # NOQA
from foundry.v2.admin.models._list_group_members_response import ListGroupMembersResponse  # NOQA
from foundry.v2.core.models._page_size import PageSize
from foundry.v2.core.models._page_token import PageToken
from foundry.v2.core.models._preview_mode import PreviewMode
from foundry.v2.core.models._principal_id import PrincipalId


class GroupMemberClient:
    def __init__(self, auth: Auth, hostname: str) -> None:
        self._api_client = ApiClient(auth=auth, hostname=hostname)

    @validate_call
    @handle_unexpected
    def add(
        self,
        group_id: PrincipalId,
        *,
        principal_ids: List[PrincipalId],
        expiration: Optional[GroupMembershipExpiration] = None,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> None:
        """

        :param group_id: groupId
        :type group_id: PrincipalId
        :param principal_ids:
        :type principal_ids: List[PrincipalId]
        :param expiration:
        :type expiration: Optional[GroupMembershipExpiration]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: None
        """

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/admin/groups/{groupId}/groupMembers/add",
                query_params={
                    "preview": preview,
                },
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

        return self._api_client.iterate_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/admin/groups/{groupId}/groupMembers",
                query_params={
                    "pageSize": page_size,
                    "preview": preview,
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

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/admin/groups/{groupId}/groupMembers",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
                    "preview": preview,
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
            ),
        )

    @validate_call
    @handle_unexpected
    def remove(
        self,
        group_id: PrincipalId,
        *,
        principal_ids: List[PrincipalId],
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> None:
        """

        :param group_id: groupId
        :type group_id: PrincipalId
        :param principal_ids:
        :type principal_ids: List[PrincipalId]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: None
        """

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/admin/groups/{groupId}/groupMembers/remove",
                query_params={
                    "preview": preview,
                },
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
            ),
        )
