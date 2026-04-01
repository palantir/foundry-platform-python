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

import annotated_types
import pydantic
import typing_extensions

from foundry_sdk import _core as core
from foundry_sdk import _errors as errors
from foundry_sdk.v2.checkpoints import errors as checkpoints_errors
from foundry_sdk.v2.checkpoints import models as checkpoints_models
from foundry_sdk.v2.core import models as core_models


class RecordClient:
    """
    The API client for the Record Resource.

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

        self.with_streaming_response = _RecordClientStreaming(self)
        self.with_raw_response = _RecordClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        record_rid: checkpoints_models.RecordRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> checkpoints_models.Record:
        """
        Retrieve a single checkpoint record by id.
        :param record_rid:
        :type record_rid: RecordRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: checkpoints_models.Record

        :raises CheckpointRecordNotFound: The checkpoint record could not be found.
        :raises CheckpointRecordPermissionDenied: The caller does not have permission to access the checkpoint record.
        :raises RecordNotFound: The given Record could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/checkpoints/records/{recordRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "recordRid": record_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=checkpoints_models.Record,
                request_timeout=request_timeout,
                throwable_errors={
                    "CheckpointRecordNotFound": checkpoints_errors.CheckpointRecordNotFound,
                    "CheckpointRecordPermissionDenied": checkpoints_errors.CheckpointRecordPermissionDenied,
                    "RecordNotFound": checkpoints_errors.RecordNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get_batch(
        self,
        body: typing_extensions.Annotated[
            typing.List[checkpoints_models.GetRecordsBatchRequestElement],
            annotated_types.Len(min_length=1, max_length=100),
        ],
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> checkpoints_models.GetRecordsBatchResponse:
        """
        Fetch multiple checkpoint records in a single request. Records not found
        or inaccessible to the user will be omitted from the response.


        The maximum batch size for this endpoint is 100.
        :param body: Body of the request
        :type body: List[GetRecordsBatchRequestElement]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: checkpoints_models.GetRecordsBatchResponse
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/checkpoints/records/getBatch",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body=body,
                response_type=checkpoints_models.GetRecordsBatchResponse,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def search(
        self,
        *,
        where: checkpoints_models.SearchCheckpointRecordsRequest,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        sort_direction: typing.Optional[checkpoints_models.SortDirection] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> checkpoints_models.SearchCheckpointRecordsResponse:
        """
        Search for checkpoint records.
        :param where:
        :type where: SearchCheckpointRecordsRequest
        :param page_size: The page size for the search request. If no value is provided, a default of `100` will be used.
        :type page_size: Optional[PageSize]
        :param page_token:
        :type page_token: Optional[PageToken]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param sort_direction: Chronological order of creation time for records to be returned in. Defaults to reverse chronological order (DESC).
        :type sort_direction: Optional[SortDirection]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: checkpoints_models.SearchCheckpointRecordsResponse

        :raises SearchRecordsPermissionDenied: Could not search the Record.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/checkpoints/records/search",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body=checkpoints_models.SearchRecordsRequest(
                    where=where,
                    page_token=page_token,
                    page_size=page_size,
                    sort_direction=sort_direction,
                ),
                response_type=checkpoints_models.SearchCheckpointRecordsResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "SearchRecordsPermissionDenied": checkpoints_errors.SearchRecordsPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _RecordClientRaw:
    def __init__(self, client: RecordClient) -> None:
        def get(_: checkpoints_models.Record): ...
        def get_batch(_: checkpoints_models.GetRecordsBatchResponse): ...
        def search(_: checkpoints_models.SearchCheckpointRecordsResponse): ...

        self.get = core.with_raw_response(get, client.get)
        self.get_batch = core.with_raw_response(get_batch, client.get_batch)
        self.search = core.with_raw_response(search, client.search)


class _RecordClientStreaming:
    def __init__(self, client: RecordClient) -> None:
        def get(_: checkpoints_models.Record): ...
        def get_batch(_: checkpoints_models.GetRecordsBatchResponse): ...
        def search(_: checkpoints_models.SearchCheckpointRecordsResponse): ...

        self.get = core.with_streaming_response(get, client.get)
        self.get_batch = core.with_streaming_response(get_batch, client.get_batch)
        self.search = core.with_streaming_response(search, client.search)


class AsyncRecordClient:
    """
    The API client for the Record Resource.

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

        self.with_streaming_response = _AsyncRecordClientStreaming(self)
        self.with_raw_response = _AsyncRecordClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        record_rid: checkpoints_models.RecordRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[checkpoints_models.Record]:
        """
        Retrieve a single checkpoint record by id.
        :param record_rid:
        :type record_rid: RecordRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[checkpoints_models.Record]

        :raises CheckpointRecordNotFound: The checkpoint record could not be found.
        :raises CheckpointRecordPermissionDenied: The caller does not have permission to access the checkpoint record.
        :raises RecordNotFound: The given Record could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/checkpoints/records/{recordRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "recordRid": record_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=checkpoints_models.Record,
                request_timeout=request_timeout,
                throwable_errors={
                    "CheckpointRecordNotFound": checkpoints_errors.CheckpointRecordNotFound,
                    "CheckpointRecordPermissionDenied": checkpoints_errors.CheckpointRecordPermissionDenied,
                    "RecordNotFound": checkpoints_errors.RecordNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get_batch(
        self,
        body: typing_extensions.Annotated[
            typing.List[checkpoints_models.GetRecordsBatchRequestElement],
            annotated_types.Len(min_length=1, max_length=100),
        ],
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[checkpoints_models.GetRecordsBatchResponse]:
        """
        Fetch multiple checkpoint records in a single request. Records not found
        or inaccessible to the user will be omitted from the response.


        The maximum batch size for this endpoint is 100.
        :param body: Body of the request
        :type body: List[GetRecordsBatchRequestElement]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[checkpoints_models.GetRecordsBatchResponse]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/checkpoints/records/getBatch",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body=body,
                response_type=checkpoints_models.GetRecordsBatchResponse,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def search(
        self,
        *,
        where: checkpoints_models.SearchCheckpointRecordsRequest,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        sort_direction: typing.Optional[checkpoints_models.SortDirection] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[checkpoints_models.SearchCheckpointRecordsResponse]:
        """
        Search for checkpoint records.
        :param where:
        :type where: SearchCheckpointRecordsRequest
        :param page_size: The page size for the search request. If no value is provided, a default of `100` will be used.
        :type page_size: Optional[PageSize]
        :param page_token:
        :type page_token: Optional[PageToken]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param sort_direction: Chronological order of creation time for records to be returned in. Defaults to reverse chronological order (DESC).
        :type sort_direction: Optional[SortDirection]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[checkpoints_models.SearchCheckpointRecordsResponse]

        :raises SearchRecordsPermissionDenied: Could not search the Record.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/checkpoints/records/search",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body=checkpoints_models.SearchRecordsRequest(
                    where=where,
                    page_token=page_token,
                    page_size=page_size,
                    sort_direction=sort_direction,
                ),
                response_type=checkpoints_models.SearchCheckpointRecordsResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "SearchRecordsPermissionDenied": checkpoints_errors.SearchRecordsPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _AsyncRecordClientRaw:
    def __init__(self, client: AsyncRecordClient) -> None:
        def get(_: checkpoints_models.Record): ...
        def get_batch(_: checkpoints_models.GetRecordsBatchResponse): ...
        def search(_: checkpoints_models.SearchCheckpointRecordsResponse): ...

        self.get = core.async_with_raw_response(get, client.get)
        self.get_batch = core.async_with_raw_response(get_batch, client.get_batch)
        self.search = core.async_with_raw_response(search, client.search)


class _AsyncRecordClientStreaming:
    def __init__(self, client: AsyncRecordClient) -> None:
        def get(_: checkpoints_models.Record): ...
        def get_batch(_: checkpoints_models.GetRecordsBatchResponse): ...
        def search(_: checkpoints_models.SearchCheckpointRecordsResponse): ...

        self.get = core.async_with_streaming_response(get, client.get)
        self.get_batch = core.async_with_streaming_response(get_batch, client.get_batch)
        self.search = core.async_with_streaming_response(search, client.search)
