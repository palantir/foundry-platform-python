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
from typing import Union

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
from foundry.v2.admin.models._list_marking_role_assignments_response import (
    ListMarkingRoleAssignmentsResponse,
)  # NOQA
from foundry.v2.admin.models._marking_role_assignment import MarkingRoleAssignment
from foundry.v2.admin.models._marking_role_update import MarkingRoleUpdate
from foundry.v2.admin.models._marking_role_update_dict import MarkingRoleUpdateDict
from foundry.v2.core.models._marking_id import MarkingId
from foundry.v2.core.models._page_size import PageSize
from foundry.v2.core.models._page_token import PageToken
from foundry.v2.core.models._preview_mode import PreviewMode


class MarkingRoleAssignmentClient:
    """
    The API client for the MarkingRoleAssignment Resource.

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
        self.with_streaming_response = _MarkingRoleAssignmentClientStreaming(
            auth=auth, hostname=hostname, config=config
        )
        self.with_raw_response = _MarkingRoleAssignmentClientRaw(
            auth=auth, hostname=hostname, config=config
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def add(
        self,
        marking_id: MarkingId,
        *,
        role_assignments: List[Union[MarkingRoleUpdate, MarkingRoleUpdateDict]],
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> None:
        """

        :param marking_id: markingId
        :type marking_id: MarkingId
        :param role_assignments:
        :type role_assignments: List[Union[MarkingRoleUpdate, MarkingRoleUpdateDict]]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: None

        :raises AddMarkingRoleAssignmentsPermissionDenied: Could not add the MarkingRoleAssignment.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/admin/markings/{markingId}/roleAssignments/add",
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
                    "roleAssignments": role_assignments,
                },
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "roleAssignments": List[Union[MarkingRoleUpdate, MarkingRoleUpdateDict]],
                    },
                ),
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "AddMarkingRoleAssignmentsPermissionDenied": admin_errors.AddMarkingRoleAssignmentsPermissionDenied,
                },
            ),
        ).decode()

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def list(
        self,
        marking_id: MarkingId,
        *,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ResourceIterator[MarkingRoleAssignment]:
        """
        List all principals who are assigned a role for the given Marking. Ignores the `pageSize` parameter.

        :param marking_id: markingId
        :type marking_id: MarkingId
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param page_token: pageToken
        :type page_token: Optional[PageToken]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ResourceIterator[MarkingRoleAssignment]
        """

        return self._api_client.iterate_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/admin/markings/{markingId}/roleAssignments",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
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
                response_type=ListMarkingRoleAssignmentsResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def page(
        self,
        marking_id: MarkingId,
        *,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ListMarkingRoleAssignmentsResponse:
        """
        List all principals who are assigned a role for the given Marking. Ignores the `pageSize` parameter.

        :param marking_id: markingId
        :type marking_id: MarkingId
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param page_token: pageToken
        :type page_token: Optional[PageToken]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ListMarkingRoleAssignmentsResponse
        """

        warnings.warn(
            "The client.admin.MarkingRoleAssignment.page(...) method has been deprecated. Please use client.admin.MarkingRoleAssignment.list(...) instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/admin/markings/{markingId}/roleAssignments",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
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
                response_type=ListMarkingRoleAssignmentsResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        ).decode()

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def remove(
        self,
        marking_id: MarkingId,
        *,
        role_assignments: List[Union[MarkingRoleUpdate, MarkingRoleUpdateDict]],
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> None:
        """

        :param marking_id: markingId
        :type marking_id: MarkingId
        :param role_assignments:
        :type role_assignments: List[Union[MarkingRoleUpdate, MarkingRoleUpdateDict]]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: None

        :raises PrincipalNotFound: A principal (User or Group) with the given PrincipalId could not be found
        :raises RemoveMarkingRoleAssignmentsPermissionDenied: Could not remove the MarkingRoleAssignment.
        :raises RemoveMarkingRoleAssignmentsRemoveAllAdministratorsNotAllowed: You cannot remove all administrators from a marking.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/admin/markings/{markingId}/roleAssignments/remove",
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
                    "roleAssignments": role_assignments,
                },
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "roleAssignments": List[Union[MarkingRoleUpdate, MarkingRoleUpdateDict]],
                    },
                ),
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "PrincipalNotFound": admin_errors.PrincipalNotFound,
                    "RemoveMarkingRoleAssignmentsPermissionDenied": admin_errors.RemoveMarkingRoleAssignmentsPermissionDenied,
                    "RemoveMarkingRoleAssignmentsRemoveAllAdministratorsNotAllowed": admin_errors.RemoveMarkingRoleAssignmentsRemoveAllAdministratorsNotAllowed,
                },
            ),
        ).decode()


class _MarkingRoleAssignmentClientRaw:
    """
    The API client for the MarkingRoleAssignment Resource.

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
        marking_id: MarkingId,
        *,
        role_assignments: List[Union[MarkingRoleUpdate, MarkingRoleUpdateDict]],
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[None]:
        """

        :param marking_id: markingId
        :type marking_id: MarkingId
        :param role_assignments:
        :type role_assignments: List[Union[MarkingRoleUpdate, MarkingRoleUpdateDict]]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[None]

        :raises AddMarkingRoleAssignmentsPermissionDenied: Could not add the MarkingRoleAssignment.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/admin/markings/{markingId}/roleAssignments/add",
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
                    "roleAssignments": role_assignments,
                },
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "roleAssignments": List[Union[MarkingRoleUpdate, MarkingRoleUpdateDict]],
                    },
                ),
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "AddMarkingRoleAssignmentsPermissionDenied": admin_errors.AddMarkingRoleAssignmentsPermissionDenied,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def list(
        self,
        marking_id: MarkingId,
        *,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[ListMarkingRoleAssignmentsResponse]:
        """
        List all principals who are assigned a role for the given Marking. Ignores the `pageSize` parameter.

        :param marking_id: markingId
        :type marking_id: MarkingId
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param page_token: pageToken
        :type page_token: Optional[PageToken]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[ListMarkingRoleAssignmentsResponse]
        """

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/admin/markings/{markingId}/roleAssignments",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
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
                response_type=ListMarkingRoleAssignmentsResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def page(
        self,
        marking_id: MarkingId,
        *,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[ListMarkingRoleAssignmentsResponse]:
        """
        List all principals who are assigned a role for the given Marking. Ignores the `pageSize` parameter.

        :param marking_id: markingId
        :type marking_id: MarkingId
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param page_token: pageToken
        :type page_token: Optional[PageToken]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[ListMarkingRoleAssignmentsResponse]
        """

        warnings.warn(
            "The client.admin.MarkingRoleAssignment.page(...) method has been deprecated. Please use client.admin.MarkingRoleAssignment.list(...) instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/admin/markings/{markingId}/roleAssignments",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
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
                response_type=ListMarkingRoleAssignmentsResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def remove(
        self,
        marking_id: MarkingId,
        *,
        role_assignments: List[Union[MarkingRoleUpdate, MarkingRoleUpdateDict]],
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[None]:
        """

        :param marking_id: markingId
        :type marking_id: MarkingId
        :param role_assignments:
        :type role_assignments: List[Union[MarkingRoleUpdate, MarkingRoleUpdateDict]]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[None]

        :raises PrincipalNotFound: A principal (User or Group) with the given PrincipalId could not be found
        :raises RemoveMarkingRoleAssignmentsPermissionDenied: Could not remove the MarkingRoleAssignment.
        :raises RemoveMarkingRoleAssignmentsRemoveAllAdministratorsNotAllowed: You cannot remove all administrators from a marking.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/admin/markings/{markingId}/roleAssignments/remove",
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
                    "roleAssignments": role_assignments,
                },
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "roleAssignments": List[Union[MarkingRoleUpdate, MarkingRoleUpdateDict]],
                    },
                ),
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "PrincipalNotFound": admin_errors.PrincipalNotFound,
                    "RemoveMarkingRoleAssignmentsPermissionDenied": admin_errors.RemoveMarkingRoleAssignmentsPermissionDenied,
                    "RemoveMarkingRoleAssignmentsRemoveAllAdministratorsNotAllowed": admin_errors.RemoveMarkingRoleAssignmentsRemoveAllAdministratorsNotAllowed,
                },
            ),
        )


