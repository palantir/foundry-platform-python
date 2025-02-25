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
from typing import cast

import pydantic

from foundry.v2.connectivity.models._rest_connection_o_auth2_dict import (
    RestConnectionOAuth2Dict,
)  # NOQA


class RestConnectionOAuth2(pydantic.BaseModel):
    """
    In order to use OAuth2 you must have an Outbound application configured in the [Foundry Control Panel Organization settings](/docs/foundry/administration/configure-outbound-applications#create-an-outbound-application).
    The RID of the Outbound application must be configured in the RestConnectionConfiguration in the `oauth2ClientRid` field.
    """

    type: Literal["oauth2"] = "oauth2"

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> RestConnectionOAuth2Dict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(RestConnectionOAuth2Dict, self.model_dump(by_alias=True, exclude_none=True))
