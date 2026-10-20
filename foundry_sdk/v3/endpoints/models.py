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
    """
    A Compass resource that groups related custom endpoint definitions and manages permissions for viewing,
    editing, publishing, and deploying them. Publishing creates a snapshot of the set's current endpoint definitions.
    """

    name: str
    """The name of the endpoint set's Compass resource."""

    rid: EndpointSetRid
    """The RID of the Compass resource that represents this endpoint set."""


class EndpointSetEndpoint(core.ModelBase):
    """
    A custom API endpoint in an endpoint set's current editable configuration. Its definition maps an HTTP method,
    URL path, and request parameters to a function or action in the Ontology.
    """

    name: str
    """The display name from the endpoint's current editable definition."""

    rid: EndpointSetEndpointRid
    """The unique identifier used with the parent endpoint set RID to retrieve this endpoint definition."""


EndpointSetEndpointRid: typing_extensions.TypeAlias = core.RID
"""A rid for an endpoint definition within an endpoint set."""


EndpointSetRid: typing_extensions.TypeAlias = core.RID
"""A rid for an endpoint set."""


class EndpointSetVersion(core.ModelBase):
    """
    A published snapshot of an endpoint set's definitions, identified by a semantic version. Published versions can
    be retrieved and listed whether or not they are deployed. Deploying a version makes its endpoints available
    on the endpoint set's subdomain.
    """

    id: EndpointSetVersionId
    """The semantic version supplied when publishing this snapshot, used to select it within its endpoint set."""


EndpointSetVersionId: typing_extensions.TypeAlias = str
"""The semantic version identifying a published snapshot of an endpoint set, for example `1.2.3`."""


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
