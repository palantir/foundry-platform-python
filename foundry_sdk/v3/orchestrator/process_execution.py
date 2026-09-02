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


class ProcessExecutionClient:
    """
    The API client for the ProcessExecution Resource.

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

        self.with_streaming_response = _ProcessExecutionClientStreaming(self)
        self.with_raw_response = _ProcessExecutionClientRaw(self)

    @cached_property
    def Signal(self):
        from foundry_sdk.v3.orchestrator.process_execution_signal import (
            ProcessExecutionSignalClient,
        )

        return ProcessExecutionSignalClient(
            auth=self._auth,
            hostname=self._hostname_supplier,
            config=self._config,
        )


class _ProcessExecutionClientRaw:
    def __init__(self, client: ProcessExecutionClient) -> None:
        pass


class _ProcessExecutionClientStreaming:
    def __init__(self, client: ProcessExecutionClient) -> None:
        pass


class AsyncProcessExecutionClient:
    """
    The API client for the ProcessExecution Resource.

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

        self.with_streaming_response = _AsyncProcessExecutionClientStreaming(self)
        self.with_raw_response = _AsyncProcessExecutionClientRaw(self)

    @cached_property
    def Signal(self):
        from foundry_sdk.v3.orchestrator.process_execution_signal import (
            AsyncProcessExecutionSignalClient,
        )

        return AsyncProcessExecutionSignalClient(
            auth=self._auth,
            hostname=self._hostname_supplier,
            config=self._config,
        )


class _AsyncProcessExecutionClientRaw:
    def __init__(self, client: AsyncProcessExecutionClient) -> None:
        pass


class _AsyncProcessExecutionClientStreaming:
    def __init__(self, client: AsyncProcessExecutionClient) -> None:
        pass
