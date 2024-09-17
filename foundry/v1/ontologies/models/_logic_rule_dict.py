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

from pydantic import Field
from typing_extensions import Annotated

from foundry.v1.ontologies.models._create_interface_object_rule_dict import (
    CreateInterfaceObjectRuleDict,
)  # NOQA
from foundry.v1.ontologies.models._create_link_rule_dict import CreateLinkRuleDict
from foundry.v1.ontologies.models._create_object_rule_dict import CreateObjectRuleDict
from foundry.v1.ontologies.models._delete_link_rule_dict import DeleteLinkRuleDict
from foundry.v1.ontologies.models._delete_object_rule_dict import DeleteObjectRuleDict
from foundry.v1.ontologies.models._modify_interface_object_rule_dict import (
    ModifyInterfaceObjectRuleDict,
)  # NOQA
from foundry.v1.ontologies.models._modify_object_rule_dict import ModifyObjectRuleDict

LogicRuleDict = Annotated[
    Union[
        ModifyInterfaceObjectRuleDict,
        ModifyObjectRuleDict,
        DeleteObjectRuleDict,
        CreateInterfaceObjectRuleDict,
        DeleteLinkRuleDict,
        CreateObjectRuleDict,
        CreateLinkRuleDict,
    ],
    Field(discriminator="type"),
]
"""LogicRule"""
