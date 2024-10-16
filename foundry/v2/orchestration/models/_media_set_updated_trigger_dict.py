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

from foundry.v2.core.models._media_set_rid import MediaSetRid
from foundry.v2.datasets.models._branch_name import BranchName


class MediaSetUpdatedTriggerDict(TypedDict):
    """
    Trigger whenever an update is made to a media set on the target
    branch. For transactional media sets, this happens when a transaction
    is committed. For non-transactional media sets, this event happens
    eventually (but not necessary immediately) after an update.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    mediaSetRid: MediaSetRid

    branchName: BranchName

    type: Literal["mediaSetUpdated"]
