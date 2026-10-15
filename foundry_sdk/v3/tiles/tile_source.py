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
from foundry_sdk.v3.core import models as core_models
from foundry_sdk.v3.tiles import errors as tiles_errors
from foundry_sdk.v3.tiles import models as tiles_models


class TileSourceClient:
    """
    The API client for the TileSource Resource.

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

        self.with_streaming_response = _TileSourceClientStreaming(self)
        self.with_raw_response = _TileSourceClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def compute_elevation(
        self,
        tile_source_id: tiles_models.TileSourceId,
        *,
        points: typing.List[core_models.Position],
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> tiles_models.ComputeElevationResponse:
        """
        Compute ground elevation at one or more points using this tile source. Results are returned in
        the same order as the requested points. Returns a not-found error if the source does not exist
        or the token cannot access it.

        Required scopes: [api:v3:tile-source:read:compute-elevation]

        :param tile_source_id:
        :type tile_source_id: TileSourceId
        :param points: The points to compute elevation for. Results are returned in the same order as the request. A request may contain at most 1,000 points by default, though the configured limit may differ; exceeding it returns a `MaxElevationPointCountExceeded` error that reports the limit.
        :type points: List[Position]
        :param preview:
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: tiles_models.ComputeElevationResponse

        :raises MaxElevationPointCountExceeded: The request contained more points than a single elevation computation allows. Reduce the number of points, or split the points across multiple requests.
        :raises TileSourceCapabilityNotSupported: The tile source cannot compute elevation because it does not provide elevation data. Use the list operation with `capability=ELEVATION` to find sources that can.
        :raises TileSourceNotFound:
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v3/platform/tileSources/{tileSourceId}/computeElevation",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "tileSourceId": tile_source_id,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body=tiles_models.ComputeElevationRequest(
                    points=points,
                ),
                response_type=tiles_models.ComputeElevationResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "MaxElevationPointCountExceeded": tiles_errors.MaxElevationPointCountExceeded,
                    "TileSourceCapabilityNotSupported": tiles_errors.TileSourceCapabilityNotSupported,
                    "TileSourceNotFound": tiles_errors.TileSourceNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        tile_source_id: tiles_models.TileSourceId,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> tiles_models.TileSource:
        """
        Get metadata for a single tile source, including its tile sets. Returns a not-found error if
        the source does not exist or the token cannot access it.

        Required scopes: [api:v3:tile-source:read:get]

        :param tile_source_id:
        :type tile_source_id: TileSourceId
        :param preview:
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: tiles_models.TileSource

        :raises TileSourceNotFound:
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v3/platform/tileSources/{tileSourceId}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "tileSourceId": tile_source_id,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=tiles_models.TileSource,
                request_timeout=request_timeout,
                throwable_errors={
                    "TileSourceNotFound": tiles_errors.TileSourceNotFound,
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
        capability: typing.Optional[tiles_models.Capability] = None,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> core.ResourceIterator[tiles_models.TileSource]:
        """
        List the tile sources accessible by the token.

        Required scopes: [api:v3:tile-source:read:list]

        :param capability:
        :type capability: Optional[Capability]
        :param page_size:
        :type page_size: Optional[PageSize]
        :param page_token:
        :type page_token: Optional[PageToken]
        :param preview:
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ResourceIterator[tiles_models.TileSource]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v3/platform/tileSources",
                query_params={
                    "capability": capability,
                    "pageSize": page_size,
                    "pageToken": page_token,
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=tiles_models.ListTileSourcesResponse,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode", "ITERATOR"),
            ),
        )


class _TileSourceClientRaw:
    def __init__(self, client: TileSourceClient) -> None:
        def compute_elevation(_: tiles_models.ComputeElevationResponse): ...
        def get(_: tiles_models.TileSource): ...
        def list(_: tiles_models.ListTileSourcesResponse): ...

        self.compute_elevation = core.with_raw_response(compute_elevation, client.compute_elevation)
        self.get = core.with_raw_response(get, client.get)
        self.list = core.with_raw_response(list, client.list)


class _TileSourceClientStreaming:
    def __init__(self, client: TileSourceClient) -> None:
        def compute_elevation(_: tiles_models.ComputeElevationResponse): ...
        def get(_: tiles_models.TileSource): ...
        def list(_: tiles_models.ListTileSourcesResponse): ...

        self.compute_elevation = core.with_streaming_response(
            compute_elevation, client.compute_elevation
        )
        self.get = core.with_streaming_response(get, client.get)
        self.list = core.with_streaming_response(list, client.list)


