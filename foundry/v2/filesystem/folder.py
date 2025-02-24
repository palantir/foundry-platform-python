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
from typing import Optional

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
from foundry.v2.filesystem.models._folder import Folder
from foundry.v2.filesystem.models._folder_rid import FolderRid
from foundry.v2.filesystem.models._list_children_of_folder_response import (
    ListChildrenOfFolderResponse,
)  # NOQA
from foundry.v2.filesystem.models._resource import Resource
from foundry.v2.filesystem.models._resource_display_name import ResourceDisplayName


class FolderClient:
    """
    The API client for the Folder Resource.

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
        self.with_streaming_response = _FolderClientStreaming(
            auth=auth, hostname=hostname, config=config
        )
        self.with_raw_response = _FolderClientRaw(auth=auth, hostname=hostname, config=config)

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def children(
        self,
        folder_rid: FolderRid,
        *,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ResourceIterator[Resource]:
        """
        List all child Resources of the Folder.

        This is a paged endpoint. The page size will be limited to 2,000 results per page. If no page size is
        provided, this page size will also be used as the default.

        :param folder_rid: folderRid
        :type folder_rid: FolderRid
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param page_token: pageToken
        :type page_token: Optional[PageToken]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ResourceIterator[Resource]
        """

        return self._api_client.iterate_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/filesystem/folders/{folderRid}/children",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
                    "preview": preview,
                },
                path_params={
                    "folderRid": folder_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ListChildrenOfFolderResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def children_page(
        self,
        folder_rid: FolderRid,
        *,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ListChildrenOfFolderResponse:
        """
        List all child Resources of the Folder.

        This is a paged endpoint. The page size will be limited to 2,000 results per page. If no page size is
        provided, this page size will also be used as the default.

        :param folder_rid: folderRid
        :type folder_rid: FolderRid
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param page_token: pageToken
        :type page_token: Optional[PageToken]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ListChildrenOfFolderResponse
        """

        warnings.warn(
            "The client.filesystem.Folder.children_page(...) method has been deprecated. Please use client.filesystem.Folder.children(...) instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/filesystem/folders/{folderRid}/children",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
                    "preview": preview,
                },
                path_params={
                    "folderRid": folder_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ListChildrenOfFolderResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        ).decode()

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def create(
        self,
        *,
        display_name: ResourceDisplayName,
        parent_folder_rid: FolderRid,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> Folder:
        """
        Creates a new Folder.
        :param display_name:
        :type display_name: ResourceDisplayName
        :param parent_folder_rid: The parent folder Resource Identifier (RID). For Projects, this will be the Space RID and for Spaces, this value will be the root folder (`ri.compass.main.folder.0`).
        :type parent_folder_rid: FolderRid
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: Folder

        :raises CreateFolderPermissionDenied: Could not create the Folder.
        :raises ResourceNameAlreadyExists: The provided resource name is already in use by another resource in the same folder.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/filesystem/folders",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "parentFolderRid": parent_folder_rid,
                    "displayName": display_name,
                },
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "parentFolderRid": FolderRid,
                        "displayName": ResourceDisplayName,
                    },
                ),
                response_type=Folder,
                request_timeout=request_timeout,
                throwable_errors={
                    "CreateFolderPermissionDenied": filesystem_errors.CreateFolderPermissionDenied,
                    "ResourceNameAlreadyExists": filesystem_errors.ResourceNameAlreadyExists,
                },
            ),
        ).decode()

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def get(
        self,
        folder_rid: FolderRid,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> Folder:
        """
        Get the Folder with the specified rid.
        :param folder_rid: folderRid
        :type folder_rid: FolderRid
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: Folder

        :raises FolderNotFound: The given Folder could not be found.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/filesystem/folders/{folderRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "folderRid": folder_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=Folder,
                request_timeout=request_timeout,
                throwable_errors={
                    "FolderNotFound": filesystem_errors.FolderNotFound,
                },
            ),
        ).decode()


class _FolderClientRaw:
    """
    The API client for the Folder Resource.

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
    def children(
        self,
        folder_rid: FolderRid,
        *,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[ListChildrenOfFolderResponse]:
        """
        List all child Resources of the Folder.

        This is a paged endpoint. The page size will be limited to 2,000 results per page. If no page size is
        provided, this page size will also be used as the default.

        :param folder_rid: folderRid
        :type folder_rid: FolderRid
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param page_token: pageToken
        :type page_token: Optional[PageToken]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[ListChildrenOfFolderResponse]
        """

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/filesystem/folders/{folderRid}/children",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
                    "preview": preview,
                },
                path_params={
                    "folderRid": folder_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ListChildrenOfFolderResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def children_page(
        self,
        folder_rid: FolderRid,
        *,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[ListChildrenOfFolderResponse]:
        """
        List all child Resources of the Folder.

        This is a paged endpoint. The page size will be limited to 2,000 results per page. If no page size is
        provided, this page size will also be used as the default.

        :param folder_rid: folderRid
        :type folder_rid: FolderRid
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param page_token: pageToken
        :type page_token: Optional[PageToken]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[ListChildrenOfFolderResponse]
        """

        warnings.warn(
            "The client.filesystem.Folder.children_page(...) method has been deprecated. Please use client.filesystem.Folder.children(...) instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/filesystem/folders/{folderRid}/children",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
                    "preview": preview,
                },
                path_params={
                    "folderRid": folder_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ListChildrenOfFolderResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def create(
        self,
        *,
        display_name: ResourceDisplayName,
        parent_folder_rid: FolderRid,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[Folder]:
        """
        Creates a new Folder.
        :param display_name:
        :type display_name: ResourceDisplayName
        :param parent_folder_rid: The parent folder Resource Identifier (RID). For Projects, this will be the Space RID and for Spaces, this value will be the root folder (`ri.compass.main.folder.0`).
        :type parent_folder_rid: FolderRid
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[Folder]

        :raises CreateFolderPermissionDenied: Could not create the Folder.
        :raises ResourceNameAlreadyExists: The provided resource name is already in use by another resource in the same folder.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/filesystem/folders",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "parentFolderRid": parent_folder_rid,
                    "displayName": display_name,
                },
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "parentFolderRid": FolderRid,
                        "displayName": ResourceDisplayName,
                    },
                ),
                response_type=Folder,
                request_timeout=request_timeout,
                throwable_errors={
                    "CreateFolderPermissionDenied": filesystem_errors.CreateFolderPermissionDenied,
                    "ResourceNameAlreadyExists": filesystem_errors.ResourceNameAlreadyExists,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def get(
        self,
        folder_rid: FolderRid,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[Folder]:
        """
        Get the Folder with the specified rid.
        :param folder_rid: folderRid
        :type folder_rid: FolderRid
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[Folder]

        :raises FolderNotFound: The given Folder could not be found.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/filesystem/folders/{folderRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "folderRid": folder_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=Folder,
                request_timeout=request_timeout,
                throwable_errors={
                    "FolderNotFound": filesystem_errors.FolderNotFound,
                },
            ),
        )


class _FolderClientStreaming:
    """
    The API client for the Folder Resource.

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
    def children(
        self,
        folder_rid: FolderRid,
        *,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[ListChildrenOfFolderResponse]:
        """
        List all child Resources of the Folder.

        This is a paged endpoint. The page size will be limited to 2,000 results per page. If no page size is
        provided, this page size will also be used as the default.

        :param folder_rid: folderRid
        :type folder_rid: FolderRid
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param page_token: pageToken
        :type page_token: Optional[PageToken]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[ListChildrenOfFolderResponse]
        """

        return self._api_client.stream_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/filesystem/folders/{folderRid}/children",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
                    "preview": preview,
                },
                path_params={
                    "folderRid": folder_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ListChildrenOfFolderResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def children_page(
        self,
        folder_rid: FolderRid,
        *,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[ListChildrenOfFolderResponse]:
        """
        List all child Resources of the Folder.

        This is a paged endpoint. The page size will be limited to 2,000 results per page. If no page size is
        provided, this page size will also be used as the default.

        :param folder_rid: folderRid
        :type folder_rid: FolderRid
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param page_token: pageToken
        :type page_token: Optional[PageToken]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[ListChildrenOfFolderResponse]
        """

        warnings.warn(
            "The client.filesystem.Folder.children_page(...) method has been deprecated. Please use client.filesystem.Folder.children(...) instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        return self._api_client.stream_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/filesystem/folders/{folderRid}/children",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
                    "preview": preview,
                },
                path_params={
                    "folderRid": folder_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ListChildrenOfFolderResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def create(
        self,
        *,
        display_name: ResourceDisplayName,
        parent_folder_rid: FolderRid,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[Folder]:
        """
        Creates a new Folder.
        :param display_name:
        :type display_name: ResourceDisplayName
        :param parent_folder_rid: The parent folder Resource Identifier (RID). For Projects, this will be the Space RID and for Spaces, this value will be the root folder (`ri.compass.main.folder.0`).
        :type parent_folder_rid: FolderRid
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[Folder]

        :raises CreateFolderPermissionDenied: Could not create the Folder.
        :raises ResourceNameAlreadyExists: The provided resource name is already in use by another resource in the same folder.
        """

        return self._api_client.stream_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/filesystem/folders",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "parentFolderRid": parent_folder_rid,
                    "displayName": display_name,
                },
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "parentFolderRid": FolderRid,
                        "displayName": ResourceDisplayName,
                    },
                ),
                response_type=Folder,
                request_timeout=request_timeout,
                throwable_errors={
                    "CreateFolderPermissionDenied": filesystem_errors.CreateFolderPermissionDenied,
                    "ResourceNameAlreadyExists": filesystem_errors.ResourceNameAlreadyExists,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def get(
        self,
        folder_rid: FolderRid,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[Folder]:
        """
        Get the Folder with the specified rid.
        :param folder_rid: folderRid
        :type folder_rid: FolderRid
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[Folder]

        :raises FolderNotFound: The given Folder could not be found.
        """

        return self._api_client.stream_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/filesystem/folders/{folderRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "folderRid": folder_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=Folder,
                request_timeout=request_timeout,
                throwable_errors={
                    "FolderNotFound": filesystem_errors.FolderNotFound,
                },
            ),
        )
