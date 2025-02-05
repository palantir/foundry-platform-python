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

from foundry.v2.ontologies.models._get_selected_property_operation_dict import (
    GetSelectedPropertyOperationDict,
)  # NOQA
from foundry.v2.ontologies.models._property_api_name import PropertyApiName


class GetSelectedPropertyOperation(pydantic.BaseModel):
    """
    Gets a single value of a property. Throws if the target object set is on the MANY side of the link and could
    explode the cardinality.

    Use collectList or collectSet which will return a list of values in that case.
    """

    selected_property_api_name: PropertyApiName = pydantic.Field(alias=str("selectedPropertyApiName"))  # type: ignore[literal-required]

    type: Literal["get"] = "get"

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> GetSelectedPropertyOperationDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(
            GetSelectedPropertyOperationDict, self.model_dump(by_alias=True, exclude_none=True)
        )
