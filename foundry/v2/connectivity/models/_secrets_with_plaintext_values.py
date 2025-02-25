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
from typing import Literal
from typing import cast

import pydantic

from foundry.v2.connectivity.models._plaintext_value import PlaintextValue
from foundry.v2.connectivity.models._secret_name import SecretName
from foundry.v2.connectivity.models._secrets_with_plaintext_values_dict import (
    SecretsWithPlaintextValuesDict,
)  # NOQA


class SecretsWithPlaintextValues(pydantic.BaseModel):
    """
    A map representing secret name to plaintext secret value pairs.
    This should be used when creating or updating additional secrets for a REST connection.
    """

    secrets: Dict[SecretName, PlaintextValue]

    """The additional secrets that can be referenced in code and webhook configurations."""

    type: Literal["asSecretsWithPlaintextValues"] = "asSecretsWithPlaintextValues"

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> SecretsWithPlaintextValuesDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(
            SecretsWithPlaintextValuesDict, self.model_dump(by_alias=True, exclude_none=True)
        )
