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


class MarkingMemberClient:
    """
    The API client for the MarkingMember Resource.

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
        self.with_streaming_response = _MarkingMemberClientStreaming(
            auth=auth, hostname=hostname, config=config
        )
        self.with_raw_response = _MarkingMemberClientRaw(
            auth=auth, hostname=hostname, config=config
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def add(
        self,
        marking_id: core_models.MarkingId,
        *,
        principal_ids: typing.List[core_models.PrincipalId],
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> None:
        """

        :param marking_id:
        :type marking_id: MarkingId
        :param principal_ids:
        :type principal_ids: List[PrincipalId]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: None

        :raises AddMarkingMembersPermissionDenied: Could not add the MarkingMember.
        :raises MarkingNotFound: The given Marking could not be found.
        :raises PrincipalNotFound: A principal (User or Group) with the given PrincipalId could not be found
        :raises RemoveMarkingMembersPermissionDenied: Could not remove the MarkingMember.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "principalIds": typing.List[core_models.PrincipalId],
                    },
                ),
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "AddMarkingMembersPermissionDenied": admin_errors.AddMarkingMembersPermissionDenied,
                    "MarkingNotFound": admin_errors.MarkingNotFound,
                    "PrincipalNotFound": admin_errors.PrincipalNotFound,
                    "RemoveMarkingMembersPermissionDenied": admin_errors.RemoveMarkingMembersPermissionDenied,
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
        transitive: typing.Optional[bool] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ResourceIterator[admin_models.MarkingMember]:
        """
        Lists all principals who can view resources protected by the given Marking. Ignores the `pageSize` parameter.
        Requires `api:admin-write` because only marking administrators can view marking members.

        :param marking_id:
        :type marking_id: MarkingId
        :param page_size: The page size to use for the endpoint.
        :type page_size: Optional[PageSize]
        :param page_token: The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
        :type page_token: Optional[PageToken]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param transitive: When true, includes the transitive members of groups contained within groups that are members of this  Marking. For example, say the Marking has member Group A, and Group A has member User B. If  `transitive=false` only Group A will be returned, but if `transitive=true` then Group A and User B  will be returned. This will recursively resolve Groups through all layers of nesting.  Defaults to false.
        :type transitive: Optional[bool]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ResourceIterator[admin_models.MarkingMember]

        :raises ListMarkingMembersPermissionDenied: The provided token does not have permission to list the members of this marking.
        """

        return self._api_client.iterate_api(
            core.RequestInfo(
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
                response_type=admin_models.ListMarkingMembersResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "ListMarkingMembersPermissionDenied": admin_errors.ListMarkingMembersPermissionDenied,
                },
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
        transitive: typing.Optional[bool] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> admin_models.ListMarkingMembersResponse:
        """
        Lists all principals who can view resources protected by the given Marking. Ignores the `pageSize` parameter.
        Requires `api:admin-write` because only marking administrators can view marking members.

        :param marking_id:
        :type marking_id: MarkingId
        :param page_size: The page size to use for the endpoint.
        :type page_size: Optional[PageSize]
        :param page_token: The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
        :type page_token: Optional[PageToken]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param transitive: When true, includes the transitive members of groups contained within groups that are members of this  Marking. For example, say the Marking has member Group A, and Group A has member User B. If  `transitive=false` only Group A will be returned, but if `transitive=true` then Group A and User B  will be returned. This will recursively resolve Groups through all layers of nesting.  Defaults to false.
        :type transitive: Optional[bool]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: admin_models.ListMarkingMembersResponse

        :raises ListMarkingMembersPermissionDenied: The provided token does not have permission to list the members of this marking.
        """

        warnings.warn(
            "The client.admin.MarkingMember.page(...) method has been deprecated. Please use client.admin.MarkingMember.list(...) instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        return self._api_client.call_api(
            core.RequestInfo(
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
                response_type=admin_models.ListMarkingMembersResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "ListMarkingMembersPermissionDenied": admin_errors.ListMarkingMembersPermissionDenied,
                },
            ),
        ).decode()

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def remove(
        self,
        marking_id: core_models.MarkingId,
        *,
        principal_ids: typing.List[core_models.PrincipalId],
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> None:
        """

        :param marking_id:
        :type marking_id: MarkingId
        :param principal_ids:
        :type principal_ids: List[PrincipalId]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: None

        :raises RemoveMarkingMembersPermissionDenied: Could not remove the MarkingMember.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "principalIds": typing.List[core_models.PrincipalId],
                    },
                ),
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "RemoveMarkingMembersPermissionDenied": admin_errors.RemoveMarkingMembersPermissionDenied,
                },
            ),
        ).decode()


class _MarkingMemberClientRaw:
    """
    The API client for the MarkingMember Resource.

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
        principal_ids: typing.List[core_models.PrincipalId],
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[None]:
        """

        :param marking_id:
        :type marking_id: MarkingId
        :param principal_ids:
        :type principal_ids: List[PrincipalId]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[None]

        :raises AddMarkingMembersPermissionDenied: Could not add the MarkingMember.
        :raises MarkingNotFound: The given Marking could not be found.
        :raises PrincipalNotFound: A principal (User or Group) with the given PrincipalId could not be found
        :raises RemoveMarkingMembersPermissionDenied: Could not remove the MarkingMember.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "principalIds": typing.List[core_models.PrincipalId],
                    },
                ),
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "AddMarkingMembersPermissionDenied": admin_errors.AddMarkingMembersPermissionDenied,
                    "MarkingNotFound": admin_errors.MarkingNotFound,
                    "PrincipalNotFound": admin_errors.PrincipalNotFound,
                    "RemoveMarkingMembersPermissionDenied": admin_errors.RemoveMarkingMembersPermissionDenied,
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
        transitive: typing.Optional[bool] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[admin_models.ListMarkingMembersResponse]:
        """
        Lists all principals who can view resources protected by the given Marking. Ignores the `pageSize` parameter.
        Requires `api:admin-write` because only marking administrators can view marking members.

        :param marking_id:
        :type marking_id: MarkingId
        :param page_size: The page size to use for the endpoint.
        :type page_size: Optional[PageSize]
        :param page_token: The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
        :type page_token: Optional[PageToken]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param transitive: When true, includes the transitive members of groups contained within groups that are members of this  Marking. For example, say the Marking has member Group A, and Group A has member User B. If  `transitive=false` only Group A will be returned, but if `transitive=true` then Group A and User B  will be returned. This will recursively resolve Groups through all layers of nesting.  Defaults to false.
        :type transitive: Optional[bool]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[admin_models.ListMarkingMembersResponse]

        :raises ListMarkingMembersPermissionDenied: The provided token does not have permission to list the members of this marking.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                response_type=admin_models.ListMarkingMembersResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "ListMarkingMembersPermissionDenied": admin_errors.ListMarkingMembersPermissionDenied,
                },
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
        transitive: typing.Optional[bool] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[admin_models.ListMarkingMembersResponse]:
        """
        Lists all principals who can view resources protected by the given Marking. Ignores the `pageSize` parameter.
        Requires `api:admin-write` because only marking administrators can view marking members.

        :param marking_id:
        :type marking_id: MarkingId
        :param page_size: The page size to use for the endpoint.
        :type page_size: Optional[PageSize]
        :param page_token: The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
        :type page_token: Optional[PageToken]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param transitive: When true, includes the transitive members of groups contained within groups that are members of this  Marking. For example, say the Marking has member Group A, and Group A has member User B. If  `transitive=false` only Group A will be returned, but if `transitive=true` then Group A and User B  will be returned. This will recursively resolve Groups through all layers of nesting.  Defaults to false.
        :type transitive: Optional[bool]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[admin_models.ListMarkingMembersResponse]

        :raises ListMarkingMembersPermissionDenied: The provided token does not have permission to list the members of this marking.
        """

        warnings.warn(
            "The client.admin.MarkingMember.page(...) method has been deprecated. Please use client.admin.MarkingMember.list(...) instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        return self._api_client.call_api(
            core.RequestInfo(
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
                response_type=admin_models.ListMarkingMembersResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "ListMarkingMembersPermissionDenied": admin_errors.ListMarkingMembersPermissionDenied,
                },
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def remove(
        self,
        marking_id: core_models.MarkingId,
        *,
        principal_ids: typing.List[core_models.PrincipalId],
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[None]:
        """

        :param marking_id:
        :type marking_id: MarkingId
        :param principal_ids:
        :type principal_ids: List[PrincipalId]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[None]

        :raises RemoveMarkingMembersPermissionDenied: Could not remove the MarkingMember.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "principalIds": typing.List[core_models.PrincipalId],
                    },
                ),
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "RemoveMarkingMembersPermissionDenied": admin_errors.RemoveMarkingMembersPermissionDenied,
                },
            ),
        )


class _MarkingMemberClientStreaming:
    """
    The API client for the MarkingMember Resource.

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
        principal_ids: typing.List[core_models.PrincipalId],
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[None]:
        """

        :param marking_id:
        :type marking_id: MarkingId
        :param principal_ids:
        :type principal_ids: List[PrincipalId]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[None]

        :raises AddMarkingMembersPermissionDenied: Could not add the MarkingMember.
        :raises MarkingNotFound: The given Marking could not be found.
        :raises PrincipalNotFound: A principal (User or Group) with the given PrincipalId could not be found
        :raises RemoveMarkingMembersPermissionDenied: Could not remove the MarkingMember.
        """

        return self._api_client.stream_api(
            core.RequestInfo(
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
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "principalIds": typing.List[core_models.PrincipalId],
                    },
                ),
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "AddMarkingMembersPermissionDenied": admin_errors.AddMarkingMembersPermissionDenied,
                    "MarkingNotFound": admin_errors.MarkingNotFound,
                    "PrincipalNotFound": admin_errors.PrincipalNotFound,
                    "RemoveMarkingMembersPermissionDenied": admin_errors.RemoveMarkingMembersPermissionDenied,
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
        transitive: typing.Optional[bool] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[admin_models.ListMarkingMembersResponse]:
        """
        Lists all principals who can view resources protected by the given Marking. Ignores the `pageSize` parameter.
        Requires `api:admin-write` because only marking administrators can view marking members.

        :param marking_id:
        :type marking_id: MarkingId
        :param page_size: The page size to use for the endpoint.
        :type page_size: Optional[PageSize]
        :param page_token: The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
        :type page_token: Optional[PageToken]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param transitive: When true, includes the transitive members of groups contained within groups that are members of this  Marking. For example, say the Marking has member Group A, and Group A has member User B. If  `transitive=false` only Group A will be returned, but if `transitive=true` then Group A and User B  will be returned. This will recursively resolve Groups through all layers of nesting.  Defaults to false.
        :type transitive: Optional[bool]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[admin_models.ListMarkingMembersResponse]

        :raises ListMarkingMembersPermissionDenied: The provided token does not have permission to list the members of this marking.
        """

        return self._api_client.stream_api(
            core.RequestInfo(
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
                response_type=admin_models.ListMarkingMembersResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "ListMarkingMembersPermissionDenied": admin_errors.ListMarkingMembersPermissionDenied,
                },
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
        transitive: typing.Optional[bool] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[admin_models.ListMarkingMembersResponse]:
        """
        Lists all principals who can view resources protected by the given Marking. Ignores the `pageSize` parameter.
        Requires `api:admin-write` because only marking administrators can view marking members.

        :param marking_id:
        :type marking_id: MarkingId
        :param page_size: The page size to use for the endpoint.
        :type page_size: Optional[PageSize]
        :param page_token: The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
        :type page_token: Optional[PageToken]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param transitive: When true, includes the transitive members of groups contained within groups that are members of this  Marking. For example, say the Marking has member Group A, and Group A has member User B. If  `transitive=false` only Group A will be returned, but if `transitive=true` then Group A and User B  will be returned. This will recursively resolve Groups through all layers of nesting.  Defaults to false.
        :type transitive: Optional[bool]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[admin_models.ListMarkingMembersResponse]

        :raises ListMarkingMembersPermissionDenied: The provided token does not have permission to list the members of this marking.
        """

        warnings.warn(
            "The client.admin.MarkingMember.page(...) method has been deprecated. Please use client.admin.MarkingMember.list(...) instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        return self._api_client.stream_api(
            core.RequestInfo(
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
                response_type=admin_models.ListMarkingMembersResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "ListMarkingMembersPermissionDenied": admin_errors.ListMarkingMembersPermissionDenied,
                },
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def remove(
        self,
        marking_id: core_models.MarkingId,
        *,
        principal_ids: typing.List[core_models.PrincipalId],
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[None]:
        """

        :param marking_id:
        :type marking_id: MarkingId
        :param principal_ids:
        :type principal_ids: List[PrincipalId]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[None]

        :raises RemoveMarkingMembersPermissionDenied: Could not remove the MarkingMember.
        """

        return self._api_client.stream_api(
            core.RequestInfo(
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
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "principalIds": typing.List[core_models.PrincipalId],
                    },
                ),
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "RemoveMarkingMembersPermissionDenied": admin_errors.RemoveMarkingMembersPermissionDenied,
                },
            ),
        )
