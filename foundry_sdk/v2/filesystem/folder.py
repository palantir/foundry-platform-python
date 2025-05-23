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

import pydantic
import typing_extensions

from foundry_sdk import _core as core
from foundry_sdk import _errors as errors
from foundry_sdk.v2.core import models as core_models
from foundry_sdk.v2.filesystem import errors as filesystem_errors
from foundry_sdk.v2.filesystem import models as filesystem_models


class FolderClient:
    """
    The API client for the Folder Resource.

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

        self.with_streaming_response = _FolderClientStreaming(self)
        self.with_raw_response = _FolderClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def children(
        self,
        folder_rid: filesystem_models.FolderRid,
        *,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> core.ResourceIterator[filesystem_models.Resource]:
        """
        List all child Resources of the Folder.

        This is a paged endpoint. The page size will be limited to 2,000 results per page. If no page size is
        provided, this page size will also be used as the default.

        :param folder_rid:
        :type folder_rid: FolderRid
        :param page_size: The page size to use for the endpoint.
        :type page_size: Optional[PageSize]
        :param page_token: The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
        :type page_token: Optional[PageToken]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ResourceIterator[filesystem_models.Resource]
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                response_type=filesystem_models.ListChildrenOfFolderResponse,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode", "ITERATOR"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def create(
        self,
        *,
        display_name: filesystem_models.ResourceDisplayName,
        parent_folder_rid: filesystem_models.FolderRid,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> filesystem_models.Folder:
        """
        Creates a new Folder.
        :param display_name:
        :type display_name: ResourceDisplayName
        :param parent_folder_rid: The parent folder Resource Identifier (RID). For Projects, this will be the Space RID and for Spaces, this value will be the root folder (`ri.compass.main.folder.0`).
        :type parent_folder_rid: FolderRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: filesystem_models.Folder

        :raises CreateFolderPermissionDenied: Could not create the Folder.
        :raises ResourceNameAlreadyExists: The provided resource name is already in use by another resource in the same folder.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "parentFolderRid": filesystem_models.FolderRid,
                        "displayName": filesystem_models.ResourceDisplayName,
                    },
                ),
                response_type=filesystem_models.Folder,
                request_timeout=request_timeout,
                throwable_errors={
                    "CreateFolderPermissionDenied": filesystem_errors.CreateFolderPermissionDenied,
                    "ResourceNameAlreadyExists": filesystem_errors.ResourceNameAlreadyExists,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        folder_rid: filesystem_models.FolderRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> filesystem_models.Folder:
        """
        Get the Folder with the specified rid.
        :param folder_rid:
        :type folder_rid: FolderRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: filesystem_models.Folder

        :raises FolderNotFound: The given Folder could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                response_type=filesystem_models.Folder,
                request_timeout=request_timeout,
                throwable_errors={
                    "FolderNotFound": filesystem_errors.FolderNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _FolderClientRaw:
    def __init__(self, client: FolderClient) -> None:
        def children(_: filesystem_models.ListChildrenOfFolderResponse): ...
        def create(_: filesystem_models.Folder): ...
        def get(_: filesystem_models.Folder): ...

        self.children = core.with_raw_response(children, client.children)
        self.create = core.with_raw_response(create, client.create)
        self.get = core.with_raw_response(get, client.get)


class _FolderClientStreaming:
    def __init__(self, client: FolderClient) -> None:
        def children(_: filesystem_models.ListChildrenOfFolderResponse): ...
        def create(_: filesystem_models.Folder): ...
        def get(_: filesystem_models.Folder): ...

        self.children = core.with_streaming_response(children, client.children)
        self.create = core.with_streaming_response(create, client.create)
        self.get = core.with_streaming_response(get, client.get)


class AsyncFolderClient:
    """
    The API client for the Folder Resource.

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
        self._api_client = core.AsyncApiClient(auth=auth, hostname=hostname, config=config)

        self.with_streaming_response = _AsyncFolderClientStreaming(self)
        self.with_raw_response = _AsyncFolderClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def children(
        self,
        folder_rid: filesystem_models.FolderRid,
        *,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> core.AsyncResourceIterator[filesystem_models.Resource]:
        """
        List all child Resources of the Folder.

        This is a paged endpoint. The page size will be limited to 2,000 results per page. If no page size is
        provided, this page size will also be used as the default.

        :param folder_rid:
        :type folder_rid: FolderRid
        :param page_size: The page size to use for the endpoint.
        :type page_size: Optional[PageSize]
        :param page_token: The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
        :type page_token: Optional[PageToken]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.AsyncResourceIterator[filesystem_models.Resource]
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                response_type=filesystem_models.ListChildrenOfFolderResponse,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode", "ITERATOR"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def create(
        self,
        *,
        display_name: filesystem_models.ResourceDisplayName,
        parent_folder_rid: filesystem_models.FolderRid,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[filesystem_models.Folder]:
        """
        Creates a new Folder.
        :param display_name:
        :type display_name: ResourceDisplayName
        :param parent_folder_rid: The parent folder Resource Identifier (RID). For Projects, this will be the Space RID and for Spaces, this value will be the root folder (`ri.compass.main.folder.0`).
        :type parent_folder_rid: FolderRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[filesystem_models.Folder]

        :raises CreateFolderPermissionDenied: Could not create the Folder.
        :raises ResourceNameAlreadyExists: The provided resource name is already in use by another resource in the same folder.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "parentFolderRid": filesystem_models.FolderRid,
                        "displayName": filesystem_models.ResourceDisplayName,
                    },
                ),
                response_type=filesystem_models.Folder,
                request_timeout=request_timeout,
                throwable_errors={
                    "CreateFolderPermissionDenied": filesystem_errors.CreateFolderPermissionDenied,
                    "ResourceNameAlreadyExists": filesystem_errors.ResourceNameAlreadyExists,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        folder_rid: filesystem_models.FolderRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[filesystem_models.Folder]:
        """
        Get the Folder with the specified rid.
        :param folder_rid:
        :type folder_rid: FolderRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[filesystem_models.Folder]

        :raises FolderNotFound: The given Folder could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                response_type=filesystem_models.Folder,
                request_timeout=request_timeout,
                throwable_errors={
                    "FolderNotFound": filesystem_errors.FolderNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _AsyncFolderClientRaw:
    def __init__(self, client: AsyncFolderClient) -> None:
        def children(_: filesystem_models.ListChildrenOfFolderResponse): ...
        def create(_: filesystem_models.Folder): ...
        def get(_: filesystem_models.Folder): ...

        self.children = core.async_with_raw_response(children, client.children)
        self.create = core.async_with_raw_response(create, client.create)
        self.get = core.async_with_raw_response(get, client.get)


class _AsyncFolderClientStreaming:
    def __init__(self, client: AsyncFolderClient) -> None:
        def children(_: filesystem_models.ListChildrenOfFolderResponse): ...
        def create(_: filesystem_models.Folder): ...
        def get(_: filesystem_models.Folder): ...

        self.children = core.async_with_streaming_response(children, client.children)
        self.create = core.async_with_streaming_response(create, client.create)
        self.get = core.async_with_streaming_response(get, client.get)
