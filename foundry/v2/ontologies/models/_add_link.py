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

from pydantic import BaseModel
from pydantic import Field

from foundry.v2.ontologies.models._add_link_dict import AddLinkDict
from foundry.v2.ontologies.models._link_side_object import LinkSideObject
from foundry.v2.ontologies.models._link_type_api_name import LinkTypeApiName


class AddLink(BaseModel):
    """AddLink"""

    link_type_api_name_ato_b: LinkTypeApiName = Field(alias="linkTypeApiNameAtoB")

    link_type_api_name_bto_a: LinkTypeApiName = Field(alias="linkTypeApiNameBtoA")

    a_side_object: LinkSideObject = Field(alias="aSideObject")

    b_side_object: LinkSideObject = Field(alias="bSideObject")

    type: Literal["addLink"]

    model_config = {"extra": "allow"}

    def to_dict(self) -> AddLinkDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(AddLinkDict, self.model_dump(by_alias=True, exclude_unset=True))
