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
from foundry_sdk.v3.endpoints import errors as endpoints_errors
from foundry_sdk.v3.endpoints import models as endpoints_models


class EndpointSetEndpointClient:
    """
    The API client for the EndpointSetEndpoint Resource.

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

        self.with_streaming_response = _EndpointSetEndpointClientStreaming(self)
        self.with_raw_response = _EndpointSetEndpointClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        endpoint_set_rid: endpoints_models.EndpointSetRid,
        endpoint_rid: endpoints_models.EndpointSetEndpointRid,
        *,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> endpoints_models.EndpointSetEndpoint:
        """

        :param endpoint_set_rid:
        :type endpoint_set_rid: EndpointSetRid
        :param endpoint_rid:
        :type endpoint_rid: EndpointSetEndpointRid
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: endpoints_models.EndpointSetEndpoint

        :raises EndpointSetEndpointNotFound:
        :raises EndpointSetNotFound:
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v3/platform/endpointSets/{endpointSetRid}/endpoints/{endpointRid}",
                query_params={},
                path_params={
                    "endpointSetRid": endpoint_set_rid,
                    "endpointRid": endpoint_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=endpoints_models.EndpointSetEndpoint,
                request_timeout=request_timeout,
                throwable_errors={
                    "EndpointSetEndpointNotFound": endpoints_errors.EndpointSetEndpointNotFound,
                    "EndpointSetNotFound": endpoints_errors.EndpointSetNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def list(
        self,
        endpoint_set_rid: endpoints_models.EndpointSetRid,
        *,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> core.ResourceIterator[endpoints_models.EndpointSetEndpoint]:
        """

        :param endpoint_set_rid:
        :type endpoint_set_rid: EndpointSetRid
        :param page_size:
        :type page_size: Optional[PageSize]
        :param page_token:
        :type page_token: Optional[PageToken]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ResourceIterator[endpoints_models.EndpointSetEndpoint]

        :raises EndpointSetNotFound:
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v3/platform/endpointSets/{endpointSetRid}/endpoints",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
                },
                path_params={
                    "endpointSetRid": endpoint_set_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=endpoints_models.ListEndpointSetEndpointsResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "EndpointSetNotFound": endpoints_errors.EndpointSetNotFound,
                },
                response_mode=_sdk_internal.get("response_mode", "ITERATOR"),
            ),
        )


class _EndpointSetEndpointClientRaw:
    def __init__(self, client: EndpointSetEndpointClient) -> None:
        def get(_: endpoints_models.EndpointSetEndpoint): ...
        def list(_: endpoints_models.ListEndpointSetEndpointsResponse): ...

        self.get = core.with_raw_response(get, client.get)
        self.list = core.with_raw_response(list, client.list)


class _EndpointSetEndpointClientStreaming:
    def __init__(self, client: EndpointSetEndpointClient) -> None:
        def get(_: endpoints_models.EndpointSetEndpoint): ...
        def list(_: endpoints_models.ListEndpointSetEndpointsResponse): ...

        self.get = core.with_streaming_response(get, client.get)
        self.list = core.with_streaming_response(list, client.list)


class AsyncEndpointSetEndpointClient:
    """
    The API client for the EndpointSetEndpoint Resource.

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

        self.with_streaming_response = _AsyncEndpointSetEndpointClientStreaming(self)
        self.with_raw_response = _AsyncEndpointSetEndpointClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        endpoint_set_rid: endpoints_models.EndpointSetRid,
        endpoint_rid: endpoints_models.EndpointSetEndpointRid,
        *,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[endpoints_models.EndpointSetEndpoint]:
        """

        :param endpoint_set_rid:
        :type endpoint_set_rid: EndpointSetRid
        :param endpoint_rid:
        :type endpoint_rid: EndpointSetEndpointRid
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[endpoints_models.EndpointSetEndpoint]

        :raises EndpointSetEndpointNotFound:
        :raises EndpointSetNotFound:
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v3/platform/endpointSets/{endpointSetRid}/endpoints/{endpointRid}",
                query_params={},
                path_params={
                    "endpointSetRid": endpoint_set_rid,
                    "endpointRid": endpoint_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=endpoints_models.EndpointSetEndpoint,
                request_timeout=request_timeout,
                throwable_errors={
                    "EndpointSetEndpointNotFound": endpoints_errors.EndpointSetEndpointNotFound,
                    "EndpointSetNotFound": endpoints_errors.EndpointSetNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def list(
        self,
        endpoint_set_rid: endpoints_models.EndpointSetRid,
        *,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> core.AsyncResourceIterator[endpoints_models.EndpointSetEndpoint]:
        """

        :param endpoint_set_rid:
        :type endpoint_set_rid: EndpointSetRid
        :param page_size:
        :type page_size: Optional[PageSize]
        :param page_token:
        :type page_token: Optional[PageToken]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.AsyncResourceIterator[endpoints_models.EndpointSetEndpoint]

        :raises EndpointSetNotFound:
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v3/platform/endpointSets/{endpointSetRid}/endpoints",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
                },
                path_params={
                    "endpointSetRid": endpoint_set_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=endpoints_models.ListEndpointSetEndpointsResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "EndpointSetNotFound": endpoints_errors.EndpointSetNotFound,
                },
                response_mode=_sdk_internal.get("response_mode", "ITERATOR"),
            ),
        )


class _AsyncEndpointSetEndpointClientRaw:
    def __init__(self, client: AsyncEndpointSetEndpointClient) -> None:
        def get(_: endpoints_models.EndpointSetEndpoint): ...
        def list(_: endpoints_models.ListEndpointSetEndpointsResponse): ...

        self.get = core.async_with_raw_response(get, client.get)
        self.list = core.async_with_raw_response(list, client.list)


class _AsyncEndpointSetEndpointClientStreaming:
    def __init__(self, client: AsyncEndpointSetEndpointClient) -> None:
        def get(_: endpoints_models.EndpointSetEndpoint): ...
        def list(_: endpoints_models.ListEndpointSetEndpointsResponse): ...

        self.get = core.async_with_streaming_response(get, client.get)
        self.list = core.async_with_streaming_response(list, client.list)
