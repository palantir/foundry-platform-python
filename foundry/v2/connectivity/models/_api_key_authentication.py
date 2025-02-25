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

from foundry.v2.connectivity.models._api_key_authentication_dict import (
    ApiKeyAuthenticationDict,
)  # NOQA
from foundry.v2.connectivity.models._encrypted_property import EncryptedProperty
from foundry.v2.connectivity.models._rest_request_api_key_location import (
    RestRequestApiKeyLocation,
)  # NOQA


class ApiKeyAuthentication(pydantic.BaseModel):
    """
    The API key used to authenticate to the external system.
    This can be configured as a header or query parameter.
    """

    location: RestRequestApiKeyLocation

    """The location of the API key in the request."""

    api_key: EncryptedProperty = pydantic.Field(alias=str("apiKey"))  # type: ignore[literal-required]

    """The value of the API key."""

    type: Literal["apiKey"] = "apiKey"

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> ApiKeyAuthenticationDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(ApiKeyAuthenticationDict, self.model_dump(by_alias=True, exclude_none=True))
