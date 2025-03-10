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
from datetime import datetime

import typing_extensions

from foundry import _errors as errors
from foundry.v2.admin import models as admin_models
from foundry.v2.core import models as core_models


class InvalidGroupMembershipExpirationParameters(typing_extensions.TypedDict):
    """The member expiration you provided does not conform to the Group's requirements for member expirations."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    groupId: core_models.PrincipalId
    expirationProvided: typing_extensions.NotRequired[admin_models.GroupMembershipExpiration]
    maximumDuration: typing_extensions.NotRequired[str]
    latestExpiration: typing_extensions.NotRequired[datetime]


@dataclass
class InvalidGroupMembershipExpiration(errors.BadRequestError):
    name: typing.Literal["InvalidGroupMembershipExpiration"]
    parameters: InvalidGroupMembershipExpirationParameters
    error_instance_id: str


__all__ = ["InvalidGroupMembershipExpiration"]
