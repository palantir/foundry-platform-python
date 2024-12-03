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
from typing_extensions import NotRequired
from typing_extensions import TypedDict

from foundry._errors import PalantirRPCException
from foundry.v1.ontologies.models._attachment_rid import AttachmentRid


class AttachmentNotFoundParameters(TypedDict):
    """
    The requested attachment is not found, or the client token does not have access to it.
    Attachments that are not attached to any objects are deleted after two weeks.
    Attachments that have not been attached to an object can only be viewed by the user who uploaded them.
    Attachments that have been attached to an object can be viewed by users who can view the object.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    attachmentRid: NotRequired[AttachmentRid]


@dataclass
class AttachmentNotFound(PalantirRPCException):
    name: Literal["AttachmentNotFound"]
    parameters: AttachmentNotFoundParameters
    error_instance_id: str


__all__ = ["AttachmentNotFound"]
