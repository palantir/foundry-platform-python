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
from typing import Optional
from typing import cast

import pydantic

from foundry.v2.ontologies.models._object_set_interface_base_type_dict import (
    ObjectSetInterfaceBaseTypeDict,
)  # NOQA


class ObjectSetInterfaceBaseType(pydantic.BaseModel):
    """ObjectSetInterfaceBaseType"""

    interface_type: str = pydantic.Field(alias=str("interfaceType"))  # type: ignore[literal-required]

    """
    An object set with objects that implement the interface with the given interface API name. The objects in 
    the object set will only have properties that implement properties of the given interface, unless you set the includeAllBaseObjectProperties flag.
    """

    include_all_base_object_properties: Optional[bool] = pydantic.Field(alias=str("includeAllBaseObjectProperties"), default=None)  # type: ignore[literal-required]

    """
    A flag that will return all of the underlying object properties for the objects that implement the interface. 
    This includes properties that don't explicitly implement an SPT on the interface.
    """

    type: Literal["interfaceBase"] = "interfaceBase"

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> ObjectSetInterfaceBaseTypeDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(
            ObjectSetInterfaceBaseTypeDict, self.model_dump(by_alias=True, exclude_none=True)
        )
