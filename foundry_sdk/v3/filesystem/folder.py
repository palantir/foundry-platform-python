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

import annotated_types
import pydantic
import typing_extensions

from foundry_sdk import _core as core
from foundry_sdk import _errors as errors
from foundry_sdk.v3.core import errors as core_errors
from foundry_sdk.v3.core import models as core_models
from foundry_sdk.v3.filesystem import errors as filesystem_errors
from foundry_sdk.v3.filesystem import models as filesystem_models


class FolderClient:
    """
    The API client for the Folder Resource.

    :param auth: Your auth configuration.
    :param hostname: The hostname supplier for resolving base URLs.
    :param config: Optionally specify the configuration for the HTTP session.
    """

    def __init__(
        self,
        auth: core.Auth,
        hostname: typing.Union[str, core.HostnameSupplier],
        config: typing.Optional[core.Config] = None,
    ):
        self._auth = auth
        if isinstance(hostname, core.HostnameSupplier):
            self._hostname_supplier = hostname
        else:
            self._hostname_supplier = core.create_hostname_supplier(hostname, config)
        self._hostname = self._hostname_supplier.get_hostname()
        self._config = config
        self._api_client = core.ApiClient(
            auth=auth, hostname=self._hostname_supplier, config=config
        )

        self.with_streaming_response = _FolderClientStreaming(self)
        self.with_raw_response = _FolderClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def create(
        self,
        *,
        display_name: filesystem_models.DisplayName,
        parent_folder_rid: core_models.FolderRid,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> filesystem_models.Folder:
        """
        Create a new folder in the given parent folder.

        Required scopes: [api:v3:folder:write:create]

        :param display_name: The display name of the folder.
        :type display_name: DisplayName
        :param parent_folder_rid: The RID of the existing project or folder in which to create the new folder. The parent must be inside a project.
        :type parent_folder_rid: FolderRid
        :param preview:
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: filesystem_models.Folder

        :raises CreateFolderOutsideProjectNotSupported: Folders can only be created within a project.
        :raises CreateFolderPermissionDenied: Could not create the folder due to insufficient permissions.
        :raises InvalidDisplayName: A display name must not be empty, must not be exactly `.` or `..`, must not contain a forward slash (`/`), and must not exceed 700 characters.
        :raises InvalidParentFolder: The specified parent resource is not a folder.
        :raises MissingDisplayName: A display name must be provided.
        :raises ParentFolderNotFound: The specified parent folder could not be found.
        :raises ResourceDisplayNameAlreadyExists: The provided resource display name is already in use by another resource in the same folder.
        :raises ResourceRegisteredForDeletion: The resource, or one of its ancestors, is registered for deletion. Resources cannot be created within, or restored within, a project or space that is registered for deletion.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v3/platform/folders",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body=filesystem_models.CreateFolderRequest(
                    display_name=display_name,
                    parent_folder_rid=parent_folder_rid,
                ),
                response_type=filesystem_models.Folder,
                request_timeout=request_timeout,
                throwable_errors={
                    "CreateFolderOutsideProjectNotSupported": filesystem_errors.CreateFolderOutsideProjectNotSupported,
                    "CreateFolderPermissionDenied": filesystem_errors.CreateFolderPermissionDenied,
                    "InvalidDisplayName": filesystem_errors.InvalidDisplayName,
                    "InvalidParentFolder": filesystem_errors.InvalidParentFolder,
                    "MissingDisplayName": filesystem_errors.MissingDisplayName,
                    "ParentFolderNotFound": filesystem_errors.ParentFolderNotFound,
                    "ResourceDisplayNameAlreadyExists": filesystem_errors.ResourceDisplayNameAlreadyExists,
                    "ResourceRegisteredForDeletion": filesystem_errors.ResourceRegisteredForDeletion,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def delete(
        self,
        folder_rid: core_models.FolderRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> None:
        """
        Move the given folder to the trash. Following this operation, the folder can be restored, using the
        `restore` operation, or permanently deleted using the `permanentlyDelete` operation.

        Required scopes: [api:v3:folder:write:delete]

        :param folder_rid:
        :type folder_rid: FolderRid
        :param preview:
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: None

        :raises DeleteFolderPermissionDenied: Could not delete the folder due to insufficient permissions.
        :raises DeleteOntologyResourcePermissionDenied: The resource, or one of its descendants, backs an ontology entity. Trashing such a resource through the filesystem would leave the ontology in an inconsistent state, so it must be deleted through the ontology APIs instead.
        :raises FoldersNotFound: The specified folders could not be found.
        :raises InvalidFolders: The given resources are not folders.
        :raises TrashingHiddenResourcesNotSupported: Hidden resources cannot be trashed.
        :raises TrashingHomeFoldersNotSupported: Home folders cannot be trashed. Home folders are created and managed by the platform.
        :raises TrashingRootFolderNotSupported: The root folder cannot be trashed.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="DELETE",
                resource_path="/v3/platform/folders/{folderRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "folderRid": folder_rid,
                },
                header_params={},
                body=None,
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "DeleteFolderPermissionDenied": filesystem_errors.DeleteFolderPermissionDenied,
                    "DeleteOntologyResourcePermissionDenied": filesystem_errors.DeleteOntologyResourcePermissionDenied,
                    "FoldersNotFound": filesystem_errors.FoldersNotFound,
                    "InvalidFolders": filesystem_errors.InvalidFolders,
                    "TrashingHiddenResourcesNotSupported": filesystem_errors.TrashingHiddenResourcesNotSupported,
                    "TrashingHomeFoldersNotSupported": filesystem_errors.TrashingHomeFoldersNotSupported,
                    "TrashingRootFolderNotSupported": filesystem_errors.TrashingRootFolderNotSupported,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def delete_batch(
        self,
        body: typing_extensions.Annotated[
            typing.List[filesystem_models.DeleteFoldersBatchRequestElement],
            annotated_types.Len(min_length=1, max_length=100),
        ],
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> None:
        """
        Trash multiple folders in a single request.

        Required scopes: [api:v3:folder:write:delete]

        :param body: Body of the request
        :type body: List[DeleteFoldersBatchRequestElement]
        :param preview:
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: None

        :raises BatchRequestSizeExceededLimit:
        :raises DeleteFolderPermissionDenied: Could not delete the folder due to insufficient permissions.
        :raises DeleteOntologyResourcePermissionDenied: The resource, or one of its descendants, backs an ontology entity. Trashing such a resource through the filesystem would leave the ontology in an inconsistent state, so it must be deleted through the ontology APIs instead.
        :raises FoldersNotFound: The specified folders could not be found.
        :raises InvalidFolders: The given resources are not folders.
        :raises MissingBatchRequest:
        :raises TrashingHiddenResourcesNotSupported: Hidden resources cannot be trashed.
        :raises TrashingHomeFoldersNotSupported: Home folders cannot be trashed. Home folders are created and managed by the platform.
        :raises TrashingRootFolderNotSupported: The root folder cannot be trashed.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v3/platform/folders/deleteBatch",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                },
                body=body,
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "BatchRequestSizeExceededLimit": core_errors.BatchRequestSizeExceededLimit,
                    "DeleteFolderPermissionDenied": filesystem_errors.DeleteFolderPermissionDenied,
                    "DeleteOntologyResourcePermissionDenied": filesystem_errors.DeleteOntologyResourcePermissionDenied,
                    "FoldersNotFound": filesystem_errors.FoldersNotFound,
                    "InvalidFolders": filesystem_errors.InvalidFolders,
                    "MissingBatchRequest": core_errors.MissingBatchRequest,
                    "TrashingHiddenResourcesNotSupported": filesystem_errors.TrashingHiddenResourcesNotSupported,
                    "TrashingHomeFoldersNotSupported": filesystem_errors.TrashingHomeFoldersNotSupported,
                    "TrashingRootFolderNotSupported": filesystem_errors.TrashingRootFolderNotSupported,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        folder_rid: core_models.FolderRid,
        *,
        include: typing.Optional[typing.List[filesystem_models.AdditionalField]] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> filesystem_models.Folder:
        """
        Get the folder with the specified resource identifier (RID).

        Required scopes: [api:v3:folder:read:get]

        :param folder_rid:
        :type folder_rid: FolderRid
        :param include:
        :type include: Optional[List[AdditionalField]]
        :param preview:
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: filesystem_models.Folder

        :raises FoldersNotFound: The specified folders could not be found.
        :raises GetResourceTimedOut: The request to retrieve resource information timed out.
        :raises GetRootFolderNotSupported: The root folder cannot be retrieved.
        :raises InvalidFolders: The given resources are not folders.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v3/platform/folders/{folderRid}",
                query_params={
                    "include": include,
                    "preview": preview,
                },
                path_params={
                    "folderRid": folder_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=filesystem_models.Folder,
                request_timeout=request_timeout,
                throwable_errors={
                    "FoldersNotFound": filesystem_errors.FoldersNotFound,
                    "GetResourceTimedOut": filesystem_errors.GetResourceTimedOut,
                    "GetRootFolderNotSupported": filesystem_errors.GetRootFolderNotSupported,
                    "InvalidFolders": filesystem_errors.InvalidFolders,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get_batch(
        self,
        body: typing_extensions.Annotated[
            typing.List[filesystem_models.GetFoldersBatchRequestElement],
            annotated_types.Len(min_length=1, max_length=2000),
        ],
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> filesystem_models.GetFoldersBatchResponse:
        """
        Fetch multiple folders in a single request.

        Required scopes: [api:v3:folder:read:get]

        :param body: Body of the request
        :type body: List[GetFoldersBatchRequestElement]
        :param preview:
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: filesystem_models.GetFoldersBatchResponse

        :raises BatchRequestSizeExceededLimit:
        :raises FoldersNotFound: The specified folders could not be found.
        :raises GetResourceTimedOut: The request to retrieve resource information timed out.
        :raises GetRootFolderNotSupported: The root folder cannot be retrieved.
        :raises InvalidFolders: The given resources are not folders.
        :raises MissingBatchRequest:
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v3/platform/folders/getBatch",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body=body,
                response_type=filesystem_models.GetFoldersBatchResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "BatchRequestSizeExceededLimit": core_errors.BatchRequestSizeExceededLimit,
                    "FoldersNotFound": filesystem_errors.FoldersNotFound,
                    "GetResourceTimedOut": filesystem_errors.GetResourceTimedOut,
                    "GetRootFolderNotSupported": filesystem_errors.GetRootFolderNotSupported,
                    "InvalidFolders": filesystem_errors.InvalidFolders,
                    "MissingBatchRequest": core_errors.MissingBatchRequest,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def restore(
        self,
        folder_rid: core_models.FolderRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> None:
        """
        Restore the given folder and any directly trashed ancestors from the trash. If the folder is not
        directly trashed, this operation will return an error.

        Required scopes: [api:v3:folder:write:restore]

        :param folder_rid:
        :type folder_rid: FolderRid
        :param preview:
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: None

        :raises FoldersNotFound: The specified folders could not be found.
        :raises InvalidDisplayNameOnRestore: Cannot restore resource because restoring it would produce an invalid display name. While the resource is still in trash, rename it to a valid name that does not contain the reserved text ' (trashed)', then retry the restore.
        :raises InvalidFolders: The given resources are not folders.
        :raises ResourceNotDirectlyTrashed: The resource is not directly trashed.
        :raises ResourceRegisteredForDeletion: The resource, or one of its ancestors, is registered for deletion. Resources cannot be created within, or restored within, a project or space that is registered for deletion.
        :raises RestoreOntologyResourcePermissionDenied: The resource, or one of the trashed ancestors that would be restored alongside it, backs an ontology entity. Restoring such a resource through the filesystem would leave the ontology in an inconsistent state, so it must be restored through the ontology APIs instead.
        :raises RestoreResourcePermissionDenied: Could not restore the resource due to insufficient permissions.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v3/platform/folders/{folderRid}/restore",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "folderRid": folder_rid,
                },
                header_params={},
                body=None,
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "FoldersNotFound": filesystem_errors.FoldersNotFound,
                    "InvalidDisplayNameOnRestore": filesystem_errors.InvalidDisplayNameOnRestore,
                    "InvalidFolders": filesystem_errors.InvalidFolders,
                    "ResourceNotDirectlyTrashed": filesystem_errors.ResourceNotDirectlyTrashed,
                    "ResourceRegisteredForDeletion": filesystem_errors.ResourceRegisteredForDeletion,
                    "RestoreOntologyResourcePermissionDenied": filesystem_errors.RestoreOntologyResourcePermissionDenied,
                    "RestoreResourcePermissionDenied": filesystem_errors.RestoreResourcePermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _FolderClientRaw:
    def __init__(self, client: FolderClient) -> None:
        def create(_: filesystem_models.Folder): ...
        def delete(_: None): ...
        def delete_batch(_: None): ...
        def get(_: filesystem_models.Folder): ...
        def get_batch(_: filesystem_models.GetFoldersBatchResponse): ...
        def restore(_: None): ...

        self.create = core.with_raw_response(create, client.create)
        self.delete = core.with_raw_response(delete, client.delete)
        self.delete_batch = core.with_raw_response(delete_batch, client.delete_batch)
        self.get = core.with_raw_response(get, client.get)
        self.get_batch = core.with_raw_response(get_batch, client.get_batch)
        self.restore = core.with_raw_response(restore, client.restore)


class _FolderClientStreaming:
    def __init__(self, client: FolderClient) -> None:
        def create(_: filesystem_models.Folder): ...
        def get(_: filesystem_models.Folder): ...
        def get_batch(_: filesystem_models.GetFoldersBatchResponse): ...

        self.create = core.with_streaming_response(create, client.create)
        self.get = core.with_streaming_response(get, client.get)
        self.get_batch = core.with_streaming_response(get_batch, client.get_batch)


class AsyncFolderClient:
    """
    The API client for the Folder Resource.

    :param auth: Your auth configuration.
    :param hostname: The hostname supplier for resolving base URLs.
    :param config: Optionally specify the configuration for the HTTP session.
    """

    def __init__(
        self,
        auth: core.Auth,
        hostname: typing.Union[str, core.HostnameSupplier],
        config: typing.Optional[core.Config] = None,
    ):
        self._auth = auth
        if isinstance(hostname, core.HostnameSupplier):
            self._hostname_supplier = hostname
        else:
            self._hostname_supplier = core.create_hostname_supplier(hostname, config)
        self._hostname = self._hostname_supplier.get_hostname()
        self._config = config
        self._api_client = core.AsyncApiClient(
            auth=auth, hostname=self._hostname_supplier, config=config
        )

        self.with_streaming_response = _AsyncFolderClientStreaming(self)
        self.with_raw_response = _AsyncFolderClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def create(
        self,
        *,
        display_name: filesystem_models.DisplayName,
        parent_folder_rid: core_models.FolderRid,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[filesystem_models.Folder]:
        """
        Create a new folder in the given parent folder.

        Required scopes: [api:v3:folder:write:create]

        :param display_name: The display name of the folder.
        :type display_name: DisplayName
        :param parent_folder_rid: The RID of the existing project or folder in which to create the new folder. The parent must be inside a project.
        :type parent_folder_rid: FolderRid
        :param preview:
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[filesystem_models.Folder]

        :raises CreateFolderOutsideProjectNotSupported: Folders can only be created within a project.
        :raises CreateFolderPermissionDenied: Could not create the folder due to insufficient permissions.
        :raises InvalidDisplayName: A display name must not be empty, must not be exactly `.` or `..`, must not contain a forward slash (`/`), and must not exceed 700 characters.
        :raises InvalidParentFolder: The specified parent resource is not a folder.
        :raises MissingDisplayName: A display name must be provided.
        :raises ParentFolderNotFound: The specified parent folder could not be found.
        :raises ResourceDisplayNameAlreadyExists: The provided resource display name is already in use by another resource in the same folder.
        :raises ResourceRegisteredForDeletion: The resource, or one of its ancestors, is registered for deletion. Resources cannot be created within, or restored within, a project or space that is registered for deletion.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v3/platform/folders",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body=filesystem_models.CreateFolderRequest(
                    display_name=display_name,
                    parent_folder_rid=parent_folder_rid,
                ),
                response_type=filesystem_models.Folder,
                request_timeout=request_timeout,
                throwable_errors={
                    "CreateFolderOutsideProjectNotSupported": filesystem_errors.CreateFolderOutsideProjectNotSupported,
                    "CreateFolderPermissionDenied": filesystem_errors.CreateFolderPermissionDenied,
                    "InvalidDisplayName": filesystem_errors.InvalidDisplayName,
                    "InvalidParentFolder": filesystem_errors.InvalidParentFolder,
                    "MissingDisplayName": filesystem_errors.MissingDisplayName,
                    "ParentFolderNotFound": filesystem_errors.ParentFolderNotFound,
                    "ResourceDisplayNameAlreadyExists": filesystem_errors.ResourceDisplayNameAlreadyExists,
                    "ResourceRegisteredForDeletion": filesystem_errors.ResourceRegisteredForDeletion,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def delete(
        self,
        folder_rid: core_models.FolderRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[None]:
        """
        Move the given folder to the trash. Following this operation, the folder can be restored, using the
        `restore` operation, or permanently deleted using the `permanentlyDelete` operation.

        Required scopes: [api:v3:folder:write:delete]

        :param folder_rid:
        :type folder_rid: FolderRid
        :param preview:
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[None]

        :raises DeleteFolderPermissionDenied: Could not delete the folder due to insufficient permissions.
        :raises DeleteOntologyResourcePermissionDenied: The resource, or one of its descendants, backs an ontology entity. Trashing such a resource through the filesystem would leave the ontology in an inconsistent state, so it must be deleted through the ontology APIs instead.
        :raises FoldersNotFound: The specified folders could not be found.
        :raises InvalidFolders: The given resources are not folders.
        :raises TrashingHiddenResourcesNotSupported: Hidden resources cannot be trashed.
        :raises TrashingHomeFoldersNotSupported: Home folders cannot be trashed. Home folders are created and managed by the platform.
        :raises TrashingRootFolderNotSupported: The root folder cannot be trashed.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="DELETE",
                resource_path="/v3/platform/folders/{folderRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "folderRid": folder_rid,
                },
                header_params={},
                body=None,
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "DeleteFolderPermissionDenied": filesystem_errors.DeleteFolderPermissionDenied,
                    "DeleteOntologyResourcePermissionDenied": filesystem_errors.DeleteOntologyResourcePermissionDenied,
                    "FoldersNotFound": filesystem_errors.FoldersNotFound,
                    "InvalidFolders": filesystem_errors.InvalidFolders,
                    "TrashingHiddenResourcesNotSupported": filesystem_errors.TrashingHiddenResourcesNotSupported,
                    "TrashingHomeFoldersNotSupported": filesystem_errors.TrashingHomeFoldersNotSupported,
                    "TrashingRootFolderNotSupported": filesystem_errors.TrashingRootFolderNotSupported,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def delete_batch(
        self,
        body: typing_extensions.Annotated[
            typing.List[filesystem_models.DeleteFoldersBatchRequestElement],
            annotated_types.Len(min_length=1, max_length=100),
        ],
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[None]:
        """
        Trash multiple folders in a single request.

        Required scopes: [api:v3:folder:write:delete]

        :param body: Body of the request
        :type body: List[DeleteFoldersBatchRequestElement]
        :param preview:
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[None]

        :raises BatchRequestSizeExceededLimit:
        :raises DeleteFolderPermissionDenied: Could not delete the folder due to insufficient permissions.
        :raises DeleteOntologyResourcePermissionDenied: The resource, or one of its descendants, backs an ontology entity. Trashing such a resource through the filesystem would leave the ontology in an inconsistent state, so it must be deleted through the ontology APIs instead.
        :raises FoldersNotFound: The specified folders could not be found.
        :raises InvalidFolders: The given resources are not folders.
        :raises MissingBatchRequest:
        :raises TrashingHiddenResourcesNotSupported: Hidden resources cannot be trashed.
        :raises TrashingHomeFoldersNotSupported: Home folders cannot be trashed. Home folders are created and managed by the platform.
        :raises TrashingRootFolderNotSupported: The root folder cannot be trashed.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v3/platform/folders/deleteBatch",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                },
                body=body,
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "BatchRequestSizeExceededLimit": core_errors.BatchRequestSizeExceededLimit,
                    "DeleteFolderPermissionDenied": filesystem_errors.DeleteFolderPermissionDenied,
                    "DeleteOntologyResourcePermissionDenied": filesystem_errors.DeleteOntologyResourcePermissionDenied,
                    "FoldersNotFound": filesystem_errors.FoldersNotFound,
                    "InvalidFolders": filesystem_errors.InvalidFolders,
                    "MissingBatchRequest": core_errors.MissingBatchRequest,
                    "TrashingHiddenResourcesNotSupported": filesystem_errors.TrashingHiddenResourcesNotSupported,
                    "TrashingHomeFoldersNotSupported": filesystem_errors.TrashingHomeFoldersNotSupported,
                    "TrashingRootFolderNotSupported": filesystem_errors.TrashingRootFolderNotSupported,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        folder_rid: core_models.FolderRid,
        *,
        include: typing.Optional[typing.List[filesystem_models.AdditionalField]] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[filesystem_models.Folder]:
        """
        Get the folder with the specified resource identifier (RID).

        Required scopes: [api:v3:folder:read:get]

        :param folder_rid:
        :type folder_rid: FolderRid
        :param include:
        :type include: Optional[List[AdditionalField]]
        :param preview:
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[filesystem_models.Folder]

        :raises FoldersNotFound: The specified folders could not be found.
        :raises GetResourceTimedOut: The request to retrieve resource information timed out.
        :raises GetRootFolderNotSupported: The root folder cannot be retrieved.
        :raises InvalidFolders: The given resources are not folders.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v3/platform/folders/{folderRid}",
                query_params={
                    "include": include,
                    "preview": preview,
                },
                path_params={
                    "folderRid": folder_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=filesystem_models.Folder,
                request_timeout=request_timeout,
                throwable_errors={
                    "FoldersNotFound": filesystem_errors.FoldersNotFound,
                    "GetResourceTimedOut": filesystem_errors.GetResourceTimedOut,
                    "GetRootFolderNotSupported": filesystem_errors.GetRootFolderNotSupported,
                    "InvalidFolders": filesystem_errors.InvalidFolders,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get_batch(
        self,
        body: typing_extensions.Annotated[
            typing.List[filesystem_models.GetFoldersBatchRequestElement],
            annotated_types.Len(min_length=1, max_length=2000),
        ],
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[filesystem_models.GetFoldersBatchResponse]:
        """
        Fetch multiple folders in a single request.

        Required scopes: [api:v3:folder:read:get]

        :param body: Body of the request
        :type body: List[GetFoldersBatchRequestElement]
        :param preview:
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[filesystem_models.GetFoldersBatchResponse]

        :raises BatchRequestSizeExceededLimit:
        :raises FoldersNotFound: The specified folders could not be found.
        :raises GetResourceTimedOut: The request to retrieve resource information timed out.
        :raises GetRootFolderNotSupported: The root folder cannot be retrieved.
        :raises InvalidFolders: The given resources are not folders.
        :raises MissingBatchRequest:
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v3/platform/folders/getBatch",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body=body,
                response_type=filesystem_models.GetFoldersBatchResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "BatchRequestSizeExceededLimit": core_errors.BatchRequestSizeExceededLimit,
                    "FoldersNotFound": filesystem_errors.FoldersNotFound,
                    "GetResourceTimedOut": filesystem_errors.GetResourceTimedOut,
                    "GetRootFolderNotSupported": filesystem_errors.GetRootFolderNotSupported,
                    "InvalidFolders": filesystem_errors.InvalidFolders,
                    "MissingBatchRequest": core_errors.MissingBatchRequest,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def restore(
        self,
        folder_rid: core_models.FolderRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[None]:
        """
        Restore the given folder and any directly trashed ancestors from the trash. If the folder is not
        directly trashed, this operation will return an error.

        Required scopes: [api:v3:folder:write:restore]

        :param folder_rid:
        :type folder_rid: FolderRid
        :param preview:
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[None]

        :raises FoldersNotFound: The specified folders could not be found.
        :raises InvalidDisplayNameOnRestore: Cannot restore resource because restoring it would produce an invalid display name. While the resource is still in trash, rename it to a valid name that does not contain the reserved text ' (trashed)', then retry the restore.
        :raises InvalidFolders: The given resources are not folders.
        :raises ResourceNotDirectlyTrashed: The resource is not directly trashed.
        :raises ResourceRegisteredForDeletion: The resource, or one of its ancestors, is registered for deletion. Resources cannot be created within, or restored within, a project or space that is registered for deletion.
        :raises RestoreOntologyResourcePermissionDenied: The resource, or one of the trashed ancestors that would be restored alongside it, backs an ontology entity. Restoring such a resource through the filesystem would leave the ontology in an inconsistent state, so it must be restored through the ontology APIs instead.
        :raises RestoreResourcePermissionDenied: Could not restore the resource due to insufficient permissions.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v3/platform/folders/{folderRid}/restore",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "folderRid": folder_rid,
                },
                header_params={},
                body=None,
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "FoldersNotFound": filesystem_errors.FoldersNotFound,
                    "InvalidDisplayNameOnRestore": filesystem_errors.InvalidDisplayNameOnRestore,
                    "InvalidFolders": filesystem_errors.InvalidFolders,
                    "ResourceNotDirectlyTrashed": filesystem_errors.ResourceNotDirectlyTrashed,
                    "ResourceRegisteredForDeletion": filesystem_errors.ResourceRegisteredForDeletion,
                    "RestoreOntologyResourcePermissionDenied": filesystem_errors.RestoreOntologyResourcePermissionDenied,
                    "RestoreResourcePermissionDenied": filesystem_errors.RestoreResourcePermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _AsyncFolderClientRaw:
    def __init__(self, client: AsyncFolderClient) -> None:
        def create(_: filesystem_models.Folder): ...
        def delete(_: None): ...
        def delete_batch(_: None): ...
        def get(_: filesystem_models.Folder): ...
        def get_batch(_: filesystem_models.GetFoldersBatchResponse): ...
        def restore(_: None): ...

        self.create = core.async_with_raw_response(create, client.create)
        self.delete = core.async_with_raw_response(delete, client.delete)
        self.delete_batch = core.async_with_raw_response(delete_batch, client.delete_batch)
        self.get = core.async_with_raw_response(get, client.get)
        self.get_batch = core.async_with_raw_response(get_batch, client.get_batch)
        self.restore = core.async_with_raw_response(restore, client.restore)


class _AsyncFolderClientStreaming:
    def __init__(self, client: AsyncFolderClient) -> None:
        def create(_: filesystem_models.Folder): ...
        def get(_: filesystem_models.Folder): ...
        def get_batch(_: filesystem_models.GetFoldersBatchResponse): ...

        self.create = core.async_with_streaming_response(create, client.create)
        self.get = core.async_with_streaming_response(get, client.get)
        self.get_batch = core.async_with_streaming_response(get_batch, client.get_batch)
