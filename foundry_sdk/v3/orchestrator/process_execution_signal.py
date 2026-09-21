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
from foundry_sdk.v3.orchestrator import errors as orchestrator_errors
from foundry_sdk.v3.orchestrator import models as orchestrator_models


class ProcessExecutionSignalClient:
    """
    The API client for the ProcessExecutionSignal Resource.

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

        self.with_streaming_response = _ProcessExecutionSignalClientStreaming(self)
        self.with_raw_response = _ProcessExecutionSignalClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def complete(
        self,
        process_execution_id: orchestrator_models.ProcessExecutionId,
        signal_id: orchestrator_models.SignalId,
        *,
        payload: typing.Optional[typing.Any] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> None:
        """
        Complete a signal on a process execution.

        A signal may be completed multiple times, each contributing toward the execution's wait conditions.
        If the execution is suspended waiting on this signal, it resumes once its wait conditions are
        satisfied. Resuming an execution runs user-authored logic. Only the token that originally invoked the
        process execution can complete its signals.
        :param process_execution_id:
        :type process_execution_id: ProcessExecutionId
        :param signal_id:
        :type signal_id: SignalId
        :param payload: Arbitrary JSON passed to the process execution that consumes the signal. Empty when the completion carries no payload.
        :type payload: Optional[Any]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: None

        :raises CompleteProcessExecutionSignalPermissionDenied: The token does not have permission to complete this signal. Signals can only be completed by the token that originally invoked the process execution.
        :raises ProcessExecutionExpired: The process execution can no longer accept signal completions because its data is outside the retention window.
        :raises ProcessExecutionNotFound:
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v3/platform/processExecutions/{processExecutionId}/signals/{signalId}/complete",
                query_params={},
                path_params={
                    "processExecutionId": process_execution_id,
                    "signalId": signal_id,
                },
                header_params={
                    "Content-Type": "application/json",
                },
                body=orchestrator_models.CompleteProcessExecutionSignalRequest(
                    payload=payload,
                ),
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "CompleteProcessExecutionSignalPermissionDenied": orchestrator_errors.CompleteProcessExecutionSignalPermissionDenied,
                    "ProcessExecutionExpired": orchestrator_errors.ProcessExecutionExpired,
                    "ProcessExecutionNotFound": orchestrator_errors.ProcessExecutionNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _ProcessExecutionSignalClientRaw:
    def __init__(self, client: ProcessExecutionSignalClient) -> None:
        def complete(_: None): ...

        self.complete = core.with_raw_response(complete, client.complete)


class _ProcessExecutionSignalClientStreaming:
    def __init__(self, client: ProcessExecutionSignalClient) -> None:
        pass


class AsyncProcessExecutionSignalClient:
    """
    The API client for the ProcessExecutionSignal Resource.

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

        self.with_streaming_response = _AsyncProcessExecutionSignalClientStreaming(self)
        self.with_raw_response = _AsyncProcessExecutionSignalClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def complete(
        self,
        process_execution_id: orchestrator_models.ProcessExecutionId,
        signal_id: orchestrator_models.SignalId,
        *,
        payload: typing.Optional[typing.Any] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[None]:
        """
        Complete a signal on a process execution.

        A signal may be completed multiple times, each contributing toward the execution's wait conditions.
        If the execution is suspended waiting on this signal, it resumes once its wait conditions are
        satisfied. Resuming an execution runs user-authored logic. Only the token that originally invoked the
        process execution can complete its signals.
        :param process_execution_id:
        :type process_execution_id: ProcessExecutionId
        :param signal_id:
        :type signal_id: SignalId
        :param payload: Arbitrary JSON passed to the process execution that consumes the signal. Empty when the completion carries no payload.
        :type payload: Optional[Any]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[None]

        :raises CompleteProcessExecutionSignalPermissionDenied: The token does not have permission to complete this signal. Signals can only be completed by the token that originally invoked the process execution.
        :raises ProcessExecutionExpired: The process execution can no longer accept signal completions because its data is outside the retention window.
        :raises ProcessExecutionNotFound:
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v3/platform/processExecutions/{processExecutionId}/signals/{signalId}/complete",
                query_params={},
                path_params={
                    "processExecutionId": process_execution_id,
                    "signalId": signal_id,
                },
                header_params={
                    "Content-Type": "application/json",
                },
                body=orchestrator_models.CompleteProcessExecutionSignalRequest(
                    payload=payload,
                ),
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "CompleteProcessExecutionSignalPermissionDenied": orchestrator_errors.CompleteProcessExecutionSignalPermissionDenied,
                    "ProcessExecutionExpired": orchestrator_errors.ProcessExecutionExpired,
                    "ProcessExecutionNotFound": orchestrator_errors.ProcessExecutionNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _AsyncProcessExecutionSignalClientRaw:
    def __init__(self, client: AsyncProcessExecutionSignalClient) -> None:
        def complete(_: None): ...

        self.complete = core.async_with_raw_response(complete, client.complete)


class _AsyncProcessExecutionSignalClientStreaming:
    def __init__(self, client: AsyncProcessExecutionSignalClient) -> None:
        pass
