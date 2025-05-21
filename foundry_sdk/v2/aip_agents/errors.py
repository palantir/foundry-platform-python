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


import typing
from dataclasses import dataclass

import typing_extensions

from foundry_sdk import _core as core
from foundry_sdk import _errors as errors
from foundry_sdk.v2.aip_agents import models as aip_agents_models
from foundry_sdk.v2.ontologies import models as ontologies_models


class AgentIterationsExceededLimitParameters(typing_extensions.TypedDict):
    """
    The Agent was unable to produce an answer in the set number of maximum iterations.
    This can happen if the Agent gets confused or stuck in a loop, or if the query is too complex.
    Try a different query or review the Agent configuration in AIP Agent Studio.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    agentRid: aip_agents_models.AgentRid
    sessionRid: aip_agents_models.SessionRid
    details: str
    """Any additional details provided for the error."""


@dataclass
class AgentIterationsExceededLimit(errors.BadRequestError):
    name: typing.Literal["AgentIterationsExceededLimit"]
    parameters: AgentIterationsExceededLimitParameters
    error_instance_id: str


class AgentNotFoundParameters(typing_extensions.TypedDict):
    """The given Agent could not be found."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    agentRid: aip_agents_models.AgentRid
    """An RID identifying an AIP Agent created in [AIP Agent Studio](https://palantir.com/docs/foundry/agent-studio/overview/)."""


@dataclass
class AgentNotFound(errors.NotFoundError):
    name: typing.Literal["AgentNotFound"]
    parameters: AgentNotFoundParameters
    error_instance_id: str


