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
from functools import cached_property

import pydantic
import typing_extensions

from foundry import _core as core
from foundry import _errors as errors
from foundry.v2.core import models as core_models
from foundry.v2.filesystem import errors as filesystem_errors
from foundry.v2.filesystem import models as filesystem_models


class ResourceClient:
    """
    The API client for the Resource Resource.

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
        self.with_streaming_response = _ResourceClientStreaming(
            auth=auth, hostname=hostname, config=config
        )
        self.with_raw_response = _ResourceClientRaw(auth=auth, hostname=hostname, config=config)

    @cached_property
    def Role(self):
        from foundry.v2.filesystem.resource_role import ResourceRoleClient

        return ResourceRoleClient(
            auth=self._auth,
            hostname=self._hostname,
            config=self._config,
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def add_markings(
        self,
        resource_rid: filesystem_models.ResourceRid,
        *,
        marking_ids: typing.List[core_models.MarkingId],
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> None:
        """
        Adds a list of Markings to a resource.
        :param resource_rid:
        :type resource_rid: ResourceRid
        :param marking_ids:
        :type marking_ids: List[MarkingId]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: None

        :raises AddMarkingsPermissionDenied: Could not addMarkings the Resource.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/filesystem/resources/{resourceRid}/addMarkings",
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
                    "markingIds": marking_ids,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "markingIds": typing.List[core_models.MarkingId],
                    },
                ),
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "AddMarkingsPermissionDenied": filesystem_errors.AddMarkingsPermissionDenied,
                },
            ),
        ).decode()

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def delete(
        self,
        resource_rid: filesystem_models.ResourceRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> None:
        """
        Move the given resource to the trash. Following this operation, the resource can be restored, using the
        `restore` operation, or permanently deleted using the `permanentlyDelete` operation.

        :param resource_rid:
        :type resource_rid: ResourceRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: None

        :raises DeleteResourcePermissionDenied: Could not delete the Resource.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="DELETE",
                resource_path="/v2/filesystem/resources/{resourceRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "resourceRid": resource_rid,
                },
                header_params={},
                body=None,
                body_type=None,
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "DeleteResourcePermissionDenied": filesystem_errors.DeleteResourcePermissionDenied,
                },
            ),
        ).decode()

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        resource_rid: filesystem_models.ResourceRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> filesystem_models.Resource:
        """
        Get the Resource with the specified rid.
        :param resource_rid:
        :type resource_rid: ResourceRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: filesystem_models.Resource

        :raises ResourceNotFound: The given Resource could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/filesystem/resources/{resourceRid}",
                query_params={
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
                response_type=filesystem_models.Resource,
                request_timeout=request_timeout,
                throwable_errors={
                    "ResourceNotFound": filesystem_errors.ResourceNotFound,
                },
            ),
        ).decode()

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get_access_requirements(
        self,
        resource_rid: filesystem_models.ResourceRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> filesystem_models.AccessRequirements:
        """
        Returns a list of access requirements a user needs in order to view a resource. Access requirements are
        composed of Organizations and Markings, and can either be applied directly to the resource or inherited.

        :param resource_rid:
        :type resource_rid: ResourceRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: filesystem_models.AccessRequirements

        :raises GetAccessRequirementsPermissionDenied: Could not getAccessRequirements the Resource.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/filesystem/resources/{resourceRid}/getAccessRequirements",
                query_params={
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
                response_type=filesystem_models.AccessRequirements,
                request_timeout=request_timeout,
                throwable_errors={
                    "GetAccessRequirementsPermissionDenied": filesystem_errors.GetAccessRequirementsPermissionDenied,
                },
            ),
        ).decode()

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get_by_path(
        self,
        *,
        path: filesystem_models.ResourcePath,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> filesystem_models.Resource:
        """
        Get a Resource by its absolute path.
        :param path: The path to the Resource. The leading slash is optional.
        :type path: ResourcePath
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: filesystem_models.Resource

        :raises GetByPathPermissionDenied: Could not getByPath the Resource.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/filesystem/resources/getByPath",
                query_params={
                    "path": path,
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=filesystem_models.Resource,
                request_timeout=request_timeout,
                throwable_errors={
                    "GetByPathPermissionDenied": filesystem_errors.GetByPathPermissionDenied,
                },
            ),
        ).decode()

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def markings(
        self,
        resource_rid: filesystem_models.ResourceRid,
        *,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ResourceIterator[core_models.MarkingId]:
        """
        List of Markings directly applied to a resource. The number of Markings on a resource is typically small
        so the `pageSize` and `pageToken` parameters are not required.

        :param resource_rid:
        :type resource_rid: ResourceRid
        :param page_size: The page size to use for the endpoint.
        :type page_size: Optional[PageSize]
        :param page_token: The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
        :type page_token: Optional[PageToken]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ResourceIterator[core_models.MarkingId]
        """

        return self._api_client.iterate_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/filesystem/resources/{resourceRid}/markings",
                query_params={
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
                response_type=filesystem_models.ListMarkingsOfResourceResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def markings_page(
        self,
        resource_rid: filesystem_models.ResourceRid,
        *,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> filesystem_models.ListMarkingsOfResourceResponse:
        """
        List of Markings directly applied to a resource. The number of Markings on a resource is typically small
        so the `pageSize` and `pageToken` parameters are not required.

        :param resource_rid:
        :type resource_rid: ResourceRid
        :param page_size: The page size to use for the endpoint.
        :type page_size: Optional[PageSize]
        :param page_token: The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
        :type page_token: Optional[PageToken]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: filesystem_models.ListMarkingsOfResourceResponse
        """

        warnings.warn(
            "The client.filesystem.Resource.markings_page(...) method has been deprecated. Please use client.filesystem.Resource.markings(...) instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/filesystem/resources/{resourceRid}/markings",
                query_params={
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
                response_type=filesystem_models.ListMarkingsOfResourceResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        ).decode()

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def permanently_delete(
        self,
        resource_rid: filesystem_models.ResourceRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> None:
        """
        Permanently delete the given resource from the trash. If the Resource is not directly trashed, a
        `ResourceNotTrashed` error will be thrown.

        :param resource_rid:
        :type resource_rid: ResourceRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: None

        :raises PermanentlyDeleteResourcePermissionDenied: Could not permanentlyDelete the Resource.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/filesystem/resources/{resourceRid}/permanentlyDelete",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "resourceRid": resource_rid,
                },
                header_params={},
                body=None,
                body_type=None,
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "PermanentlyDeleteResourcePermissionDenied": filesystem_errors.PermanentlyDeleteResourcePermissionDenied,
                },
            ),
        ).decode()

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def remove_markings(
        self,
        resource_rid: filesystem_models.ResourceRid,
        *,
        marking_ids: typing.List[core_models.MarkingId],
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> None:
        """
        Removes Markings from a resource.
        :param resource_rid:
        :type resource_rid: ResourceRid
        :param marking_ids:
        :type marking_ids: List[MarkingId]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: None

        :raises RemoveMarkingsPermissionDenied: Could not removeMarkings the Resource.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/filesystem/resources/{resourceRid}/removeMarkings",
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
                    "markingIds": marking_ids,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "markingIds": typing.List[core_models.MarkingId],
                    },
                ),
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "RemoveMarkingsPermissionDenied": filesystem_errors.RemoveMarkingsPermissionDenied,
                },
            ),
        ).decode()

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def restore(
        self,
        resource_rid: filesystem_models.ResourceRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> None:
        """
        Restore the given resource and any directly trashed ancestors from the trash. If the resource is not
        trashed, this operation will be ignored.

        :param resource_rid:
        :type resource_rid: ResourceRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: None

        :raises RestoreResourcePermissionDenied: Could not restore the Resource.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/filesystem/resources/{resourceRid}/restore",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "resourceRid": resource_rid,
                },
                header_params={},
                body=None,
                body_type=None,
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "RestoreResourcePermissionDenied": filesystem_errors.RestoreResourcePermissionDenied,
                },
            ),
        ).decode()


class _ResourceClientRaw:
    """
    The API client for the Resource Resource.

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
    def add_markings(
        self,
        resource_rid: filesystem_models.ResourceRid,
        *,
        marking_ids: typing.List[core_models.MarkingId],
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[None]:
        """
        Adds a list of Markings to a resource.
        :param resource_rid:
        :type resource_rid: ResourceRid
        :param marking_ids:
        :type marking_ids: List[MarkingId]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[None]

        :raises AddMarkingsPermissionDenied: Could not addMarkings the Resource.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/filesystem/resources/{resourceRid}/addMarkings",
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
                    "markingIds": marking_ids,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "markingIds": typing.List[core_models.MarkingId],
                    },
                ),
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "AddMarkingsPermissionDenied": filesystem_errors.AddMarkingsPermissionDenied,
                },
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def delete(
        self,
        resource_rid: filesystem_models.ResourceRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[None]:
        """
        Move the given resource to the trash. Following this operation, the resource can be restored, using the
        `restore` operation, or permanently deleted using the `permanentlyDelete` operation.

        :param resource_rid:
        :type resource_rid: ResourceRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[None]

        :raises DeleteResourcePermissionDenied: Could not delete the Resource.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="DELETE",
                resource_path="/v2/filesystem/resources/{resourceRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "resourceRid": resource_rid,
                },
                header_params={},
                body=None,
                body_type=None,
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "DeleteResourcePermissionDenied": filesystem_errors.DeleteResourcePermissionDenied,
                },
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        resource_rid: filesystem_models.ResourceRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[filesystem_models.Resource]:
        """
        Get the Resource with the specified rid.
        :param resource_rid:
        :type resource_rid: ResourceRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[filesystem_models.Resource]

        :raises ResourceNotFound: The given Resource could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/filesystem/resources/{resourceRid}",
                query_params={
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
                response_type=filesystem_models.Resource,
                request_timeout=request_timeout,
                throwable_errors={
                    "ResourceNotFound": filesystem_errors.ResourceNotFound,
                },
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get_access_requirements(
        self,
        resource_rid: filesystem_models.ResourceRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[filesystem_models.AccessRequirements]:
        """
        Returns a list of access requirements a user needs in order to view a resource. Access requirements are
        composed of Organizations and Markings, and can either be applied directly to the resource or inherited.

        :param resource_rid:
        :type resource_rid: ResourceRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[filesystem_models.AccessRequirements]

        :raises GetAccessRequirementsPermissionDenied: Could not getAccessRequirements the Resource.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/filesystem/resources/{resourceRid}/getAccessRequirements",
                query_params={
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
                response_type=filesystem_models.AccessRequirements,
                request_timeout=request_timeout,
                throwable_errors={
                    "GetAccessRequirementsPermissionDenied": filesystem_errors.GetAccessRequirementsPermissionDenied,
                },
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get_by_path(
        self,
        *,
        path: filesystem_models.ResourcePath,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[filesystem_models.Resource]:
        """
        Get a Resource by its absolute path.
        :param path: The path to the Resource. The leading slash is optional.
        :type path: ResourcePath
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[filesystem_models.Resource]

        :raises GetByPathPermissionDenied: Could not getByPath the Resource.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/filesystem/resources/getByPath",
                query_params={
                    "path": path,
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=filesystem_models.Resource,
                request_timeout=request_timeout,
                throwable_errors={
                    "GetByPathPermissionDenied": filesystem_errors.GetByPathPermissionDenied,
                },
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def markings(
        self,
        resource_rid: filesystem_models.ResourceRid,
        *,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[filesystem_models.ListMarkingsOfResourceResponse]:
        """
        List of Markings directly applied to a resource. The number of Markings on a resource is typically small
        so the `pageSize` and `pageToken` parameters are not required.

        :param resource_rid:
        :type resource_rid: ResourceRid
        :param page_size: The page size to use for the endpoint.
        :type page_size: Optional[PageSize]
        :param page_token: The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
        :type page_token: Optional[PageToken]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[filesystem_models.ListMarkingsOfResourceResponse]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/filesystem/resources/{resourceRid}/markings",
                query_params={
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
                response_type=filesystem_models.ListMarkingsOfResourceResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def markings_page(
        self,
        resource_rid: filesystem_models.ResourceRid,
        *,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[filesystem_models.ListMarkingsOfResourceResponse]:
        """
        List of Markings directly applied to a resource. The number of Markings on a resource is typically small
        so the `pageSize` and `pageToken` parameters are not required.

        :param resource_rid:
        :type resource_rid: ResourceRid
        :param page_size: The page size to use for the endpoint.
        :type page_size: Optional[PageSize]
        :param page_token: The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
        :type page_token: Optional[PageToken]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[filesystem_models.ListMarkingsOfResourceResponse]
        """

        warnings.warn(
            "The client.filesystem.Resource.markings_page(...) method has been deprecated. Please use client.filesystem.Resource.markings(...) instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/filesystem/resources/{resourceRid}/markings",
                query_params={
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
                response_type=filesystem_models.ListMarkingsOfResourceResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def permanently_delete(
        self,
        resource_rid: filesystem_models.ResourceRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[None]:
        """
        Permanently delete the given resource from the trash. If the Resource is not directly trashed, a
        `ResourceNotTrashed` error will be thrown.

        :param resource_rid:
        :type resource_rid: ResourceRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[None]

        :raises PermanentlyDeleteResourcePermissionDenied: Could not permanentlyDelete the Resource.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/filesystem/resources/{resourceRid}/permanentlyDelete",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "resourceRid": resource_rid,
                },
                header_params={},
                body=None,
                body_type=None,
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "PermanentlyDeleteResourcePermissionDenied": filesystem_errors.PermanentlyDeleteResourcePermissionDenied,
                },
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def remove_markings(
        self,
        resource_rid: filesystem_models.ResourceRid,
        *,
        marking_ids: typing.List[core_models.MarkingId],
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[None]:
        """
        Removes Markings from a resource.
        :param resource_rid:
        :type resource_rid: ResourceRid
        :param marking_ids:
        :type marking_ids: List[MarkingId]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[None]

        :raises RemoveMarkingsPermissionDenied: Could not removeMarkings the Resource.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/filesystem/resources/{resourceRid}/removeMarkings",
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
                    "markingIds": marking_ids,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "markingIds": typing.List[core_models.MarkingId],
                    },
                ),
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "RemoveMarkingsPermissionDenied": filesystem_errors.RemoveMarkingsPermissionDenied,
                },
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
    ) -> core.ApiResponse[None]:
        """
        Restore the given resource and any directly trashed ancestors from the trash. If the resource is not
        trashed, this operation will be ignored.

        :param resource_rid:
        :type resource_rid: ResourceRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[None]

        :raises RestoreResourcePermissionDenied: Could not restore the Resource.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/filesystem/resources/{resourceRid}/restore",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "resourceRid": resource_rid,
                },
                header_params={},
                body=None,
                body_type=None,
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "RestoreResourcePermissionDenied": filesystem_errors.RestoreResourcePermissionDenied,
                },
            ),
        )


class _ResourceClientStreaming:
    """
    The API client for the Resource Resource.

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
    def add_markings(
        self,
        resource_rid: filesystem_models.ResourceRid,
        *,
        marking_ids: typing.List[core_models.MarkingId],
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[None]:
        """
        Adds a list of Markings to a resource.
        :param resource_rid:
        :type resource_rid: ResourceRid
        :param marking_ids:
        :type marking_ids: List[MarkingId]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[None]

        :raises AddMarkingsPermissionDenied: Could not addMarkings the Resource.
        """

        return self._api_client.stream_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/filesystem/resources/{resourceRid}/addMarkings",
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
                    "markingIds": marking_ids,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "markingIds": typing.List[core_models.MarkingId],
                    },
                ),
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "AddMarkingsPermissionDenied": filesystem_errors.AddMarkingsPermissionDenied,
                },
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def delete(
        self,
        resource_rid: filesystem_models.ResourceRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[None]:
        """
        Move the given resource to the trash. Following this operation, the resource can be restored, using the
        `restore` operation, or permanently deleted using the `permanentlyDelete` operation.

        :param resource_rid:
        :type resource_rid: ResourceRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[None]

        :raises DeleteResourcePermissionDenied: Could not delete the Resource.
        """

        return self._api_client.stream_api(
            core.RequestInfo(
                method="DELETE",
                resource_path="/v2/filesystem/resources/{resourceRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "resourceRid": resource_rid,
                },
                header_params={},
                body=None,
                body_type=None,
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "DeleteResourcePermissionDenied": filesystem_errors.DeleteResourcePermissionDenied,
                },
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        resource_rid: filesystem_models.ResourceRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[filesystem_models.Resource]:
        """
        Get the Resource with the specified rid.
        :param resource_rid:
        :type resource_rid: ResourceRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[filesystem_models.Resource]

        :raises ResourceNotFound: The given Resource could not be found.
        """

        return self._api_client.stream_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/filesystem/resources/{resourceRid}",
                query_params={
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
                response_type=filesystem_models.Resource,
                request_timeout=request_timeout,
                throwable_errors={
                    "ResourceNotFound": filesystem_errors.ResourceNotFound,
                },
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get_access_requirements(
        self,
        resource_rid: filesystem_models.ResourceRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[filesystem_models.AccessRequirements]:
        """
        Returns a list of access requirements a user needs in order to view a resource. Access requirements are
        composed of Organizations and Markings, and can either be applied directly to the resource or inherited.

        :param resource_rid:
        :type resource_rid: ResourceRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[filesystem_models.AccessRequirements]

        :raises GetAccessRequirementsPermissionDenied: Could not getAccessRequirements the Resource.
        """

        return self._api_client.stream_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/filesystem/resources/{resourceRid}/getAccessRequirements",
                query_params={
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
                response_type=filesystem_models.AccessRequirements,
                request_timeout=request_timeout,
                throwable_errors={
                    "GetAccessRequirementsPermissionDenied": filesystem_errors.GetAccessRequirementsPermissionDenied,
                },
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get_by_path(
        self,
        *,
        path: filesystem_models.ResourcePath,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[filesystem_models.Resource]:
        """
        Get a Resource by its absolute path.
        :param path: The path to the Resource. The leading slash is optional.
        :type path: ResourcePath
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[filesystem_models.Resource]

        :raises GetByPathPermissionDenied: Could not getByPath the Resource.
        """

        return self._api_client.stream_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/filesystem/resources/getByPath",
                query_params={
                    "path": path,
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=filesystem_models.Resource,
                request_timeout=request_timeout,
                throwable_errors={
                    "GetByPathPermissionDenied": filesystem_errors.GetByPathPermissionDenied,
                },
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def markings(
        self,
        resource_rid: filesystem_models.ResourceRid,
        *,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[filesystem_models.ListMarkingsOfResourceResponse]:
        """
        List of Markings directly applied to a resource. The number of Markings on a resource is typically small
        so the `pageSize` and `pageToken` parameters are not required.

        :param resource_rid:
        :type resource_rid: ResourceRid
        :param page_size: The page size to use for the endpoint.
        :type page_size: Optional[PageSize]
        :param page_token: The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
        :type page_token: Optional[PageToken]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[filesystem_models.ListMarkingsOfResourceResponse]
        """

        return self._api_client.stream_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/filesystem/resources/{resourceRid}/markings",
                query_params={
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
                response_type=filesystem_models.ListMarkingsOfResourceResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def markings_page(
        self,
        resource_rid: filesystem_models.ResourceRid,
        *,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[filesystem_models.ListMarkingsOfResourceResponse]:
        """
        List of Markings directly applied to a resource. The number of Markings on a resource is typically small
        so the `pageSize` and `pageToken` parameters are not required.

        :param resource_rid:
        :type resource_rid: ResourceRid
        :param page_size: The page size to use for the endpoint.
        :type page_size: Optional[PageSize]
        :param page_token: The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
        :type page_token: Optional[PageToken]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[filesystem_models.ListMarkingsOfResourceResponse]
        """

        warnings.warn(
            "The client.filesystem.Resource.markings_page(...) method has been deprecated. Please use client.filesystem.Resource.markings(...) instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        return self._api_client.stream_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/filesystem/resources/{resourceRid}/markings",
                query_params={
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
                response_type=filesystem_models.ListMarkingsOfResourceResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def permanently_delete(
        self,
        resource_rid: filesystem_models.ResourceRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[None]:
        """
        Permanently delete the given resource from the trash. If the Resource is not directly trashed, a
        `ResourceNotTrashed` error will be thrown.

        :param resource_rid:
        :type resource_rid: ResourceRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[None]

        :raises PermanentlyDeleteResourcePermissionDenied: Could not permanentlyDelete the Resource.
        """

        return self._api_client.stream_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/filesystem/resources/{resourceRid}/permanentlyDelete",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "resourceRid": resource_rid,
                },
                header_params={},
                body=None,
                body_type=None,
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "PermanentlyDeleteResourcePermissionDenied": filesystem_errors.PermanentlyDeleteResourcePermissionDenied,
                },
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def remove_markings(
        self,
        resource_rid: filesystem_models.ResourceRid,
        *,
        marking_ids: typing.List[core_models.MarkingId],
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[None]:
        """
        Removes Markings from a resource.
        :param resource_rid:
        :type resource_rid: ResourceRid
        :param marking_ids:
        :type marking_ids: List[MarkingId]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[None]

        :raises RemoveMarkingsPermissionDenied: Could not removeMarkings the Resource.
        """

        return self._api_client.stream_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/filesystem/resources/{resourceRid}/removeMarkings",
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
                    "markingIds": marking_ids,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "markingIds": typing.List[core_models.MarkingId],
                    },
                ),
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "RemoveMarkingsPermissionDenied": filesystem_errors.RemoveMarkingsPermissionDenied,
                },
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
    ) -> core.StreamingContextManager[None]:
        """
        Restore the given resource and any directly trashed ancestors from the trash. If the resource is not
        trashed, this operation will be ignored.

        :param resource_rid:
        :type resource_rid: ResourceRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[None]

        :raises RestoreResourcePermissionDenied: Could not restore the Resource.
        """

        return self._api_client.stream_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/filesystem/resources/{resourceRid}/restore",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "resourceRid": resource_rid,
                },
                header_params={},
                body=None,
                body_type=None,
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "RestoreResourcePermissionDenied": filesystem_errors.RestoreResourcePermissionDenied,
                },
            ),
        )
