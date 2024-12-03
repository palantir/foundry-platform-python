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
from typing import Literal

import pydantic
from typing_extensions import TypedDict

from foundry._errors import PalantirRPCException
from foundry.v2.third_party_applications.models._third_party_application_rid import (
    ThirdPartyApplicationRid,
)  # NOQA
from foundry.v2.third_party_applications.models._version_version import VersionVersion


class DeleteVersionPermissionDeniedParameters(TypedDict):
    """Could not delete the Version."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    thirdPartyApplicationRid: ThirdPartyApplicationRid
    """An RID identifying a third-party application created in Developer Console."""

    versionVersion: VersionVersion
    """The semantic version of the Website."""


@dataclass
class DeleteVersionPermissionDenied(PalantirRPCException):
    name: Literal["DeleteVersionPermissionDenied"]
    parameters: DeleteVersionPermissionDeniedParameters
    error_instance_id: str


__all__ = ["DeleteVersionPermissionDenied"]
