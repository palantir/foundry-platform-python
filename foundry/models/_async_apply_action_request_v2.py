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
from typing import Optional
from typing import cast

from pydantic import BaseModel

from foundry.models._async_apply_action_request_v2_dict import AsyncApplyActionRequestV2Dict  # NOQA
from foundry.models._data_value import DataValue
from foundry.models._parameter_id import ParameterId


class AsyncApplyActionRequestV2(BaseModel):
    """AsyncApplyActionRequestV2"""

    parameters: Dict[ParameterId, Optional[DataValue]]

    model_config = {"extra": "allow"}

    def to_dict(self) -> AsyncApplyActionRequestV2Dict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(
            AsyncApplyActionRequestV2Dict, self.model_dump(by_alias=True, exclude_unset=True)
        )
