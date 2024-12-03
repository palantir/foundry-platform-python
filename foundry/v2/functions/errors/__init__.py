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


from foundry.v2.functions.errors._execute_query_permission_denied import (
    ExecuteQueryPermissionDenied,
)  # NOQA
from foundry.v2.functions.errors._get_by_rid_queries_permission_denied import (
    GetByRidQueriesPermissionDenied,
)  # NOQA
from foundry.v2.functions.errors._invalid_query_parameter_value import (
    InvalidQueryParameterValue,
)  # NOQA
from foundry.v2.functions.errors._missing_parameter import MissingParameter
from foundry.v2.functions.errors._query_encountered_user_facing_error import (
    QueryEncounteredUserFacingError,
)  # NOQA
from foundry.v2.functions.errors._query_memory_exceeded_limit import (
    QueryMemoryExceededLimit,
)  # NOQA
from foundry.v2.functions.errors._query_not_found import QueryNotFound
from foundry.v2.functions.errors._query_runtime_error import QueryRuntimeError
from foundry.v2.functions.errors._query_time_exceeded_limit import QueryTimeExceededLimit  # NOQA
from foundry.v2.functions.errors._unknown_parameter import UnknownParameter
from foundry.v2.functions.errors._value_type_not_found import ValueTypeNotFound
from foundry.v2.functions.errors._version_id_not_found import VersionIdNotFound

__all__ = [
    "ExecuteQueryPermissionDenied",
    "GetByRidQueriesPermissionDenied",
    "InvalidQueryParameterValue",
    "MissingParameter",
    "QueryEncounteredUserFacingError",
    "QueryMemoryExceededLimit",
    "QueryNotFound",
    "QueryRuntimeError",
    "QueryTimeExceededLimit",
    "UnknownParameter",
    "ValueTypeNotFound",
    "VersionIdNotFound",
]