class AsyncTileSourceClient:
    """
    The API client for the TileSource Resource.

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

        self.with_streaming_response = _AsyncTileSourceClientStreaming(self)
        self.with_raw_response = _AsyncTileSourceClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def compute_elevation(
        self,
        tile_source_id: tiles_models.TileSourceId,
        *,
        points: typing.List[core_models.Position],
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[tiles_models.ComputeElevationResponse]:
        """
        Compute ground elevation at one or more points using this tile source. Results are returned in
        the same order as the requested points. Returns a not-found error if the source does not exist
        or the token cannot access it.

        Required scopes: [api:v3:tile-source:read:compute-elevation]

        :param tile_source_id:
        :type tile_source_id: TileSourceId
        :param points: The points to compute elevation for. Results are returned in the same order as the request. A request may contain at most 1,000 points by default, though the configured limit may differ; exceeding it returns a `MaxElevationPointCountExceeded` error that reports the limit.
        :type points: List[Position]
        :param preview:
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[tiles_models.ComputeElevationResponse]

        :raises MaxElevationPointCountExceeded: The request contained more points than a single elevation computation allows. Reduce the number of points, or split the points across multiple requests.
        :raises TileSourceCapabilityNotSupported: The tile source cannot compute elevation because it does not provide elevation data. Use the list operation with `capability=ELEVATION` to find sources that can.
        :raises TileSourceNotFound:
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v3/platform/tileSources/{tileSourceId}/computeElevation",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "tileSourceId": tile_source_id,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body=tiles_models.ComputeElevationRequest(
                    points=points,
                ),
                response_type=tiles_models.ComputeElevationResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "MaxElevationPointCountExceeded": tiles_errors.MaxElevationPointCountExceeded,
                    "TileSourceCapabilityNotSupported": tiles_errors.TileSourceCapabilityNotSupported,
                    "TileSourceNotFound": tiles_errors.TileSourceNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        tile_source_id: tiles_models.TileSourceId,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[tiles_models.TileSource]:
        """
        Get metadata for a single tile source, including its tile sets. Returns a not-found error if
        the source does not exist or the token cannot access it.

        Required scopes: [api:v3:tile-source:read:get]

        :param tile_source_id:
        :type tile_source_id: TileSourceId
        :param preview:
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[tiles_models.TileSource]

        :raises TileSourceNotFound:
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v3/platform/tileSources/{tileSourceId}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "tileSourceId": tile_source_id,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=tiles_models.TileSource,
                request_timeout=request_timeout,
                throwable_errors={
                    "TileSourceNotFound": tiles_errors.TileSourceNotFound,
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
        capability: typing.Optional[tiles_models.Capability] = None,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> core.AsyncResourceIterator[tiles_models.TileSource]:
        """
        List the tile sources accessible by the token.

        Required scopes: [api:v3:tile-source:read:list]

        :param capability:
        :type capability: Optional[Capability]
        :param page_size:
        :type page_size: Optional[PageSize]
        :param page_token:
        :type page_token: Optional[PageToken]
        :param preview:
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.AsyncResourceIterator[tiles_models.TileSource]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v3/platform/tileSources",
                query_params={
                    "capability": capability,
                    "pageSize": page_size,
                    "pageToken": page_token,
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=tiles_models.ListTileSourcesResponse,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode", "ITERATOR"),
            ),
        )


class _AsyncTileSourceClientRaw:
    def __init__(self, client: AsyncTileSourceClient) -> None:
        def compute_elevation(_: tiles_models.ComputeElevationResponse): ...
        def get(_: tiles_models.TileSource): ...
        def list(_: tiles_models.ListTileSourcesResponse): ...

        self.compute_elevation = core.async_with_raw_response(
            compute_elevation, client.compute_elevation
        )
        self.get = core.async_with_raw_response(get, client.get)
        self.list = core.async_with_raw_response(list, client.list)


class _AsyncTileSourceClientStreaming:
    def __init__(self, client: AsyncTileSourceClient) -> None:
        def compute_elevation(_: tiles_models.ComputeElevationResponse): ...
        def get(_: tiles_models.TileSource): ...
        def list(_: tiles_models.ListTileSourcesResponse): ...

        self.compute_elevation = core.async_with_streaming_response(
            compute_elevation, client.compute_elevation
        )
        self.get = core.async_with_streaming_response(get, client.get)
        self.list = core.async_with_streaming_response(list, client.list)
