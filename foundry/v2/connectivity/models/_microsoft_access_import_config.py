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

from foundry.v2.connectivity.models._microsoft_access_import_config_dict import (
    MicrosoftAccessImportConfigDict,
)  # NOQA


class MicrosoftAccessImportConfig(pydantic.BaseModel):
    """The import configuration for a [Microsoft Access connection](docs/foundry/available-connectors/microsoft-access)."""

    query: str

    """
    A single SQL query can be executed per sync, which should output a data table 
    and avoid operations like invoking stored procedures. 
    The query results are saved to the output dataset in Foundry.
    """

    type: Literal["microsoftAccessImportConfig"] = "microsoftAccessImportConfig"

    model_config = {"extra": "allow"}

    def to_dict(self) -> MicrosoftAccessImportConfigDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(
            MicrosoftAccessImportConfigDict, self.model_dump(by_alias=True, exclude_unset=True)
        )