class _MarkingRoleAssignmentClientStreaming:
    """
    The API client for the MarkingRoleAssignment Resource.

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
        marking_id: MarkingId,
        *,
        role_assignments: List[Union[MarkingRoleUpdate, MarkingRoleUpdateDict]],
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[None]:
        """

        :param marking_id: markingId
        :type marking_id: MarkingId
        :param role_assignments:
        :type role_assignments: List[Union[MarkingRoleUpdate, MarkingRoleUpdateDict]]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[None]

        :raises AddMarkingRoleAssignmentsPermissionDenied: Could not add the MarkingRoleAssignment.
        """

        return self._api_client.stream_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/admin/markings/{markingId}/roleAssignments/add",
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
                    "roleAssignments": role_assignments,
                },
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "roleAssignments": List[Union[MarkingRoleUpdate, MarkingRoleUpdateDict]],
                    },
                ),
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "AddMarkingRoleAssignmentsPermissionDenied": admin_errors.AddMarkingRoleAssignmentsPermissionDenied,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def list(
        self,
        marking_id: MarkingId,
        *,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[ListMarkingRoleAssignmentsResponse]:
        """
        List all principals who are assigned a role for the given Marking. Ignores the `pageSize` parameter.

        :param marking_id: markingId
        :type marking_id: MarkingId
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param page_token: pageToken
        :type page_token: Optional[PageToken]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[ListMarkingRoleAssignmentsResponse]
        """

        return self._api_client.stream_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/admin/markings/{markingId}/roleAssignments",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
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
                response_type=ListMarkingRoleAssignmentsResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def page(
        self,
        marking_id: MarkingId,
        *,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[ListMarkingRoleAssignmentsResponse]:
        """
        List all principals who are assigned a role for the given Marking. Ignores the `pageSize` parameter.

        :param marking_id: markingId
        :type marking_id: MarkingId
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param page_token: pageToken
        :type page_token: Optional[PageToken]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[ListMarkingRoleAssignmentsResponse]
        """

        warnings.warn(
            "The client.admin.MarkingRoleAssignment.page(...) method has been deprecated. Please use client.admin.MarkingRoleAssignment.list(...) instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        return self._api_client.stream_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/admin/markings/{markingId}/roleAssignments",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
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
                response_type=ListMarkingRoleAssignmentsResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def remove(
        self,
        marking_id: MarkingId,
        *,
        role_assignments: List[Union[MarkingRoleUpdate, MarkingRoleUpdateDict]],
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[None]:
        """

        :param marking_id: markingId
        :type marking_id: MarkingId
        :param role_assignments:
        :type role_assignments: List[Union[MarkingRoleUpdate, MarkingRoleUpdateDict]]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[None]

        :raises PrincipalNotFound: A principal (User or Group) with the given PrincipalId could not be found
        :raises RemoveMarkingRoleAssignmentsPermissionDenied: Could not remove the MarkingRoleAssignment.
        :raises RemoveMarkingRoleAssignmentsRemoveAllAdministratorsNotAllowed: You cannot remove all administrators from a marking.
        """

        return self._api_client.stream_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/admin/markings/{markingId}/roleAssignments/remove",
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
                    "roleAssignments": role_assignments,
                },
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "roleAssignments": List[Union[MarkingRoleUpdate, MarkingRoleUpdateDict]],
                    },
                ),
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "PrincipalNotFound": admin_errors.PrincipalNotFound,
                    "RemoveMarkingRoleAssignmentsPermissionDenied": admin_errors.RemoveMarkingRoleAssignmentsPermissionDenied,
                    "RemoveMarkingRoleAssignmentsRemoveAllAdministratorsNotAllowed": admin_errors.RemoveMarkingRoleAssignmentsRemoveAllAdministratorsNotAllowed,
                },
            ),
        )
