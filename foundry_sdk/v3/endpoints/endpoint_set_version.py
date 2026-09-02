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


class EndpointSetVersionClient:
    """
    The API client for the EndpointSetVersion Resource.

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

        self.with_streaming_response = _EndpointSetVersionClientStreaming(self)
        self.with_raw_response = _EndpointSetVersionClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        endpoint_set_rid: endpoints_models.EndpointSetRid,
        version_id: endpoints_models.EndpointSetVersionId,
        *,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> endpoints_models.EndpointSetVersion:
        """

        :param endpoint_set_rid:
        :type endpoint_set_rid: EndpointSetRid
        :param version_id:
        :type version_id: EndpointSetVersionId
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: endpoints_models.EndpointSetVersion

        :raises EndpointSetNotFound:
        :raises EndpointSetVersionNotFound:
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v3/platform/endpointSets/{endpointSetRid}/versions/{versionId}",
                query_params={},
                path_params={
                    "endpointSetRid": endpoint_set_rid,
                    "versionId": version_id,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=endpoints_models.EndpointSetVersion,
                request_timeout=request_timeout,
                throwable_errors={
                    "EndpointSetNotFound": endpoints_errors.EndpointSetNotFound,
                    "EndpointSetVersionNotFound": endpoints_errors.EndpointSetVersionNotFound,
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
    ) -> core.ResourceIterator[endpoints_models.EndpointSetVersion]:
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
        :rtype: core.ResourceIterator[endpoints_models.EndpointSetVersion]

        :raises EndpointSetNotFound:
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v3/platform/endpointSets/{endpointSetRid}/versions",
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
                response_type=endpoints_models.ListEndpointSetVersionsResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "EndpointSetNotFound": endpoints_errors.EndpointSetNotFound,
                },
                response_mode=_sdk_internal.get("response_mode", "ITERATOR"),
            ),
        )


class _EndpointSetVersionClientRaw:
    def __init__(self, client: EndpointSetVersionClient) -> None:
        def get(_: endpoints_models.EndpointSetVersion): ...
        def list(_: endpoints_models.ListEndpointSetVersionsResponse): ...

        self.get = core.with_raw_response(get, client.get)
        self.list = core.with_raw_response(list, client.list)


class _EndpointSetVersionClientStreaming:
    def __init__(self, client: EndpointSetVersionClient) -> None:
        def get(_: endpoints_models.EndpointSetVersion): ...
        def list(_: endpoints_models.ListEndpointSetVersionsResponse): ...

        self.get = core.with_streaming_response(get, client.get)
        self.list = core.with_streaming_response(list, client.list)


class AsyncEndpointSetVersionClient:
    """
    The API client for the EndpointSetVersion Resource.

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

        self.with_streaming_response = _AsyncEndpointSetVersionClientStreaming(self)
        self.with_raw_response = _AsyncEndpointSetVersionClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        endpoint_set_rid: endpoints_models.EndpointSetRid,
        version_id: endpoints_models.EndpointSetVersionId,
        *,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[endpoints_models.EndpointSetVersion]:
        """

        :param endpoint_set_rid:
        :type endpoint_set_rid: EndpointSetRid
        :param version_id:
        :type version_id: EndpointSetVersionId
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[endpoints_models.EndpointSetVersion]

        :raises EndpointSetNotFound:
        :raises EndpointSetVersionNotFound:
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v3/platform/endpointSets/{endpointSetRid}/versions/{versionId}",
                query_params={},
                path_params={
                    "endpointSetRid": endpoint_set_rid,
                    "versionId": version_id,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=endpoints_models.EndpointSetVersion,
                request_timeout=request_timeout,
                throwable_errors={
                    "EndpointSetNotFound": endpoints_errors.EndpointSetNotFound,
                    "EndpointSetVersionNotFound": endpoints_errors.EndpointSetVersionNotFound,
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
    ) -> core.AsyncResourceIterator[endpoints_models.EndpointSetVersion]:
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
        :rtype: core.AsyncResourceIterator[endpoints_models.EndpointSetVersion]

        :raises EndpointSetNotFound:
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v3/platform/endpointSets/{endpointSetRid}/versions",
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
                response_type=endpoints_models.ListEndpointSetVersionsResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "EndpointSetNotFound": endpoints_errors.EndpointSetNotFound,
                },
                response_mode=_sdk_internal.get("response_mode", "ITERATOR"),
            ),
        )


class _AsyncEndpointSetVersionClientRaw:
    def __init__(self, client: AsyncEndpointSetVersionClient) -> None:
        def get(_: endpoints_models.EndpointSetVersion): ...
        def list(_: endpoints_models.ListEndpointSetVersionsResponse): ...

        self.get = core.async_with_raw_response(get, client.get)
        self.list = core.async_with_raw_response(list, client.list)


class _AsyncEndpointSetVersionClientStreaming:
    def __init__(self, client: AsyncEndpointSetVersionClient) -> None:
        def get(_: endpoints_models.EndpointSetVersion): ...
        def list(_: endpoints_models.ListEndpointSetVersionsResponse): ...

        self.get = core.async_with_streaming_response(get, client.get)
        self.list = core.async_with_streaming_response(list, client.list)
