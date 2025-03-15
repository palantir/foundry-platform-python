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
import typing_extensions

from foundry import _core as core


class ListVersionsResponse(pydantic.BaseModel):
    """ListVersionsResponse"""

    data: typing.List[Version]
    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ListVersionsResponseDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            ListVersionsResponseDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class ListVersionsResponseDict(typing_extensions.TypedDict):
    """ListVersionsResponse"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    data: typing.List[VersionDict]
    nextPageToken: typing_extensions.NotRequired[core_models.PageToken]


Subdomain = str
"""A subdomain from which a website is served."""


class ThirdPartyApplication(pydantic.BaseModel):
    """ThirdPartyApplication"""

    rid: ThirdPartyApplicationRid
    """An RID identifying a third-party application created in Developer Console."""

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ThirdPartyApplicationDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            ThirdPartyApplicationDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class ThirdPartyApplicationDict(typing_extensions.TypedDict):
    """ThirdPartyApplication"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    rid: ThirdPartyApplicationRid
    """An RID identifying a third-party application created in Developer Console."""


ThirdPartyApplicationRid = core.RID
"""An RID identifying a third-party application created in Developer Console."""


class Version(pydantic.BaseModel):
    """Version"""

    version: VersionVersion
    """The semantic version of the Website."""

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "VersionDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(VersionDict, self.model_dump(by_alias=True, exclude_none=True))


class VersionDict(typing_extensions.TypedDict):
    """Version"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    version: VersionVersion
    """The semantic version of the Website."""


VersionVersion = str
"""The semantic version of the Website."""


class Website(pydantic.BaseModel):
    """Website"""

    deployed_version: typing.Optional[VersionVersion] = pydantic.Field(alias=str("deployedVersion"), default=None)  # type: ignore[literal-required]
    """The version of the Website that is currently deployed."""

    subdomains: typing.List[Subdomain]
    """The subdomains from which the Website is currently served."""

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "WebsiteDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(WebsiteDict, self.model_dump(by_alias=True, exclude_none=True))


class WebsiteDict(typing_extensions.TypedDict):
    """Website"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    deployedVersion: typing_extensions.NotRequired[VersionVersion]
    """The version of the Website that is currently deployed."""

    subdomains: typing.List[Subdomain]
    """The subdomains from which the Website is currently served."""


from foundry.v2.core import models as core_models  # noqa: E402

__all__ = [
    "ListVersionsResponse",
    "ListVersionsResponseDict",
    "Subdomain",
    "ThirdPartyApplication",
    "ThirdPartyApplicationDict",
    "ThirdPartyApplicationRid",
    "Version",
    "VersionDict",
    "VersionVersion",
    "Website",
    "WebsiteDict",
]
