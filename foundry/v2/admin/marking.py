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
from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import Union

import pydantic
from annotated_types import Len
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
from foundry.v2.admin.marking_member import MarkingMemberClient
from foundry.v2.admin.marking_role_assignment import MarkingRoleAssignmentClient
from foundry.v2.admin.models._get_markings_batch_request_element import (
    GetMarkingsBatchRequestElement,
)  # NOQA
from foundry.v2.admin.models._get_markings_batch_request_element_dict import (
    GetMarkingsBatchRequestElementDict,
)  # NOQA
from foundry.v2.admin.models._get_markings_batch_response import GetMarkingsBatchResponse  # NOQA
from foundry.v2.admin.models._list_markings_response import ListMarkingsResponse
from foundry.v2.admin.models._marking import Marking
from foundry.v2.admin.models._marking_category_id import MarkingCategoryId
from foundry.v2.admin.models._marking_name import MarkingName
from foundry.v2.admin.models._marking_role_update import MarkingRoleUpdate
from foundry.v2.admin.models._marking_role_update_dict import MarkingRoleUpdateDict
from foundry.v2.core.models._marking_id import MarkingId
from foundry.v2.core.models._page_size import PageSize
from foundry.v2.core.models._page_token import PageToken
from foundry.v2.core.models._preview_mode import PreviewMode
from foundry.v2.core.models._principal_id import PrincipalId


