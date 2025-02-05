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
from typing import Optional
from typing import cast

import pydantic

from foundry.v2.core.models._display_name import DisplayName
from foundry.v2.ontologies.models._function_rid import FunctionRid
from foundry.v2.ontologies.models._function_version import FunctionVersion
from foundry.v2.ontologies.models._parameter_id import ParameterId
from foundry.v2.ontologies.models._query_api_name import QueryApiName
from foundry.v2.ontologies.models._query_data_type import QueryDataType
from foundry.v2.ontologies.models._query_parameter_v2 import QueryParameterV2
from foundry.v2.ontologies.models._query_type_v2_dict import QueryTypeV2Dict


class QueryTypeV2(pydantic.BaseModel):
    """Represents a query type in the Ontology."""

    api_name: QueryApiName = pydantic.Field(alias=str("apiName"))  # type: ignore[literal-required]

    description: Optional[str] = None

    display_name: Optional[DisplayName] = pydantic.Field(alias=str("displayName"), default=None)  # type: ignore[literal-required]

    parameters: Dict[ParameterId, QueryParameterV2]

    output: QueryDataType

    rid: FunctionRid

    version: FunctionVersion

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> QueryTypeV2Dict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(QueryTypeV2Dict, self.model_dump(by_alias=True, exclude_none=True))
