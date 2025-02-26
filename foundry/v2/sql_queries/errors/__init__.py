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


from foundry.v2.sql_queries.errors._cancel_query_permission_denied import (
    CancelQueryPermissionDenied,
)  # NOQA
from foundry.v2.sql_queries.errors._execute_query_permission_denied import (
    ExecuteQueryPermissionDenied,
)  # NOQA
from foundry.v2.sql_queries.errors._get_results_permission_denied import (
    GetResultsPermissionDenied,
)  # NOQA
from foundry.v2.sql_queries.errors._get_status_permission_denied import (
    GetStatusPermissionDenied,
)  # NOQA
from foundry.v2.sql_queries.errors._query_canceled import QueryCanceled
from foundry.v2.sql_queries.errors._query_failed import QueryFailed
from foundry.v2.sql_queries.errors._query_parse_error import QueryParseError
from foundry.v2.sql_queries.errors._query_permission_denied import QueryPermissionDenied
from foundry.v2.sql_queries.errors._query_running import QueryRunning
from foundry.v2.sql_queries.errors._read_query_inputs_permission_denied import (
    ReadQueryInputsPermissionDenied,
)  # NOQA

__all__ = [
    "CancelQueryPermissionDenied",
    "ExecuteQueryPermissionDenied",
    "GetResultsPermissionDenied",
    "GetStatusPermissionDenied",
    "QueryCanceled",
    "QueryFailed",
    "QueryParseError",
    "QueryPermissionDenied",
    "QueryRunning",
    "ReadQueryInputsPermissionDenied",
]
