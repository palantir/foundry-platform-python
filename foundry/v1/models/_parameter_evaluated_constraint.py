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

from typing import Annotated
from typing import Union

from pydantic import Field

from foundry.v1.models._array_size_constraint import ArraySizeConstraint
from foundry.v1.models._group_member_constraint import GroupMemberConstraint
from foundry.v1.models._object_property_value_constraint import (
    ObjectPropertyValueConstraint,
)  # NOQA
from foundry.v1.models._object_query_result_constraint import ObjectQueryResultConstraint  # NOQA
from foundry.v1.models._one_of_constraint import OneOfConstraint
from foundry.v1.models._range_constraint import RangeConstraint
from foundry.v1.models._string_length_constraint import StringLengthConstraint
from foundry.v1.models._string_regex_match_constraint import StringRegexMatchConstraint
from foundry.v1.models._unevaluable_constraint import UnevaluableConstraint

ParameterEvaluatedConstraint = Annotated[
    Union[
        ArraySizeConstraint,
        GroupMemberConstraint,
        ObjectPropertyValueConstraint,
        ObjectQueryResultConstraint,
        OneOfConstraint,
        RangeConstraint,
        StringLengthConstraint,
        StringRegexMatchConstraint,
        UnevaluableConstraint,
    ],
    Field(discriminator="type"),
]
"""
A constraint that an action parameter value must satisfy in order to be considered valid.
Constraints can be configured on action parameters in the **Ontology Manager**. 
Applicable constraints are determined dynamically based on parameter inputs. 
Parameter values are evaluated against the final set of constraints.

The type of the constraint.
| Type                  | Description                                                                                                                                                                                                                     |
|-----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `arraySize`           | The parameter expects an array of values and the size of the array must fall within the defined range.                                                                                                                          |
| `groupMember`         | The parameter value must be the user id of a member belonging to at least one of the groups defined by the constraint.                                                                                                          |
| `objectPropertyValue` | The parameter value must be a property value of an object found within an object set.                                                                                                                                           |
| `objectQueryResult`   | The parameter value must be the primary key of an object found within an object set.                                                                                                                                            |
| `oneOf`               | The parameter has a manually predefined set of options.                                                                                                                                                                         |
| `range`               | The parameter value must be within the defined range.                                                                                                                                                                           |
| `stringLength`        | The parameter value must have a length within the defined range.                                                                                                                                                                |
| `stringRegexMatch`    | The parameter value must match a predefined regular expression.                                                                                                                                                                 |
| `unevaluable`         | The parameter cannot be evaluated because it depends on another parameter or object set that can't be evaluated. This can happen when a parameter's allowed values are defined by another parameter that is missing or invalid. |
"""
