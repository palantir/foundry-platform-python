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
from foundry.v2.ontologies import models as ontologies_models


class ObjectTypeIdsNotFoundParameters(typing_extensions.TypedDict):
    """
    Some object types are configured for use by the Agent but could not be found.
    The object types either do not exist or the client token does not have access.
    Object types can be checked by listing available object types through the API, or searching in [Ontology Manager](/docs/foundry/ontology-manager/overview/).
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    agentRid: aip_agents_models.AgentRid
    sessionRid: typing_extensions.NotRequired[aip_agents_models.SessionRid]
    """The session RID where the error occurred. This is omitted if the error occurred during session creation."""

    objectTypeIds: typing.List[ontologies_models.ObjectTypeId]


@dataclass
class ObjectTypeIdsNotFound(errors.NotFoundError):
    name: typing.Literal["ObjectTypeIdsNotFound"]
    parameters: ObjectTypeIdsNotFoundParameters
    error_instance_id: str


__all__ = ["ObjectTypeIdsNotFound"]
