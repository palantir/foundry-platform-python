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


from __future__ import annotations

from typing import Union

import pydantic
from typing_extensions import Annotated

from foundry.v2.connectivity.models._agent_proxy_runtime import AgentProxyRuntime
from foundry.v2.connectivity.models._agent_worker_runtime import AgentWorkerRuntime
from foundry.v2.connectivity.models._direct_connection_runtime import (
    DirectConnectionRuntime,
)  # NOQA

RuntimePlatform = Annotated[
    Union[DirectConnectionRuntime, AgentProxyRuntime, AgentWorkerRuntime],
    pydantic.Field(discriminator="type"),
]
"""
[The runtime of a Connection](/docs/foundry/data-connection/core-concepts/#runtimes), which defines the
networking configuration and where capabilities are executed.
"""
