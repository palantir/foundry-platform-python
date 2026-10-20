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


class ResourceClient:
    """
    The API client for the Resource Resource.

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

        self.with_streaming_response = _ResourceClientStreaming(self)
        self.with_raw_response = _ResourceClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def delete(
        self,
        resource_rid: filesystem_models.ResourceRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> None:
        """
        Move the given resource to the trash. Following this operation, the resource can be restored, using the
        `restore` operation, or permanently deleted using the `permanentlyDelete` operation.

        Required scopes: [api:v3:resource:write:delete]

        :param resource_rid:
        :type resource_rid: ResourceRid
        :param preview:
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: None

        :raises DeleteOntologyResourcePermissionDenied: The resource, or one of its descendants, backs an ontology entity. Trashing such a resource through the filesystem would leave the ontology in an inconsistent state, so it must be deleted through the ontology APIs instead.
        :raises DeleteResourcePermissionDenied: Could not delete the resource due to insufficient permissions.
        :raises DeleteServiceSpaceNotSupported: The service's space cannot be deleted.
        :raises DeleteUserSpaceNotSupported: The user's space cannot be deleted.
        :raises ResourceNotFound:
        :raises TrashingAutosavedResourcesNotSupported: Auto-saved resources cannot be trashed.
        :raises TrashingHiddenResourcesNotSupported: Hidden resources cannot be trashed.
        :raises TrashingHomeFoldersNotSupported: Home folders cannot be trashed. Home folders are created and managed by the platform.
        :raises TrashingRootFolderNotSupported: The root folder cannot be trashed.
        :raises TrashingSpacesNotSupported: Space trashing has been disabled.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="DELETE",
                resource_path="/v3/platform/resources/{resourceRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "resourceRid": resource_rid,
                },
                header_params={},
                body=None,
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "DeleteOntologyResourcePermissionDenied": filesystem_errors.DeleteOntologyResourcePermissionDenied,
                    "DeleteResourcePermissionDenied": filesystem_errors.DeleteResourcePermissionDenied,
                    "DeleteServiceSpaceNotSupported": filesystem_errors.DeleteServiceSpaceNotSupported,
                    "DeleteUserSpaceNotSupported": filesystem_errors.DeleteUserSpaceNotSupported,
                    "ResourceNotFound": filesystem_errors.ResourceNotFound,
                    "TrashingAutosavedResourcesNotSupported": filesystem_errors.TrashingAutosavedResourcesNotSupported,
                    "TrashingHiddenResourcesNotSupported": filesystem_errors.TrashingHiddenResourcesNotSupported,
                    "TrashingHomeFoldersNotSupported": filesystem_errors.TrashingHomeFoldersNotSupported,
                    "TrashingRootFolderNotSupported": filesystem_errors.TrashingRootFolderNotSupported,
                    "TrashingSpacesNotSupported": filesystem_errors.TrashingSpacesNotSupported,
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
            typing.List[filesystem_models.DeleteResourcesBatchRequestElement],
            annotated_types.Len(min_length=1, max_length=100),
        ],
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> None:
        """
        Trash multiple resources in a single request.

        Required scopes: [api:v3:resource:write:delete]

        :param body: Body of the request
        :type body: List[DeleteResourcesBatchRequestElement]
        :param preview:
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: None

        :raises BatchRequestSizeExceededLimit: Thrown when a batch request exceeds the endpoint's maximum batch size.
        :raises DeleteOntologyResourcePermissionDenied: The resource, or one of its descendants, backs an ontology entity. Trashing such a resource through the filesystem would leave the ontology in an inconsistent state, so it must be deleted through the ontology APIs instead.
        :raises DeleteResourcePermissionDenied: Could not delete the resource due to insufficient permissions.
        :raises DeleteServiceSpaceNotSupported: The service's space cannot be deleted.
        :raises DeleteUserSpaceNotSupported: The user's space cannot be deleted.
        :raises MissingBatchRequest: Thrown when a batch request contains no elements.
        :raises ResourceNotFound:
        :raises TrashingAutosavedResourcesNotSupported: Auto-saved resources cannot be trashed.
        :raises TrashingHiddenResourcesNotSupported: Hidden resources cannot be trashed.
        :raises TrashingHomeFoldersNotSupported: Home folders cannot be trashed. Home folders are created and managed by the platform.
        :raises TrashingRootFolderNotSupported: The root folder cannot be trashed.
        :raises TrashingSpacesNotSupported: Space trashing has been disabled.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v3/platform/resources/deleteBatch",
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
                    "DeleteOntologyResourcePermissionDenied": filesystem_errors.DeleteOntologyResourcePermissionDenied,
                    "DeleteResourcePermissionDenied": filesystem_errors.DeleteResourcePermissionDenied,
                    "DeleteServiceSpaceNotSupported": filesystem_errors.DeleteServiceSpaceNotSupported,
                    "DeleteUserSpaceNotSupported": filesystem_errors.DeleteUserSpaceNotSupported,
                    "MissingBatchRequest": core_errors.MissingBatchRequest,
                    "ResourceNotFound": filesystem_errors.ResourceNotFound,
                    "TrashingAutosavedResourcesNotSupported": filesystem_errors.TrashingAutosavedResourcesNotSupported,
                    "TrashingHiddenResourcesNotSupported": filesystem_errors.TrashingHiddenResourcesNotSupported,
                    "TrashingHomeFoldersNotSupported": filesystem_errors.TrashingHomeFoldersNotSupported,
                    "TrashingRootFolderNotSupported": filesystem_errors.TrashingRootFolderNotSupported,
                    "TrashingSpacesNotSupported": filesystem_errors.TrashingSpacesNotSupported,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        resource_rid: filesystem_models.ResourceRid,
        *,
        include: typing.Optional[typing.List[filesystem_models.AdditionalField]] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> filesystem_models.Resource:
        """
        Get the resource with the specified resource identifier (RID).

        Required scopes: [api:v3:resource:read:get]

        :param resource_rid:
        :type resource_rid: ResourceRid
        :param include:
        :type include: Optional[List[AdditionalField]]
        :param preview:
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: filesystem_models.Resource

        :raises GetResourceTimedOut: The request to retrieve resource information timed out.
        :raises GetRootFolderNotSupported: The root folder cannot be retrieved.
        :raises ResourceNotFound:
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v3/platform/resources/{resourceRid}",
                query_params={
                    "include": include,
                    "preview": preview,
                },
                path_params={
                    "resourceRid": resource_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=filesystem_models.Resource,
                request_timeout=request_timeout,
                throwable_errors={
                    "GetResourceTimedOut": filesystem_errors.GetResourceTimedOut,
                    "GetRootFolderNotSupported": filesystem_errors.GetRootFolderNotSupported,
                    "ResourceNotFound": filesystem_errors.ResourceNotFound,
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
            typing.List[filesystem_models.GetResourcesBatchRequestElement],
            annotated_types.Len(min_length=1, max_length=2000),
        ],
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> filesystem_models.GetResourcesBatchResponse:
        """
        Fetch multiple resources in a single request.

        Required scopes: [api:v3:resource:read:get]

        :param body: Body of the request
        :type body: List[GetResourcesBatchRequestElement]
        :param preview:
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: filesystem_models.GetResourcesBatchResponse

        :raises BatchRequestSizeExceededLimit: Thrown when a batch request exceeds the endpoint's maximum batch size.
        :raises GetResourceTimedOut: The request to retrieve resource information timed out.
        :raises GetRootFolderNotSupported: The root folder cannot be retrieved.
        :raises MissingBatchRequest: Thrown when a batch request contains no elements.
        :raises ResourceNotFound:
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v3/platform/resources/getBatch",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body=body,
                response_type=filesystem_models.GetResourcesBatchResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "BatchRequestSizeExceededLimit": core_errors.BatchRequestSizeExceededLimit,
                    "GetResourceTimedOut": filesystem_errors.GetResourceTimedOut,
                    "GetRootFolderNotSupported": filesystem_errors.GetRootFolderNotSupported,
                    "MissingBatchRequest": core_errors.MissingBatchRequest,
                    "ResourceNotFound": filesystem_errors.ResourceNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get_by_path(
        self,
        *,
        path: filesystem_models.ResourcePath,
        include: typing.Optional[typing.List[filesystem_models.AdditionalField]] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> filesystem_models.Resource:
        """
        Get a resource by its absolute path. The leading slash is optional.

        Required scopes: [api:v3:resource:read:get-by-path]

        :param path:
        :type path: ResourcePath
        :param include:
        :type include: Optional[List[AdditionalField]]
        :param preview:
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: filesystem_models.Resource

        :raises GetResourceTimedOut: The request to retrieve resource information timed out.
        :raises GetRootFolderNotSupported: The root folder cannot be retrieved.
        :raises InvalidPath: The given path is invalid.  A valid path has all components separated by a single `/`.
        :raises PathNotFound: The given path could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v3/platform/resources/getByPath",
                query_params={
                    "path": path,
                    "include": include,
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=filesystem_models.Resource,
                request_timeout=request_timeout,
                throwable_errors={
                    "GetResourceTimedOut": filesystem_errors.GetResourceTimedOut,
                    "GetRootFolderNotSupported": filesystem_errors.GetRootFolderNotSupported,
                    "InvalidPath": filesystem_errors.InvalidPath,
                    "PathNotFound": filesystem_errors.PathNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def restore(
        self,
        resource_rid: filesystem_models.ResourceRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> None:
        """
        Restore the given resource and any directly trashed ancestors from the trash. If the resource is not
        directly trashed, this operation will return an error.

        Required scopes: [api:v3:resource:write:restore]

        :param resource_rid:
        :type resource_rid: ResourceRid
        :param preview:
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: None

        :raises InvalidDisplayNameOnRestore: Cannot restore resource because restoring it would produce an invalid display name. While the resource is still in trash, rename it to a valid name that does not contain the reserved text ' (trashed)', then retry the restore.
        :raises ResourceNotDirectlyTrashed: The resource is not directly trashed.
        :raises ResourceNotFound:
        :raises ResourceRegisteredForDeletion: The resource, or one of its ancestors, is registered for deletion. Resources cannot be created within, or restored within, a project or space that is registered for deletion.
        :raises RestoreOntologyResourcePermissionDenied: The resource, or one of the trashed ancestors that would be restored alongside it, backs an ontology entity. Restoring such a resource through the filesystem would leave the ontology in an inconsistent state, so it must be restored through the ontology APIs instead.
        :raises RestoreResourcePermissionDenied: Could not restore the resource due to insufficient permissions.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v3/platform/resources/{resourceRid}/restore",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "resourceRid": resource_rid,
                },
                header_params={},
                body=None,
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "InvalidDisplayNameOnRestore": filesystem_errors.InvalidDisplayNameOnRestore,
                    "ResourceNotDirectlyTrashed": filesystem_errors.ResourceNotDirectlyTrashed,
                    "ResourceNotFound": filesystem_errors.ResourceNotFound,
                    "ResourceRegisteredForDeletion": filesystem_errors.ResourceRegisteredForDeletion,
                    "RestoreOntologyResourcePermissionDenied": filesystem_errors.RestoreOntologyResourcePermissionDenied,
                    "RestoreResourcePermissionDenied": filesystem_errors.RestoreResourcePermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _ResourceClientRaw:
    def __init__(self, client: ResourceClient) -> None:
        def delete(_: None): ...
        def delete_batch(_: None): ...
        def get(_: filesystem_models.Resource): ...
        def get_batch(_: filesystem_models.GetResourcesBatchResponse): ...
        def get_by_path(_: filesystem_models.Resource): ...
        def restore(_: None): ...

        self.delete = core.with_raw_response(delete, client.delete)
        self.delete_batch = core.with_raw_response(delete_batch, client.delete_batch)
        self.get = core.with_raw_response(get, client.get)
        self.get_batch = core.with_raw_response(get_batch, client.get_batch)
        self.get_by_path = core.with_raw_response(get_by_path, client.get_by_path)
        self.restore = core.with_raw_response(restore, client.restore)


class _ResourceClientStreaming:
    def __init__(self, client: ResourceClient) -> None:
        def get(_: filesystem_models.Resource): ...
        def get_batch(_: filesystem_models.GetResourcesBatchResponse): ...
        def get_by_path(_: filesystem_models.Resource): ...

        self.get = core.with_streaming_response(get, client.get)
        self.get_batch = core.with_streaming_response(get_batch, client.get_batch)
        self.get_by_path = core.with_streaming_response(get_by_path, client.get_by_path)


class AsyncResourceClient:
    """
    The API client for the Resource Resource.

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

        self.with_streaming_response = _AsyncResourceClientStreaming(self)
        self.with_raw_response = _AsyncResourceClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def delete(
        self,
        resource_rid: filesystem_models.ResourceRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[None]:
        """
        Move the given resource to the trash. Following this operation, the resource can be restored, using the
        `restore` operation, or permanently deleted using the `permanentlyDelete` operation.

        Required scopes: [api:v3:resource:write:delete]

        :param resource_rid:
        :type resource_rid: ResourceRid
        :param preview:
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[None]

        :raises DeleteOntologyResourcePermissionDenied: The resource, or one of its descendants, backs an ontology entity. Trashing such a resource through the filesystem would leave the ontology in an inconsistent state, so it must be deleted through the ontology APIs instead.
        :raises DeleteResourcePermissionDenied: Could not delete the resource due to insufficient permissions.
        :raises DeleteServiceSpaceNotSupported: The service's space cannot be deleted.
        :raises DeleteUserSpaceNotSupported: The user's space cannot be deleted.
        :raises ResourceNotFound:
        :raises TrashingAutosavedResourcesNotSupported: Auto-saved resources cannot be trashed.
        :raises TrashingHiddenResourcesNotSupported: Hidden resources cannot be trashed.
        :raises TrashingHomeFoldersNotSupported: Home folders cannot be trashed. Home folders are created and managed by the platform.
        :raises TrashingRootFolderNotSupported: The root folder cannot be trashed.
        :raises TrashingSpacesNotSupported: Space trashing has been disabled.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="DELETE",
                resource_path="/v3/platform/resources/{resourceRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "resourceRid": resource_rid,
                },
                header_params={},
                body=None,
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "DeleteOntologyResourcePermissionDenied": filesystem_errors.DeleteOntologyResourcePermissionDenied,
                    "DeleteResourcePermissionDenied": filesystem_errors.DeleteResourcePermissionDenied,
                    "DeleteServiceSpaceNotSupported": filesystem_errors.DeleteServiceSpaceNotSupported,
                    "DeleteUserSpaceNotSupported": filesystem_errors.DeleteUserSpaceNotSupported,
                    "ResourceNotFound": filesystem_errors.ResourceNotFound,
                    "TrashingAutosavedResourcesNotSupported": filesystem_errors.TrashingAutosavedResourcesNotSupported,
                    "TrashingHiddenResourcesNotSupported": filesystem_errors.TrashingHiddenResourcesNotSupported,
                    "TrashingHomeFoldersNotSupported": filesystem_errors.TrashingHomeFoldersNotSupported,
                    "TrashingRootFolderNotSupported": filesystem_errors.TrashingRootFolderNotSupported,
                    "TrashingSpacesNotSupported": filesystem_errors.TrashingSpacesNotSupported,
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
            typing.List[filesystem_models.DeleteResourcesBatchRequestElement],
            annotated_types.Len(min_length=1, max_length=100),
        ],
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[None]:
        """
        Trash multiple resources in a single request.

        Required scopes: [api:v3:resource:write:delete]

        :param body: Body of the request
        :type body: List[DeleteResourcesBatchRequestElement]
        :param preview:
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[None]

        :raises BatchRequestSizeExceededLimit: Thrown when a batch request exceeds the endpoint's maximum batch size.
        :raises DeleteOntologyResourcePermissionDenied: The resource, or one of its descendants, backs an ontology entity. Trashing such a resource through the filesystem would leave the ontology in an inconsistent state, so it must be deleted through the ontology APIs instead.
        :raises DeleteResourcePermissionDenied: Could not delete the resource due to insufficient permissions.
        :raises DeleteServiceSpaceNotSupported: The service's space cannot be deleted.
        :raises DeleteUserSpaceNotSupported: The user's space cannot be deleted.
        :raises MissingBatchRequest: Thrown when a batch request contains no elements.
        :raises ResourceNotFound:
        :raises TrashingAutosavedResourcesNotSupported: Auto-saved resources cannot be trashed.
        :raises TrashingHiddenResourcesNotSupported: Hidden resources cannot be trashed.
        :raises TrashingHomeFoldersNotSupported: Home folders cannot be trashed. Home folders are created and managed by the platform.
        :raises TrashingRootFolderNotSupported: The root folder cannot be trashed.
        :raises TrashingSpacesNotSupported: Space trashing has been disabled.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v3/platform/resources/deleteBatch",
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
                    "DeleteOntologyResourcePermissionDenied": filesystem_errors.DeleteOntologyResourcePermissionDenied,
                    "DeleteResourcePermissionDenied": filesystem_errors.DeleteResourcePermissionDenied,
                    "DeleteServiceSpaceNotSupported": filesystem_errors.DeleteServiceSpaceNotSupported,
                    "DeleteUserSpaceNotSupported": filesystem_errors.DeleteUserSpaceNotSupported,
                    "MissingBatchRequest": core_errors.MissingBatchRequest,
                    "ResourceNotFound": filesystem_errors.ResourceNotFound,
                    "TrashingAutosavedResourcesNotSupported": filesystem_errors.TrashingAutosavedResourcesNotSupported,
                    "TrashingHiddenResourcesNotSupported": filesystem_errors.TrashingHiddenResourcesNotSupported,
                    "TrashingHomeFoldersNotSupported": filesystem_errors.TrashingHomeFoldersNotSupported,
                    "TrashingRootFolderNotSupported": filesystem_errors.TrashingRootFolderNotSupported,
                    "TrashingSpacesNotSupported": filesystem_errors.TrashingSpacesNotSupported,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        resource_rid: filesystem_models.ResourceRid,
        *,
        include: typing.Optional[typing.List[filesystem_models.AdditionalField]] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[filesystem_models.Resource]:
        """
        Get the resource with the specified resource identifier (RID).

        Required scopes: [api:v3:resource:read:get]

        :param resource_rid:
        :type resource_rid: ResourceRid
        :param include:
        :type include: Optional[List[AdditionalField]]
        :param preview:
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[filesystem_models.Resource]

        :raises GetResourceTimedOut: The request to retrieve resource information timed out.
        :raises GetRootFolderNotSupported: The root folder cannot be retrieved.
        :raises ResourceNotFound:
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v3/platform/resources/{resourceRid}",
                query_params={
                    "include": include,
                    "preview": preview,
                },
                path_params={
                    "resourceRid": resource_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=filesystem_models.Resource,
                request_timeout=request_timeout,
                throwable_errors={
                    "GetResourceTimedOut": filesystem_errors.GetResourceTimedOut,
                    "GetRootFolderNotSupported": filesystem_errors.GetRootFolderNotSupported,
                    "ResourceNotFound": filesystem_errors.ResourceNotFound,
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
            typing.List[filesystem_models.GetResourcesBatchRequestElement],
            annotated_types.Len(min_length=1, max_length=2000),
        ],
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[filesystem_models.GetResourcesBatchResponse]:
        """
        Fetch multiple resources in a single request.

        Required scopes: [api:v3:resource:read:get]

        :param body: Body of the request
        :type body: List[GetResourcesBatchRequestElement]
        :param preview:
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[filesystem_models.GetResourcesBatchResponse]

        :raises BatchRequestSizeExceededLimit: Thrown when a batch request exceeds the endpoint's maximum batch size.
        :raises GetResourceTimedOut: The request to retrieve resource information timed out.
        :raises GetRootFolderNotSupported: The root folder cannot be retrieved.
        :raises MissingBatchRequest: Thrown when a batch request contains no elements.
        :raises ResourceNotFound:
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v3/platform/resources/getBatch",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body=body,
                response_type=filesystem_models.GetResourcesBatchResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "BatchRequestSizeExceededLimit": core_errors.BatchRequestSizeExceededLimit,
                    "GetResourceTimedOut": filesystem_errors.GetResourceTimedOut,
                    "GetRootFolderNotSupported": filesystem_errors.GetRootFolderNotSupported,
                    "MissingBatchRequest": core_errors.MissingBatchRequest,
                    "ResourceNotFound": filesystem_errors.ResourceNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get_by_path(
        self,
        *,
        path: filesystem_models.ResourcePath,
        include: typing.Optional[typing.List[filesystem_models.AdditionalField]] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[filesystem_models.Resource]:
        """
        Get a resource by its absolute path. The leading slash is optional.

        Required scopes: [api:v3:resource:read:get-by-path]

        :param path:
        :type path: ResourcePath
        :param include:
        :type include: Optional[List[AdditionalField]]
        :param preview:
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[filesystem_models.Resource]

        :raises GetResourceTimedOut: The request to retrieve resource information timed out.
        :raises GetRootFolderNotSupported: The root folder cannot be retrieved.
        :raises InvalidPath: The given path is invalid.  A valid path has all components separated by a single `/`.
        :raises PathNotFound: The given path could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v3/platform/resources/getByPath",
                query_params={
                    "path": path,
                    "include": include,
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=filesystem_models.Resource,
                request_timeout=request_timeout,
                throwable_errors={
                    "GetResourceTimedOut": filesystem_errors.GetResourceTimedOut,
                    "GetRootFolderNotSupported": filesystem_errors.GetRootFolderNotSupported,
                    "InvalidPath": filesystem_errors.InvalidPath,
                    "PathNotFound": filesystem_errors.PathNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def restore(
        self,
        resource_rid: filesystem_models.ResourceRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[None]:
        """
        Restore the given resource and any directly trashed ancestors from the trash. If the resource is not
        directly trashed, this operation will return an error.

        Required scopes: [api:v3:resource:write:restore]

        :param resource_rid:
        :type resource_rid: ResourceRid
        :param preview:
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[None]

        :raises InvalidDisplayNameOnRestore: Cannot restore resource because restoring it would produce an invalid display name. While the resource is still in trash, rename it to a valid name that does not contain the reserved text ' (trashed)', then retry the restore.
        :raises ResourceNotDirectlyTrashed: The resource is not directly trashed.
        :raises ResourceNotFound:
        :raises ResourceRegisteredForDeletion: The resource, or one of its ancestors, is registered for deletion. Resources cannot be created within, or restored within, a project or space that is registered for deletion.
        :raises RestoreOntologyResourcePermissionDenied: The resource, or one of the trashed ancestors that would be restored alongside it, backs an ontology entity. Restoring such a resource through the filesystem would leave the ontology in an inconsistent state, so it must be restored through the ontology APIs instead.
        :raises RestoreResourcePermissionDenied: Could not restore the resource due to insufficient permissions.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v3/platform/resources/{resourceRid}/restore",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "resourceRid": resource_rid,
                },
                header_params={},
                body=None,
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "InvalidDisplayNameOnRestore": filesystem_errors.InvalidDisplayNameOnRestore,
                    "ResourceNotDirectlyTrashed": filesystem_errors.ResourceNotDirectlyTrashed,
                    "ResourceNotFound": filesystem_errors.ResourceNotFound,
                    "ResourceRegisteredForDeletion": filesystem_errors.ResourceRegisteredForDeletion,
                    "RestoreOntologyResourcePermissionDenied": filesystem_errors.RestoreOntologyResourcePermissionDenied,
                    "RestoreResourcePermissionDenied": filesystem_errors.RestoreResourcePermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _AsyncResourceClientRaw:
    def __init__(self, client: AsyncResourceClient) -> None:
        def delete(_: None): ...
        def delete_batch(_: None): ...
        def get(_: filesystem_models.Resource): ...
        def get_batch(_: filesystem_models.GetResourcesBatchResponse): ...
        def get_by_path(_: filesystem_models.Resource): ...
        def restore(_: None): ...

        self.delete = core.async_with_raw_response(delete, client.delete)
        self.delete_batch = core.async_with_raw_response(delete_batch, client.delete_batch)
        self.get = core.async_with_raw_response(get, client.get)
        self.get_batch = core.async_with_raw_response(get_batch, client.get_batch)
        self.get_by_path = core.async_with_raw_response(get_by_path, client.get_by_path)
        self.restore = core.async_with_raw_response(restore, client.restore)


class _AsyncResourceClientStreaming:
    def __init__(self, client: AsyncResourceClient) -> None:
        def get(_: filesystem_models.Resource): ...
        def get_batch(_: filesystem_models.GetResourcesBatchResponse): ...
        def get_by_path(_: filesystem_models.Resource): ...

        self.get = core.async_with_streaming_response(get, client.get)
        self.get_batch = core.async_with_streaming_response(get_batch, client.get_batch)
        self.get_by_path = core.async_with_streaming_response(get_by_path, client.get_by_path)
