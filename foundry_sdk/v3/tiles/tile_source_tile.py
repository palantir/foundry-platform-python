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


class TileSourceTileClient:
    """
    The API client for the TileSourceTile Resource.

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

        self.with_streaming_response = _TileSourceTileClientStreaming(self)
        self.with_raw_response = _TileSourceTileClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        tile_source_id: tiles_models.TileSourceId,
        z: int,
        x: int,
        y: int,
        *,
        format: typing.Optional[tiles_models.TileFormat] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        tiling_scheme: typing.Optional[tiles_models.TilingScheme] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> bytes:
        """
        Get a tile from a tile source.

        Required scopes: [api:v3:tile-source-tile:read:get]

        :param tile_source_id:
        :type tile_source_id: TileSourceId
        :param z:
        :type z: int
        :param x:
        :type x: int
        :param y:
        :type y: int
        :param format:
        :type format: Optional[TileFormat]
        :param preview:
        :type preview: Optional[PreviewMode]
        :param tiling_scheme:
        :type tiling_scheme: Optional[TilingScheme]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: bytes

        :raises TileSourceNotFound:
        :raises TileSourceTileNotFound:
        :raises TileSourceTileSetNotSupported: The tile source does not provide a tile set matching the requested format and tiling scheme. Use the tile source's `tileSets` metadata to select a supported combination.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v3/media/tileSources/{tileSourceId}/tiles/{z}/{x}/{y}",
                query_params={
                    "format": format,
                    "preview": preview,
                    "tilingScheme": tiling_scheme,
                },
                path_params={
                    "tileSourceId": tile_source_id,
                    "z": z,
                    "x": x,
                    "y": y,
                },
                header_params={
                    "Accept": "application/octet-stream",
                },
                body=None,
                response_type=bytes,
                request_timeout=request_timeout,
                throwable_errors={
                    "TileSourceNotFound": tiles_errors.TileSourceNotFound,
                    "TileSourceTileNotFound": tiles_errors.TileSourceTileNotFound,
                    "TileSourceTileSetNotSupported": tiles_errors.TileSourceTileSetNotSupported,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _TileSourceTileClientRaw:
    def __init__(self, client: TileSourceTileClient) -> None:
        def get(_: bytes): ...

        self.get = core.with_raw_response(get, client.get)


class _TileSourceTileClientStreaming:
    def __init__(self, client: TileSourceTileClient) -> None:
        def get(_: bytes): ...

        self.get = core.with_streaming_response(get, client.get)


class AsyncTileSourceTileClient:
    """
    The API client for the TileSourceTile Resource.

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

        self.with_streaming_response = _AsyncTileSourceTileClientStreaming(self)
        self.with_raw_response = _AsyncTileSourceTileClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        tile_source_id: tiles_models.TileSourceId,
        z: int,
        x: int,
        y: int,
        *,
        format: typing.Optional[tiles_models.TileFormat] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        tiling_scheme: typing.Optional[tiles_models.TilingScheme] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[bytes]:
        """
        Get a tile from a tile source.

        Required scopes: [api:v3:tile-source-tile:read:get]

        :param tile_source_id:
        :type tile_source_id: TileSourceId
        :param z:
        :type z: int
        :param x:
        :type x: int
        :param y:
        :type y: int
        :param format:
        :type format: Optional[TileFormat]
        :param preview:
        :type preview: Optional[PreviewMode]
        :param tiling_scheme:
        :type tiling_scheme: Optional[TilingScheme]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[bytes]

        :raises TileSourceNotFound:
        :raises TileSourceTileNotFound:
        :raises TileSourceTileSetNotSupported: The tile source does not provide a tile set matching the requested format and tiling scheme. Use the tile source's `tileSets` metadata to select a supported combination.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v3/media/tileSources/{tileSourceId}/tiles/{z}/{x}/{y}",
                query_params={
                    "format": format,
                    "preview": preview,
                    "tilingScheme": tiling_scheme,
                },
                path_params={
                    "tileSourceId": tile_source_id,
                    "z": z,
                    "x": x,
                    "y": y,
                },
                header_params={
                    "Accept": "application/octet-stream",
                },
                body=None,
                response_type=bytes,
                request_timeout=request_timeout,
                throwable_errors={
                    "TileSourceNotFound": tiles_errors.TileSourceNotFound,
                    "TileSourceTileNotFound": tiles_errors.TileSourceTileNotFound,
                    "TileSourceTileSetNotSupported": tiles_errors.TileSourceTileSetNotSupported,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _AsyncTileSourceTileClientRaw:
    def __init__(self, client: AsyncTileSourceTileClient) -> None:
        def get(_: bytes): ...

        self.get = core.async_with_raw_response(get, client.get)


class _AsyncTileSourceTileClientStreaming:
    def __init__(self, client: AsyncTileSourceTileClient) -> None:
        def get(_: bytes): ...

        self.get = core.async_with_streaming_response(get, client.get)
