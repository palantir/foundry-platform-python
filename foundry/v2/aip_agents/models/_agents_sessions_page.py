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
from typing import Optional
from typing import cast

import pydantic

from foundry.v2.aip_agents.models._agents_sessions_page_dict import AgentsSessionsPageDict  # NOQA
from foundry.v2.aip_agents.models._page_token import PageToken
from foundry.v2.aip_agents.models._session import Session


class AgentsSessionsPage(pydantic.BaseModel):
    """
    A page of results for sessions across all accessible Agents for the calling user.
    Sessions are returned in order of most recently updated first.
    """

    next_page_token: Optional[PageToken] = pydantic.Field(alias="nextPageToken", default=None)
    """
    The page token that should be used when requesting the next page of results.
    Empty if there are no more results to retrieve.
    """

    data: List[Session]

    model_config = {"extra": "allow"}

    def to_dict(self) -> AgentsSessionsPageDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(AgentsSessionsPageDict, self.model_dump(by_alias=True, exclude_unset=True))
