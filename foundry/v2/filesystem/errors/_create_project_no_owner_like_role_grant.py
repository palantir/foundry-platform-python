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

from dataclasses import dataclass
from typing import List
from typing import Literal

from typing_extensions import TypedDict

from foundry._errors import BadRequestError
from foundry.v2.core.models._role_id import RoleId


class CreateProjectNoOwnerLikeRoleGrantParameters(TypedDict):
    """The create project request would create a project with no principal being granted an owner-like role. As a result, there would be no user with administrative privileges over the project. A role is defined to be owner-like if it has the `compass:edit-project` operation. In the common case of the default role-set, this is just the `compass:manage` role."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    grantedRoleIds: List[RoleId]

    roleSetOwnerLikeRoleIds: List[RoleId]


@dataclass
class CreateProjectNoOwnerLikeRoleGrant(BadRequestError):
    name: Literal["CreateProjectNoOwnerLikeRoleGrant"]
    parameters: CreateProjectNoOwnerLikeRoleGrantParameters
    error_instance_id: str


__all__ = ["CreateProjectNoOwnerLikeRoleGrant"]
