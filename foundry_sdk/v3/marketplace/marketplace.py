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
from foundry_sdk.v3.marketplace import errors as marketplace_errors
from foundry_sdk.v3.marketplace import models as marketplace_models


class MarketplaceClient:
    """
    The API client for the Marketplace Resource.

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

        self.with_streaming_response = _MarketplaceClientStreaming(self)
        self.with_raw_response = _MarketplaceClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        marketplace_rid: marketplace_models.MarketplaceRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> marketplace_models.Marketplace:
        """
        Get a local or remote Marketplace store by its RID, including its current display metadata.

        Required scopes: [api:v3:marketplace:read:get]

        :param marketplace_rid:
        :type marketplace_rid: MarketplaceRid
        :param preview:
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: marketplace_models.Marketplace

        :raises MarketplaceNotFound:
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v3/platform/marketplaces/{marketplaceRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "marketplaceRid": marketplace_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=marketplace_models.Marketplace,
                request_timeout=request_timeout,
                throwable_errors={
                    "MarketplaceNotFound": marketplace_errors.MarketplaceNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _MarketplaceClientRaw:
    def __init__(self, client: MarketplaceClient) -> None:
        def get(_: marketplace_models.Marketplace): ...

        self.get = core.with_raw_response(get, client.get)


class _MarketplaceClientStreaming:
    def __init__(self, client: MarketplaceClient) -> None:
        def get(_: marketplace_models.Marketplace): ...

        self.get = core.with_streaming_response(get, client.get)


class AsyncMarketplaceClient:
    """
    The API client for the Marketplace Resource.

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

        self.with_streaming_response = _AsyncMarketplaceClientStreaming(self)
        self.with_raw_response = _AsyncMarketplaceClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        marketplace_rid: marketplace_models.MarketplaceRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[marketplace_models.Marketplace]:
        """
        Get a local or remote Marketplace store by its RID, including its current display metadata.

        Required scopes: [api:v3:marketplace:read:get]

        :param marketplace_rid:
        :type marketplace_rid: MarketplaceRid
        :param preview:
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[marketplace_models.Marketplace]

        :raises MarketplaceNotFound:
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v3/platform/marketplaces/{marketplaceRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "marketplaceRid": marketplace_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=marketplace_models.Marketplace,
                request_timeout=request_timeout,
                throwable_errors={
                    "MarketplaceNotFound": marketplace_errors.MarketplaceNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _AsyncMarketplaceClientRaw:
    def __init__(self, client: AsyncMarketplaceClient) -> None:
        def get(_: marketplace_models.Marketplace): ...

        self.get = core.async_with_raw_response(get, client.get)


class _AsyncMarketplaceClientStreaming:
    def __init__(self, client: AsyncMarketplaceClient) -> None:
        def get(_: marketplace_models.Marketplace): ...

        self.get = core.async_with_streaming_response(get, client.get)
