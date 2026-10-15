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


class ProjectClient:
    """
    The API client for the Project Resource.

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

        self.with_streaming_response = _ProjectClientStreaming(self)
        self.with_raw_response = _ProjectClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def delete(
        self,
        project_rid: filesystem_models.ProjectRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> None:
        """
        Move the given project to the trash. Following this operation, the project can be restored, using the
        `restore` operation, or permanently deleted using the `permanentlyDelete` operation.

        Required scopes: [api:v3:project:write:delete]

        :param project_rid:
        :type project_rid: ProjectRid
        :param preview:
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: None

        :raises DeleteOntologyResourcePermissionDenied: The resource, or one of its descendants, backs an ontology entity. Trashing such a resource through the filesystem would leave the ontology in an inconsistent state, so it must be deleted through the ontology APIs instead.
        :raises DeleteProjectPermissionDenied: Could not delete the project due to insufficient permissions.
        :raises InvalidProjects: The given resources are not projects.
        :raises ProjectsNotFound: The specified projects could not be found.
        :raises TrashingHomeFoldersNotSupported: Home folders cannot be trashed. Home folders are created and managed by the platform.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="DELETE",
                resource_path="/v3/platform/projects/{projectRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "projectRid": project_rid,
                },
                header_params={},
                body=None,
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "DeleteOntologyResourcePermissionDenied": filesystem_errors.DeleteOntologyResourcePermissionDenied,
                    "DeleteProjectPermissionDenied": filesystem_errors.DeleteProjectPermissionDenied,
                    "InvalidProjects": filesystem_errors.InvalidProjects,
                    "ProjectsNotFound": filesystem_errors.ProjectsNotFound,
                    "TrashingHomeFoldersNotSupported": filesystem_errors.TrashingHomeFoldersNotSupported,
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
            typing.List[filesystem_models.DeleteProjectsBatchRequestElement],
            annotated_types.Len(min_length=1, max_length=100),
        ],
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> None:
        """
        Trash multiple projects in a single request.

        Required scopes: [api:v3:project:write:delete]

        :param body: Body of the request
        :type body: List[DeleteProjectsBatchRequestElement]
        :param preview:
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: None

        :raises BatchRequestSizeExceededLimit:
        :raises DeleteOntologyResourcePermissionDenied: The resource, or one of its descendants, backs an ontology entity. Trashing such a resource through the filesystem would leave the ontology in an inconsistent state, so it must be deleted through the ontology APIs instead.
        :raises DeleteProjectPermissionDenied: Could not delete the project due to insufficient permissions.
        :raises InvalidProjects: The given resources are not projects.
        :raises MissingBatchRequest:
        :raises ProjectsNotFound: The specified projects could not be found.
        :raises TrashingHomeFoldersNotSupported: Home folders cannot be trashed. Home folders are created and managed by the platform.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v3/platform/projects/deleteBatch",
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
                    "DeleteProjectPermissionDenied": filesystem_errors.DeleteProjectPermissionDenied,
                    "InvalidProjects": filesystem_errors.InvalidProjects,
                    "MissingBatchRequest": core_errors.MissingBatchRequest,
                    "ProjectsNotFound": filesystem_errors.ProjectsNotFound,
                    "TrashingHomeFoldersNotSupported": filesystem_errors.TrashingHomeFoldersNotSupported,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        project_rid: filesystem_models.ProjectRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> filesystem_models.Project:
        """
        Get the project with the specified resource identifier (RID).

        Required scopes: [api:v3:project:read:get]

        :param project_rid:
        :type project_rid: ProjectRid
        :param preview:
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: filesystem_models.Project

        :raises GetResourceTimedOut: The request to retrieve resource information timed out.
        :raises InvalidProjects: The given resources are not projects.
        :raises ProjectsNotFound: The specified projects could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v3/platform/projects/{projectRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "projectRid": project_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=filesystem_models.Project,
                request_timeout=request_timeout,
                throwable_errors={
                    "GetResourceTimedOut": filesystem_errors.GetResourceTimedOut,
                    "InvalidProjects": filesystem_errors.InvalidProjects,
                    "ProjectsNotFound": filesystem_errors.ProjectsNotFound,
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
            typing.List[filesystem_models.GetProjectsBatchRequestElement],
            annotated_types.Len(min_length=1, max_length=1000),
        ],
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> filesystem_models.GetProjectsBatchResponse:
        """
        Fetch multiple projects in a single request.

        Required scopes: [api:v3:project:read:get]

        :param body: Body of the request
        :type body: List[GetProjectsBatchRequestElement]
        :param preview:
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: filesystem_models.GetProjectsBatchResponse

        :raises BatchRequestSizeExceededLimit:
        :raises GetResourceTimedOut: The request to retrieve resource information timed out.
        :raises InvalidProjects: The given resources are not projects.
        :raises MissingBatchRequest:
        :raises ProjectsNotFound: The specified projects could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v3/platform/projects/getBatch",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body=body,
                response_type=filesystem_models.GetProjectsBatchResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "BatchRequestSizeExceededLimit": core_errors.BatchRequestSizeExceededLimit,
                    "GetResourceTimedOut": filesystem_errors.GetResourceTimedOut,
                    "InvalidProjects": filesystem_errors.InvalidProjects,
                    "MissingBatchRequest": core_errors.MissingBatchRequest,
                    "ProjectsNotFound": filesystem_errors.ProjectsNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def restore(
        self,
        project_rid: filesystem_models.ProjectRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> None:
        """
        Restore the given project and any directly trashed ancestors from the trash. If the project is not
        directly trashed, this operation will return an error.

        Required scopes: [api:v3:project:write:restore]

        :param project_rid:
        :type project_rid: ProjectRid
        :param preview:
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: None

        :raises InvalidDisplayNameOnRestore: Cannot restore resource because restoring it would produce an invalid display name. While the resource is still in trash, rename it to a valid name that does not contain the reserved text ' (trashed)', then retry the restore.
        :raises InvalidProjects: The given resources are not projects.
        :raises ProjectsNotFound: The specified projects could not be found.
        :raises ResourceNotDirectlyTrashed: The resource is not directly trashed.
        :raises ResourceRegisteredForDeletion: The resource, or one of its ancestors, is registered for deletion. Resources cannot be created within, or restored within, a project or space that is registered for deletion.
        :raises RestoreOntologyResourcePermissionDenied: The resource, or one of the trashed ancestors that would be restored alongside it, backs an ontology entity. Restoring such a resource through the filesystem would leave the ontology in an inconsistent state, so it must be restored through the ontology APIs instead.
        :raises RestoreResourcePermissionDenied: Could not restore the resource due to insufficient permissions.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v3/platform/projects/{projectRid}/restore",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "projectRid": project_rid,
                },
                header_params={},
                body=None,
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "InvalidDisplayNameOnRestore": filesystem_errors.InvalidDisplayNameOnRestore,
                    "InvalidProjects": filesystem_errors.InvalidProjects,
                    "ProjectsNotFound": filesystem_errors.ProjectsNotFound,
                    "ResourceNotDirectlyTrashed": filesystem_errors.ResourceNotDirectlyTrashed,
                    "ResourceRegisteredForDeletion": filesystem_errors.ResourceRegisteredForDeletion,
                    "RestoreOntologyResourcePermissionDenied": filesystem_errors.RestoreOntologyResourcePermissionDenied,
                    "RestoreResourcePermissionDenied": filesystem_errors.RestoreResourcePermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _ProjectClientRaw:
    def __init__(self, client: ProjectClient) -> None:
        def delete(_: None): ...
        def delete_batch(_: None): ...
        def get(_: filesystem_models.Project): ...
        def get_batch(_: filesystem_models.GetProjectsBatchResponse): ...
        def restore(_: None): ...

        self.delete = core.with_raw_response(delete, client.delete)
        self.delete_batch = core.with_raw_response(delete_batch, client.delete_batch)
        self.get = core.with_raw_response(get, client.get)
        self.get_batch = core.with_raw_response(get_batch, client.get_batch)
        self.restore = core.with_raw_response(restore, client.restore)


