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
from typing import cast

import pydantic

from foundry.v2.ontologies.models._action_type_api_name import ActionTypeApiName
from foundry.v2.ontologies.models._action_type_v2 import ActionTypeV2
from foundry.v2.ontologies.models._interface_type import InterfaceType
from foundry.v2.ontologies.models._interface_type_api_name import InterfaceTypeApiName
from foundry.v2.ontologies.models._object_type_api_name import ObjectTypeApiName
from foundry.v2.ontologies.models._object_type_full_metadata import ObjectTypeFullMetadata  # NOQA
from foundry.v2.ontologies.models._ontology_full_metadata_dict import (
    OntologyFullMetadataDict,
)  # NOQA
from foundry.v2.ontologies.models._ontology_v2 import OntologyV2
from foundry.v2.ontologies.models._query_api_name import QueryApiName
from foundry.v2.ontologies.models._query_type_v2 import QueryTypeV2
from foundry.v2.ontologies.models._shared_property_type import SharedPropertyType
from foundry.v2.ontologies.models._shared_property_type_api_name import (
    SharedPropertyTypeApiName,
)  # NOQA


class OntologyFullMetadata(pydantic.BaseModel):
    """OntologyFullMetadata"""

    ontology: OntologyV2

    object_types: Dict[ObjectTypeApiName, ObjectTypeFullMetadata] = pydantic.Field(
        alias="objectTypes"
    )

    action_types: Dict[ActionTypeApiName, ActionTypeV2] = pydantic.Field(alias="actionTypes")

    query_types: Dict[QueryApiName, QueryTypeV2] = pydantic.Field(alias="queryTypes")

    interface_types: Dict[InterfaceTypeApiName, InterfaceType] = pydantic.Field(
        alias="interfaceTypes"
    )

    shared_property_types: Dict[SharedPropertyTypeApiName, SharedPropertyType] = pydantic.Field(
        alias="sharedPropertyTypes"
    )

    model_config = {"extra": "allow"}

    def to_dict(self) -> OntologyFullMetadataDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(OntologyFullMetadataDict, self.model_dump(by_alias=True, exclude_unset=True))
