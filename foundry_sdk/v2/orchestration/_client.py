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

from foundry_sdk import _core as core


class OrchestrationClient:
    """
    The API client for the Orchestration Namespace.

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

    @cached_property
    def Build(self):
        from foundry_sdk.v2.orchestration.build import BuildClient

        return BuildClient(
            auth=self._auth,
            hostname=self._hostname,
            config=self._config,
        )

    @cached_property
    def Job(self):
        from foundry_sdk.v2.orchestration.job import JobClient

        return JobClient(
            auth=self._auth,
            hostname=self._hostname,
            config=self._config,
        )

    @cached_property
    def Schedule(self):
        from foundry_sdk.v2.orchestration.schedule import ScheduleClient

        return ScheduleClient(
            auth=self._auth,
            hostname=self._hostname,
            config=self._config,
        )

    @cached_property
    def ScheduleRun(self):
        from foundry_sdk.v2.orchestration.schedule_run import ScheduleRunClient

        return ScheduleRunClient(
            auth=self._auth,
            hostname=self._hostname,
            config=self._config,
        )

    @cached_property
    def ScheduleVersion(self):
        from foundry_sdk.v2.orchestration.schedule_version import ScheduleVersionClient

        return ScheduleVersionClient(
            auth=self._auth,
            hostname=self._hostname,
            config=self._config,
        )


class AsyncOrchestrationClient:
    """
    The Async API client for the Orchestration Namespace.

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
        from foundry_sdk.v2.orchestration.build import AsyncBuildClient
        from foundry_sdk.v2.orchestration.job import AsyncJobClient
        from foundry_sdk.v2.orchestration.schedule import AsyncScheduleClient
        from foundry_sdk.v2.orchestration.schedule_run import AsyncScheduleRunClient
        from foundry_sdk.v2.orchestration.schedule_version import AsyncScheduleVersionClient  # NOQA

        self.Build = AsyncBuildClient(auth=auth, hostname=hostname, config=config)

        self.Job = AsyncJobClient(auth=auth, hostname=hostname, config=config)

        self.Schedule = AsyncScheduleClient(auth=auth, hostname=hostname, config=config)

        self.ScheduleRun = AsyncScheduleRunClient(auth=auth, hostname=hostname, config=config)

        self.ScheduleVersion = AsyncScheduleVersionClient(
            auth=auth, hostname=hostname, config=config
        )