class _ProjectClientStreaming:
    def __init__(self, client: ProjectClient) -> None:
        def get(_: filesystem_models.Project): ...
        def get_batch(_: filesystem_models.GetProjectsBatchResponse): ...

        self.get = core.with_streaming_response(get, client.get)
        self.get_batch = core.with_streaming_response(get_batch, client.get_batch)


class AsyncProjectClient:
    """
    The API client for the Project Resource.

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

        self.with_streaming_response = _AsyncProjectClientStreaming(self)
        self.with_raw_response = _AsyncProjectClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def delete(
        self,
        project_rid: filesystem_models.ProjectRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[None]:
        """
        Move the given project to the trash. Following this operation, the project can be restored, using the
        `restore` operation, or permanently deleted using the `permanentlyDelete` operation.

        Required scopes: [api:v3:project:write:delete]

        :param project_rid:
        :type project_rid: ProjectRid
        :param preview:
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[None]

        :raises DeleteOntologyResourcePermissionDenied: The resource, or one of its descendants, backs an ontology entity. Trashing such a resource through the filesystem would leave the ontology in an inconsistent state, so it must be deleted through the ontology APIs instead.
        :raises DeleteProjectPermissionDenied: Could not delete the project due to insufficient permissions.
        :raises InvalidProjects: The given resources are not projects.
        :raises ProjectsNotFound: The specified projects could not be found.
        :raises TrashingHomeFoldersNotSupported: Home folders cannot be trashed. Home folders are created and managed by the platform.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="DELETE",
                resource_path="/v3/platform/projects/{projectRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "projectRid": project_rid,
                },
                header_params={},
                body=None,
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "DeleteOntologyResourcePermissionDenied": filesystem_errors.DeleteOntologyResourcePermissionDenied,
                    "DeleteProjectPermissionDenied": filesystem_errors.DeleteProjectPermissionDenied,
                    "InvalidProjects": filesystem_errors.InvalidProjects,
                    "ProjectsNotFound": filesystem_errors.ProjectsNotFound,
                    "TrashingHomeFoldersNotSupported": filesystem_errors.TrashingHomeFoldersNotSupported,
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
            typing.List[filesystem_models.DeleteProjectsBatchRequestElement],
            annotated_types.Len(min_length=1, max_length=100),
        ],
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[None]:
        """
        Trash multiple projects in a single request.

        Required scopes: [api:v3:project:write:delete]

        :param body: Body of the request
        :type body: List[DeleteProjectsBatchRequestElement]
        :param preview:
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[None]

        :raises BatchRequestSizeExceededLimit:
        :raises DeleteOntologyResourcePermissionDenied: The resource, or one of its descendants, backs an ontology entity. Trashing such a resource through the filesystem would leave the ontology in an inconsistent state, so it must be deleted through the ontology APIs instead.
        :raises DeleteProjectPermissionDenied: Could not delete the project due to insufficient permissions.
        :raises InvalidProjects: The given resources are not projects.
        :raises MissingBatchRequest:
        :raises ProjectsNotFound: The specified projects could not be found.
        :raises TrashingHomeFoldersNotSupported: Home folders cannot be trashed. Home folders are created and managed by the platform.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v3/platform/projects/deleteBatch",
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
                    "DeleteProjectPermissionDenied": filesystem_errors.DeleteProjectPermissionDenied,
                    "InvalidProjects": filesystem_errors.InvalidProjects,
                    "MissingBatchRequest": core_errors.MissingBatchRequest,
                    "ProjectsNotFound": filesystem_errors.ProjectsNotFound,
                    "TrashingHomeFoldersNotSupported": filesystem_errors.TrashingHomeFoldersNotSupported,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        project_rid: filesystem_models.ProjectRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[filesystem_models.Project]:
        """
        Get the project with the specified resource identifier (RID).

        Required scopes: [api:v3:project:read:get]

        :param project_rid:
        :type project_rid: ProjectRid
        :param preview:
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[filesystem_models.Project]

        :raises GetResourceTimedOut: The request to retrieve resource information timed out.
        :raises InvalidProjects: The given resources are not projects.
        :raises ProjectsNotFound: The specified projects could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v3/platform/projects/{projectRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "projectRid": project_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=filesystem_models.Project,
                request_timeout=request_timeout,
                throwable_errors={
                    "GetResourceTimedOut": filesystem_errors.GetResourceTimedOut,
                    "InvalidProjects": filesystem_errors.InvalidProjects,
                    "ProjectsNotFound": filesystem_errors.ProjectsNotFound,
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
            typing.List[filesystem_models.GetProjectsBatchRequestElement],
            annotated_types.Len(min_length=1, max_length=1000),
        ],
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[filesystem_models.GetProjectsBatchResponse]:
        """
        Fetch multiple projects in a single request.

        Required scopes: [api:v3:project:read:get]

        :param body: Body of the request
        :type body: List[GetProjectsBatchRequestElement]
        :param preview:
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[filesystem_models.GetProjectsBatchResponse]

        :raises BatchRequestSizeExceededLimit:
        :raises GetResourceTimedOut: The request to retrieve resource information timed out.
        :raises InvalidProjects: The given resources are not projects.
        :raises MissingBatchRequest:
        :raises ProjectsNotFound: The specified projects could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v3/platform/projects/getBatch",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body=body,
                response_type=filesystem_models.GetProjectsBatchResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "BatchRequestSizeExceededLimit": core_errors.BatchRequestSizeExceededLimit,
                    "GetResourceTimedOut": filesystem_errors.GetResourceTimedOut,
                    "InvalidProjects": filesystem_errors.InvalidProjects,
                    "MissingBatchRequest": core_errors.MissingBatchRequest,
                    "ProjectsNotFound": filesystem_errors.ProjectsNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def restore(
        self,
        project_rid: filesystem_models.ProjectRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[None]:
        """
        Restore the given project and any directly trashed ancestors from the trash. If the project is not
        directly trashed, this operation will return an error.

        Required scopes: [api:v3:project:write:restore]

        :param project_rid:
        :type project_rid: ProjectRid
        :param preview:
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[None]

        :raises InvalidDisplayNameOnRestore: Cannot restore resource because restoring it would produce an invalid display name. While the resource is still in trash, rename it to a valid name that does not contain the reserved text ' (trashed)', then retry the restore.
        :raises InvalidProjects: The given resources are not projects.
        :raises ProjectsNotFound: The specified projects could not be found.
        :raises ResourceNotDirectlyTrashed: The resource is not directly trashed.
        :raises ResourceRegisteredForDeletion: The resource, or one of its ancestors, is registered for deletion. Resources cannot be created within, or restored within, a project or space that is registered for deletion.
        :raises RestoreOntologyResourcePermissionDenied: The resource, or one of the trashed ancestors that would be restored alongside it, backs an ontology entity. Restoring such a resource through the filesystem would leave the ontology in an inconsistent state, so it must be restored through the ontology APIs instead.
        :raises RestoreResourcePermissionDenied: Could not restore the resource due to insufficient permissions.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v3/platform/projects/{projectRid}/restore",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "projectRid": project_rid,
                },
                header_params={},
                body=None,
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "InvalidDisplayNameOnRestore": filesystem_errors.InvalidDisplayNameOnRestore,
                    "InvalidProjects": filesystem_errors.InvalidProjects,
                    "ProjectsNotFound": filesystem_errors.ProjectsNotFound,
                    "ResourceNotDirectlyTrashed": filesystem_errors.ResourceNotDirectlyTrashed,
                    "ResourceRegisteredForDeletion": filesystem_errors.ResourceRegisteredForDeletion,
                    "RestoreOntologyResourcePermissionDenied": filesystem_errors.RestoreOntologyResourcePermissionDenied,
                    "RestoreResourcePermissionDenied": filesystem_errors.RestoreResourcePermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _AsyncProjectClientRaw:
    def __init__(self, client: AsyncProjectClient) -> None:
        def delete(_: None): ...
        def delete_batch(_: None): ...
        def get(_: filesystem_models.Project): ...
        def get_batch(_: filesystem_models.GetProjectsBatchResponse): ...
        def restore(_: None): ...

        self.delete = core.async_with_raw_response(delete, client.delete)
        self.delete_batch = core.async_with_raw_response(delete_batch, client.delete_batch)
        self.get = core.async_with_raw_response(get, client.get)
        self.get_batch = core.async_with_raw_response(get_batch, client.get_batch)
        self.restore = core.async_with_raw_response(restore, client.restore)


class _AsyncProjectClientStreaming:
    def __init__(self, client: AsyncProjectClient) -> None:
        def get(_: filesystem_models.Project): ...
        def get_batch(_: filesystem_models.GetProjectsBatchResponse): ...

        self.get = core.async_with_streaming_response(get, client.get)
        self.get_batch = core.async_with_streaming_response(get_batch, client.get_batch)
