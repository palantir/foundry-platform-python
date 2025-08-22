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
from foundry_sdk.v2.widgets import errors as widgets_errors
from foundry_sdk.v2.widgets import models as widgets_models


class ReleaseClient:
    """
    The API client for the Release Resource.

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

        self.with_streaming_response = _ReleaseClientStreaming(self)
        self.with_raw_response = _ReleaseClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def delete(
        self,
        widget_set_rid: widgets_models.WidgetSetRid,
        release_version: widgets_models.ReleaseVersion,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> None:
        """
        Delete the Release with the specified version.
        :param widget_set_rid: A Resource Identifier (RID) identifying a widget set.
        :type widget_set_rid: WidgetSetRid
        :param release_version: The semantic version of the widget set.
        :type release_version: ReleaseVersion
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: None

        :raises DeleteReleasePermissionDenied: Could not delete the Release.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="DELETE",
                resource_path="/v2/widgets/widgetSets/{widgetSetRid}/releases/{releaseVersion}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "widgetSetRid": widget_set_rid,
                    "releaseVersion": release_version,
                },
                header_params={},
                body=None,
                body_type=None,
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "DeleteReleasePermissionDenied": widgets_errors.DeleteReleasePermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        widget_set_rid: widgets_models.WidgetSetRid,
        release_version: widgets_models.ReleaseVersion,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> widgets_models.Release:
        """
        Get the Release with the specified version.
        :param widget_set_rid: A Resource Identifier (RID) identifying a widget set.
        :type widget_set_rid: WidgetSetRid
        :param release_version: The semantic version of the widget set.
        :type release_version: ReleaseVersion
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: widgets_models.Release

        :raises ReleaseNotFound: The given Release could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/widgets/widgetSets/{widgetSetRid}/releases/{releaseVersion}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "widgetSetRid": widget_set_rid,
                    "releaseVersion": release_version,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=widgets_models.Release,
                request_timeout=request_timeout,
                throwable_errors={
                    "ReleaseNotFound": widgets_errors.ReleaseNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def list(
        self,
        widget_set_rid: widgets_models.WidgetSetRid,
        *,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> core.ResourceIterator[widgets_models.Release]:
        """
        Lists all Releases.

        This is a paged endpoint. Each page may be smaller or larger than the requested page size. However, it is guaranteed that if there are more results available, the `nextPageToken` field will be populated. To get the next page, make the same request again, but set the value of the `pageToken` query parameter to be value of the `nextPageToken` value of the previous response. If there is no `nextPageToken` field in the response, you are on the last page.
        :param widget_set_rid: A Resource Identifier (RID) identifying a widget set.
        :type widget_set_rid: WidgetSetRid
        :param page_size: The page size to use for the endpoint.
        :type page_size: Optional[PageSize]
        :param page_token: The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
        :type page_token: Optional[PageToken]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ResourceIterator[widgets_models.Release]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/widgets/widgetSets/{widgetSetRid}/releases",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
                    "preview": preview,
                },
                path_params={
                    "widgetSetRid": widget_set_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=widgets_models.ListReleasesResponse,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode", "ITERATOR"),
            ),
        )


class _ReleaseClientRaw:
    def __init__(self, client: ReleaseClient) -> None:
        def delete(_: None): ...
        def get(_: widgets_models.Release): ...
        def list(_: widgets_models.ListReleasesResponse): ...

        self.delete = core.with_raw_response(delete, client.delete)
        self.get = core.with_raw_response(get, client.get)
        self.list = core.with_raw_response(list, client.list)


class _ReleaseClientStreaming:
    def __init__(self, client: ReleaseClient) -> None:
        def get(_: widgets_models.Release): ...
        def list(_: widgets_models.ListReleasesResponse): ...

        self.get = core.with_streaming_response(get, client.get)
        self.list = core.with_streaming_response(list, client.list)


class AsyncReleaseClient:
    """
    The API client for the Release Resource.

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

        self.with_streaming_response = _AsyncReleaseClientStreaming(self)
        self.with_raw_response = _AsyncReleaseClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def delete(
        self,
        widget_set_rid: widgets_models.WidgetSetRid,
        release_version: widgets_models.ReleaseVersion,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[None]:
        """
        Delete the Release with the specified version.
        :param widget_set_rid: A Resource Identifier (RID) identifying a widget set.
        :type widget_set_rid: WidgetSetRid
        :param release_version: The semantic version of the widget set.
        :type release_version: ReleaseVersion
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[None]

        :raises DeleteReleasePermissionDenied: Could not delete the Release.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="DELETE",
                resource_path="/v2/widgets/widgetSets/{widgetSetRid}/releases/{releaseVersion}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "widgetSetRid": widget_set_rid,
                    "releaseVersion": release_version,
                },
                header_params={},
                body=None,
                body_type=None,
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "DeleteReleasePermissionDenied": widgets_errors.DeleteReleasePermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        widget_set_rid: widgets_models.WidgetSetRid,
        release_version: widgets_models.ReleaseVersion,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[widgets_models.Release]:
        """
        Get the Release with the specified version.
        :param widget_set_rid: A Resource Identifier (RID) identifying a widget set.
        :type widget_set_rid: WidgetSetRid
        :param release_version: The semantic version of the widget set.
        :type release_version: ReleaseVersion
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[widgets_models.Release]

        :raises ReleaseNotFound: The given Release could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/widgets/widgetSets/{widgetSetRid}/releases/{releaseVersion}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "widgetSetRid": widget_set_rid,
                    "releaseVersion": release_version,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=widgets_models.Release,
                request_timeout=request_timeout,
                throwable_errors={
                    "ReleaseNotFound": widgets_errors.ReleaseNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def list(
        self,
        widget_set_rid: widgets_models.WidgetSetRid,
        *,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> core.AsyncResourceIterator[widgets_models.Release]:
        """
        Lists all Releases.

        This is a paged endpoint. Each page may be smaller or larger than the requested page size. However, it is guaranteed that if there are more results available, the `nextPageToken` field will be populated. To get the next page, make the same request again, but set the value of the `pageToken` query parameter to be value of the `nextPageToken` value of the previous response. If there is no `nextPageToken` field in the response, you are on the last page.
        :param widget_set_rid: A Resource Identifier (RID) identifying a widget set.
        :type widget_set_rid: WidgetSetRid
        :param page_size: The page size to use for the endpoint.
        :type page_size: Optional[PageSize]
        :param page_token: The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
        :type page_token: Optional[PageToken]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.AsyncResourceIterator[widgets_models.Release]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/widgets/widgetSets/{widgetSetRid}/releases",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
                    "preview": preview,
                },
                path_params={
                    "widgetSetRid": widget_set_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=widgets_models.ListReleasesResponse,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode", "ITERATOR"),
            ),
        )


class _AsyncReleaseClientRaw:
    def __init__(self, client: AsyncReleaseClient) -> None:
        def delete(_: None): ...
        def get(_: widgets_models.Release): ...
        def list(_: widgets_models.ListReleasesResponse): ...

        self.delete = core.async_with_raw_response(delete, client.delete)
        self.get = core.async_with_raw_response(get, client.get)
        self.list = core.async_with_raw_response(list, client.list)


class _AsyncReleaseClientStreaming:
    def __init__(self, client: AsyncReleaseClient) -> None:
        def get(_: widgets_models.Release): ...
        def list(_: widgets_models.ListReleasesResponse): ...

        self.get = core.async_with_streaming_response(get, client.get)
        self.list = core.async_with_streaming_response(list, client.list)
