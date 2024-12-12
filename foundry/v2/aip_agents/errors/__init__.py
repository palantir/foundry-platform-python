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


from foundry.v2.aip_agents.errors._agent_iterations_exceeded_limit import (
    AgentIterationsExceededLimit,
)  # NOQA
from foundry.v2.aip_agents.errors._agent_not_found import AgentNotFound
from foundry.v2.aip_agents.errors._agent_version_not_found import AgentVersionNotFound
from foundry.v2.aip_agents.errors._blocking_continue_session_permission_denied import (
    BlockingContinueSessionPermissionDenied,
)  # NOQA
from foundry.v2.aip_agents.errors._cancel_session_failed_message_not_in_progress import (
    CancelSessionFailedMessageNotInProgress,
)  # NOQA
from foundry.v2.aip_agents.errors._cancel_session_permission_denied import (
    CancelSessionPermissionDenied,
)  # NOQA
from foundry.v2.aip_agents.errors._content_not_found import ContentNotFound
from foundry.v2.aip_agents.errors._context_size_exceeded_limit import (
    ContextSizeExceededLimit,
)  # NOQA
from foundry.v2.aip_agents.errors._create_session_permission_denied import (
    CreateSessionPermissionDenied,
)  # NOQA
from foundry.v2.aip_agents.errors._function_locator_not_found import FunctionLocatorNotFound  # NOQA
from foundry.v2.aip_agents.errors._get_all_sessions_agents_permission_denied import (
    GetAllSessionsAgentsPermissionDenied,
)  # NOQA
from foundry.v2.aip_agents.errors._get_rag_context_for_session_permission_denied import (
    GetRagContextForSessionPermissionDenied,
)  # NOQA
from foundry.v2.aip_agents.errors._invalid_agent_version import InvalidAgentVersion
from foundry.v2.aip_agents.errors._invalid_parameter import InvalidParameter
from foundry.v2.aip_agents.errors._invalid_parameter_type import InvalidParameterType
from foundry.v2.aip_agents.errors._list_sessions_for_agents_permission_denied import (
    ListSessionsForAgentsPermissionDenied,
)  # NOQA
from foundry.v2.aip_agents.errors._no_published_agent_version import NoPublishedAgentVersion  # NOQA
from foundry.v2.aip_agents.errors._object_type_ids_not_found import ObjectTypeIdsNotFound  # NOQA
from foundry.v2.aip_agents.errors._object_type_rids_not_found import ObjectTypeRidsNotFound  # NOQA
from foundry.v2.aip_agents.errors._rate_limit_exceeded import RateLimitExceeded
from foundry.v2.aip_agents.errors._session_execution_failed import SessionExecutionFailed  # NOQA
from foundry.v2.aip_agents.errors._session_not_found import SessionNotFound
from foundry.v2.aip_agents.errors._streaming_continue_session_permission_denied import (
    StreamingContinueSessionPermissionDenied,
)  # NOQA

__all__ = [
    "AgentIterationsExceededLimit",
    "AgentNotFound",
    "AgentVersionNotFound",
    "BlockingContinueSessionPermissionDenied",
    "CancelSessionFailedMessageNotInProgress",
    "CancelSessionPermissionDenied",
    "ContentNotFound",
    "ContextSizeExceededLimit",
    "CreateSessionPermissionDenied",
    "FunctionLocatorNotFound",
    "GetAllSessionsAgentsPermissionDenied",
    "GetRagContextForSessionPermissionDenied",
    "InvalidAgentVersion",
    "InvalidParameter",
    "InvalidParameterType",
    "ListSessionsForAgentsPermissionDenied",
    "NoPublishedAgentVersion",
    "ObjectTypeIdsNotFound",
    "ObjectTypeRidsNotFound",
    "RateLimitExceeded",
    "SessionExecutionFailed",
    "SessionNotFound",
    "StreamingContinueSessionPermissionDenied",
]
