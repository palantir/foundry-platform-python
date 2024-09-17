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

from typing import List
from typing import Literal

from pydantic import StrictBool
from typing_extensions import TypedDict

from foundry.v2.ontologies.models._parameter_option_dict import ParameterOptionDict


class OneOfConstraintDict(TypedDict):
    """The parameter has a manually predefined set of options."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    options: List[ParameterOptionDict]

    otherValuesAllowed: StrictBool
    """A flag denoting whether custom, user provided values will be considered valid. This is configured via the **Allowed "Other" value** toggle in the **Ontology Manager**."""

    type: Literal["oneOf"]
