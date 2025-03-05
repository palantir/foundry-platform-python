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


from foundry._core import ApiResponse
from foundry._core import Auth
from foundry._core import ConfidentialClientAuth
from foundry._core import Config
from foundry._core import PublicClientAuth
from foundry._core import ResourceIterator
from foundry._core import StreamedApiResponse
from foundry._core import StreamingContextManager
from foundry._core import UserTokenAuth
from foundry._errors import ApiNotFoundError
from foundry._errors import BadRequestError
from foundry._errors import ConflictError
from foundry._errors import ConnectionError
from foundry._errors import ConnectTimeout
from foundry._errors import EnvironmentNotConfigured
from foundry._errors import InternalServerError
from foundry._errors import NotAuthenticated
from foundry._errors import NotFoundError
from foundry._errors import PalantirException
from foundry._errors import PalantirRPCException
from foundry._errors import PermissionDeniedError
from foundry._errors import ProxyError
from foundry._errors import RateLimitError
from foundry._errors import ReadTimeout
from foundry._errors import RequestEntityTooLargeError
from foundry._errors import SDKInternalError
from foundry._errors import StreamConsumedError
from foundry._errors import TimeoutError
from foundry._errors import UnauthorizedError
from foundry._errors import UnprocessableEntityError
from foundry._errors import WriteTimeout

# The OpenAPI document version from the spec information
# See https://swagger.io/specification/#info-object
# The SDK version
from foundry._versions import __openapi_document_version__
from foundry._versions import __version__

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
]
