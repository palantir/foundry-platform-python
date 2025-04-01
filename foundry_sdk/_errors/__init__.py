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


from foundry_sdk._errors.api_not_found import ApiNotFoundError
from foundry_sdk._errors.connection_error import ConnectionError
from foundry_sdk._errors.connection_error import ProxyError
from foundry_sdk._errors.environment_not_configured import EnvironmentNotConfigured
from foundry_sdk._errors.not_authenticated import NotAuthenticated
from foundry_sdk._errors.palantir_exception import PalantirException
from foundry_sdk._errors.palantir_rpc_exception import BadRequestError
from foundry_sdk._errors.palantir_rpc_exception import ConflictError
from foundry_sdk._errors.palantir_rpc_exception import InternalServerError
from foundry_sdk._errors.palantir_rpc_exception import NotFoundError
from foundry_sdk._errors.palantir_rpc_exception import PalantirRPCException
from foundry_sdk._errors.palantir_rpc_exception import PermissionDeniedError
from foundry_sdk._errors.palantir_rpc_exception import RateLimitError
from foundry_sdk._errors.palantir_rpc_exception import RequestEntityTooLargeError
from foundry_sdk._errors.palantir_rpc_exception import UnauthorizedError
from foundry_sdk._errors.palantir_rpc_exception import UnprocessableEntityError
from foundry_sdk._errors.sdk_internal_error import SDKInternalError
from foundry_sdk._errors.sdk_internal_error import handle_unexpected
from foundry_sdk._errors.stream_error import StreamConsumedError
from foundry_sdk._errors.timeout_error import ConnectTimeout
from foundry_sdk._errors.timeout_error import ReadTimeout
from foundry_sdk._errors.timeout_error import TimeoutError
from foundry_sdk._errors.timeout_error import WriteTimeout
from foundry_sdk._errors.utils import deserialize_error
