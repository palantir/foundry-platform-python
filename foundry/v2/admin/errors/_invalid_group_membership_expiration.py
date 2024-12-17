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
from datetime import datetime
from typing import Literal

import pydantic
from typing_extensions import NotRequired
from typing_extensions import TypedDict

from foundry._errors import PalantirRPCException
from foundry.v2.admin.models._group_membership_expiration import GroupMembershipExpiration  # NOQA
from foundry.v2.core.models._principal_id import PrincipalId


class InvalidGroupMembershipExpirationParameters(TypedDict):
    """The member expiration you provided does not conform to the Group's requirements for member expirations."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    groupId: PrincipalId

    expirationProvided: NotRequired[GroupMembershipExpiration]

    maximumDuration: NotRequired[str]

    latestExpiration: NotRequired[datetime]


@dataclass
class InvalidGroupMembershipExpiration(PalantirRPCException):
    name: Literal["InvalidGroupMembershipExpiration"]
    parameters: InvalidGroupMembershipExpirationParameters
    error_instance_id: str


__all__ = ["InvalidGroupMembershipExpiration"]
