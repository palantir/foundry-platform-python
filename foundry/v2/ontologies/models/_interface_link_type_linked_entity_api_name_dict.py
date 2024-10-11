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

from typing import Union

import pydantic
from typing_extensions import Annotated

from foundry.v2.ontologies.models._linked_interface_type_api_name_dict import (
    LinkedInterfaceTypeApiNameDict,
)  # NOQA
from foundry.v2.ontologies.models._linked_object_type_api_name_dict import (
    LinkedObjectTypeApiNameDict,
)  # NOQA

InterfaceLinkTypeLinkedEntityApiNameDict = Annotated[
    Union[LinkedObjectTypeApiNameDict, LinkedInterfaceTypeApiNameDict],
    pydantic.Field(discriminator="type"),
]
"""A reference to the linked entity. This can either be an object or an interface type."""
