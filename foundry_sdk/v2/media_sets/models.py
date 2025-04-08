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

BranchName = str
"""
A name for a media set branch. Valid branch names must be (a) non-empty, (b) less than 256 characters, and 
(c) not a valid ResourceIdentifier.
"""


BranchRid = core.RID
"""A resource identifier that identifies a branch of a media set."""


class GetMediaItemInfoResponse(pydantic.BaseModel):
    """GetMediaItemInfoResponse"""

    view_rid: core_models.MediaSetViewRid = pydantic.Field(alias=str("viewRid"))  # type: ignore[literal-required]
    path: typing.Optional[core_models.MediaItemPath] = None
    logical_timestamp: LogicalTimestamp = pydantic.Field(alias=str("logicalTimestamp"))  # type: ignore[literal-required]
    attribution: typing.Optional[MediaAttribution] = None
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


LogicalTimestamp = core.Long
"""
A number representing a logical ordering to be used for transactions, etc.
This can be interpreted as a timestamp in microseconds, but may differ slightly from system clock time due 
to clock drift and slight adjustments for the sake of ordering.

Only positive timestamps (representing times after epoch) are supported.
"""


class MediaAttribution(pydantic.BaseModel):
    """MediaAttribution"""

    creator_id: core_models.UserId = pydantic.Field(alias=str("creatorId"))  # type: ignore[literal-required]
    creation_timestamp: core.AwareDatetime = pydantic.Field(alias=str("creationTimestamp"))  # type: ignore[literal-required]
    """The timestamp when the media item was created, in ISO 8601 timestamp format."""

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class PutMediaItemResponse(pydantic.BaseModel):
    """PutMediaItemResponse"""

    media_item_rid: core_models.MediaItemRid = pydantic.Field(alias=str("mediaItemRid"))  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


TransactionId = core.UUID
"""An identifier which represents a transaction on a media set."""


__all__ = [
    "BranchName",
    "BranchRid",
    "GetMediaItemInfoResponse",
    "LogicalTimestamp",
    "MediaAttribution",
    "PutMediaItemResponse",
    "TransactionId",
]
