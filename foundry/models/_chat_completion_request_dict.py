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

from typing import Dict
from typing import List

from typing_extensions import TypedDict

from foundry.models._chat_message_dict import ChatMessageDict
from foundry.models._parameter_key import ParameterKey
from foundry.models._parameter_value import ParameterValue


class ChatCompletionRequestDict(TypedDict):
    """ChatCompletionRequest"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    messages: List[ChatMessageDict]

    parameters: Dict[ParameterKey, ParameterValue]
    """
    Any additional model-specific parameters:
    - for global models, the keys can be one of the following
        (refer to https://platform.openai.com/docs/api-reference/chat/create for documentation on these parameters):
      - `temperature`
      - `top_p`
      - `n`
      - `stop`
      - `max_tokens`
      - `presence_penalty`
      - `frequency_penalty`
      - `logit_bias`
    """
