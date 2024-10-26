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

from datetime import datetime

import pydantic
from typing_extensions import TypedDict


class SessionMetadataDict(TypedDict):
    """Metadata for a conversation session with an Agent."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    title: pydantic.StrictStr
    """The title of the session."""

    createdTime: datetime
    """The time the session was created."""

    updatedTime: datetime
    """The time the session was last updated."""

    messageCount: pydantic.StrictInt
    """
    The count of messages in the session. Includes both user messages and Agent replies, so each
    complete exchange counts as two messages.
    """

    estimatedExpiresTime: datetime
    """
    The estimated time the session is due to expire. Once a session has expired, it can no longer
    be accessed and a new session must be created.
    The expiry time is automatically extended when new exchanges are added to the session.
    """
