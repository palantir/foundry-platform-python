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
from foundry.v2.core.models._page_size import PageSize
from foundry.v2.core.models._page_token import PageToken
from foundry.v2.core.models._preview_mode import PreviewMode
from foundry.v2.filesystem import errors as filesystem_errors
from foundry.v2.filesystem.models._list_resource_roles_response import (
    ListResourceRolesResponse,
)  # NOQA
from foundry.v2.filesystem.models._resource_rid import ResourceRid
from foundry.v2.filesystem.models._resource_role import ResourceRole
from foundry.v2.filesystem.models._resource_role_dict import ResourceRoleDict


class ResourceRoleClient:
    """
    The API client for the ResourceRole Resource.

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
        self.with_streaming_response = _ResourceRoleClientStreaming(
            auth=auth, hostname=hostname, config=config
        )
        self.with_raw_response = _ResourceRoleClientRaw(auth=auth, hostname=hostname, config=config)

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def add(
        self,
        resource_rid: ResourceRid,
        *,
        roles: List[Union[ResourceRole, ResourceRoleDict]],
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> None:
        """

        :param resource_rid: resourceRid
        :type resource_rid: ResourceRid
        :param roles:
        :type roles: List[Union[ResourceRole, ResourceRoleDict]]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: None

        :raises AddResourceRolesPermissionDenied: Could not add the ResourceRole.
        """

        return self._api_client.call_api(
            RequestInfo(
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
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "roles": List[Union[ResourceRole, ResourceRoleDict]],
                    },
                ),
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "AddResourceRolesPermissionDenied": filesystem_errors.AddResourceRolesPermissionDenied,
                },
            ),
        ).decode()

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def list(
        self,
        resource_rid: ResourceRid,
        *,
        include_inherited: Optional[bool] = None,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ResourceIterator[ResourceRole]:
        """
        List the roles on a resource.

        :param resource_rid: resourceRid
        :type resource_rid: ResourceRid
        :param include_inherited: includeInherited
        :type include_inherited: Optional[bool]
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param page_token: pageToken
        :type page_token: Optional[PageToken]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ResourceIterator[ResourceRole]
        """

        return self._api_client.iterate_api(
            RequestInfo(
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
                response_type=ListResourceRolesResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def page(
        self,
        resource_rid: ResourceRid,
        *,
        include_inherited: Optional[bool] = None,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ListResourceRolesResponse:
        """
        List the roles on a resource.

        :param resource_rid: resourceRid
        :type resource_rid: ResourceRid
        :param include_inherited: includeInherited
        :type include_inherited: Optional[bool]
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param page_token: pageToken
        :type page_token: Optional[PageToken]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ListResourceRolesResponse
        """

        warnings.warn(
            "The client.filesystem.Role.page(...) method has been deprecated. Please use client.filesystem.Role.list(...) instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        return self._api_client.call_api(
            RequestInfo(
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
                response_type=ListResourceRolesResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        ).decode()

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def remove(
        self,
        resource_rid: ResourceRid,
        *,
        roles: List[Union[ResourceRole, ResourceRoleDict]],
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> None:
        """

        :param resource_rid: resourceRid
        :type resource_rid: ResourceRid
        :param roles:
        :type roles: List[Union[ResourceRole, ResourceRoleDict]]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: None

        :raises RemoveResourceRolesPermissionDenied: Could not remove the ResourceRole.
        """

        return self._api_client.call_api(
            RequestInfo(
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
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "roles": List[Union[ResourceRole, ResourceRoleDict]],
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
        resource_rid: ResourceRid,
        *,
        roles: List[Union[ResourceRole, ResourceRoleDict]],
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[None]:
        """

        :param resource_rid: resourceRid
        :type resource_rid: ResourceRid
        :param roles:
        :type roles: List[Union[ResourceRole, ResourceRoleDict]]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[None]

        :raises AddResourceRolesPermissionDenied: Could not add the ResourceRole.
        """

        return self._api_client.call_api(
            RequestInfo(
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
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "roles": List[Union[ResourceRole, ResourceRoleDict]],
                    },
                ),
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "AddResourceRolesPermissionDenied": filesystem_errors.AddResourceRolesPermissionDenied,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def list(
        self,
        resource_rid: ResourceRid,
        *,
        include_inherited: Optional[bool] = None,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[ListResourceRolesResponse]:
        """
        List the roles on a resource.

        :param resource_rid: resourceRid
        :type resource_rid: ResourceRid
        :param include_inherited: includeInherited
        :type include_inherited: Optional[bool]
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param page_token: pageToken
        :type page_token: Optional[PageToken]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[ListResourceRolesResponse]
        """

        return self._api_client.call_api(
            RequestInfo(
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
                response_type=ListResourceRolesResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def page(
        self,
        resource_rid: ResourceRid,
        *,
        include_inherited: Optional[bool] = None,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[ListResourceRolesResponse]:
        """
        List the roles on a resource.

        :param resource_rid: resourceRid
        :type resource_rid: ResourceRid
        :param include_inherited: includeInherited
        :type include_inherited: Optional[bool]
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param page_token: pageToken
        :type page_token: Optional[PageToken]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[ListResourceRolesResponse]
        """

        warnings.warn(
            "The client.filesystem.Role.page(...) method has been deprecated. Please use client.filesystem.Role.list(...) instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        return self._api_client.call_api(
            RequestInfo(
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
                response_type=ListResourceRolesResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def remove(
        self,
        resource_rid: ResourceRid,
        *,
        roles: List[Union[ResourceRole, ResourceRoleDict]],
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[None]:
        """

        :param resource_rid: resourceRid
        :type resource_rid: ResourceRid
        :param roles:
        :type roles: List[Union[ResourceRole, ResourceRoleDict]]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[None]

        :raises RemoveResourceRolesPermissionDenied: Could not remove the ResourceRole.
        """

        return self._api_client.call_api(
            RequestInfo(
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
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "roles": List[Union[ResourceRole, ResourceRoleDict]],
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
        resource_rid: ResourceRid,
        *,
        roles: List[Union[ResourceRole, ResourceRoleDict]],
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[None]:
        """

        :param resource_rid: resourceRid
        :type resource_rid: ResourceRid
        :param roles:
        :type roles: List[Union[ResourceRole, ResourceRoleDict]]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[None]

        :raises AddResourceRolesPermissionDenied: Could not add the ResourceRole.
        """

        return self._api_client.stream_api(
            RequestInfo(
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
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "roles": List[Union[ResourceRole, ResourceRoleDict]],
                    },
                ),
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "AddResourceRolesPermissionDenied": filesystem_errors.AddResourceRolesPermissionDenied,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def list(
        self,
        resource_rid: ResourceRid,
        *,
        include_inherited: Optional[bool] = None,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[ListResourceRolesResponse]:
        """
        List the roles on a resource.

        :param resource_rid: resourceRid
        :type resource_rid: ResourceRid
        :param include_inherited: includeInherited
        :type include_inherited: Optional[bool]
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param page_token: pageToken
        :type page_token: Optional[PageToken]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[ListResourceRolesResponse]
        """

        return self._api_client.stream_api(
            RequestInfo(
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
                response_type=ListResourceRolesResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def page(
        self,
        resource_rid: ResourceRid,
        *,
        include_inherited: Optional[bool] = None,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[ListResourceRolesResponse]:
        """
        List the roles on a resource.

        :param resource_rid: resourceRid
        :type resource_rid: ResourceRid
        :param include_inherited: includeInherited
        :type include_inherited: Optional[bool]
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param page_token: pageToken
        :type page_token: Optional[PageToken]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[ListResourceRolesResponse]
        """

        warnings.warn(
            "The client.filesystem.Role.page(...) method has been deprecated. Please use client.filesystem.Role.list(...) instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        return self._api_client.stream_api(
            RequestInfo(
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
                response_type=ListResourceRolesResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def remove(
        self,
        resource_rid: ResourceRid,
        *,
        roles: List[Union[ResourceRole, ResourceRoleDict]],
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[None]:
        """

        :param resource_rid: resourceRid
        :type resource_rid: ResourceRid
        :param roles:
        :type roles: List[Union[ResourceRole, ResourceRoleDict]]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[None]

        :raises RemoveResourceRolesPermissionDenied: Could not remove the ResourceRole.
        """

        return self._api_client.stream_api(
            RequestInfo(
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
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "roles": List[Union[ResourceRole, ResourceRoleDict]],
                    },
                ),
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "RemoveResourceRolesPermissionDenied": filesystem_errors.RemoveResourceRolesPermissionDenied,
                },
            ),
        )
