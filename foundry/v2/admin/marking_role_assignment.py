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


import typing
import warnings

import pydantic
import typing_extensions

from foundry import _core as core
from foundry import _errors as errors
from foundry.v2.admin import errors as admin_errors
from foundry.v2.admin import models as admin_models
from foundry.v2.core import models as core_models


class MarkingRoleAssignmentClient:
    """
    The API client for the MarkingRoleAssignment Resource.

    :param auth: Your auth configuration.
    :param hostname: Your Foundry hostname (for example, "myfoundry.palantirfoundry.com"). This can also include your API gateway service URI.
    :param config: Optionally specify the configuration for the HTTP session.
    """

    def __init__(
        self,
        auth: core.Auth,
        hostname: str,
        config: typing.Optional[core.Config] = None,
    ):
        self._auth = auth
        self._hostname = hostname
        self._config = config
        self._api_client = core.ApiClient(auth=auth, hostname=hostname, config=config)
        self.with_streaming_response = _MarkingRoleAssignmentClientStreaming(
            auth=auth, hostname=hostname, config=config
        )
        self.with_raw_response = _MarkingRoleAssignmentClientRaw(
            auth=auth, hostname=hostname, config=config
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def add(
        self,
        marking_id: core_models.MarkingId,
        *,
        role_assignments: typing.List[
            typing.Union[admin_models.MarkingRoleUpdate, admin_models.MarkingRoleUpdateDict]
        ],
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> None:
        """

        :param marking_id:
        :type marking_id: MarkingId
        :param role_assignments:
        :type role_assignments: List[Union[MarkingRoleUpdate, MarkingRoleUpdateDict]]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: None

        :raises AddMarkingRoleAssignmentsPermissionDenied: Could not add the MarkingRoleAssignment.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "roleAssignments": typing.List[
                            typing.Union[
                                admin_models.MarkingRoleUpdate, admin_models.MarkingRoleUpdateDict
                            ]
                        ],
                    },
                ),
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "AddMarkingRoleAssignmentsPermissionDenied": admin_errors.AddMarkingRoleAssignmentsPermissionDenied,
                },
            ),
        ).decode()

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def list(
        self,
        marking_id: core_models.MarkingId,
        *,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ResourceIterator[admin_models.MarkingRoleAssignment]:
        """
        List all principals who are assigned a role for the given Marking. Ignores the `pageSize` parameter.

        :param marking_id:
        :type marking_id: MarkingId
        :param page_size: The page size to use for the endpoint.
        :type page_size: Optional[PageSize]
        :param page_token: The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
        :type page_token: Optional[PageToken]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ResourceIterator[admin_models.MarkingRoleAssignment]
        """

        return self._api_client.iterate_api(
            core.RequestInfo(
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
                response_type=admin_models.ListMarkingRoleAssignmentsResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def page(
        self,
        marking_id: core_models.MarkingId,
        *,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> admin_models.ListMarkingRoleAssignmentsResponse:
        """
        List all principals who are assigned a role for the given Marking. Ignores the `pageSize` parameter.

        :param marking_id:
        :type marking_id: MarkingId
        :param page_size: The page size to use for the endpoint.
        :type page_size: Optional[PageSize]
        :param page_token: The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
        :type page_token: Optional[PageToken]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: admin_models.ListMarkingRoleAssignmentsResponse
        """

        warnings.warn(
            "The client.admin.MarkingRoleAssignment.page(...) method has been deprecated. Please use client.admin.MarkingRoleAssignment.list(...) instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        return self._api_client.call_api(
            core.RequestInfo(
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
                response_type=admin_models.ListMarkingRoleAssignmentsResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        ).decode()

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def remove(
        self,
        marking_id: core_models.MarkingId,
        *,
        role_assignments: typing.List[
            typing.Union[admin_models.MarkingRoleUpdate, admin_models.MarkingRoleUpdateDict]
        ],
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> None:
        """

        :param marking_id:
        :type marking_id: MarkingId
        :param role_assignments:
        :type role_assignments: List[Union[MarkingRoleUpdate, MarkingRoleUpdateDict]]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: None

        :raises MarkingNotFound: The given Marking could not be found.
        :raises PrincipalNotFound: A principal (User or Group) with the given PrincipalId could not be found
        :raises RemoveMarkingMembersPermissionDenied: Could not remove the MarkingMember.
        :raises RemoveMarkingRoleAssignmentsPermissionDenied: Could not remove the MarkingRoleAssignment.
        :raises RemoveMarkingRoleAssignmentsRemoveAllAdministratorsNotAllowed: You cannot remove all administrators from a marking.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "roleAssignments": typing.List[
                            typing.Union[
                                admin_models.MarkingRoleUpdate, admin_models.MarkingRoleUpdateDict
                            ]
                        ],
                    },
                ),
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "MarkingNotFound": admin_errors.MarkingNotFound,
                    "PrincipalNotFound": admin_errors.PrincipalNotFound,
                    "RemoveMarkingMembersPermissionDenied": admin_errors.RemoveMarkingMembersPermissionDenied,
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
        auth: core.Auth,
        hostname: str,
        config: typing.Optional[core.Config] = None,
    ):
        self._auth = auth
        self._hostname = hostname
        self._config = config
        self._api_client = core.ApiClient(auth=auth, hostname=hostname, config=config)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def add(
        self,
        marking_id: core_models.MarkingId,
        *,
        role_assignments: typing.List[
            typing.Union[admin_models.MarkingRoleUpdate, admin_models.MarkingRoleUpdateDict]
        ],
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[None]:
        """

        :param marking_id:
        :type marking_id: MarkingId
        :param role_assignments:
        :type role_assignments: List[Union[MarkingRoleUpdate, MarkingRoleUpdateDict]]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[None]

        :raises AddMarkingRoleAssignmentsPermissionDenied: Could not add the MarkingRoleAssignment.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "roleAssignments": typing.List[
                            typing.Union[
                                admin_models.MarkingRoleUpdate, admin_models.MarkingRoleUpdateDict
                            ]
                        ],
                    },
                ),
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "AddMarkingRoleAssignmentsPermissionDenied": admin_errors.AddMarkingRoleAssignmentsPermissionDenied,
                },
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def list(
        self,
        marking_id: core_models.MarkingId,
        *,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[admin_models.ListMarkingRoleAssignmentsResponse]:
        """
        List all principals who are assigned a role for the given Marking. Ignores the `pageSize` parameter.

        :param marking_id:
        :type marking_id: MarkingId
        :param page_size: The page size to use for the endpoint.
        :type page_size: Optional[PageSize]
        :param page_token: The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
        :type page_token: Optional[PageToken]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[admin_models.ListMarkingRoleAssignmentsResponse]
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                response_type=admin_models.ListMarkingRoleAssignmentsResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def page(
        self,
        marking_id: core_models.MarkingId,
        *,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[admin_models.ListMarkingRoleAssignmentsResponse]:
        """
        List all principals who are assigned a role for the given Marking. Ignores the `pageSize` parameter.

        :param marking_id:
        :type marking_id: MarkingId
        :param page_size: The page size to use for the endpoint.
        :type page_size: Optional[PageSize]
        :param page_token: The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
        :type page_token: Optional[PageToken]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[admin_models.ListMarkingRoleAssignmentsResponse]
        """

        warnings.warn(
            "The client.admin.MarkingRoleAssignment.page(...) method has been deprecated. Please use client.admin.MarkingRoleAssignment.list(...) instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        return self._api_client.call_api(
            core.RequestInfo(
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
                response_type=admin_models.ListMarkingRoleAssignmentsResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def remove(
        self,
        marking_id: core_models.MarkingId,
        *,
        role_assignments: typing.List[
            typing.Union[admin_models.MarkingRoleUpdate, admin_models.MarkingRoleUpdateDict]
        ],
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[None]:
        """

        :param marking_id:
        :type marking_id: MarkingId
        :param role_assignments:
        :type role_assignments: List[Union[MarkingRoleUpdate, MarkingRoleUpdateDict]]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[None]

        :raises MarkingNotFound: The given Marking could not be found.
        :raises PrincipalNotFound: A principal (User or Group) with the given PrincipalId could not be found
        :raises RemoveMarkingMembersPermissionDenied: Could not remove the MarkingMember.
        :raises RemoveMarkingRoleAssignmentsPermissionDenied: Could not remove the MarkingRoleAssignment.
        :raises RemoveMarkingRoleAssignmentsRemoveAllAdministratorsNotAllowed: You cannot remove all administrators from a marking.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "roleAssignments": typing.List[
                            typing.Union[
                                admin_models.MarkingRoleUpdate, admin_models.MarkingRoleUpdateDict
                            ]
                        ],
                    },
                ),
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "MarkingNotFound": admin_errors.MarkingNotFound,
                    "PrincipalNotFound": admin_errors.PrincipalNotFound,
                    "RemoveMarkingMembersPermissionDenied": admin_errors.RemoveMarkingMembersPermissionDenied,
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
        auth: core.Auth,
        hostname: str,
        config: typing.Optional[core.Config] = None,
    ):
        self._auth = auth
        self._hostname = hostname
        self._config = config
        self._api_client = core.ApiClient(auth=auth, hostname=hostname, config=config)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def add(
        self,
        marking_id: core_models.MarkingId,
        *,
        role_assignments: typing.List[
            typing.Union[admin_models.MarkingRoleUpdate, admin_models.MarkingRoleUpdateDict]
        ],
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[None]:
        """

        :param marking_id:
        :type marking_id: MarkingId
        :param role_assignments:
        :type role_assignments: List[Union[MarkingRoleUpdate, MarkingRoleUpdateDict]]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[None]

        :raises AddMarkingRoleAssignmentsPermissionDenied: Could not add the MarkingRoleAssignment.
        """

        return self._api_client.stream_api(
            core.RequestInfo(
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
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "roleAssignments": typing.List[
                            typing.Union[
                                admin_models.MarkingRoleUpdate, admin_models.MarkingRoleUpdateDict
                            ]
                        ],
                    },
                ),
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "AddMarkingRoleAssignmentsPermissionDenied": admin_errors.AddMarkingRoleAssignmentsPermissionDenied,
                },
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def list(
        self,
        marking_id: core_models.MarkingId,
        *,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[admin_models.ListMarkingRoleAssignmentsResponse]:
        """
        List all principals who are assigned a role for the given Marking. Ignores the `pageSize` parameter.

        :param marking_id:
        :type marking_id: MarkingId
        :param page_size: The page size to use for the endpoint.
        :type page_size: Optional[PageSize]
        :param page_token: The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
        :type page_token: Optional[PageToken]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[admin_models.ListMarkingRoleAssignmentsResponse]
        """

        return self._api_client.stream_api(
            core.RequestInfo(
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
                response_type=admin_models.ListMarkingRoleAssignmentsResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def page(
        self,
        marking_id: core_models.MarkingId,
        *,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[admin_models.ListMarkingRoleAssignmentsResponse]:
        """
        List all principals who are assigned a role for the given Marking. Ignores the `pageSize` parameter.

        :param marking_id:
        :type marking_id: MarkingId
        :param page_size: The page size to use for the endpoint.
        :type page_size: Optional[PageSize]
        :param page_token: The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
        :type page_token: Optional[PageToken]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[admin_models.ListMarkingRoleAssignmentsResponse]
        """

        warnings.warn(
            "The client.admin.MarkingRoleAssignment.page(...) method has been deprecated. Please use client.admin.MarkingRoleAssignment.list(...) instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        return self._api_client.stream_api(
            core.RequestInfo(
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
                response_type=admin_models.ListMarkingRoleAssignmentsResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def remove(
        self,
        marking_id: core_models.MarkingId,
        *,
        role_assignments: typing.List[
            typing.Union[admin_models.MarkingRoleUpdate, admin_models.MarkingRoleUpdateDict]
        ],
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[None]:
        """

        :param marking_id:
        :type marking_id: MarkingId
        :param role_assignments:
        :type role_assignments: List[Union[MarkingRoleUpdate, MarkingRoleUpdateDict]]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[None]

        :raises MarkingNotFound: The given Marking could not be found.
        :raises PrincipalNotFound: A principal (User or Group) with the given PrincipalId could not be found
        :raises RemoveMarkingMembersPermissionDenied: Could not remove the MarkingMember.
        :raises RemoveMarkingRoleAssignmentsPermissionDenied: Could not remove the MarkingRoleAssignment.
        :raises RemoveMarkingRoleAssignmentsRemoveAllAdministratorsNotAllowed: You cannot remove all administrators from a marking.
        """

        return self._api_client.stream_api(
            core.RequestInfo(
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
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "roleAssignments": typing.List[
                            typing.Union[
                                admin_models.MarkingRoleUpdate, admin_models.MarkingRoleUpdateDict
                            ]
                        ],
                    },
                ),
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "MarkingNotFound": admin_errors.MarkingNotFound,
                    "PrincipalNotFound": admin_errors.PrincipalNotFound,
                    "RemoveMarkingMembersPermissionDenied": admin_errors.RemoveMarkingMembersPermissionDenied,
                    "RemoveMarkingRoleAssignmentsPermissionDenied": admin_errors.RemoveMarkingRoleAssignmentsPermissionDenied,
                    "RemoveMarkingRoleAssignmentsRemoveAllAdministratorsNotAllowed": admin_errors.RemoveMarkingRoleAssignmentsRemoveAllAdministratorsNotAllowed,
                },
            ),
        )
