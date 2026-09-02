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

import typing

import pydantic
import typing_extensions

from foundry_sdk import _core as core
from foundry_sdk.v3.core import models as core_models


class EndpointSet(core.ModelBase):
    """EndpointSet"""

    name: str
    rid: EndpointSetRid


class EndpointSetEndpoint(core.ModelBase):
    """EndpointSetEndpoint"""

    name: str
    rid: EndpointSetEndpointRid


EndpointSetEndpointRid: typing_extensions.TypeAlias = core.RID
"""EndpointSetEndpointRid"""


EndpointSetRid: typing_extensions.TypeAlias = core.RID
"""EndpointSetRid"""


class EndpointSetVersion(core.ModelBase):
    """EndpointSetVersion"""

    id: EndpointSetVersionId


EndpointSetVersionId: typing_extensions.TypeAlias = str
"""EndpointSetVersionId"""


class ListEndpointSetEndpointsResponse(core.ModelBase):
    """ListEndpointSetEndpointsResponse"""

    data: typing.List[EndpointSetEndpoint]
    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]


class ListEndpointSetVersionsResponse(core.ModelBase):
    """ListEndpointSetVersionsResponse"""

    data: typing.List[EndpointSetVersion]
    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]


core.resolve_forward_references_in_module(__name__)

__all__ = [
    "EndpointSet",
    "EndpointSetEndpoint",
    "EndpointSetEndpointRid",
    "EndpointSetRid",
    "EndpointSetVersion",
    "EndpointSetVersionId",
    "ListEndpointSetEndpointsResponse",
    "ListEndpointSetVersionsResponse",
]
