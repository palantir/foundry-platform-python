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

from typing_extensions import TypedDict

from foundry.v1.models._object_set_stream_subscribe_request_dict import (
    ObjectSetStreamSubscribeRequestDict,
)  # NOQA
from foundry.v1.models._request_id import RequestId


class ObjectSetStreamSubscribeRequestsDict(TypedDict):
    """
    The list of object sets that should be subscribed to. A client can stop subscribing to an object set
    by removing the request from subsequent ObjectSetStreamSubscribeRequests.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    id: RequestId

    requests: List[ObjectSetStreamSubscribeRequestDict]
