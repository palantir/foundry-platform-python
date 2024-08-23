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

from pydantic import StrictStr
from typing_extensions import NotRequired
from typing_extensions import TypedDict

from foundry.v1.models._display_name import DisplayName
from foundry.v1.models._function_rid import FunctionRid
from foundry.v1.models._function_version import FunctionVersion
from foundry.v1.models._ontology_data_type_dict import OntologyDataTypeDict
from foundry.v1.models._parameter_dict import ParameterDict
from foundry.v1.models._parameter_id import ParameterId
from foundry.v1.models._query_api_name import QueryApiName


class QueryTypeDict(TypedDict):
    """Represents a query type in the Ontology."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    apiName: QueryApiName

    description: NotRequired[StrictStr]

    displayName: NotRequired[DisplayName]

    parameters: Dict[ParameterId, ParameterDict]

    output: NotRequired[OntologyDataTypeDict]

    rid: FunctionRid

    version: FunctionVersion
