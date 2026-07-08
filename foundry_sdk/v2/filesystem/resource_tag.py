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


class ResourceTagClient:
    """
    The API client for the ResourceTag Resource.

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

        self.with_streaming_response = _ResourceTagClientStreaming(self)
        self.with_raw_response = _ResourceTagClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def add(
        self,
        resource_rid: filesystem_models.ResourceRid,
        *,
        tag_rids: typing.List[filesystem_models.TagRid],
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> None:
        """
        Apply tags to a resource.
        :param resource_rid:
        :type resource_rid: ResourceRid
        :param tag_rids:
        :type tag_rids: List[TagRid]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: None

        :raises AddResourceTagsPermissionDenied: Could not add the ResourceTag.
        :raises ForbiddenOperationOnAutosavedResource: Performing this operation on an autosaved resource is not supported.
        :raises ForbiddenOperationOnHiddenResource: Performing this operation on a hidden resource is not supported.
        :raises ResourceNotFound: The given Resource could not be found.
        :raises TagNotFound: At least one of the provided tag RIDs could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/filesystem/resources/{resourceRid}/tags/add",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "resourceRid": resource_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                },
                body=filesystem_models.AddResourceTagsRequest(
                    tag_rids=tag_rids,
                ),
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "AddResourceTagsPermissionDenied": filesystem_errors.AddResourceTagsPermissionDenied,
                    "ForbiddenOperationOnAutosavedResource": filesystem_errors.ForbiddenOperationOnAutosavedResource,
                    "ForbiddenOperationOnHiddenResource": filesystem_errors.ForbiddenOperationOnHiddenResource,
                    "ResourceNotFound": filesystem_errors.ResourceNotFound,
                    "TagNotFound": filesystem_errors.TagNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def list(
        self,
        resource_rid: filesystem_models.ResourceRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> filesystem_models.ListResourceTagsResponse:
        """
        List the tags applied to a resource.

        :param resource_rid:
        :type resource_rid: ResourceRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: filesystem_models.ListResourceTagsResponse

        :raises ResourceNotFound: The given Resource could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/filesystem/resources/{resourceRid}/tags",
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
                response_type=filesystem_models.ListResourceTagsResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "ResourceNotFound": filesystem_errors.ResourceNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def remove(
        self,
        resource_rid: filesystem_models.ResourceRid,
        *,
        tag_rids: typing.List[filesystem_models.TagRid],
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> None:
        """
        Remove tags from a resource.
        :param resource_rid:
        :type resource_rid: ResourceRid
        :param tag_rids:
        :type tag_rids: List[TagRid]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: None

        :raises ForbiddenOperationOnAutosavedResource: Performing this operation on an autosaved resource is not supported.
        :raises ForbiddenOperationOnHiddenResource: Performing this operation on a hidden resource is not supported.
        :raises RemoveResourceTagsPermissionDenied: Could not remove the ResourceTag.
        :raises ResourceNotFound: The given Resource could not be found.
        :raises TagNotFound: At least one of the provided tag RIDs could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/filesystem/resources/{resourceRid}/tags/remove",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "resourceRid": resource_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                },
                body=filesystem_models.RemoveResourceTagsRequest(
                    tag_rids=tag_rids,
                ),
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "ForbiddenOperationOnAutosavedResource": filesystem_errors.ForbiddenOperationOnAutosavedResource,
                    "ForbiddenOperationOnHiddenResource": filesystem_errors.ForbiddenOperationOnHiddenResource,
                    "RemoveResourceTagsPermissionDenied": filesystem_errors.RemoveResourceTagsPermissionDenied,
                    "ResourceNotFound": filesystem_errors.ResourceNotFound,
                    "TagNotFound": filesystem_errors.TagNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _ResourceTagClientRaw:
    def __init__(self, client: ResourceTagClient) -> None:
        def add(_: None): ...
        def list(_: filesystem_models.ListResourceTagsResponse): ...
        def remove(_: None): ...

        self.add = core.with_raw_response(add, client.add)
        self.list = core.with_raw_response(list, client.list)
        self.remove = core.with_raw_response(remove, client.remove)


class _ResourceTagClientStreaming:
    def __init__(self, client: ResourceTagClient) -> None:
        def list(_: filesystem_models.ListResourceTagsResponse): ...

        self.list = core.with_streaming_response(list, client.list)


class AsyncResourceTagClient:
    """
    The API client for the ResourceTag Resource.

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

        self.with_streaming_response = _AsyncResourceTagClientStreaming(self)
        self.with_raw_response = _AsyncResourceTagClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def add(
        self,
        resource_rid: filesystem_models.ResourceRid,
        *,
        tag_rids: typing.List[filesystem_models.TagRid],
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[None]:
        """
        Apply tags to a resource.
        :param resource_rid:
        :type resource_rid: ResourceRid
        :param tag_rids:
        :type tag_rids: List[TagRid]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[None]

        :raises AddResourceTagsPermissionDenied: Could not add the ResourceTag.
        :raises ForbiddenOperationOnAutosavedResource: Performing this operation on an autosaved resource is not supported.
        :raises ForbiddenOperationOnHiddenResource: Performing this operation on a hidden resource is not supported.
        :raises ResourceNotFound: The given Resource could not be found.
        :raises TagNotFound: At least one of the provided tag RIDs could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/filesystem/resources/{resourceRid}/tags/add",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "resourceRid": resource_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                },
                body=filesystem_models.AddResourceTagsRequest(
                    tag_rids=tag_rids,
                ),
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "AddResourceTagsPermissionDenied": filesystem_errors.AddResourceTagsPermissionDenied,
                    "ForbiddenOperationOnAutosavedResource": filesystem_errors.ForbiddenOperationOnAutosavedResource,
                    "ForbiddenOperationOnHiddenResource": filesystem_errors.ForbiddenOperationOnHiddenResource,
                    "ResourceNotFound": filesystem_errors.ResourceNotFound,
                    "TagNotFound": filesystem_errors.TagNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def list(
        self,
        resource_rid: filesystem_models.ResourceRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[filesystem_models.ListResourceTagsResponse]:
        """
        List the tags applied to a resource.

        :param resource_rid:
        :type resource_rid: ResourceRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[filesystem_models.ListResourceTagsResponse]

        :raises ResourceNotFound: The given Resource could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/filesystem/resources/{resourceRid}/tags",
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
                response_type=filesystem_models.ListResourceTagsResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "ResourceNotFound": filesystem_errors.ResourceNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def remove(
        self,
        resource_rid: filesystem_models.ResourceRid,
        *,
        tag_rids: typing.List[filesystem_models.TagRid],
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[None]:
        """
        Remove tags from a resource.
        :param resource_rid:
        :type resource_rid: ResourceRid
        :param tag_rids:
        :type tag_rids: List[TagRid]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[None]

        :raises ForbiddenOperationOnAutosavedResource: Performing this operation on an autosaved resource is not supported.
        :raises ForbiddenOperationOnHiddenResource: Performing this operation on a hidden resource is not supported.
        :raises RemoveResourceTagsPermissionDenied: Could not remove the ResourceTag.
        :raises ResourceNotFound: The given Resource could not be found.
        :raises TagNotFound: At least one of the provided tag RIDs could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/filesystem/resources/{resourceRid}/tags/remove",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "resourceRid": resource_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                },
                body=filesystem_models.RemoveResourceTagsRequest(
                    tag_rids=tag_rids,
                ),
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "ForbiddenOperationOnAutosavedResource": filesystem_errors.ForbiddenOperationOnAutosavedResource,
                    "ForbiddenOperationOnHiddenResource": filesystem_errors.ForbiddenOperationOnHiddenResource,
                    "RemoveResourceTagsPermissionDenied": filesystem_errors.RemoveResourceTagsPermissionDenied,
                    "ResourceNotFound": filesystem_errors.ResourceNotFound,
                    "TagNotFound": filesystem_errors.TagNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _AsyncResourceTagClientRaw:
    def __init__(self, client: AsyncResourceTagClient) -> None:
        def add(_: None): ...
        def list(_: filesystem_models.ListResourceTagsResponse): ...
        def remove(_: None): ...

        self.add = core.async_with_raw_response(add, client.add)
        self.list = core.async_with_raw_response(list, client.list)
        self.remove = core.async_with_raw_response(remove, client.remove)


class _AsyncResourceTagClientStreaming:
    def __init__(self, client: AsyncResourceTagClient) -> None:
        def list(_: filesystem_models.ListResourceTagsResponse): ...

        self.list = core.async_with_streaming_response(list, client.list)
