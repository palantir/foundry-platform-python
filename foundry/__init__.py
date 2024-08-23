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


from foundry._core.confidential_client_auth import ConfidentialClientAuth
from foundry._core.foundry_token_auth_client import UserTokenAuth
from foundry._errors.environment_not_configured import EnvironmentNotConfigured
from foundry._errors.not_authenticated import NotAuthenticated
from foundry._errors.palantir_rpc_exception import PalantirRPCException

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
    "ConfidentialClientAuth",
    "UserTokenAuth",
    "NotAuthenticated",
    "EnvironmentNotConfigured",
    "PalantirRPCException",
]
