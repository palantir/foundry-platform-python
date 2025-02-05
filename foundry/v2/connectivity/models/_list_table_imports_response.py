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

from foundry.v2.connectivity.models._list_table_imports_response_dict import (
    ListTableImportsResponseDict,
)  # NOQA
from foundry.v2.connectivity.models._table_import import TableImport
from foundry.v2.core.models._page_token import PageToken


class ListTableImportsResponse(pydantic.BaseModel):
    """ListTableImportsResponse"""

    data: List[TableImport]

    next_page_token: Optional[PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> ListTableImportsResponseDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(ListTableImportsResponseDict, self.model_dump(by_alias=True, exclude_none=True))
