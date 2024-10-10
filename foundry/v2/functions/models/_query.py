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
from foundry.v2.functions.models._function_rid import FunctionRid
from foundry.v2.functions.models._function_version import FunctionVersion
from foundry.v2.functions.models._parameter import Parameter
from foundry.v2.functions.models._parameter_id import ParameterId
from foundry.v2.functions.models._query_api_name import QueryApiName
from foundry.v2.functions.models._query_data_type import QueryDataType
from foundry.v2.functions.models._query_dict import QueryDict


class Query(pydantic.BaseModel):
    """Query"""

    api_name: QueryApiName = pydantic.Field(alias="apiName")

    description: Optional[pydantic.StrictStr] = None

    display_name: Optional[DisplayName] = pydantic.Field(alias="displayName", default=None)

    parameters: Dict[ParameterId, Parameter]

    output: QueryDataType

    rid: FunctionRid

    version: FunctionVersion

    model_config = {"extra": "allow"}

    def to_dict(self) -> QueryDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(QueryDict, self.model_dump(by_alias=True, exclude_unset=True))
