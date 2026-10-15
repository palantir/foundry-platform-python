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


class SpaceClient:
    """
    The API client for the Space Resource.

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
        self._config = config
        self._api_client = core.ApiClient(
            auth=auth, hostname=self._hostname_supplier, config=config
        )

        self.with_streaming_response = _SpaceClientStreaming(self)
        self.with_raw_response = _SpaceClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def delete(
        self,
        space_rid: filesystem_models.SpaceRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> None:
        """
        Move the given space to the trash. Following this operation, the space can be restored, using the
        `restore` operation, or permanently deleted using the `permanentlyDelete` operation.

        Required scopes: [api:v3:space:write:delete]

        :param space_rid:
        :type space_rid: SpaceRid
        :param preview:
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: None

        :raises DeleteOntologyResourcePermissionDenied: The resource, or one of its descendants, backs an ontology entity. Trashing such a resource through the filesystem would leave the ontology in an inconsistent state, so it must be deleted through the ontology APIs instead.
        :raises DeleteServiceSpaceNotSupported: The service's space cannot be deleted.
        :raises DeleteSpacePermissionDenied: Could not delete the space due to insufficient permissions.
        :raises DeleteUserSpaceNotSupported: The user's space cannot be deleted.
        :raises InvalidSpaces: The given resources are not spaces.
        :raises SpacesNotFound: The specified spaces could not be found.
        :raises TrashingSpacesNotSupported: Space trashing has been disabled.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="DELETE",
                resource_path="/v3/platform/spaces/{spaceRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "spaceRid": space_rid,
                },
                header_params={},
                body=None,
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "DeleteOntologyResourcePermissionDenied": filesystem_errors.DeleteOntologyResourcePermissionDenied,
                    "DeleteServiceSpaceNotSupported": filesystem_errors.DeleteServiceSpaceNotSupported,
                    "DeleteSpacePermissionDenied": filesystem_errors.DeleteSpacePermissionDenied,
                    "DeleteUserSpaceNotSupported": filesystem_errors.DeleteUserSpaceNotSupported,
                    "InvalidSpaces": filesystem_errors.InvalidSpaces,
                    "SpacesNotFound": filesystem_errors.SpacesNotFound,
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
            typing.List[filesystem_models.DeleteSpacesBatchRequestElement],
            annotated_types.Len(min_length=1, max_length=100),
        ],
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> None:
        """
        Trash multiple spaces in a single request.

        Required scopes: [api:v3:space:write:delete]

        :param body: Body of the request
        :type body: List[DeleteSpacesBatchRequestElement]
        :param preview:
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: None

        :raises BatchRequestSizeExceededLimit:
        :raises DeleteOntologyResourcePermissionDenied: The resource, or one of its descendants, backs an ontology entity. Trashing such a resource through the filesystem would leave the ontology in an inconsistent state, so it must be deleted through the ontology APIs instead.
        :raises DeleteServiceSpaceNotSupported: The service's space cannot be deleted.
        :raises DeleteSpacePermissionDenied: Could not delete the space due to insufficient permissions.
        :raises DeleteUserSpaceNotSupported: The user's space cannot be deleted.
        :raises InvalidSpaces: The given resources are not spaces.
        :raises MissingBatchRequest:
        :raises SpacesNotFound: The specified spaces could not be found.
        :raises TrashingSpacesNotSupported: Space trashing has been disabled.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v3/platform/spaces/deleteBatch",
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
                    "DeleteServiceSpaceNotSupported": filesystem_errors.DeleteServiceSpaceNotSupported,
                    "DeleteSpacePermissionDenied": filesystem_errors.DeleteSpacePermissionDenied,
                    "DeleteUserSpaceNotSupported": filesystem_errors.DeleteUserSpaceNotSupported,
                    "InvalidSpaces": filesystem_errors.InvalidSpaces,
                    "MissingBatchRequest": core_errors.MissingBatchRequest,
                    "SpacesNotFound": filesystem_errors.SpacesNotFound,
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
        space_rid: filesystem_models.SpaceRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> filesystem_models.Space:
        """
        Get the space with the specified resource identifier (RID).

        Required scopes: [api:v3:space:read:get]

        :param space_rid:
        :type space_rid: SpaceRid
        :param preview:
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: filesystem_models.Space

        :raises GetResourceTimedOut: The request to retrieve resource information timed out.
        :raises InvalidSpaces: The given resources are not spaces.
        :raises SpacesNotFound: The specified spaces could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v3/platform/spaces/{spaceRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "spaceRid": space_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=filesystem_models.Space,
                request_timeout=request_timeout,
                throwable_errors={
                    "GetResourceTimedOut": filesystem_errors.GetResourceTimedOut,
                    "InvalidSpaces": filesystem_errors.InvalidSpaces,
                    "SpacesNotFound": filesystem_errors.SpacesNotFound,
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
            typing.List[filesystem_models.GetSpacesBatchRequestElement],
            annotated_types.Len(min_length=1, max_length=200),
        ],
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> filesystem_models.GetSpacesBatchResponse:
        """
        Fetch multiple spaces in a single request.

        Required scopes: [api:v3:space:read:get]

        :param body: Body of the request
        :type body: List[GetSpacesBatchRequestElement]
        :param preview:
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: filesystem_models.GetSpacesBatchResponse

        :raises BatchRequestSizeExceededLimit:
        :raises GetResourceTimedOut: The request to retrieve resource information timed out.
        :raises InvalidSpaces: The given resources are not spaces.
        :raises MissingBatchRequest:
        :raises SpacesNotFound: The specified spaces could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v3/platform/spaces/getBatch",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body=body,
                response_type=filesystem_models.GetSpacesBatchResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "BatchRequestSizeExceededLimit": core_errors.BatchRequestSizeExceededLimit,
                    "GetResourceTimedOut": filesystem_errors.GetResourceTimedOut,
                    "InvalidSpaces": filesystem_errors.InvalidSpaces,
                    "MissingBatchRequest": core_errors.MissingBatchRequest,
                    "SpacesNotFound": filesystem_errors.SpacesNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def list(
        self,
        *,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> core.ResourceIterator[filesystem_models.Space]:
        """
        Lists all spaces.

        This is a paginated endpoint. Each page may be smaller or larger than the requested page size.
        It is guaranteed that if there are more results available, the `nextPageToken` field will be populated.
        To get the next page, make the same request again, but set the value of the `pageToken` query parameter
        to be value of the `nextPageToken` value of the previous response.
        If there is no `nextPageToken` field in the response, you are on the last page.

        The default page size is 200. The maximum page size is 200. Requests for a larger page size will be
        clamped to 200. If pageSize is 0, the default page size is used.

        Required scopes: [api:v3:space:read:list]

        :param page_size:
        :type page_size: Optional[PageSize]
        :param page_token:
        :type page_token: Optional[PageToken]
        :param preview:
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ResourceIterator[filesystem_models.Space]

        :raises InvalidPageSize: The provided page size was negative. Page sizes must be greater than or equal to zero.
        :raises ListSpacesTimedOut: The request to list spaces timed out.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v3/platform/spaces",
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
                response_type=filesystem_models.ListSpacesResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "InvalidPageSize": core_errors.InvalidPageSize,
                    "ListSpacesTimedOut": filesystem_errors.ListSpacesTimedOut,
                },
                response_mode=_sdk_internal.get("response_mode", "ITERATOR"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def restore(
        self,
        space_rid: filesystem_models.SpaceRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> None:
        """
        Restore the given space and any directly trashed ancestors from the trash. If the space is not
        directly trashed, this operation will return an error.

        Required scopes: [api:v3:space:write:restore]

        :param space_rid:
        :type space_rid: SpaceRid
        :param preview:
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: None

        :raises InvalidDisplayNameOnRestore: Cannot restore resource because restoring it would produce an invalid display name. While the resource is still in trash, rename it to a valid name that does not contain the reserved text ' (trashed)', then retry the restore.
        :raises InvalidSpaces: The given resources are not spaces.
        :raises ResourceNotDirectlyTrashed: The resource is not directly trashed.
        :raises ResourceRegisteredForDeletion: The resource, or one of its ancestors, is registered for deletion. Resources cannot be created within, or restored within, a project or space that is registered for deletion.
        :raises RestoreOntologyResourcePermissionDenied: The resource, or one of the trashed ancestors that would be restored alongside it, backs an ontology entity. Restoring such a resource through the filesystem would leave the ontology in an inconsistent state, so it must be restored through the ontology APIs instead.
        :raises RestoreResourcePermissionDenied: Could not restore the resource due to insufficient permissions.
        :raises SpacesNotFound: The specified spaces could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v3/platform/spaces/{spaceRid}/restore",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "spaceRid": space_rid,
                },
                header_params={},
                body=None,
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "InvalidDisplayNameOnRestore": filesystem_errors.InvalidDisplayNameOnRestore,
                    "InvalidSpaces": filesystem_errors.InvalidSpaces,
                    "ResourceNotDirectlyTrashed": filesystem_errors.ResourceNotDirectlyTrashed,
                    "ResourceRegisteredForDeletion": filesystem_errors.ResourceRegisteredForDeletion,
                    "RestoreOntologyResourcePermissionDenied": filesystem_errors.RestoreOntologyResourcePermissionDenied,
                    "RestoreResourcePermissionDenied": filesystem_errors.RestoreResourcePermissionDenied,
                    "SpacesNotFound": filesystem_errors.SpacesNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _SpaceClientRaw:
    def __init__(self, client: SpaceClient) -> None:
        def delete(_: None): ...
        def delete_batch(_: None): ...
        def get(_: filesystem_models.Space): ...
        def get_batch(_: filesystem_models.GetSpacesBatchResponse): ...
        def list(_: filesystem_models.ListSpacesResponse): ...
        def restore(_: None): ...

        self.delete = core.with_raw_response(delete, client.delete)
        self.delete_batch = core.with_raw_response(delete_batch, client.delete_batch)
        self.get = core.with_raw_response(get, client.get)
        self.get_batch = core.with_raw_response(get_batch, client.get_batch)
        self.list = core.with_raw_response(list, client.list)
        self.restore = core.with_raw_response(restore, client.restore)


class _SpaceClientStreaming:
    def __init__(self, client: SpaceClient) -> None:
        def get(_: filesystem_models.Space): ...
        def get_batch(_: filesystem_models.GetSpacesBatchResponse): ...
        def list(_: filesystem_models.ListSpacesResponse): ...

        self.get = core.with_streaming_response(get, client.get)
        self.get_batch = core.with_streaming_response(get_batch, client.get_batch)
        self.list = core.with_streaming_response(list, client.list)


class AsyncSpaceClient:
    """
    The API client for the Space Resource.

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
        self._config = config
        self._api_client = core.AsyncApiClient(
            auth=auth, hostname=self._hostname_supplier, config=config
        )

        self.with_streaming_response = _AsyncSpaceClientStreaming(self)
        self.with_raw_response = _AsyncSpaceClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def delete(
        self,
        space_rid: filesystem_models.SpaceRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[None]:
        """
        Move the given space to the trash. Following this operation, the space can be restored, using the
        `restore` operation, or permanently deleted using the `permanentlyDelete` operation.

        Required scopes: [api:v3:space:write:delete]

        :param space_rid:
        :type space_rid: SpaceRid
        :param preview:
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[None]

        :raises DeleteOntologyResourcePermissionDenied: The resource, or one of its descendants, backs an ontology entity. Trashing such a resource through the filesystem would leave the ontology in an inconsistent state, so it must be deleted through the ontology APIs instead.
        :raises DeleteServiceSpaceNotSupported: The service's space cannot be deleted.
        :raises DeleteSpacePermissionDenied: Could not delete the space due to insufficient permissions.
        :raises DeleteUserSpaceNotSupported: The user's space cannot be deleted.
        :raises InvalidSpaces: The given resources are not spaces.
        :raises SpacesNotFound: The specified spaces could not be found.
        :raises TrashingSpacesNotSupported: Space trashing has been disabled.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="DELETE",
                resource_path="/v3/platform/spaces/{spaceRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "spaceRid": space_rid,
                },
                header_params={},
                body=None,
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "DeleteOntologyResourcePermissionDenied": filesystem_errors.DeleteOntologyResourcePermissionDenied,
                    "DeleteServiceSpaceNotSupported": filesystem_errors.DeleteServiceSpaceNotSupported,
                    "DeleteSpacePermissionDenied": filesystem_errors.DeleteSpacePermissionDenied,
                    "DeleteUserSpaceNotSupported": filesystem_errors.DeleteUserSpaceNotSupported,
                    "InvalidSpaces": filesystem_errors.InvalidSpaces,
                    "SpacesNotFound": filesystem_errors.SpacesNotFound,
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
            typing.List[filesystem_models.DeleteSpacesBatchRequestElement],
            annotated_types.Len(min_length=1, max_length=100),
        ],
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[None]:
        """
        Trash multiple spaces in a single request.

        Required scopes: [api:v3:space:write:delete]

        :param body: Body of the request
        :type body: List[DeleteSpacesBatchRequestElement]
        :param preview:
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[None]

        :raises BatchRequestSizeExceededLimit:
        :raises DeleteOntologyResourcePermissionDenied: The resource, or one of its descendants, backs an ontology entity. Trashing such a resource through the filesystem would leave the ontology in an inconsistent state, so it must be deleted through the ontology APIs instead.
        :raises DeleteServiceSpaceNotSupported: The service's space cannot be deleted.
        :raises DeleteSpacePermissionDenied: Could not delete the space due to insufficient permissions.
        :raises DeleteUserSpaceNotSupported: The user's space cannot be deleted.
        :raises InvalidSpaces: The given resources are not spaces.
        :raises MissingBatchRequest:
        :raises SpacesNotFound: The specified spaces could not be found.
        :raises TrashingSpacesNotSupported: Space trashing has been disabled.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v3/platform/spaces/deleteBatch",
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
                    "DeleteServiceSpaceNotSupported": filesystem_errors.DeleteServiceSpaceNotSupported,
                    "DeleteSpacePermissionDenied": filesystem_errors.DeleteSpacePermissionDenied,
                    "DeleteUserSpaceNotSupported": filesystem_errors.DeleteUserSpaceNotSupported,
                    "InvalidSpaces": filesystem_errors.InvalidSpaces,
                    "MissingBatchRequest": core_errors.MissingBatchRequest,
                    "SpacesNotFound": filesystem_errors.SpacesNotFound,
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
        space_rid: filesystem_models.SpaceRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[filesystem_models.Space]:
        """
        Get the space with the specified resource identifier (RID).

        Required scopes: [api:v3:space:read:get]

        :param space_rid:
        :type space_rid: SpaceRid
        :param preview:
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[filesystem_models.Space]

        :raises GetResourceTimedOut: The request to retrieve resource information timed out.
        :raises InvalidSpaces: The given resources are not spaces.
        :raises SpacesNotFound: The specified spaces could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v3/platform/spaces/{spaceRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "spaceRid": space_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=filesystem_models.Space,
                request_timeout=request_timeout,
                throwable_errors={
                    "GetResourceTimedOut": filesystem_errors.GetResourceTimedOut,
                    "InvalidSpaces": filesystem_errors.InvalidSpaces,
                    "SpacesNotFound": filesystem_errors.SpacesNotFound,
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
            typing.List[filesystem_models.GetSpacesBatchRequestElement],
            annotated_types.Len(min_length=1, max_length=200),
        ],
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[filesystem_models.GetSpacesBatchResponse]:
        """
        Fetch multiple spaces in a single request.

        Required scopes: [api:v3:space:read:get]

        :param body: Body of the request
        :type body: List[GetSpacesBatchRequestElement]
        :param preview:
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[filesystem_models.GetSpacesBatchResponse]

        :raises BatchRequestSizeExceededLimit:
        :raises GetResourceTimedOut: The request to retrieve resource information timed out.
        :raises InvalidSpaces: The given resources are not spaces.
        :raises MissingBatchRequest:
        :raises SpacesNotFound: The specified spaces could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v3/platform/spaces/getBatch",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body=body,
                response_type=filesystem_models.GetSpacesBatchResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "BatchRequestSizeExceededLimit": core_errors.BatchRequestSizeExceededLimit,
                    "GetResourceTimedOut": filesystem_errors.GetResourceTimedOut,
                    "InvalidSpaces": filesystem_errors.InvalidSpaces,
                    "MissingBatchRequest": core_errors.MissingBatchRequest,
                    "SpacesNotFound": filesystem_errors.SpacesNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def list(
        self,
        *,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> core.AsyncResourceIterator[filesystem_models.Space]:
        """
        Lists all spaces.

        This is a paginated endpoint. Each page may be smaller or larger than the requested page size.
        It is guaranteed that if there are more results available, the `nextPageToken` field will be populated.
        To get the next page, make the same request again, but set the value of the `pageToken` query parameter
        to be value of the `nextPageToken` value of the previous response.
        If there is no `nextPageToken` field in the response, you are on the last page.

        The default page size is 200. The maximum page size is 200. Requests for a larger page size will be
        clamped to 200. If pageSize is 0, the default page size is used.

        Required scopes: [api:v3:space:read:list]

        :param page_size:
        :type page_size: Optional[PageSize]
        :param page_token:
        :type page_token: Optional[PageToken]
        :param preview:
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.AsyncResourceIterator[filesystem_models.Space]

        :raises InvalidPageSize: The provided page size was negative. Page sizes must be greater than or equal to zero.
        :raises ListSpacesTimedOut: The request to list spaces timed out.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v3/platform/spaces",
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
                response_type=filesystem_models.ListSpacesResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "InvalidPageSize": core_errors.InvalidPageSize,
                    "ListSpacesTimedOut": filesystem_errors.ListSpacesTimedOut,
                },
                response_mode=_sdk_internal.get("response_mode", "ITERATOR"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def restore(
        self,
        space_rid: filesystem_models.SpaceRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[None]:
        """
        Restore the given space and any directly trashed ancestors from the trash. If the space is not
        directly trashed, this operation will return an error.

        Required scopes: [api:v3:space:write:restore]

        :param space_rid:
        :type space_rid: SpaceRid
        :param preview:
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[None]

        :raises InvalidDisplayNameOnRestore: Cannot restore resource because restoring it would produce an invalid display name. While the resource is still in trash, rename it to a valid name that does not contain the reserved text ' (trashed)', then retry the restore.
        :raises InvalidSpaces: The given resources are not spaces.
        :raises ResourceNotDirectlyTrashed: The resource is not directly trashed.
        :raises ResourceRegisteredForDeletion: The resource, or one of its ancestors, is registered for deletion. Resources cannot be created within, or restored within, a project or space that is registered for deletion.
        :raises RestoreOntologyResourcePermissionDenied: The resource, or one of the trashed ancestors that would be restored alongside it, backs an ontology entity. Restoring such a resource through the filesystem would leave the ontology in an inconsistent state, so it must be restored through the ontology APIs instead.
        :raises RestoreResourcePermissionDenied: Could not restore the resource due to insufficient permissions.
        :raises SpacesNotFound: The specified spaces could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v3/platform/spaces/{spaceRid}/restore",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "spaceRid": space_rid,
                },
                header_params={},
                body=None,
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "InvalidDisplayNameOnRestore": filesystem_errors.InvalidDisplayNameOnRestore,
                    "InvalidSpaces": filesystem_errors.InvalidSpaces,
                    "ResourceNotDirectlyTrashed": filesystem_errors.ResourceNotDirectlyTrashed,
                    "ResourceRegisteredForDeletion": filesystem_errors.ResourceRegisteredForDeletion,
                    "RestoreOntologyResourcePermissionDenied": filesystem_errors.RestoreOntologyResourcePermissionDenied,
                    "RestoreResourcePermissionDenied": filesystem_errors.RestoreResourcePermissionDenied,
                    "SpacesNotFound": filesystem_errors.SpacesNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _AsyncSpaceClientRaw:
    def __init__(self, client: AsyncSpaceClient) -> None:
        def delete(_: None): ...
        def delete_batch(_: None): ...
        def get(_: filesystem_models.Space): ...
        def get_batch(_: filesystem_models.GetSpacesBatchResponse): ...
        def list(_: filesystem_models.ListSpacesResponse): ...
        def restore(_: None): ...

        self.delete = core.async_with_raw_response(delete, client.delete)
        self.delete_batch = core.async_with_raw_response(delete_batch, client.delete_batch)
        self.get = core.async_with_raw_response(get, client.get)
        self.get_batch = core.async_with_raw_response(get_batch, client.get_batch)
        self.list = core.async_with_raw_response(list, client.list)
        self.restore = core.async_with_raw_response(restore, client.restore)


class _AsyncSpaceClientStreaming:
    def __init__(self, client: AsyncSpaceClient) -> None:
        def get(_: filesystem_models.Space): ...
        def get_batch(_: filesystem_models.GetSpacesBatchResponse): ...
        def list(_: filesystem_models.ListSpacesResponse): ...

        self.get = core.async_with_streaming_response(get, client.get)
        self.get_batch = core.async_with_streaming_response(get_batch, client.get_batch)
        self.list = core.async_with_streaming_response(list, client.list)
