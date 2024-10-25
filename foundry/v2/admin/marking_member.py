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

import pydantic
from typing_extensions import Annotated
from typing_extensions import TypedDict

from foundry._core import ApiClient
from foundry._core import Auth
from foundry._core import RequestInfo
from foundry._core import ResourceIterator
from foundry._errors import handle_unexpected
from foundry.v2.admin.models._list_marking_members_response import (
    ListMarkingMembersResponse,
)  # NOQA
from foundry.v2.admin.models._marking_member import MarkingMember
from foundry.v2.core.models._marking_id import MarkingId
from foundry.v2.core.models._page_size import PageSize
from foundry.v2.core.models._page_token import PageToken
from foundry.v2.core.models._preview_mode import PreviewMode
from foundry.v2.core.models._principal_id import PrincipalId


class MarkingMemberClient:
    def __init__(self, auth: Auth, hostname: str) -> None:
        self._api_client = ApiClient(auth=auth, hostname=hostname)

    @pydantic.validate_call
    @handle_unexpected
    def add(
        self,
        marking_id: MarkingId,
        *,
        principal_ids: List[PrincipalId],
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> None:
        """

        :param marking_id: markingId
        :type marking_id: MarkingId
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
                resource_path="/v2/admin/markings/{markingId}/markingMembers/add",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "markingId": marking_id,
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

    @pydantic.validate_call
    @handle_unexpected
    def list(
        self,
        marking_id: MarkingId,
        *,
        page_size: Optional[PageSize] = None,
        preview: Optional[PreviewMode] = None,
        transitive: Optional[pydantic.StrictBool] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ResourceIterator[MarkingMember]:
        """
        Lists all principals who can view resources protected by the given Marking. Ignores the `pageSize` parameter.
        Requires `api:admin-write` because only marking administrators can view marking members.

        :param marking_id: markingId
        :type marking_id: MarkingId
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param transitive: transitive
        :type transitive: Optional[pydantic.StrictBool]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ResourceIterator[MarkingMember]
        """

        return self._api_client.iterate_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/admin/markings/{markingId}/markingMembers",
                query_params={
                    "pageSize": page_size,
                    "preview": preview,
                    "transitive": transitive,
                },
                path_params={
                    "markingId": marking_id,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ListMarkingMembersResponse,
                request_timeout=request_timeout,
            ),
        )

    @pydantic.validate_call
    @handle_unexpected
    def page(
        self,
        marking_id: MarkingId,
        *,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        preview: Optional[PreviewMode] = None,
        transitive: Optional[pydantic.StrictBool] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ListMarkingMembersResponse:
        """
        Lists all principals who can view resources protected by the given Marking. Ignores the `pageSize` parameter.
        Requires `api:admin-write` because only marking administrators can view marking members.

        :param marking_id: markingId
        :type marking_id: MarkingId
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param page_token: pageToken
        :type page_token: Optional[PageToken]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param transitive: transitive
        :type transitive: Optional[pydantic.StrictBool]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ListMarkingMembersResponse
        """

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/admin/markings/{markingId}/markingMembers",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
                    "preview": preview,
                    "transitive": transitive,
                },
                path_params={
                    "markingId": marking_id,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ListMarkingMembersResponse,
                request_timeout=request_timeout,
            ),
        )

    @pydantic.validate_call
    @handle_unexpected
    def remove(
        self,
        marking_id: MarkingId,
        *,
        principal_ids: List[PrincipalId],
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> None:
        """

        :param marking_id: markingId
        :type marking_id: MarkingId
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
                resource_path="/v2/admin/markings/{markingId}/markingMembers/remove",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "markingId": marking_id,
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
