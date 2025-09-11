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

from foundry_sdk import _core as core
from foundry_sdk.v2.core import models as core_models

BranchName = str
"""
A name for a media set branch. Valid branch names must be (a) non-empty, (b) less than 256 characters, and 
(c) not a valid ResourceIdentifier.
"""


BranchRid = core.RID
"""A resource identifier that identifies a branch of a media set."""


class GetMediaItemInfoResponse(core.ModelBase):
    """GetMediaItemInfoResponse"""

    view_rid: core_models.MediaSetViewRid = pydantic.Field(alias=str("viewRid"))  # type: ignore[literal-required]
    path: typing.Optional[core_models.MediaItemPath] = None
    logical_timestamp: LogicalTimestamp = pydantic.Field(alias=str("logicalTimestamp"))  # type: ignore[literal-required]
    attribution: typing.Optional[MediaAttribution] = None


class GetMediaItemRidByPathResponse(core.ModelBase):
    """GetMediaItemRidByPathResponse"""

    media_item_rid: typing.Optional[core_models.MediaItemRid] = pydantic.Field(alias=str("mediaItemRid"), default=None)  # type: ignore[literal-required]


LogicalTimestamp = core.Long
"""
A number representing a logical ordering to be used for transactions, etc.
This can be interpreted as a timestamp in microseconds, but may differ slightly from system clock time due 
to clock drift and slight adjustments for the sake of ordering.

Only positive timestamps (representing times after epoch) are supported.
"""


class MediaAttribution(core.ModelBase):
    """MediaAttribution"""

    creator_id: core_models.UserId = pydantic.Field(alias=str("creatorId"))  # type: ignore[literal-required]
    creation_timestamp: core.AwareDatetime = pydantic.Field(alias=str("creationTimestamp"))  # type: ignore[literal-required]
    """The timestamp when the media item was created, in ISO 8601 timestamp format."""


MediaItemXmlFormat = typing.Literal["DOCX", "XLSX", "PPTX"]
"""Format of the media item attempted to be decoded based on the XML structure."""


class PutMediaItemResponse(core.ModelBase):
    """PutMediaItemResponse"""

    media_item_rid: core_models.MediaItemRid = pydantic.Field(alias=str("mediaItemRid"))  # type: ignore[literal-required]


class TrackedTransformationFailedResponse(core.ModelBase):
    """TrackedTransformationFailedResponse"""

    type: typing.Literal["failed"] = "failed"


class TrackedTransformationPendingResponse(core.ModelBase):
    """TrackedTransformationPendingResponse"""

    type: typing.Literal["pending"] = "pending"


TrackedTransformationResponse = typing_extensions.Annotated[
    typing.Union[
        TrackedTransformationPendingResponse,
        TrackedTransformationFailedResponse,
        "TrackedTransformationSuccessfulResponse",
    ],
    pydantic.Field(discriminator="type"),
]
"""TrackedTransformationResponse"""


class TrackedTransformationSuccessfulResponse(core.ModelBase):
    """TrackedTransformationSuccessfulResponse"""

    type: typing.Literal["successful"] = "successful"


TransactionId = core.UUID
"""An identifier which represents a transaction on a media set."""


core.resolve_forward_references(TrackedTransformationResponse, globalns=globals(), localns=locals())

__all__ = [
    "BranchName",
    "BranchRid",
    "GetMediaItemInfoResponse",
    "GetMediaItemRidByPathResponse",
    "LogicalTimestamp",
    "MediaAttribution",
    "MediaItemXmlFormat",
    "PutMediaItemResponse",
    "TrackedTransformationFailedResponse",
    "TrackedTransformationPendingResponse",
    "TrackedTransformationResponse",
    "TrackedTransformationSuccessfulResponse",
    "TransactionId",
]
