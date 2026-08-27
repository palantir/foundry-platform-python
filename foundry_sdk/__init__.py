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


from foundry_sdk._core import (
    ApiResponse,
    ArrowTableResponse,
    AsyncApiResponse,
    AsyncPageIterator,
    AsyncResourceIterator,
    Auth,
    ConfidentialClientAuth,
    Config,
    PageIterator,
    ParquetTableResponse,
    PublicClientAuth,
    ResourceIterator,
    StreamedApiResponse,
    StreamingContextManager,
    TableResponse,
    UserTokenAuth,
)

# Context and environment variables
from foundry_sdk._core.context_and_environment_vars import (
    ADDITIONAL_USER_AGENTS,
    ATTRIBUTION_VAR,
    HOSTNAME_ENV_VAR,
    HOSTNAME_VAR,
    SAMPLED_ENV_VAR,
    SAMPLED_VAR,
    SCENARIO_RID_VAR,
    SPAN_ID_ENV_VAR,
    SPAN_ID_VAR,
    TOKEN_ENV_VAR,
    TOKEN_VAR,
    TRACE_ID_ENV_VAR,
    TRACE_ID_VAR,
    TRANSACTION_ID_VAR,
)
from foundry_sdk._errors import (
    ApiNotFoundError,
    BadRequestError,
    ConflictError,
    ConnectionError,
    ConnectTimeout,
    EnvironmentNotConfigured,
    InternalServerError,
    NotAuthenticated,
    NotFoundError,
    PalantirException,
    PalantirRPCException,
    PermissionDeniedError,
    ProxyError,
    RateLimitError,
    ReadTimeout,
    RequestEntityTooLargeError,
    SDKInternalError,
    ServiceUnavailable,
    StreamConsumedError,
    TimeoutError,
    UnauthorizedError,
    UnprocessableEntityError,
    WriteTimeout,
)

# The OpenAPI document version from the spec information
# See https://swagger.io/specification/#info-object
# The SDK version
from foundry_sdk._version import __openapi_document_version__, __version__
from foundry_sdk.v2 import AsyncFoundryClient, FoundryClient

# The OpenAPI specification version
# See https://swagger.io/specification/#versions


__all__ = [
    "__version__",
    "__openapi_document_version__",
    "Auth",
    "ConfidentialClientAuth",
    "PublicClientAuth",
    "UserTokenAuth",
    "Config",
    "ADDITIONAL_USER_AGENTS",
    "ATTRIBUTION_VAR",
    "HOSTNAME_VAR",
    "HOSTNAME_ENV_VAR",
    "SAMPLED_ENV_VAR",
    "SAMPLED_VAR",
    "SCENARIO_RID_VAR",
    "SPAN_ID_ENV_VAR",
    "SPAN_ID_VAR",
    "TOKEN_VAR",
    "TOKEN_ENV_VAR",
    "TRACE_ID_ENV_VAR",
    "TRACE_ID_VAR",
    "TRANSACTION_ID_VAR",
    "PalantirException",
    "EnvironmentNotConfigured",
    "NotAuthenticated",
    "ConnectionError",
    "ProxyError",
    "PalantirRPCException",
    "BadRequestError",
    "UnauthorizedError",
    "PermissionDeniedError",
    "NotFoundError",
    "UnprocessableEntityError",
    "RateLimitError",
    "ServiceUnavailable",
    "RequestEntityTooLargeError",
    "ConflictError",
    "InternalServerError",
    "SDKInternalError",
    "StreamConsumedError",
    "ConnectTimeout",
    "ReadTimeout",
    "WriteTimeout",
    "TimeoutError",
    "ApiNotFoundError",
    "FoundryClient",
    "AsyncFoundryClient",
    "ResourceIterator",
    "AsyncResourceIterator",
    "PageIterator",
    "AsyncPageIterator",
]
