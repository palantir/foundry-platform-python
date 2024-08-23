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

from typing import Dict

from typing_extensions import TypedDict

from foundry.v1.models._action_type_api_name import ActionTypeApiName
from foundry.v1.models._action_type_v2_dict import ActionTypeV2Dict
from foundry.v1.models._interface_type_api_name import InterfaceTypeApiName
from foundry.v1.models._interface_type_dict import InterfaceTypeDict
from foundry.v1.models._object_type_api_name import ObjectTypeApiName
from foundry.v1.models._object_type_full_metadata_dict import ObjectTypeFullMetadataDict
from foundry.v1.models._ontology_v2_dict import OntologyV2Dict
from foundry.v1.models._query_api_name import QueryApiName
from foundry.v1.models._query_type_v2_dict import QueryTypeV2Dict
from foundry.v1.models._shared_property_type_api_name import SharedPropertyTypeApiName
from foundry.v1.models._shared_property_type_dict import SharedPropertyTypeDict


class OntologyFullMetadataDict(TypedDict):
    """OntologyFullMetadata"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    ontology: OntologyV2Dict

    objectTypes: Dict[ObjectTypeApiName, ObjectTypeFullMetadataDict]

    actionTypes: Dict[ActionTypeApiName, ActionTypeV2Dict]

    queryTypes: Dict[QueryApiName, QueryTypeV2Dict]

    interfaceTypes: Dict[InterfaceTypeApiName, InterfaceTypeDict]

    sharedPropertyTypes: Dict[SharedPropertyTypeApiName, SharedPropertyTypeDict]
