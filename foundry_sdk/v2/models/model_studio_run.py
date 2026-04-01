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
from foundry_sdk.v2.models import errors as models_errors
from foundry_sdk.v2.models import models as models_models


class ModelStudioRunClient:
    """
    The API client for the ModelStudioRun Resource.

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

        self.with_streaming_response = _ModelStudioRunClientStreaming(self)
        self.with_raw_response = _ModelStudioRunClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def list(
        self,
        model_studio_rid: models_models.ModelStudioRid,
        *,
        config_version: typing.Optional[models_models.ModelStudioConfigVersionNumber] = None,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> core.ResourceIterator[models_models.ModelStudioRun]:
        """
        Lists all runs for a Model Studio.
        :param model_studio_rid:
        :type model_studio_rid: ModelStudioRid
        :param config_version: Filter runs by configuration version.
        :type config_version: Optional[ModelStudioConfigVersionNumber]
        :param page_size: The page size to use for the endpoint.
        :type page_size: Optional[PageSize]
        :param page_token: The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
        :type page_token: Optional[PageToken]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ResourceIterator[models_models.ModelStudioRun]

        :raises ModelStudioConfigVersionNotFound: The requested Model Studio configuration version was not found.
        :raises ModelStudioNotFound: The requested Model Studio was not found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/models/modelStudios/{modelStudioRid}/runs",
                query_params={
                    "configVersion": config_version,
                    "pageSize": page_size,
                    "pageToken": page_token,
                    "preview": preview,
                },
                path_params={
                    "modelStudioRid": model_studio_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=models_models.ListModelStudioRunsResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "ModelStudioConfigVersionNotFound": models_errors.ModelStudioConfigVersionNotFound,
                    "ModelStudioNotFound": models_errors.ModelStudioNotFound,
                },
                response_mode=_sdk_internal.get("response_mode", "ITERATOR"),
            ),
        )


class _ModelStudioRunClientRaw:
    def __init__(self, client: ModelStudioRunClient) -> None:
        def list(_: models_models.ListModelStudioRunsResponse): ...

        self.list = core.with_raw_response(list, client.list)


class _ModelStudioRunClientStreaming:
    def __init__(self, client: ModelStudioRunClient) -> None:
        def list(_: models_models.ListModelStudioRunsResponse): ...

        self.list = core.with_streaming_response(list, client.list)


class AsyncModelStudioRunClient:
    """
    The API client for the ModelStudioRun Resource.

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

        self.with_streaming_response = _AsyncModelStudioRunClientStreaming(self)
        self.with_raw_response = _AsyncModelStudioRunClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def list(
        self,
        model_studio_rid: models_models.ModelStudioRid,
        *,
        config_version: typing.Optional[models_models.ModelStudioConfigVersionNumber] = None,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> core.AsyncResourceIterator[models_models.ModelStudioRun]:
        """
        Lists all runs for a Model Studio.
        :param model_studio_rid:
        :type model_studio_rid: ModelStudioRid
        :param config_version: Filter runs by configuration version.
        :type config_version: Optional[ModelStudioConfigVersionNumber]
        :param page_size: The page size to use for the endpoint.
        :type page_size: Optional[PageSize]
        :param page_token: The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
        :type page_token: Optional[PageToken]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.AsyncResourceIterator[models_models.ModelStudioRun]

        :raises ModelStudioConfigVersionNotFound: The requested Model Studio configuration version was not found.
        :raises ModelStudioNotFound: The requested Model Studio was not found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/models/modelStudios/{modelStudioRid}/runs",
                query_params={
                    "configVersion": config_version,
                    "pageSize": page_size,
                    "pageToken": page_token,
                    "preview": preview,
                },
                path_params={
                    "modelStudioRid": model_studio_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=models_models.ListModelStudioRunsResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "ModelStudioConfigVersionNotFound": models_errors.ModelStudioConfigVersionNotFound,
                    "ModelStudioNotFound": models_errors.ModelStudioNotFound,
                },
                response_mode=_sdk_internal.get("response_mode", "ITERATOR"),
            ),
        )


class _AsyncModelStudioRunClientRaw:
    def __init__(self, client: AsyncModelStudioRunClient) -> None:
        def list(_: models_models.ListModelStudioRunsResponse): ...

        self.list = core.async_with_raw_response(list, client.list)


class _AsyncModelStudioRunClientStreaming:
    def __init__(self, client: AsyncModelStudioRunClient) -> None:
        def list(_: models_models.ListModelStudioRunsResponse): ...

        self.list = core.async_with_streaming_response(list, client.list)
