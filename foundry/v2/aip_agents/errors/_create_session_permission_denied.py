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
from dataclasses import dataclass

import typing_extensions

from foundry import _errors as errors
from foundry.v2.aip_agents import models as aip_agents_models


class CreateSessionPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not create the Session."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    agentRid: aip_agents_models.AgentRid
    """An RID identifying an AIP Agent created in [AIP Agent Studio](/docs/foundry/agent-studio/overview/)."""


@dataclass
class CreateSessionPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["CreateSessionPermissionDenied"]
    parameters: CreateSessionPermissionDeniedParameters
    error_instance_id: str


__all__ = ["CreateSessionPermissionDenied"]
