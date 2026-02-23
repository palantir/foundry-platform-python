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


class ModelsClient:
    """
    The API client for the Models Namespace.

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
    def LiveDeployment(self):
        from foundry_sdk.v2.models.live_deployment import LiveDeploymentClient

        return LiveDeploymentClient(
            auth=self._auth,
            hostname=self._hostname,
            config=self._config,
        )

    @cached_property
    def Model(self):
        from foundry_sdk.v2.models.model import ModelClient

        return ModelClient(
            auth=self._auth,
            hostname=self._hostname,
            config=self._config,
        )

    @cached_property
    def ModelStudio(self):
        from foundry_sdk.v2.models.model_studio import ModelStudioClient

        return ModelStudioClient(
            auth=self._auth,
            hostname=self._hostname,
            config=self._config,
        )

    @cached_property
    def ModelStudioTrainer(self):
        from foundry_sdk.v2.models.model_studio_trainer import ModelStudioTrainerClient

        return ModelStudioTrainerClient(
            auth=self._auth,
            hostname=self._hostname,
            config=self._config,
        )


class AsyncModelsClient:
    """
    The Async API client for the Models Namespace.

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
        from foundry_sdk.v2.models.live_deployment import AsyncLiveDeploymentClient
        from foundry_sdk.v2.models.model import AsyncModelClient
        from foundry_sdk.v2.models.model_studio import AsyncModelStudioClient
        from foundry_sdk.v2.models.model_studio_trainer import AsyncModelStudioTrainerClient  # NOQA

        self.LiveDeployment = AsyncLiveDeploymentClient(auth=auth, hostname=hostname, config=config)

        self.Model = AsyncModelClient(auth=auth, hostname=hostname, config=config)

        self.ModelStudio = AsyncModelStudioClient(auth=auth, hostname=hostname, config=config)

        self.ModelStudioTrainer = AsyncModelStudioTrainerClient(
            auth=auth, hostname=hostname, config=config
        )
