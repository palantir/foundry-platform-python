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

# coding: utf-8

"""
    Palantir OpenAPI

    The Palantir REST API. Please see https://www.palantir.com/docs for more details.

    The version of the OpenAPI document: 1.738.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
import pprint
from typing import Union
try:
    from typing import Annotated
except ImportError:
    from typing_extensions import Annotated
from typing import Any, ClassVar, Dict, List, Literal, Optional, Set
from pydantic import Field
from pydantic import TypeAdapter
from typing_extensions import Self

from foundry.models.create_link_rule import CreateLinkRule
from foundry.models.create_object_rule import CreateObjectRule
from foundry.models.delete_link_rule import DeleteLinkRule
from foundry.models.delete_object_rule import DeleteObjectRule
from foundry.models.modify_object_rule import ModifyObjectRule



"""
LogicRule
"""
LogicRule = Annotated[Union[CreateLinkRule, CreateObjectRule, DeleteLinkRule, DeleteObjectRule, ModifyObjectRule], Field(discriminator="type")]




# Create an instance of a type adapter. This has a non-trivial overhead according
# to the documentation so we do this once. This also forces us to validate the
# correctness of the discriminator.
object.__setattr__(LogicRule, "type_adapter", TypeAdapter(LogicRule))
