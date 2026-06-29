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


from foundry_sdk._errors.api_not_found import ApiNotFoundError as ApiNotFoundError
from foundry_sdk._errors.connection_error import ConnectionError as ConnectionError
from foundry_sdk._errors.connection_error import ProxyError as ProxyError
from foundry_sdk._errors.environment_not_configured import (
    EnvironmentNotConfigured as EnvironmentNotConfigured,
)  # NOQA
from foundry_sdk._errors.not_authenticated import NotAuthenticated as NotAuthenticated
from foundry_sdk._errors.palantir_exception import PalantirException as PalantirException  # NOQA
from foundry_sdk._errors.palantir_qos_exception import (
    PalantirQoSException as PalantirQoSException,
)  # NOQA
from foundry_sdk._errors.palantir_qos_exception import RateLimitError as RateLimitError
from foundry_sdk._errors.palantir_qos_exception import (
    ServiceUnavailable as ServiceUnavailable,
)  # NOQA
from foundry_sdk._errors.palantir_rpc_exception import BadRequestError as BadRequestError  # NOQA
from foundry_sdk._errors.palantir_rpc_exception import ConflictError as ConflictError
from foundry_sdk._errors.palantir_rpc_exception import (
    InternalServerError as InternalServerError,
)  # NOQA
from foundry_sdk._errors.palantir_rpc_exception import NotFoundError as NotFoundError
from foundry_sdk._errors.palantir_rpc_exception import (
    PalantirRPCException as PalantirRPCException,
)  # NOQA
from foundry_sdk._errors.palantir_rpc_exception import (
    PermissionDeniedError as PermissionDeniedError,
)  # NOQA
from foundry_sdk._errors.palantir_rpc_exception import (
    RequestEntityTooLargeError as RequestEntityTooLargeError,
)  # NOQA
from foundry_sdk._errors.palantir_rpc_exception import (
    UnauthorizedError as UnauthorizedError,
)  # NOQA
from foundry_sdk._errors.palantir_rpc_exception import (
    UnprocessableEntityError as UnprocessableEntityError,
)  # NOQA
from foundry_sdk._errors.sdk_internal_error import SDKInternalError as SDKInternalError
from foundry_sdk._errors.sdk_internal_error import handle_unexpected as handle_unexpected  # NOQA
from foundry_sdk._errors.sse_error import SseContentTypeError as SseContentTypeError
from foundry_sdk._errors.sse_error import SseEventDecodeError as SseEventDecodeError
from foundry_sdk._errors.stream_error import StreamConsumedError as StreamConsumedError
from foundry_sdk._errors.timeout_error import ConnectTimeout as ConnectTimeout
from foundry_sdk._errors.timeout_error import ReadTimeout as ReadTimeout
from foundry_sdk._errors.timeout_error import TimeoutError as TimeoutError
from foundry_sdk._errors.timeout_error import WriteTimeout as WriteTimeout
from foundry_sdk._errors.utils import deserialize_error as deserialize_error