class AgentVersionNotFoundParameters(typing_extensions.TypedDict):
    """The given AgentVersion could not be found."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    agentRid: aip_agents_models.AgentRid
    """An RID identifying an AIP Agent created in [AIP Agent Studio](https://palantir.com/docs/foundry/agent-studio/overview/)."""

    agentVersionString: aip_agents_models.AgentVersionString
    """The semantic version of the Agent, formatted as "majorVersion.minorVersion"."""


@dataclass
class AgentVersionNotFound(errors.NotFoundError):
    name: typing.Literal["AgentVersionNotFound"]
    parameters: AgentVersionNotFoundParameters
    error_instance_id: str


class BlockingContinueSessionPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not blockingContinue the Session."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    agentRid: aip_agents_models.AgentRid
    """An RID identifying an AIP Agent created in [AIP Agent Studio](https://palantir.com/docs/foundry/agent-studio/overview/)."""

    sessionRid: aip_agents_models.SessionRid
    """The Resource Identifier (RID) of the conversation session."""


@dataclass
class BlockingContinueSessionPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["BlockingContinueSessionPermissionDenied"]
    parameters: BlockingContinueSessionPermissionDeniedParameters
    error_instance_id: str


class CancelSessionFailedMessageNotInProgressParameters(typing_extensions.TypedDict):
    """
    Unable to cancel the requested session exchange as no in-progress exchange was found
    for the provided message identifier.
    This is expected if no exchange was initiated with the provided message identifier
    through a `streamingContinue` request, or if the exchange for this identifier has already completed
    and cannot be canceled, or if the exchange has already been canceled.
    This error can also occur if the cancellation was requested immediately after requesting the exchange
    through a `streamingContinue` request, and the exchange has not started yet.
    Clients should handle these errors gracefully, and can reload the session content to get the latest
    conversation state.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    messageId: aip_agents_models.MessageId
    """The message identifier that was requested for cancellation."""

    agentRid: aip_agents_models.AgentRid
    sessionRid: aip_agents_models.SessionRid


@dataclass
class CancelSessionFailedMessageNotInProgress(errors.BadRequestError):
    name: typing.Literal["CancelSessionFailedMessageNotInProgress"]
    parameters: CancelSessionFailedMessageNotInProgressParameters
    error_instance_id: str


class CancelSessionPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not cancel the Session."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    agentRid: aip_agents_models.AgentRid
    """An RID identifying an AIP Agent created in [AIP Agent Studio](https://palantir.com/docs/foundry/agent-studio/overview/)."""

    sessionRid: aip_agents_models.SessionRid
    """The Resource Identifier (RID) of the conversation session."""


@dataclass
class CancelSessionPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["CancelSessionPermissionDenied"]
    parameters: CancelSessionPermissionDeniedParameters
    error_instance_id: str


class ContentNotFoundParameters(typing_extensions.TypedDict):
    """The given Content could not be found."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    agentRid: aip_agents_models.AgentRid
    """An RID identifying an AIP Agent created in [AIP Agent Studio](https://palantir.com/docs/foundry/agent-studio/overview/)."""

    sessionRid: aip_agents_models.SessionRid
    """The Resource Identifier (RID) of the conversation session."""


@dataclass
class ContentNotFound(errors.NotFoundError):
    name: typing.Literal["ContentNotFound"]
    parameters: ContentNotFoundParameters
    error_instance_id: str


class ContextSizeExceededLimitParameters(typing_extensions.TypedDict):
    """
    Failed to generate a response for a session because the context size of the LLM has been exceeded.
    Clients should either retry with a shorter message or create a new session and try re-sending the message.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    agentRid: aip_agents_models.AgentRid
    sessionRid: aip_agents_models.SessionRid
    details: str
    """Any additional details provided for the error."""


@dataclass
class ContextSizeExceededLimit(errors.BadRequestError):
    name: typing.Literal["ContextSizeExceededLimit"]
    parameters: ContextSizeExceededLimitParameters
    error_instance_id: str


class CreateSessionPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not create the Session."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    agentRid: aip_agents_models.AgentRid
    """An RID identifying an AIP Agent created in [AIP Agent Studio](https://palantir.com/docs/foundry/agent-studio/overview/)."""


@dataclass
class CreateSessionPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["CreateSessionPermissionDenied"]
    parameters: CreateSessionPermissionDeniedParameters
    error_instance_id: str


class FunctionLocatorNotFoundParameters(typing_extensions.TypedDict):
    """
    The specified function locator is configured for use by the Agent but could not be found.
    The function type or version may not exist or the client token does not have access.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    agentRid: aip_agents_models.AgentRid
    sessionRid: typing_extensions.NotRequired[aip_agents_models.SessionRid]
    """The session RID where the error occurred. This is omitted if the error occurred during session creation."""

    functionRid: core.RID
    functionVersion: str


@dataclass
class FunctionLocatorNotFound(errors.NotFoundError):
    name: typing.Literal["FunctionLocatorNotFound"]
    parameters: FunctionLocatorNotFoundParameters
    error_instance_id: str


class GetAllSessionsAgentsPermissionDeniedParameters(typing_extensions.TypedDict):
    """
    The calling user does not have permission to list all sessions across all Agents.
    Listing all sessions across all agents requires the `api:aip-agents-write` scope.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class GetAllSessionsAgentsPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["GetAllSessionsAgentsPermissionDenied"]
    parameters: GetAllSessionsAgentsPermissionDeniedParameters
    error_instance_id: str


class GetRagContextForSessionPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not ragContext the Session."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    agentRid: aip_agents_models.AgentRid
    """An RID identifying an AIP Agent created in [AIP Agent Studio](https://palantir.com/docs/foundry/agent-studio/overview/)."""

    sessionRid: aip_agents_models.SessionRid
    """The Resource Identifier (RID) of the conversation session."""


@dataclass
class GetRagContextForSessionPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["GetRagContextForSessionPermissionDenied"]
    parameters: GetRagContextForSessionPermissionDeniedParameters
    error_instance_id: str


class InvalidAgentVersionParameters(typing_extensions.TypedDict):
    """The provided version string is not a valid format for an Agent version."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    agentRid: aip_agents_models.AgentRid
    version: aip_agents_models.AgentVersionString


@dataclass
class InvalidAgentVersion(errors.BadRequestError):
    name: typing.Literal["InvalidAgentVersion"]
    parameters: InvalidAgentVersionParameters
    error_instance_id: str


class InvalidParameterParameters(typing_extensions.TypedDict):
    """
    The provided application variable is not valid for the Agent for this session.
    Check the available application variables for the Agent under the `parameters` property, and version through the API with `getAgent`, or in AIP Agent Studio.
    The Agent version used for the session can be checked through the API with `getSession`.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    agentRid: aip_agents_models.AgentRid
    sessionRid: aip_agents_models.SessionRid
    parameter: aip_agents_models.ParameterId


@dataclass
class InvalidParameter(errors.BadRequestError):
    name: typing.Literal["InvalidParameter"]
    parameters: InvalidParameterParameters
    error_instance_id: str


class InvalidParameterTypeParameters(typing_extensions.TypedDict):
    """
    The provided value does not match the expected type for the application variable configured on the Agent for this session.
    Check the available application variables for the Agent under the `parameters` property, and version through the API with `getAgent`, or in AIP Agent Studio.
    The Agent version used for the session can be checked through the API with `getSession`.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    agentRid: aip_agents_models.AgentRid
    sessionRid: aip_agents_models.SessionRid
    parameter: aip_agents_models.ParameterId
    expectedType: str
    receivedType: str


@dataclass
class InvalidParameterType(errors.BadRequestError):
    name: typing.Literal["InvalidParameterType"]
    parameters: InvalidParameterTypeParameters
    error_instance_id: str


class ListSessionsForAgentsPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not allSessions the Agent."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class ListSessionsForAgentsPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["ListSessionsForAgentsPermissionDenied"]
    parameters: ListSessionsForAgentsPermissionDeniedParameters
    error_instance_id: str


class NoPublishedAgentVersionParameters(typing_extensions.TypedDict):
    """
    Failed to retrieve the latest published version of the Agent because the Agent has no published versions.
    Try publishing the Agent in AIP Agent Studio to use the latest published version, or specify the version of the Agent to use.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    agentRid: aip_agents_models.AgentRid


@dataclass
class NoPublishedAgentVersion(errors.BadRequestError):
    name: typing.Literal["NoPublishedAgentVersion"]
    parameters: NoPublishedAgentVersionParameters
    error_instance_id: str


class ObjectTypeIdsNotFoundParameters(typing_extensions.TypedDict):
    """
    Some object types are configured for use by the Agent but could not be found.
    The object types either do not exist or the client token does not have access.
    Object types can be checked by listing available object types through the API, or searching in [Ontology Manager](https://palantir.com/docs/foundry/ontology-manager/overview/).
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    agentRid: aip_agents_models.AgentRid
    sessionRid: typing_extensions.NotRequired[aip_agents_models.SessionRid]
    """The session RID where the error occurred. This is omitted if the error occurred during session creation."""

    objectTypeIds: typing.List[ontologies_models.ObjectTypeId]


@dataclass
class ObjectTypeIdsNotFound(errors.NotFoundError):
    name: typing.Literal["ObjectTypeIdsNotFound"]
    parameters: ObjectTypeIdsNotFoundParameters
    error_instance_id: str


class ObjectTypeRidsNotFoundParameters(typing_extensions.TypedDict):
    """
    Some object types are configured for use by the Agent but could not be found.
    The object types either do not exist or the client token does not have access.
    Object types can be checked by listing available object types through the API, or searching in [Ontology Manager](https://palantir.com/docs/foundry/ontology-manager/overview/).
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    agentRid: aip_agents_models.AgentRid
    sessionRid: typing_extensions.NotRequired[aip_agents_models.SessionRid]
    """The session RID where the error occurred. This is omitted if the error occurred during session creation."""

    objectTypeRids: typing.List[ontologies_models.ObjectTypeRid]


@dataclass
class ObjectTypeRidsNotFound(errors.NotFoundError):
    name: typing.Literal["ObjectTypeRidsNotFound"]
    parameters: ObjectTypeRidsNotFoundParameters
    error_instance_id: str


class RateLimitExceededParameters(typing_extensions.TypedDict):
    """Failed to generate a response as the model rate limits were exceeded. Clients should wait and retry."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    agentRid: aip_agents_models.AgentRid
    sessionRid: aip_agents_models.SessionRid
    details: str
    """Any additional details provided for the error."""


@dataclass
class RateLimitExceeded(errors.BadRequestError):
    name: typing.Literal["RateLimitExceeded"]
    parameters: RateLimitExceededParameters
    error_instance_id: str


class SessionExecutionFailedParameters(typing_extensions.TypedDict):
    """Failed to generate a response for a session due to an unexpected error."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    agentRid: aip_agents_models.AgentRid
    sessionRid: aip_agents_models.SessionRid
    message: str
    """The error message."""

    details: str
    """Any additional details provided for the error."""


@dataclass
class SessionExecutionFailed(errors.InternalServerError):
    name: typing.Literal["SessionExecutionFailed"]
    parameters: SessionExecutionFailedParameters
    error_instance_id: str


class SessionNotFoundParameters(typing_extensions.TypedDict):
    """The given Session could not be found."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    agentRid: aip_agents_models.AgentRid
    """An RID identifying an AIP Agent created in [AIP Agent Studio](https://palantir.com/docs/foundry/agent-studio/overview/)."""

    sessionRid: aip_agents_models.SessionRid
    """The Resource Identifier (RID) of the conversation session."""


@dataclass
class SessionNotFound(errors.NotFoundError):
    name: typing.Literal["SessionNotFound"]
    parameters: SessionNotFoundParameters
    error_instance_id: str


class SessionTraceIdAlreadyExistsParameters(typing_extensions.TypedDict):
    """The provided trace ID already exists for the session and cannot be reused."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    agentRid: aip_agents_models.AgentRid
    sessionRid: aip_agents_models.SessionRid
    sessionTraceId: aip_agents_models.SessionTraceId


@dataclass
class SessionTraceIdAlreadyExists(errors.BadRequestError):
    name: typing.Literal["SessionTraceIdAlreadyExists"]
    parameters: SessionTraceIdAlreadyExistsParameters
    error_instance_id: str


class SessionTraceNotFoundParameters(typing_extensions.TypedDict):
    """The given SessionTrace could not be found."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    sessionTraceId: aip_agents_models.SessionTraceId
    """The unique identifier for the trace."""

    agentRid: aip_agents_models.AgentRid
    """An RID identifying an AIP Agent created in [AIP Agent Studio](https://palantir.com/docs/foundry/agent-studio/overview/)."""

    sessionRid: aip_agents_models.SessionRid
    """The Resource Identifier (RID) of the conversation session."""


@dataclass
class SessionTraceNotFound(errors.NotFoundError):
    name: typing.Literal["SessionTraceNotFound"]
    parameters: SessionTraceNotFoundParameters
    error_instance_id: str


class StreamingContinueSessionPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not streamingContinue the Session."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    agentRid: aip_agents_models.AgentRid
    """An RID identifying an AIP Agent created in [AIP Agent Studio](https://palantir.com/docs/foundry/agent-studio/overview/)."""

    sessionRid: aip_agents_models.SessionRid
    """The Resource Identifier (RID) of the conversation session."""


@dataclass
class StreamingContinueSessionPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["StreamingContinueSessionPermissionDenied"]
    parameters: StreamingContinueSessionPermissionDeniedParameters
    error_instance_id: str


class UpdateSessionTitlePermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not updateTitle the Session."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    agentRid: aip_agents_models.AgentRid
    """An RID identifying an AIP Agent created in [AIP Agent Studio](https://palantir.com/docs/foundry/agent-studio/overview/)."""

    sessionRid: aip_agents_models.SessionRid
    """The Resource Identifier (RID) of the conversation session."""


@dataclass
class UpdateSessionTitlePermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["UpdateSessionTitlePermissionDenied"]
    parameters: UpdateSessionTitlePermissionDeniedParameters
    error_instance_id: str


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
    "SessionTraceIdAlreadyExists",
    "SessionTraceNotFound",
    "StreamingContinueSessionPermissionDenied",
    "UpdateSessionTitlePermissionDenied",
]
