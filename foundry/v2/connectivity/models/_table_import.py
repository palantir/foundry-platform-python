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

from typing import Optional
from typing import cast

import pydantic

from foundry.v2.connectivity.models._connection_rid import ConnectionRid
from foundry.v2.connectivity.models._table_import_allow_schema_changes import (
    TableImportAllowSchemaChanges,
)  # NOQA
from foundry.v2.connectivity.models._table_import_config import TableImportConfig
from foundry.v2.connectivity.models._table_import_dict import TableImportDict
from foundry.v2.connectivity.models._table_import_display_name import TableImportDisplayName  # NOQA
from foundry.v2.connectivity.models._table_import_mode import TableImportMode
from foundry.v2.connectivity.models._table_import_rid import TableImportRid
from foundry.v2.datasets.models._branch_name import BranchName
from foundry.v2.datasets.models._dataset_rid import DatasetRid


class TableImport(pydantic.BaseModel):
    """TableImport"""

    rid: TableImportRid

    connection_rid: ConnectionRid = pydantic.Field(alias=str("connectionRid"))  # type: ignore[literal-required]

    """The RID of the Connection (also known as a source) that the Table Import uses to import data."""

    dataset_rid: DatasetRid = pydantic.Field(alias=str("datasetRid"))  # type: ignore[literal-required]

    """The RID of the output dataset."""

    branch_name: Optional[BranchName] = pydantic.Field(alias=str("branchName"), default=None)  # type: ignore[literal-required]

    """The branch name in the output dataset that will contain the imported data. Defaults to `master` for most enrollments."""

    display_name: TableImportDisplayName = pydantic.Field(alias=str("displayName"))  # type: ignore[literal-required]

    import_mode: TableImportMode = pydantic.Field(alias=str("importMode"))  # type: ignore[literal-required]

    allow_schema_changes: TableImportAllowSchemaChanges = pydantic.Field(alias=str("allowSchemaChanges"))  # type: ignore[literal-required]

    """Allow the TableImport to succeed if the schema of imported rows does not match the existing dataset's schema. Defaults to false for new table imports."""

    config: TableImportConfig

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> TableImportDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(TableImportDict, self.model_dump(by_alias=True, exclude_none=True))
