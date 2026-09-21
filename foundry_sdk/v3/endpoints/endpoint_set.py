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
from functools import cached_property

import pydantic
import typing_extensions

from foundry_sdk import _core as core
from foundry_sdk import _errors as errors
from foundry_sdk.v3.endpoints import errors as endpoints_errors
from foundry_sdk.v3.endpoints import models as endpoints_models


class EndpointSetClient:
    """
    The API client for the EndpointSet Resource.

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

        self.with_streaming_response = _EndpointSetClientStreaming(self)
        self.with_raw_response = _EndpointSetClientRaw(self)

    @cached_property
    def Endpoint(self):
        from foundry_sdk.v3.endpoints.endpoint_set_endpoint import (
            EndpointSetEndpointClient,
        )

        return EndpointSetEndpointClient(
            auth=self._auth,
            hostname=self._hostname_supplier,
            config=self._config,
        )

    @cached_property
    def Version(self):
        from foundry_sdk.v3.endpoints.endpoint_set_version import (
            EndpointSetVersionClient,
        )

        return EndpointSetVersionClient(
            auth=self._auth,
            hostname=self._hostname_supplier,
            config=self._config,
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        endpoint_set_rid: endpoints_models.EndpointSetRid,
        *,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> endpoints_models.EndpointSet:
        """

        :param endpoint_set_rid:
        :type endpoint_set_rid: EndpointSetRid
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: endpoints_models.EndpointSet

        :raises EndpointSetNotFound:
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v3/platform/endpointSets/{endpointSetRid}",
                query_params={},
                path_params={
                    "endpointSetRid": endpoint_set_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=endpoints_models.EndpointSet,
                request_timeout=request_timeout,
                throwable_errors={
                    "EndpointSetNotFound": endpoints_errors.EndpointSetNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _EndpointSetClientRaw:
    def __init__(self, client: EndpointSetClient) -> None:
        def get(_: endpoints_models.EndpointSet): ...

        self.get = core.with_raw_response(get, client.get)


class _EndpointSetClientStreaming:
    def __init__(self, client: EndpointSetClient) -> None:
        def get(_: endpoints_models.EndpointSet): ...

        self.get = core.with_streaming_response(get, client.get)


class AsyncEndpointSetClient:
    """
    The API client for the EndpointSet Resource.

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

        self.with_streaming_response = _AsyncEndpointSetClientStreaming(self)
        self.with_raw_response = _AsyncEndpointSetClientRaw(self)

    @cached_property
    def Endpoint(self):
        from foundry_sdk.v3.endpoints.endpoint_set_endpoint import (
            AsyncEndpointSetEndpointClient,
        )

        return AsyncEndpointSetEndpointClient(
            auth=self._auth,
            hostname=self._hostname_supplier,
            config=self._config,
        )

    @cached_property
    def Version(self):
        from foundry_sdk.v3.endpoints.endpoint_set_version import (
            AsyncEndpointSetVersionClient,
        )

        return AsyncEndpointSetVersionClient(
            auth=self._auth,
            hostname=self._hostname_supplier,
            config=self._config,
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        endpoint_set_rid: endpoints_models.EndpointSetRid,
        *,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[endpoints_models.EndpointSet]:
        """

        :param endpoint_set_rid:
        :type endpoint_set_rid: EndpointSetRid
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[endpoints_models.EndpointSet]

        :raises EndpointSetNotFound:
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v3/platform/endpointSets/{endpointSetRid}",
                query_params={},
                path_params={
                    "endpointSetRid": endpoint_set_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=endpoints_models.EndpointSet,
                request_timeout=request_timeout,
                throwable_errors={
                    "EndpointSetNotFound": endpoints_errors.EndpointSetNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _AsyncEndpointSetClientRaw:
    def __init__(self, client: AsyncEndpointSetClient) -> None:
        def get(_: endpoints_models.EndpointSet): ...

        self.get = core.async_with_raw_response(get, client.get)


class _AsyncEndpointSetClientStreaming:
    def __init__(self, client: AsyncEndpointSetClient) -> None:
        def get(_: endpoints_models.EndpointSet): ...

        self.get = core.async_with_streaming_response(get, client.get)
