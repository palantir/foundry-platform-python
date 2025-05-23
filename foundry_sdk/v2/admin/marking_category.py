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
from foundry_sdk.v2.admin import errors as admin_errors
from foundry_sdk.v2.admin import models as admin_models
from foundry_sdk.v2.core import errors as core_errors
from foundry_sdk.v2.core import models as core_models


class MarkingCategoryClient:
    """
    The API client for the MarkingCategory Resource.

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

        self.with_streaming_response = _MarkingCategoryClientStreaming(self)
        self.with_raw_response = _MarkingCategoryClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        marking_category_id: admin_models.MarkingCategoryId,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> admin_models.MarkingCategory:
        """
        Get the MarkingCategory with the specified id.
        :param marking_category_id:
        :type marking_category_id: MarkingCategoryId
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: admin_models.MarkingCategory

        :raises GetMarkingCategoryPermissionDenied: The provided token does not have permission to view the marking category.
        :raises MarkingCategoryNotFound: The given MarkingCategory could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/admin/markingCategories/{markingCategoryId}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "markingCategoryId": marking_category_id,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=admin_models.MarkingCategory,
                request_timeout=request_timeout,
                throwable_errors={
                    "GetMarkingCategoryPermissionDenied": admin_errors.GetMarkingCategoryPermissionDenied,
                    "MarkingCategoryNotFound": admin_errors.MarkingCategoryNotFound,
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
    ) -> core.ResourceIterator[admin_models.MarkingCategory]:
        """
        Maximum page size 100.
        :param page_size: The page size to use for the endpoint.
        :type page_size: Optional[PageSize]
        :param page_token: The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
        :type page_token: Optional[PageToken]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ResourceIterator[admin_models.MarkingCategory]

        :raises InvalidPageSize: The provided page size was zero or negative. Page sizes must be greater than zero.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/admin/markingCategories",
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
                body_type=None,
                response_type=admin_models.ListMarkingCategoriesResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "InvalidPageSize": core_errors.InvalidPageSize,
                },
                response_mode=_sdk_internal.get("response_mode", "ITERATOR"),
            ),
        )


class _MarkingCategoryClientRaw:
    def __init__(self, client: MarkingCategoryClient) -> None:
        def get(_: admin_models.MarkingCategory): ...
        def list(_: admin_models.ListMarkingCategoriesResponse): ...

        self.get = core.with_raw_response(get, client.get)
        self.list = core.with_raw_response(list, client.list)


class _MarkingCategoryClientStreaming:
    def __init__(self, client: MarkingCategoryClient) -> None:
        def get(_: admin_models.MarkingCategory): ...
        def list(_: admin_models.ListMarkingCategoriesResponse): ...

        self.get = core.with_streaming_response(get, client.get)
        self.list = core.with_streaming_response(list, client.list)


class AsyncMarkingCategoryClient:
    """
    The API client for the MarkingCategory Resource.

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

        self.with_streaming_response = _AsyncMarkingCategoryClientStreaming(self)
        self.with_raw_response = _AsyncMarkingCategoryClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        marking_category_id: admin_models.MarkingCategoryId,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[admin_models.MarkingCategory]:
        """
        Get the MarkingCategory with the specified id.
        :param marking_category_id:
        :type marking_category_id: MarkingCategoryId
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[admin_models.MarkingCategory]

        :raises GetMarkingCategoryPermissionDenied: The provided token does not have permission to view the marking category.
        :raises MarkingCategoryNotFound: The given MarkingCategory could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/admin/markingCategories/{markingCategoryId}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "markingCategoryId": marking_category_id,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=admin_models.MarkingCategory,
                request_timeout=request_timeout,
                throwable_errors={
                    "GetMarkingCategoryPermissionDenied": admin_errors.GetMarkingCategoryPermissionDenied,
                    "MarkingCategoryNotFound": admin_errors.MarkingCategoryNotFound,
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
    ) -> core.AsyncResourceIterator[admin_models.MarkingCategory]:
        """
        Maximum page size 100.
        :param page_size: The page size to use for the endpoint.
        :type page_size: Optional[PageSize]
        :param page_token: The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
        :type page_token: Optional[PageToken]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.AsyncResourceIterator[admin_models.MarkingCategory]

        :raises InvalidPageSize: The provided page size was zero or negative. Page sizes must be greater than zero.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/admin/markingCategories",
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
                body_type=None,
                response_type=admin_models.ListMarkingCategoriesResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "InvalidPageSize": core_errors.InvalidPageSize,
                },
                response_mode=_sdk_internal.get("response_mode", "ITERATOR"),
            ),
        )


class _AsyncMarkingCategoryClientRaw:
    def __init__(self, client: AsyncMarkingCategoryClient) -> None:
        def get(_: admin_models.MarkingCategory): ...
        def list(_: admin_models.ListMarkingCategoriesResponse): ...

        self.get = core.async_with_raw_response(get, client.get)
        self.list = core.async_with_raw_response(list, client.list)


class _AsyncMarkingCategoryClientStreaming:
    def __init__(self, client: AsyncMarkingCategoryClient) -> None:
        def get(_: admin_models.MarkingCategory): ...
        def list(_: admin_models.ListMarkingCategoriesResponse): ...

        self.get = core.async_with_streaming_response(get, client.get)
        self.list = core.async_with_streaming_response(list, client.list)
