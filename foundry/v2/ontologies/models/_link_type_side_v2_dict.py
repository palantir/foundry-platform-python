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

from typing_extensions import NotRequired
from typing_extensions import TypedDict

from foundry.v2.core.models._display_name import DisplayName
from foundry.v2.core.models._release_status import ReleaseStatus
from foundry.v2.ontologies.models._link_type_api_name import LinkTypeApiName
from foundry.v2.ontologies.models._link_type_rid import LinkTypeRid
from foundry.v2.ontologies.models._link_type_side_cardinality import LinkTypeSideCardinality  # NOQA
from foundry.v2.ontologies.models._object_type_api_name import ObjectTypeApiName
from foundry.v2.ontologies.models._property_api_name import PropertyApiName


class LinkTypeSideV2Dict(TypedDict):
    """LinkTypeSideV2"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    apiName: LinkTypeApiName

    displayName: DisplayName

    status: ReleaseStatus

    objectTypeApiName: ObjectTypeApiName

    cardinality: LinkTypeSideCardinality

    foreignKeyPropertyApiName: NotRequired[PropertyApiName]

    linkTypeRid: LinkTypeRid