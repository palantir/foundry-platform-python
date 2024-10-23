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

from foundry.v2.functions.models._value_type_reference_dict import ValueTypeReferenceDict  # NOQA
from foundry.v2.functions.models._value_type_rid import ValueTypeRid
from foundry.v2.functions.models._value_type_version_id import ValueTypeVersionId


class ValueTypeReference(pydantic.BaseModel):
    """A reference to a value type that has been registered in the Ontology."""

    rid: ValueTypeRid

    version_id: ValueTypeVersionId = pydantic.Field(alias="versionId")

    type: Literal["valueTypeReference"]

    model_config = {"extra": "allow"}

    def to_dict(self) -> ValueTypeReferenceDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(ValueTypeReferenceDict, self.model_dump(by_alias=True, exclude_unset=True))
