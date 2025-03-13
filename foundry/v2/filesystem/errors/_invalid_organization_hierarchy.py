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


import typing
from dataclasses import dataclass

import typing_extensions

from foundry import _errors as errors
from foundry.v2.core import models as core_models


class InvalidOrganizationHierarchyParameters(typing_extensions.TypedDict):
    """
    Organizations on a project must also exist on the parent space. This error is thrown if the configuration
    of a project's organizations (on creation or subsequently) results in the project being marked with either
    no organizations in a marked space, or with an organization that is not present on the parent space.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    organizationRids: typing.List[core_models.OrganizationRid]


@dataclass
class InvalidOrganizationHierarchy(errors.BadRequestError):
    name: typing.Literal["InvalidOrganizationHierarchy"]
    parameters: InvalidOrganizationHierarchyParameters
    error_instance_id: str


__all__ = ["InvalidOrganizationHierarchy"]
