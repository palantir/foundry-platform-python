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


class ProjectResourceReferenceClient:
    """
    The API client for the ProjectResourceReference Resource.

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

        self.with_streaming_response = _ProjectResourceReferenceClientStreaming(self)
        self.with_raw_response = _ProjectResourceReferenceClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def add(
        self,
        project_rid: filesystem_models.ProjectRid,
        *,
        resources: typing.List[filesystem_models.AddResourceReferenceRequest],
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> None:
        """
        Add references to the given project

        :param project_rid:
        :type project_rid: ProjectRid
        :param resources:
        :type resources: List[AddResourceReferenceRequest]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: None

        :raises AddProjectResourceReferencesPermissionDenied: Could not add the ProjectResourceReference.
        :raises InvalidProject: The provided resource identifier does not refer to a valid project.
        :raises InvalidResourceReference: The resource reference is invalid. This can occur when the resource identifier is malformed, the resource type does not match the reference type, or the resource cannot be added as a reference.
        :raises ProjectNotFound: The given Project could not be found.
        :raises ResourceNotFound: The given Resource could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/filesystem/projects/{projectRid}/references/add",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "projectRid": project_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                },
                body=filesystem_models.AddProjectResourceReferencesRequest(
                    resources=resources,
                ),
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "AddProjectResourceReferencesPermissionDenied": filesystem_errors.AddProjectResourceReferencesPermissionDenied,
                    "InvalidProject": filesystem_errors.InvalidProject,
                    "InvalidResourceReference": filesystem_errors.InvalidResourceReference,
                    "ProjectNotFound": filesystem_errors.ProjectNotFound,
                    "ResourceNotFound": filesystem_errors.ResourceNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def list(
        self,
        project_rid: filesystem_models.ProjectRid,
        *,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        reference_type: typing.Optional[filesystem_models.ProjectResourceReferenceType] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> core.ResourceIterator[filesystem_models.ProjectResourceReference]:
        """
        List all references in the given project

        :param project_rid:
        :type project_rid: ProjectRid
        :param page_size: The page size to use for the endpoint.
        :type page_size: Optional[PageSize]
        :param page_token: The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
        :type page_token: Optional[PageToken]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param reference_type: Filter references by type. If not provided, all references are returned.
        :type reference_type: Optional[ProjectResourceReferenceType]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ResourceIterator[filesystem_models.ProjectResourceReference]

        :raises ProjectNotFound: The given Project could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/filesystem/projects/{projectRid}/references",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
                    "preview": preview,
                    "referenceType": reference_type,
                },
                path_params={
                    "projectRid": project_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=filesystem_models.ListProjectResourceReferencesResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "ProjectNotFound": filesystem_errors.ProjectNotFound,
                },
                response_mode=_sdk_internal.get("response_mode", "ITERATOR"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def remove(
        self,
        project_rid: filesystem_models.ProjectRid,
        *,
        resources: typing.List[core.RID],
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> None:
        """
        Remove references from the given project

        :param project_rid:
        :type project_rid: ProjectRid
        :param resources: The resource identifiers to remove as references. These may be either filesystem or external resource identifiers.
        :type resources: List[RID]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: None

        :raises InvalidProject: The provided resource identifier does not refer to a valid project.
        :raises InvalidResourceReference: The resource reference is invalid. This can occur when the resource identifier is malformed, the resource type does not match the reference type, or the resource cannot be added as a reference.
        :raises ProjectNotFound: The given Project could not be found.
        :raises RemoveProjectResourceReferencesPermissionDenied: Could not remove the ProjectResourceReference.
        :raises ResourceNotFound: The given Resource could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/filesystem/projects/{projectRid}/references/remove",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "projectRid": project_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                },
                body=filesystem_models.RemoveProjectResourceReferencesRequest(
                    resources=resources,
                ),
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "InvalidProject": filesystem_errors.InvalidProject,
                    "InvalidResourceReference": filesystem_errors.InvalidResourceReference,
                    "ProjectNotFound": filesystem_errors.ProjectNotFound,
                    "RemoveProjectResourceReferencesPermissionDenied": filesystem_errors.RemoveProjectResourceReferencesPermissionDenied,
                    "ResourceNotFound": filesystem_errors.ResourceNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _ProjectResourceReferenceClientRaw:
    def __init__(self, client: ProjectResourceReferenceClient) -> None:
        def add(_: None): ...
        def list(_: filesystem_models.ListProjectResourceReferencesResponse): ...
        def remove(_: None): ...

        self.add = core.with_raw_response(add, client.add)
        self.list = core.with_raw_response(list, client.list)
        self.remove = core.with_raw_response(remove, client.remove)


class _ProjectResourceReferenceClientStreaming:
    def __init__(self, client: ProjectResourceReferenceClient) -> None:
        def list(_: filesystem_models.ListProjectResourceReferencesResponse): ...

        self.list = core.with_streaming_response(list, client.list)


class AsyncProjectResourceReferenceClient:
    """
    The API client for the ProjectResourceReference Resource.

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

        self.with_streaming_response = _AsyncProjectResourceReferenceClientStreaming(self)
        self.with_raw_response = _AsyncProjectResourceReferenceClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def add(
        self,
        project_rid: filesystem_models.ProjectRid,
        *,
        resources: typing.List[filesystem_models.AddResourceReferenceRequest],
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[None]:
        """
        Add references to the given project

        :param project_rid:
        :type project_rid: ProjectRid
        :param resources:
        :type resources: List[AddResourceReferenceRequest]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[None]

        :raises AddProjectResourceReferencesPermissionDenied: Could not add the ProjectResourceReference.
        :raises InvalidProject: The provided resource identifier does not refer to a valid project.
        :raises InvalidResourceReference: The resource reference is invalid. This can occur when the resource identifier is malformed, the resource type does not match the reference type, or the resource cannot be added as a reference.
        :raises ProjectNotFound: The given Project could not be found.
        :raises ResourceNotFound: The given Resource could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/filesystem/projects/{projectRid}/references/add",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "projectRid": project_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                },
                body=filesystem_models.AddProjectResourceReferencesRequest(
                    resources=resources,
                ),
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "AddProjectResourceReferencesPermissionDenied": filesystem_errors.AddProjectResourceReferencesPermissionDenied,
                    "InvalidProject": filesystem_errors.InvalidProject,
                    "InvalidResourceReference": filesystem_errors.InvalidResourceReference,
                    "ProjectNotFound": filesystem_errors.ProjectNotFound,
                    "ResourceNotFound": filesystem_errors.ResourceNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def list(
        self,
        project_rid: filesystem_models.ProjectRid,
        *,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        reference_type: typing.Optional[filesystem_models.ProjectResourceReferenceType] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> core.AsyncResourceIterator[filesystem_models.ProjectResourceReference]:
        """
        List all references in the given project

        :param project_rid:
        :type project_rid: ProjectRid
        :param page_size: The page size to use for the endpoint.
        :type page_size: Optional[PageSize]
        :param page_token: The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
        :type page_token: Optional[PageToken]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param reference_type: Filter references by type. If not provided, all references are returned.
        :type reference_type: Optional[ProjectResourceReferenceType]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.AsyncResourceIterator[filesystem_models.ProjectResourceReference]

        :raises ProjectNotFound: The given Project could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/filesystem/projects/{projectRid}/references",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
                    "preview": preview,
                    "referenceType": reference_type,
                },
                path_params={
                    "projectRid": project_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=filesystem_models.ListProjectResourceReferencesResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "ProjectNotFound": filesystem_errors.ProjectNotFound,
                },
                response_mode=_sdk_internal.get("response_mode", "ITERATOR"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def remove(
        self,
        project_rid: filesystem_models.ProjectRid,
        *,
        resources: typing.List[core.RID],
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[None]:
        """
        Remove references from the given project

        :param project_rid:
        :type project_rid: ProjectRid
        :param resources: The resource identifiers to remove as references. These may be either filesystem or external resource identifiers.
        :type resources: List[RID]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[None]

        :raises InvalidProject: The provided resource identifier does not refer to a valid project.
        :raises InvalidResourceReference: The resource reference is invalid. This can occur when the resource identifier is malformed, the resource type does not match the reference type, or the resource cannot be added as a reference.
        :raises ProjectNotFound: The given Project could not be found.
        :raises RemoveProjectResourceReferencesPermissionDenied: Could not remove the ProjectResourceReference.
        :raises ResourceNotFound: The given Resource could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/filesystem/projects/{projectRid}/references/remove",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "projectRid": project_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                },
                body=filesystem_models.RemoveProjectResourceReferencesRequest(
                    resources=resources,
                ),
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "InvalidProject": filesystem_errors.InvalidProject,
                    "InvalidResourceReference": filesystem_errors.InvalidResourceReference,
                    "ProjectNotFound": filesystem_errors.ProjectNotFound,
                    "RemoveProjectResourceReferencesPermissionDenied": filesystem_errors.RemoveProjectResourceReferencesPermissionDenied,
                    "ResourceNotFound": filesystem_errors.ResourceNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _AsyncProjectResourceReferenceClientRaw:
    def __init__(self, client: AsyncProjectResourceReferenceClient) -> None:
        def add(_: None): ...
        def list(_: filesystem_models.ListProjectResourceReferencesResponse): ...
        def remove(_: None): ...

        self.add = core.async_with_raw_response(add, client.add)
        self.list = core.async_with_raw_response(list, client.list)
        self.remove = core.async_with_raw_response(remove, client.remove)


class _AsyncProjectResourceReferenceClientStreaming:
    def __init__(self, client: AsyncProjectResourceReferenceClient) -> None:
        def list(_: filesystem_models.ListProjectResourceReferencesResponse): ...

        self.list = core.async_with_streaming_response(list, client.list)
