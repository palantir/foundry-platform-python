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

from typing import Literal

from typing_extensions import TypedDict

from foundry.models._attachment_rid import AttachmentRid
from foundry.models._filename import Filename
from foundry.models._media_type import MediaType
from foundry.models._size_bytes import SizeBytes


class AttachmentV2Dict(TypedDict):
    """The representation of an attachment."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    filename: Filename

    mediaType: MediaType

    rid: AttachmentRid

    sizeBytes: SizeBytes

    type: Literal["single"]
