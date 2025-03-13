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
from foundry.v2.core import models as core_models
from foundry.v2.filesystem import errors as filesystem_errors
from foundry.v2.filesystem import models as filesystem_models


class ResourceRoleClient:
    """
    The API client for the ResourceRole Resource.

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
        self.with_streaming_response = _ResourceRoleClientStreaming(
            auth=auth, hostname=hostname, config=config
        )
        self.with_raw_response = _ResourceRoleClientRaw(auth=auth, hostname=hostname, config=config)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def add(
        self,
        resource_rid: filesystem_models.ResourceRid,
        *,
        roles: typing.List[
            typing.Union[filesystem_models.ResourceRole, filesystem_models.ResourceRoleDict]
        ],
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> None:
        """

        :param resource_rid:
        :type resource_rid: ResourceRid
        :param roles:
        :type roles: List[Union[ResourceRole, ResourceRoleDict]]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: None

        :raises AddResourceRolesPermissionDenied: Could not add the ResourceRole.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/filesystem/resources/{resourceRid}/roles/add",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "resourceRid": resource_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                },
                body={
                    "roles": roles,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "roles": typing.List[
                            typing.Union[
                                filesystem_models.ResourceRole, filesystem_models.ResourceRoleDict
                            ]
                        ],
                    },
                ),
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "AddResourceRolesPermissionDenied": filesystem_errors.AddResourceRolesPermissionDenied,
                },
            ),
        ).decode()

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def list(
        self,
        resource_rid: filesystem_models.ResourceRid,
        *,
        include_inherited: typing.Optional[bool] = None,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ResourceIterator[filesystem_models.ResourceRole]:
        """
        List the roles on a resource.

        :param resource_rid:
        :type resource_rid: ResourceRid
        :param include_inherited: Whether to include inherited roles on the resource.
        :type include_inherited: Optional[bool]
        :param page_size: The page size to use for the endpoint.
        :type page_size: Optional[PageSize]
        :param page_token: The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
        :type page_token: Optional[PageToken]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ResourceIterator[filesystem_models.ResourceRole]
        """

        return self._api_client.iterate_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/filesystem/resources/{resourceRid}/roles",
                query_params={
                    "includeInherited": include_inherited,
                    "pageSize": page_size,
                    "pageToken": page_token,
                    "preview": preview,
                },
                path_params={
                    "resourceRid": resource_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=filesystem_models.ListResourceRolesResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def page(
        self,
        resource_rid: filesystem_models.ResourceRid,
        *,
        include_inherited: typing.Optional[bool] = None,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> filesystem_models.ListResourceRolesResponse:
        """
        List the roles on a resource.

        :param resource_rid:
        :type resource_rid: ResourceRid
        :param include_inherited: Whether to include inherited roles on the resource.
        :type include_inherited: Optional[bool]
        :param page_size: The page size to use for the endpoint.
        :type page_size: Optional[PageSize]
        :param page_token: The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
        :type page_token: Optional[PageToken]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: filesystem_models.ListResourceRolesResponse
        """

        warnings.warn(
            "The client.filesystem.Role.page(...) method has been deprecated. Please use client.filesystem.Role.list(...) instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/filesystem/resources/{resourceRid}/roles",
                query_params={
                    "includeInherited": include_inherited,
                    "pageSize": page_size,
                    "pageToken": page_token,
                    "preview": preview,
                },
                path_params={
                    "resourceRid": resource_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=filesystem_models.ListResourceRolesResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        ).decode()

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def remove(
        self,
        resource_rid: filesystem_models.ResourceRid,
        *,
        roles: typing.List[
            typing.Union[filesystem_models.ResourceRole, filesystem_models.ResourceRoleDict]
        ],
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> None:
        """

        :param resource_rid:
        :type resource_rid: ResourceRid
        :param roles:
        :type roles: List[Union[ResourceRole, ResourceRoleDict]]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: None

        :raises RemoveResourceRolesPermissionDenied: Could not remove the ResourceRole.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/filesystem/resources/{resourceRid}/roles/remove",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "resourceRid": resource_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                },
                body={
                    "roles": roles,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "roles": typing.List[
                            typing.Union[
                                filesystem_models.ResourceRole, filesystem_models.ResourceRoleDict
                            ]
                        ],
                    },
                ),
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "RemoveResourceRolesPermissionDenied": filesystem_errors.RemoveResourceRolesPermissionDenied,
                },
            ),
        ).decode()


class _ResourceRoleClientRaw:
    """
    The API client for the ResourceRole Resource.

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
        resource_rid: filesystem_models.ResourceRid,
        *,
        roles: typing.List[
            typing.Union[filesystem_models.ResourceRole, filesystem_models.ResourceRoleDict]
        ],
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[None]:
        """

        :param resource_rid:
        :type resource_rid: ResourceRid
        :param roles:
        :type roles: List[Union[ResourceRole, ResourceRoleDict]]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[None]

        :raises AddResourceRolesPermissionDenied: Could not add the ResourceRole.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/filesystem/resources/{resourceRid}/roles/add",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "resourceRid": resource_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                },
                body={
                    "roles": roles,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "roles": typing.List[
                            typing.Union[
                                filesystem_models.ResourceRole, filesystem_models.ResourceRoleDict
                            ]
                        ],
                    },
                ),
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "AddResourceRolesPermissionDenied": filesystem_errors.AddResourceRolesPermissionDenied,
                },
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def list(
        self,
        resource_rid: filesystem_models.ResourceRid,
        *,
        include_inherited: typing.Optional[bool] = None,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[filesystem_models.ListResourceRolesResponse]:
        """
        List the roles on a resource.

        :param resource_rid:
        :type resource_rid: ResourceRid
        :param include_inherited: Whether to include inherited roles on the resource.
        :type include_inherited: Optional[bool]
        :param page_size: The page size to use for the endpoint.
        :type page_size: Optional[PageSize]
        :param page_token: The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
        :type page_token: Optional[PageToken]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[filesystem_models.ListResourceRolesResponse]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/filesystem/resources/{resourceRid}/roles",
                query_params={
                    "includeInherited": include_inherited,
                    "pageSize": page_size,
                    "pageToken": page_token,
                    "preview": preview,
                },
                path_params={
                    "resourceRid": resource_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=filesystem_models.ListResourceRolesResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def page(
        self,
        resource_rid: filesystem_models.ResourceRid,
        *,
        include_inherited: typing.Optional[bool] = None,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[filesystem_models.ListResourceRolesResponse]:
        """
        List the roles on a resource.

        :param resource_rid:
        :type resource_rid: ResourceRid
        :param include_inherited: Whether to include inherited roles on the resource.
        :type include_inherited: Optional[bool]
        :param page_size: The page size to use for the endpoint.
        :type page_size: Optional[PageSize]
        :param page_token: The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
        :type page_token: Optional[PageToken]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[filesystem_models.ListResourceRolesResponse]
        """

        warnings.warn(
            "The client.filesystem.Role.page(...) method has been deprecated. Please use client.filesystem.Role.list(...) instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/filesystem/resources/{resourceRid}/roles",
                query_params={
                    "includeInherited": include_inherited,
                    "pageSize": page_size,
                    "pageToken": page_token,
                    "preview": preview,
                },
                path_params={
                    "resourceRid": resource_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=filesystem_models.ListResourceRolesResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def remove(
        self,
        resource_rid: filesystem_models.ResourceRid,
        *,
        roles: typing.List[
            typing.Union[filesystem_models.ResourceRole, filesystem_models.ResourceRoleDict]
        ],
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[None]:
        """

        :param resource_rid:
        :type resource_rid: ResourceRid
        :param roles:
        :type roles: List[Union[ResourceRole, ResourceRoleDict]]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[None]

        :raises RemoveResourceRolesPermissionDenied: Could not remove the ResourceRole.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/filesystem/resources/{resourceRid}/roles/remove",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "resourceRid": resource_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                },
                body={
                    "roles": roles,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "roles": typing.List[
                            typing.Union[
                                filesystem_models.ResourceRole, filesystem_models.ResourceRoleDict
                            ]
                        ],
                    },
                ),
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "RemoveResourceRolesPermissionDenied": filesystem_errors.RemoveResourceRolesPermissionDenied,
                },
            ),
        )


class _ResourceRoleClientStreaming:
    """
    The API client for the ResourceRole Resource.

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
        resource_rid: filesystem_models.ResourceRid,
        *,
        roles: typing.List[
            typing.Union[filesystem_models.ResourceRole, filesystem_models.ResourceRoleDict]
        ],
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[None]:
        """

        :param resource_rid:
        :type resource_rid: ResourceRid
        :param roles:
        :type roles: List[Union[ResourceRole, ResourceRoleDict]]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[None]

        :raises AddResourceRolesPermissionDenied: Could not add the ResourceRole.
        """

        return self._api_client.stream_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/filesystem/resources/{resourceRid}/roles/add",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "resourceRid": resource_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                },
                body={
                    "roles": roles,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "roles": typing.List[
                            typing.Union[
                                filesystem_models.ResourceRole, filesystem_models.ResourceRoleDict
                            ]
                        ],
                    },
                ),
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "AddResourceRolesPermissionDenied": filesystem_errors.AddResourceRolesPermissionDenied,
                },
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def list(
        self,
        resource_rid: filesystem_models.ResourceRid,
        *,
        include_inherited: typing.Optional[bool] = None,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[filesystem_models.ListResourceRolesResponse]:
        """
        List the roles on a resource.

        :param resource_rid:
        :type resource_rid: ResourceRid
        :param include_inherited: Whether to include inherited roles on the resource.
        :type include_inherited: Optional[bool]
        :param page_size: The page size to use for the endpoint.
        :type page_size: Optional[PageSize]
        :param page_token: The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
        :type page_token: Optional[PageToken]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[filesystem_models.ListResourceRolesResponse]
        """

        return self._api_client.stream_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/filesystem/resources/{resourceRid}/roles",
                query_params={
                    "includeInherited": include_inherited,
                    "pageSize": page_size,
                    "pageToken": page_token,
                    "preview": preview,
                },
                path_params={
                    "resourceRid": resource_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=filesystem_models.ListResourceRolesResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def page(
        self,
        resource_rid: filesystem_models.ResourceRid,
        *,
        include_inherited: typing.Optional[bool] = None,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[filesystem_models.ListResourceRolesResponse]:
        """
        List the roles on a resource.

        :param resource_rid:
        :type resource_rid: ResourceRid
        :param include_inherited: Whether to include inherited roles on the resource.
        :type include_inherited: Optional[bool]
        :param page_size: The page size to use for the endpoint.
        :type page_size: Optional[PageSize]
        :param page_token: The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
        :type page_token: Optional[PageToken]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[filesystem_models.ListResourceRolesResponse]
        """

        warnings.warn(
            "The client.filesystem.Role.page(...) method has been deprecated. Please use client.filesystem.Role.list(...) instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        return self._api_client.stream_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/filesystem/resources/{resourceRid}/roles",
                query_params={
                    "includeInherited": include_inherited,
                    "pageSize": page_size,
                    "pageToken": page_token,
                    "preview": preview,
                },
                path_params={
                    "resourceRid": resource_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=filesystem_models.ListResourceRolesResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def remove(
        self,
        resource_rid: filesystem_models.ResourceRid,
        *,
        roles: typing.List[
            typing.Union[filesystem_models.ResourceRole, filesystem_models.ResourceRoleDict]
        ],
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[None]:
        """

        :param resource_rid:
        :type resource_rid: ResourceRid
        :param roles:
        :type roles: List[Union[ResourceRole, ResourceRoleDict]]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[None]

        :raises RemoveResourceRolesPermissionDenied: Could not remove the ResourceRole.
        """

        return self._api_client.stream_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/filesystem/resources/{resourceRid}/roles/remove",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "resourceRid": resource_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                },
                body={
                    "roles": roles,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "roles": typing.List[
                            typing.Union[
                                filesystem_models.ResourceRole, filesystem_models.ResourceRoleDict
                            ]
                        ],
                    },
                ),
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "RemoveResourceRolesPermissionDenied": filesystem_errors.RemoveResourceRolesPermissionDenied,
                },
            ),
        )
