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


class OrganizationClient:
    """
    The API client for the Organization Resource.

    :param auth: Your auth configuration.
    :param hostname: Your Foundry hostname (for example, "myfoundry.palantirfoundry.com"). This can also include your API gateway service URI.
    :param config: Optionally specify the configuration for the HTTP session.
    """

    def __init__(
        self,
        auth: core.Auth,
        hostname: str,
        config: typing.Optional[core.Config] = None,
    ):
        self._auth = auth
        self._hostname = hostname
        self._config = config
        self._api_client = core.ApiClient(auth=auth, hostname=hostname, config=config)

        self.with_streaming_response = _OrganizationClientStreaming(self)
        self.with_raw_response = _OrganizationClientRaw(self)

    @cached_property
    def LogFile(self):
        from foundry_sdk.v2.audit.log_file import LogFileClient

        return LogFileClient(
            auth=self._auth,
            hostname=self._hostname,
            config=self._config,
        )


class _OrganizationClientRaw:
    def __init__(self, client: OrganizationClient) -> None:
        pass


class _OrganizationClientStreaming:
    def __init__(self, client: OrganizationClient) -> None:
        pass


class AsyncOrganizationClient:
    """
    The API client for the Organization Resource.

    :param auth: Your auth configuration.
    :param hostname: Your Foundry hostname (for example, "myfoundry.palantirfoundry.com"). This can also include your API gateway service URI.
    :param config: Optionally specify the configuration for the HTTP session.
    """

    def __init__(
        self,
        auth: core.Auth,
        hostname: str,
        config: typing.Optional[core.Config] = None,
    ):
        self._auth = auth
        self._hostname = hostname
        self._config = config
        self._api_client = core.AsyncApiClient(auth=auth, hostname=hostname, config=config)

        self.with_streaming_response = _AsyncOrganizationClientStreaming(self)
        self.with_raw_response = _AsyncOrganizationClientRaw(self)

    @cached_property
    def LogFile(self):
        from foundry_sdk.v2.audit.log_file import AsyncLogFileClient

        return AsyncLogFileClient(
            auth=self._auth,
            hostname=self._hostname,
            config=self._config,
        )


class _AsyncOrganizationClientRaw:
    def __init__(self, client: AsyncOrganizationClient) -> None:
        pass


class _AsyncOrganizationClientStreaming:
    def __init__(self, client: AsyncOrganizationClient) -> None:
        pass
