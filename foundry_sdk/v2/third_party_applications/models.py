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

import typing

import pydantic

from foundry_sdk import _core as core
from foundry_sdk.v2.core import models as core_models


class ListVersionsResponse(core.ModelBase):
    """ListVersionsResponse"""

    data: typing.List[Version]
    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]


Subdomain = str
"""A subdomain from which a website is served."""


class ThirdPartyApplication(core.ModelBase):
    """ThirdPartyApplication"""

    rid: ThirdPartyApplicationRid
    """An RID identifying a third-party application created in Developer Console."""


ThirdPartyApplicationRid = core.RID
"""An RID identifying a third-party application created in Developer Console."""


class Version(core.ModelBase):
    """Version"""

    version: VersionVersion
    """The semantic version of the Website."""


VersionVersion = str
"""The semantic version of the Website."""


class Website(core.ModelBase):
    """Website"""

    deployed_version: typing.Optional[VersionVersion] = pydantic.Field(alias=str("deployedVersion"), default=None)  # type: ignore[literal-required]
    """The version of the Website that is currently deployed."""

    subdomains: typing.List[Subdomain]
    """The subdomains from which the Website is currently served."""


__all__ = [
    "ListVersionsResponse",
    "Subdomain",
    "ThirdPartyApplication",
    "ThirdPartyApplicationRid",
    "Version",
    "VersionVersion",
    "Website",
]
