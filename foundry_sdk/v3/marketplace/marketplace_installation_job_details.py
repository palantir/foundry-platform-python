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


class MarketplaceInstallationJobDetailsClient:
    """
    The API client for the MarketplaceInstallationJobDetails Resource.

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

        self.with_streaming_response = _MarketplaceInstallationJobDetailsClientStreaming(self)
        self.with_raw_response = _MarketplaceInstallationJobDetailsClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        marketplace_installation_job_rid: marketplace_models.MarketplaceInstallationJobRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> marketplace_models.MarketplaceInstallationJobDetails:
        """
        Get available validation results and failure diagnostics for an installation job or draft. Use the
        installation job's `status` to track its progress and outcome. These details can help explain why a draft or
        job has not progressed or completed as expected.

        Draft owners receive full validation errors. Other authorized viewers receive a validation summary instead.
        Failed and aborted jobs return HTTP 200 with their available diagnostics. An explicit abort or a
        validation-only submission rejection may have no failure diagnostics.
        The job remains queryable under the same RID after its draft is submitted, subject to retention and access.

        Required scopes: [api:v3:marketplace-installation-job-details:read:get]

        :param marketplace_installation_job_rid:
        :type marketplace_installation_job_rid: MarketplaceInstallationJobRid
        :param preview:
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: marketplace_models.MarketplaceInstallationJobDetails

        :raises InstallationInputApiNamesNotEnabled: One or more installations have product inputs without API names. Enable input API name generation for those products before interacting with them.
        :raises MarketplaceInstallationJobNotFound:
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v3/platform/marketplaceInstallationJobs/{marketplaceInstallationJobRid}/details",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "marketplaceInstallationJobRid": marketplace_installation_job_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=marketplace_models.MarketplaceInstallationJobDetails,
                request_timeout=request_timeout,
                throwable_errors={
                    "InstallationInputApiNamesNotEnabled": marketplace_errors.InstallationInputApiNamesNotEnabled,
                    "MarketplaceInstallationJobNotFound": marketplace_errors.MarketplaceInstallationJobNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _MarketplaceInstallationJobDetailsClientRaw:
    def __init__(self, client: MarketplaceInstallationJobDetailsClient) -> None:
        def get(_: marketplace_models.MarketplaceInstallationJobDetails): ...

        self.get = core.with_raw_response(get, client.get)


class _MarketplaceInstallationJobDetailsClientStreaming:
    def __init__(self, client: MarketplaceInstallationJobDetailsClient) -> None:
        def get(_: marketplace_models.MarketplaceInstallationJobDetails): ...

        self.get = core.with_streaming_response(get, client.get)


class AsyncMarketplaceInstallationJobDetailsClient:
    """
    The API client for the MarketplaceInstallationJobDetails Resource.

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

        self.with_streaming_response = _AsyncMarketplaceInstallationJobDetailsClientStreaming(self)
        self.with_raw_response = _AsyncMarketplaceInstallationJobDetailsClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        marketplace_installation_job_rid: marketplace_models.MarketplaceInstallationJobRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[marketplace_models.MarketplaceInstallationJobDetails]:
        """
        Get available validation results and failure diagnostics for an installation job or draft. Use the
        installation job's `status` to track its progress and outcome. These details can help explain why a draft or
        job has not progressed or completed as expected.

        Draft owners receive full validation errors. Other authorized viewers receive a validation summary instead.
        Failed and aborted jobs return HTTP 200 with their available diagnostics. An explicit abort or a
        validation-only submission rejection may have no failure diagnostics.
        The job remains queryable under the same RID after its draft is submitted, subject to retention and access.

        Required scopes: [api:v3:marketplace-installation-job-details:read:get]

        :param marketplace_installation_job_rid:
        :type marketplace_installation_job_rid: MarketplaceInstallationJobRid
        :param preview:
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[marketplace_models.MarketplaceInstallationJobDetails]

        :raises InstallationInputApiNamesNotEnabled: One or more installations have product inputs without API names. Enable input API name generation for those products before interacting with them.
        :raises MarketplaceInstallationJobNotFound:
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v3/platform/marketplaceInstallationJobs/{marketplaceInstallationJobRid}/details",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "marketplaceInstallationJobRid": marketplace_installation_job_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=marketplace_models.MarketplaceInstallationJobDetails,
                request_timeout=request_timeout,
                throwable_errors={
                    "InstallationInputApiNamesNotEnabled": marketplace_errors.InstallationInputApiNamesNotEnabled,
                    "MarketplaceInstallationJobNotFound": marketplace_errors.MarketplaceInstallationJobNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _AsyncMarketplaceInstallationJobDetailsClientRaw:
    def __init__(self, client: AsyncMarketplaceInstallationJobDetailsClient) -> None:
        def get(_: marketplace_models.MarketplaceInstallationJobDetails): ...

        self.get = core.async_with_raw_response(get, client.get)


class _AsyncMarketplaceInstallationJobDetailsClientStreaming:
    def __init__(self, client: AsyncMarketplaceInstallationJobDetailsClient) -> None:
        def get(_: marketplace_models.MarketplaceInstallationJobDetails): ...

        self.get = core.async_with_streaming_response(get, client.get)
