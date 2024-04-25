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
from typing import cast

from pydantic import BaseModel

from foundry.models._chat_completion_request_dict import ChatCompletionRequestDict
from foundry.models._chat_message import ChatMessage
from foundry.models._parameter_key import ParameterKey
from foundry.models._parameter_value import ParameterValue


class ChatCompletionRequest(BaseModel):
    """ChatCompletionRequest"""

    messages: List[ChatMessage]

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

    model_config = {"extra": "allow"}

    def to_dict(self) -> ChatCompletionRequestDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(ChatCompletionRequestDict, self.model_dump(by_alias=True, exclude_unset=True))
