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

from typing import Union

import pydantic
from typing_extensions import Annotated

from foundry.v2.connectivity.models._jdbc_import_config_dict import JdbcImportConfigDict
from foundry.v2.connectivity.models._microsoft_access_import_config_dict import (
    MicrosoftAccessImportConfigDict,
)  # NOQA
from foundry.v2.connectivity.models._microsoft_sql_server_import_config_dict import (
    MicrosoftSqlServerImportConfigDict,
)  # NOQA
from foundry.v2.connectivity.models._oracle_import_config_dict import OracleImportConfigDict  # NOQA
from foundry.v2.connectivity.models._postgre_sql_import_config_dict import (
    PostgreSqlImportConfigDict,
)  # NOQA

TableImportConfigDict = Annotated[
    Union[
        JdbcImportConfigDict,
        MicrosoftSqlServerImportConfigDict,
        PostgreSqlImportConfigDict,
        MicrosoftAccessImportConfigDict,
        OracleImportConfigDict,
    ],
    pydantic.Field(discriminator="type"),
]
"""The import configuration for a specific [connector type](docs/foundry/data-integration/source-type-overview)."""
