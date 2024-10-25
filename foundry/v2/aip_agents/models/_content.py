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

from typing import List
from typing import cast

import pydantic

from foundry.v2.aip_agents.models._content_dict import ContentDict
from foundry.v2.aip_agents.models._session_exchange import SessionExchange


class Content(pydantic.BaseModel):
    """Content"""

    exchanges: List[SessionExchange]
    """
    The conversation history for the session, represented as a list of exchanges.
    Each exchange represents an initiating message from the user and the Agent's response.
    Exchanges are returned in chronological order, starting with the first exchange.
    """

    model_config = {"extra": "allow"}

    def to_dict(self) -> ContentDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(ContentDict, self.model_dump(by_alias=True, exclude_unset=True))
