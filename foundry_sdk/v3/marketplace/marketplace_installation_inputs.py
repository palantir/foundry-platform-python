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


class MarketplaceInstallationInputsClient:
    """
    The API client for the MarketplaceInstallationInputs Resource.

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

        self.with_streaming_response = _MarketplaceInstallationInputsClientStreaming(self)
        self.with_raw_response = _MarketplaceInstallationInputsClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        marketplace_installation_rid: marketplace_models.MarketplaceInstallationRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        selection: typing.Optional[marketplace_models.InstallationInputSelection] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> marketplace_models.MarketplaceInstallationInputs:
        """
        Get the current fulfilled input values and explicit unset inputs of an installation.

        By default, only manually fulfilled inputs are returned. Set `selection` to `ALL` to return fulfilled inputs
        from every stored source. Explicitly unset inputs are returned regardless of `selection`.

        Optional inputs with neither a value nor an explicit unset are omitted.

        Returned values may use a different supported representation from the value originally provided.

        Credential values expose secret names only, never plaintext, and cannot be submitted to another installation job.

        Required scopes: [api:v3:marketplace-installation-inputs:read:get]

        :param marketplace_installation_rid:
        :type marketplace_installation_rid: MarketplaceInstallationRid
        :param preview:
        :type preview: Optional[PreviewMode]
        :param selection:
        :type selection: Optional[InstallationInputSelection]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: marketplace_models.MarketplaceInstallationInputs

        :raises InstallationInputApiNamesNotEnabled: One or more installations have product inputs without API names. Enable input API name generation for those products before interacting with them.
        :raises MarketplaceInstallationNotFound:
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v3/platform/marketplaceInstallations/{marketplaceInstallationRid}/inputs",
                query_params={
                    "preview": preview,
                    "selection": selection,
                },
                path_params={
                    "marketplaceInstallationRid": marketplace_installation_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=marketplace_models.MarketplaceInstallationInputs,
                request_timeout=request_timeout,
                throwable_errors={
                    "InstallationInputApiNamesNotEnabled": marketplace_errors.InstallationInputApiNamesNotEnabled,
                    "MarketplaceInstallationNotFound": marketplace_errors.MarketplaceInstallationNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _MarketplaceInstallationInputsClientRaw:
    def __init__(self, client: MarketplaceInstallationInputsClient) -> None:
        def get(_: marketplace_models.MarketplaceInstallationInputs): ...

        self.get = core.with_raw_response(get, client.get)


class _MarketplaceInstallationInputsClientStreaming:
    def __init__(self, client: MarketplaceInstallationInputsClient) -> None:
        def get(_: marketplace_models.MarketplaceInstallationInputs): ...

        self.get = core.with_streaming_response(get, client.get)


class AsyncMarketplaceInstallationInputsClient:
    """
    The API client for the MarketplaceInstallationInputs Resource.

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

        self.with_streaming_response = _AsyncMarketplaceInstallationInputsClientStreaming(self)
        self.with_raw_response = _AsyncMarketplaceInstallationInputsClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        marketplace_installation_rid: marketplace_models.MarketplaceInstallationRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        selection: typing.Optional[marketplace_models.InstallationInputSelection] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[marketplace_models.MarketplaceInstallationInputs]:
        """
        Get the current fulfilled input values and explicit unset inputs of an installation.

        By default, only manually fulfilled inputs are returned. Set `selection` to `ALL` to return fulfilled inputs
        from every stored source. Explicitly unset inputs are returned regardless of `selection`.

        Optional inputs with neither a value nor an explicit unset are omitted.

        Returned values may use a different supported representation from the value originally provided.

        Credential values expose secret names only, never plaintext, and cannot be submitted to another installation job.

        Required scopes: [api:v3:marketplace-installation-inputs:read:get]

        :param marketplace_installation_rid:
        :type marketplace_installation_rid: MarketplaceInstallationRid
        :param preview:
        :type preview: Optional[PreviewMode]
        :param selection:
        :type selection: Optional[InstallationInputSelection]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[marketplace_models.MarketplaceInstallationInputs]

        :raises InstallationInputApiNamesNotEnabled: One or more installations have product inputs without API names. Enable input API name generation for those products before interacting with them.
        :raises MarketplaceInstallationNotFound:
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v3/platform/marketplaceInstallations/{marketplaceInstallationRid}/inputs",
                query_params={
                    "preview": preview,
                    "selection": selection,
                },
                path_params={
                    "marketplaceInstallationRid": marketplace_installation_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=marketplace_models.MarketplaceInstallationInputs,
                request_timeout=request_timeout,
                throwable_errors={
                    "InstallationInputApiNamesNotEnabled": marketplace_errors.InstallationInputApiNamesNotEnabled,
                    "MarketplaceInstallationNotFound": marketplace_errors.MarketplaceInstallationNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _AsyncMarketplaceInstallationInputsClientRaw:
    def __init__(self, client: AsyncMarketplaceInstallationInputsClient) -> None:
        def get(_: marketplace_models.MarketplaceInstallationInputs): ...

        self.get = core.async_with_raw_response(get, client.get)


class _AsyncMarketplaceInstallationInputsClientStreaming:
    def __init__(self, client: AsyncMarketplaceInstallationInputsClient) -> None:
        def get(_: marketplace_models.MarketplaceInstallationInputs): ...

        self.get = core.async_with_streaming_response(get, client.get)
