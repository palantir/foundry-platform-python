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
from foundry_sdk.v2.functions import errors as functions_errors
from foundry_sdk.v2.functions import models as functions_models


class ExecutionClient:
    """
    The API client for the Execution Resource.

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

        self.with_streaming_response = _ExecutionClientStreaming(self)
        self.with_raw_response = _ExecutionClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def cancel(
        self,
        execution_id: functions_models.ExecutionId,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> functions_models.CancelExecutionResponse:
        """
        Cancel a running async query execution. This endpoint is idempotent.

        :param execution_id:
        :type execution_id: ExecutionId
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: functions_models.CancelExecutionResponse

        :raises CancelExecutionPermissionDenied: Could not cancel the Execution.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/functions/executions/{executionId}/cancel",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "executionId": execution_id,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=functions_models.CancelExecutionResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "CancelExecutionPermissionDenied": functions_errors.CancelExecutionPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get_result(
        self,
        execution_id: functions_models.ExecutionId,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        timeout: typing.Optional[int] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> functions_models.GetExecutionResultResponse:
        """
        Poll for the result of an async query execution.

        Returns a discriminated union:
        - running: execution is still in progress.
        - succeeded: execution completed successfully with a return value.

        If the execution failed, a service error is thrown.

        Use the timeout parameter for long-polling: the server holds the
        connection open for up to the specified number of seconds. If the
        execution completes within that window, the result is returned
        immediately. Otherwise, the running variant is returned.

        :param execution_id:
        :type execution_id: ExecutionId
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param timeout: Maximum time in seconds to hold the connection open while waiting for execution to complete. Default: 0 (immediate status check). Values above 280 are clamped to 280.
        :type timeout: Optional[int]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: functions_models.GetExecutionResultResponse

        :raises GetResultExecutionPermissionDenied: Could not getResult the Execution.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/functions/executions/{executionId}/getResult",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "executionId": execution_id,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body=functions_models.GetResultExecutionRequest(
                    timeout=timeout,
                ),
                response_type=functions_models.GetExecutionResultResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "GetResultExecutionPermissionDenied": functions_errors.GetResultExecutionPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _ExecutionClientRaw:
    def __init__(self, client: ExecutionClient) -> None:
        def cancel(_: functions_models.CancelExecutionResponse): ...
        def get_result(_: functions_models.GetExecutionResultResponse): ...

        self.cancel = core.with_raw_response(cancel, client.cancel)
        self.get_result = core.with_raw_response(get_result, client.get_result)


class _ExecutionClientStreaming:
    def __init__(self, client: ExecutionClient) -> None:
        def cancel(_: functions_models.CancelExecutionResponse): ...
        def get_result(_: functions_models.GetExecutionResultResponse): ...

        self.cancel = core.with_streaming_response(cancel, client.cancel)
        self.get_result = core.with_streaming_response(get_result, client.get_result)


class AsyncExecutionClient:
    """
    The API client for the Execution Resource.

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

        self.with_streaming_response = _AsyncExecutionClientStreaming(self)
        self.with_raw_response = _AsyncExecutionClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def cancel(
        self,
        execution_id: functions_models.ExecutionId,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[functions_models.CancelExecutionResponse]:
        """
        Cancel a running async query execution. This endpoint is idempotent.

        :param execution_id:
        :type execution_id: ExecutionId
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[functions_models.CancelExecutionResponse]

        :raises CancelExecutionPermissionDenied: Could not cancel the Execution.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/functions/executions/{executionId}/cancel",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "executionId": execution_id,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=functions_models.CancelExecutionResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "CancelExecutionPermissionDenied": functions_errors.CancelExecutionPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get_result(
        self,
        execution_id: functions_models.ExecutionId,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        timeout: typing.Optional[int] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[functions_models.GetExecutionResultResponse]:
        """
        Poll for the result of an async query execution.

        Returns a discriminated union:
        - running: execution is still in progress.
        - succeeded: execution completed successfully with a return value.

        If the execution failed, a service error is thrown.

        Use the timeout parameter for long-polling: the server holds the
        connection open for up to the specified number of seconds. If the
        execution completes within that window, the result is returned
        immediately. Otherwise, the running variant is returned.

        :param execution_id:
        :type execution_id: ExecutionId
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param timeout: Maximum time in seconds to hold the connection open while waiting for execution to complete. Default: 0 (immediate status check). Values above 280 are clamped to 280.
        :type timeout: Optional[int]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[functions_models.GetExecutionResultResponse]

        :raises GetResultExecutionPermissionDenied: Could not getResult the Execution.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/functions/executions/{executionId}/getResult",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "executionId": execution_id,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body=functions_models.GetResultExecutionRequest(
                    timeout=timeout,
                ),
                response_type=functions_models.GetExecutionResultResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "GetResultExecutionPermissionDenied": functions_errors.GetResultExecutionPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _AsyncExecutionClientRaw:
    def __init__(self, client: AsyncExecutionClient) -> None:
        def cancel(_: functions_models.CancelExecutionResponse): ...
        def get_result(_: functions_models.GetExecutionResultResponse): ...

        self.cancel = core.async_with_raw_response(cancel, client.cancel)
        self.get_result = core.async_with_raw_response(get_result, client.get_result)


class _AsyncExecutionClientStreaming:
    def __init__(self, client: AsyncExecutionClient) -> None:
        def cancel(_: functions_models.CancelExecutionResponse): ...
        def get_result(_: functions_models.GetExecutionResultResponse): ...

        self.cancel = core.async_with_streaming_response(cancel, client.cancel)
        self.get_result = core.async_with_streaming_response(get_result, client.get_result)
