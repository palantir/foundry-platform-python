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
from typing import cast

import pydantic

from foundry.v2.aip_agents.models._session_metadata_dict import SessionMetadataDict


class SessionMetadata(pydantic.BaseModel):
    """Metadata for a conversation session with an Agent."""

    title: pydantic.StrictStr
    """The title of the session."""

    created_time: datetime = pydantic.Field(alias="createdTime")
    """The time the session was created."""

    updated_time: datetime = pydantic.Field(alias="updatedTime")
    """The time the session was last updated."""

    message_count: pydantic.StrictInt = pydantic.Field(alias="messageCount")
    """
    The count of messages in the session. Includes both user messages and Agent replies, so each
    complete exchange counts as two messages.
    """

    estimated_expires_time: datetime = pydantic.Field(alias="estimatedExpiresTime")
    """
    The estimated time the session is due to expire. Once a session has expired, it can no longer
    be accessed and a new session must be created.
    The expiry time is automatically extended when new exchanges are added to the session.
    """

    model_config = {"extra": "allow"}

    def to_dict(self) -> SessionMetadataDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(SessionMetadataDict, self.model_dump(by_alias=True, exclude_unset=True))