class MarkingClient:
    """
    The API client for the Marking Resource.

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
        self._api_client = ApiClient(auth=auth, hostname=hostname, config=config)
        self.with_streaming_response = _MarkingClientStreaming(
            auth=auth, hostname=hostname, config=config
        )
        self.with_raw_response = _MarkingClientRaw(auth=auth, hostname=hostname, config=config)
        self.MarkingMember = MarkingMemberClient(auth=auth, hostname=hostname, config=config)
        self.MarkingRoleAssignment = MarkingRoleAssignmentClient(
            auth=auth, hostname=hostname, config=config
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def create(
        self,
        *,
        category_id: MarkingCategoryId,
        initial_members: List[PrincipalId],
        initial_role_assignments: List[Union[MarkingRoleUpdate, MarkingRoleUpdateDict]],
        name: MarkingName,
        description: Optional[str] = None,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> Marking:
        """
        Creates a new Marking.
        :param category_id:
        :type category_id: MarkingCategoryId
        :param initial_members: Users and Groups that will be able to view resources protected by this Marking. This can be changed later through the MarkingMember operations.
        :type initial_members: List[PrincipalId]
        :param initial_role_assignments: The initial roles that will be assigned when the Marking is created. At least one ADMIN role must be provided. This can be changed later through the MarkingRoleAssignment operations.  WARNING: If you do not include your own principal ID or the ID of a Group that you are a member of, you will create a Marking that you cannot administer.
        :type initial_role_assignments: List[Union[MarkingRoleUpdate, MarkingRoleUpdateDict]]
        :param name:
        :type name: MarkingName
        :param description:
        :type description: Optional[str]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: Marking
        """

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/admin/markings",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "initialRoleAssignments": initial_role_assignments,
                    "initialMembers": initial_members,
                    "name": name,
                    "description": description,
                    "categoryId": category_id,
                },
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "initialRoleAssignments": List[
                            Union[MarkingRoleUpdate, MarkingRoleUpdateDict]
                        ],
                        "initialMembers": List[PrincipalId],
                        "name": MarkingName,
                        "description": Optional[str],
                        "categoryId": MarkingCategoryId,
                    },
                ),
                response_type=Marking,
                request_timeout=request_timeout,
            ),
        ).decode()

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def get(
        self,
        marking_id: MarkingId,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> Marking:
        """
        Get the Marking with the specified id.
        :param marking_id: markingId
        :type marking_id: MarkingId
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: Marking
        """

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/admin/markings/{markingId}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "markingId": marking_id,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=Marking,
                request_timeout=request_timeout,
            ),
        ).decode()

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def get_batch(
        self,
        body: Annotated[
            List[Union[GetMarkingsBatchRequestElement, GetMarkingsBatchRequestElementDict]],
            Len(min_length=1, max_length=500),
        ],
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> GetMarkingsBatchResponse:
        """
        Execute multiple get requests on Marking.

        The maximum batch size for this endpoint is 500.
        :param body: Body of the request
        :type body: Annotated[List[Union[GetMarkingsBatchRequestElement, GetMarkingsBatchRequestElementDict]], Len(min_length=1, max_length=500)]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: GetMarkingsBatchResponse
        """

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/admin/markings/getBatch",
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
                    List[GetMarkingsBatchRequestElementDict], Len(min_length=1, max_length=500)
                ],
                response_type=GetMarkingsBatchResponse,
                request_timeout=request_timeout,
            ),
        ).decode()

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def list(
        self,
        *,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ResourceIterator[Marking]:
        """
        Maximum page size 100.
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param page_token: pageToken
        :type page_token: Optional[PageToken]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ResourceIterator[Marking]
        """

        return self._api_client.iterate_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/admin/markings",
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
                response_type=ListMarkingsResponse,
                request_timeout=request_timeout,
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def page(
        self,
        *,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ListMarkingsResponse:
        """
        Maximum page size 100.
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param page_token: pageToken
        :type page_token: Optional[PageToken]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ListMarkingsResponse
        """

        warnings.warn(
            "The client.admin.Marking.page(...) method has been deprecated. Please use client.admin.Marking.list(...) instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/admin/markings",
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
                response_type=ListMarkingsResponse,
                request_timeout=request_timeout,
            ),
        ).decode()


class _MarkingClientRaw:
    """
    The API client for the Marking Resource.

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
        self._api_client = ApiClient(auth=auth, hostname=hostname, config=config)

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def create(
        self,
        *,
        category_id: MarkingCategoryId,
        initial_members: List[PrincipalId],
        initial_role_assignments: List[Union[MarkingRoleUpdate, MarkingRoleUpdateDict]],
        name: MarkingName,
        description: Optional[str] = None,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[Marking]:
        """
        Creates a new Marking.
        :param category_id:
        :type category_id: MarkingCategoryId
        :param initial_members: Users and Groups that will be able to view resources protected by this Marking. This can be changed later through the MarkingMember operations.
        :type initial_members: List[PrincipalId]
        :param initial_role_assignments: The initial roles that will be assigned when the Marking is created. At least one ADMIN role must be provided. This can be changed later through the MarkingRoleAssignment operations.  WARNING: If you do not include your own principal ID or the ID of a Group that you are a member of, you will create a Marking that you cannot administer.
        :type initial_role_assignments: List[Union[MarkingRoleUpdate, MarkingRoleUpdateDict]]
        :param name:
        :type name: MarkingName
        :param description:
        :type description: Optional[str]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[Marking]
        """

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/admin/markings",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "initialRoleAssignments": initial_role_assignments,
                    "initialMembers": initial_members,
                    "name": name,
                    "description": description,
                    "categoryId": category_id,
                },
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "initialRoleAssignments": List[
                            Union[MarkingRoleUpdate, MarkingRoleUpdateDict]
                        ],
                        "initialMembers": List[PrincipalId],
                        "name": MarkingName,
                        "description": Optional[str],
                        "categoryId": MarkingCategoryId,
                    },
                ),
                response_type=Marking,
                request_timeout=request_timeout,
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def get(
        self,
        marking_id: MarkingId,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[Marking]:
        """
        Get the Marking with the specified id.
        :param marking_id: markingId
        :type marking_id: MarkingId
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[Marking]
        """

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/admin/markings/{markingId}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "markingId": marking_id,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=Marking,
                request_timeout=request_timeout,
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def get_batch(
        self,
        body: Annotated[
            List[Union[GetMarkingsBatchRequestElement, GetMarkingsBatchRequestElementDict]],
            Len(min_length=1, max_length=500),
        ],
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[GetMarkingsBatchResponse]:
        """
        Execute multiple get requests on Marking.

        The maximum batch size for this endpoint is 500.
        :param body: Body of the request
        :type body: Annotated[List[Union[GetMarkingsBatchRequestElement, GetMarkingsBatchRequestElementDict]], Len(min_length=1, max_length=500)]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[GetMarkingsBatchResponse]
        """

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/admin/markings/getBatch",
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
                    List[GetMarkingsBatchRequestElementDict], Len(min_length=1, max_length=500)
                ],
                response_type=GetMarkingsBatchResponse,
                request_timeout=request_timeout,
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def list(
        self,
        *,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[ListMarkingsResponse]:
        """
        Maximum page size 100.
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param page_token: pageToken
        :type page_token: Optional[PageToken]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[ListMarkingsResponse]
        """

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/admin/markings",
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
                response_type=ListMarkingsResponse,
                request_timeout=request_timeout,
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def page(
        self,
        *,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[ListMarkingsResponse]:
        """
        Maximum page size 100.
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param page_token: pageToken
        :type page_token: Optional[PageToken]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[ListMarkingsResponse]
        """

        warnings.warn(
            "The client.admin.Marking.page(...) method has been deprecated. Please use client.admin.Marking.list(...) instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/admin/markings",
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
                response_type=ListMarkingsResponse,
                request_timeout=request_timeout,
            ),
        )


class _MarkingClientStreaming:
    """
    The API client for the Marking Resource.

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
        self._api_client = ApiClient(auth=auth, hostname=hostname, config=config)

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def create(
        self,
        *,
        category_id: MarkingCategoryId,
        initial_members: List[PrincipalId],
        initial_role_assignments: List[Union[MarkingRoleUpdate, MarkingRoleUpdateDict]],
        name: MarkingName,
        description: Optional[str] = None,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[Marking]:
        """
        Creates a new Marking.
        :param category_id:
        :type category_id: MarkingCategoryId
        :param initial_members: Users and Groups that will be able to view resources protected by this Marking. This can be changed later through the MarkingMember operations.
        :type initial_members: List[PrincipalId]
        :param initial_role_assignments: The initial roles that will be assigned when the Marking is created. At least one ADMIN role must be provided. This can be changed later through the MarkingRoleAssignment operations.  WARNING: If you do not include your own principal ID or the ID of a Group that you are a member of, you will create a Marking that you cannot administer.
        :type initial_role_assignments: List[Union[MarkingRoleUpdate, MarkingRoleUpdateDict]]
        :param name:
        :type name: MarkingName
        :param description:
        :type description: Optional[str]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[Marking]
        """

        return self._api_client.stream_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/admin/markings",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "initialRoleAssignments": initial_role_assignments,
                    "initialMembers": initial_members,
                    "name": name,
                    "description": description,
                    "categoryId": category_id,
                },
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "initialRoleAssignments": List[
                            Union[MarkingRoleUpdate, MarkingRoleUpdateDict]
                        ],
                        "initialMembers": List[PrincipalId],
                        "name": MarkingName,
                        "description": Optional[str],
                        "categoryId": MarkingCategoryId,
                    },
                ),
                response_type=Marking,
                request_timeout=request_timeout,
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def get(
        self,
        marking_id: MarkingId,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[Marking]:
        """
        Get the Marking with the specified id.
        :param marking_id: markingId
        :type marking_id: MarkingId
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[Marking]
        """

        return self._api_client.stream_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/admin/markings/{markingId}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "markingId": marking_id,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=Marking,
                request_timeout=request_timeout,
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def get_batch(
        self,
        body: Annotated[
            List[Union[GetMarkingsBatchRequestElement, GetMarkingsBatchRequestElementDict]],
            Len(min_length=1, max_length=500),
        ],
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[GetMarkingsBatchResponse]:
        """
        Execute multiple get requests on Marking.

        The maximum batch size for this endpoint is 500.
        :param body: Body of the request
        :type body: Annotated[List[Union[GetMarkingsBatchRequestElement, GetMarkingsBatchRequestElementDict]], Len(min_length=1, max_length=500)]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[GetMarkingsBatchResponse]
        """

        return self._api_client.stream_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/admin/markings/getBatch",
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
                    List[GetMarkingsBatchRequestElementDict], Len(min_length=1, max_length=500)
                ],
                response_type=GetMarkingsBatchResponse,
                request_timeout=request_timeout,
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def list(
        self,
        *,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[ListMarkingsResponse]:
        """
        Maximum page size 100.
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param page_token: pageToken
        :type page_token: Optional[PageToken]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[ListMarkingsResponse]
        """

        return self._api_client.stream_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/admin/markings",
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
                response_type=ListMarkingsResponse,
                request_timeout=request_timeout,
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def page(
        self,
        *,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[ListMarkingsResponse]:
        """
        Maximum page size 100.
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param page_token: pageToken
        :type page_token: Optional[PageToken]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[ListMarkingsResponse]
        """

        warnings.warn(
            "The client.admin.Marking.page(...) method has been deprecated. Please use client.admin.Marking.list(...) instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        return self._api_client.stream_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/admin/markings",
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
                response_type=ListMarkingsResponse,
                request_timeout=request_timeout,
            ),
        )
