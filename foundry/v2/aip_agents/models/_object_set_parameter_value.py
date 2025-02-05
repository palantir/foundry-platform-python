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

from typing import Literal
from typing import cast

import pydantic

from foundry.v2.aip_agents.models._object_set_parameter_value_dict import (
    ObjectSetParameterValueDict,
)  # NOQA
from foundry.v2.ontologies.models._object_set import ObjectSet
from foundry.v2.ontologies.models._ontology_identifier import OntologyIdentifier


class ObjectSetParameterValue(pydantic.BaseModel):
    """A value passed for `ObjectSetParameter` application variable types."""

    object_set: ObjectSet = pydantic.Field(alias=str("objectSet"))  # type: ignore[literal-required]

    ontology: OntologyIdentifier

    """
    The API name of the Ontology for the provided `ObjectSet`.
    To find the API name, use the `List ontologies` endpoint or check the [Ontology Manager](/docs/foundry/ontology-manager/overview/).
    """

    type: Literal["objectSet"] = "objectSet"

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> ObjectSetParameterValueDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(ObjectSetParameterValueDict, self.model_dump(by_alias=True, exclude_none=True))
