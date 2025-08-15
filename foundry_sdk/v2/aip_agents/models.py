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

import typing

import pydantic
import typing_extensions

from foundry_sdk import _core as core
from foundry_sdk.v2.core import models as core_models
from foundry_sdk.v2.functions import models as functions_models
from foundry_sdk.v2.ontologies import models as ontologies_models


class Agent(core.ModelBase):
    """Agent"""

    rid: AgentRid
    """An RID identifying an AIP Agent created in [AIP Agent Studio](https://palantir.com/docs/foundry/agent-studio/overview/)."""

    version: AgentVersionString
    """The version of this instance of the Agent."""

    metadata: AgentMetadata
    parameters: typing.Dict[ParameterId, Parameter]
    """
    The types and names of variables configured for the Agent in [AIP Agent Studio](https://palantir.com/docs/foundry/agent-studio/overview/) in the [application state](https://palantir.com/docs/foundry/agent-studio/application-state/).
    These variables can be used to send custom values in prompts sent to an Agent to customize and control the Agent's behavior.
    """


AgentMarkdownResponse = str
"""The final answer for an exchange. Responses are formatted using markdown."""


class AgentMetadata(core.ModelBase):
    """Metadata for an Agent."""

    display_name: str = pydantic.Field(alias=str("displayName"))  # type: ignore[literal-required]
    """The name of the Agent."""

    description: typing.Optional[str] = None
    """The description for the Agent."""

    input_placeholder: typing.Optional[str] = pydantic.Field(alias=str("inputPlaceholder"), default=None)  # type: ignore[literal-required]
    """The default text to show as the placeholder input for chats with the Agent."""

    suggested_prompts: typing.List[str] = pydantic.Field(alias=str("suggestedPrompts"))  # type: ignore[literal-required]
    """Prompts to show to the user as example messages to start a conversation with the Agent."""


AgentRid = core.RID
"""An RID identifying an AIP Agent created in [AIP Agent Studio](https://palantir.com/docs/foundry/agent-studio/overview/)."""


class AgentSessionRagContextResponse(core.ModelBase):
    """Context retrieved from an Agent's configured context data sources which was relevant to the supplied user message."""

    object_contexts: typing.List[ObjectContext] = pydantic.Field(alias=str("objectContexts"))  # type: ignore[literal-required]
    function_retrieved_contexts: typing.List[FunctionRetrievedContext] = pydantic.Field(alias=str("functionRetrievedContexts"))  # type: ignore[literal-required]


class AgentVersion(core.ModelBase):
    """AgentVersion"""

    string: AgentVersionString
    """The semantic version of the Agent, formatted as "majorVersion.minorVersion"."""

    version: AgentVersionDetails
    """Semantic version details of the Agent."""


class AgentVersionDetails(core.ModelBase):
    """Semantic version details for an Agent."""

    major: int
    """The major version of the Agent. Incremented every time the Agent is published."""

    minor: int
    """The minor version of the Agent. Incremented every time the Agent is saved."""


AgentVersionString = str
"""The semantic version of the Agent, formatted as "majorVersion.minorVersion"."""


class AgentsSessionsPage(core.ModelBase):
    """
    A page of results for sessions across all accessible Agents for the calling user.
    Sessions are returned in order of most recently updated first.
    """

    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]
    """
    The page token that should be used when requesting the next page of results.
    Empty if there are no more results to retrieve.
    """

    data: typing.List[Session]


class CancelSessionResponse(core.ModelBase):
    """CancelSessionResponse"""

    result: typing.Optional[SessionExchangeResult] = None
    """
    If the `response` field was specified, this returns the result that was added to the session for the canceled exchange, with the client-provided response.
    If no `response` was specified in the request, this returns an empty response, as no exchange was added to the session.
    """


class Content(core.ModelBase):
    """Content"""

    exchanges: typing.List[SessionExchange]
    """
    The conversation history for the session, represented as a list of exchanges.
    Each exchange represents an initiating message from the user and the Agent's response.
    Exchanges are returned in chronological order, starting with the first exchange.
    """


class FailureToolCallOutput(core.ModelBase):
    """The failed output of a tool call."""

    correction_message: str = pydantic.Field(alias=str("correctionMessage"))  # type: ignore[literal-required]
    """
    The correction message returned by the tool if the tool call was not successful.
    This is a message that the tool returned to the Agent, which may be used to correct the
    Agent's input to the tool.
    """

    type: typing.Literal["failure"] = "failure"


class FunctionRetrievedContext(core.ModelBase):
    """Context retrieved from running a function to include as additional context in the prompt to the Agent."""

    function_rid: functions_models.FunctionRid = pydantic.Field(alias=str("functionRid"))  # type: ignore[literal-required]
    function_version: functions_models.FunctionVersion = pydantic.Field(alias=str("functionVersion"))  # type: ignore[literal-required]
    retrieved_prompt: str = pydantic.Field(alias=str("retrievedPrompt"))  # type: ignore[literal-required]
    """String content returned from a context retrieval function."""

    type: typing.Literal["functionRetrievedContext"] = "functionRetrievedContext"


InputContext = typing_extensions.Annotated[
    typing.Union[FunctionRetrievedContext, "ObjectContext"], pydantic.Field(discriminator="type")
]
"""Custom retrieved [context](https://palantir.com/docs/foundry/agent-studio/retrieval-context/) to provide to an Agent for continuing a session."""


class ListAgentVersionsResponse(core.ModelBase):
    """ListAgentVersionsResponse"""

    data: typing.List[AgentVersion]
    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]


class ListSessionsResponse(core.ModelBase):
    """ListSessionsResponse"""

    data: typing.List[Session]
    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]


MessageId = core.UUID
"""
An ephemeral client-generated Universally Unique Identifier (UUID) to identify a message for streamed session responses.
This can be used by clients to cancel a streamed exchange.
"""


class ObjectContext(core.ModelBase):
    """Details of relevant retrieved object instances for a user's message to include as additional context in the prompt to the Agent."""

    object_rids: typing.List[ontologies_models.ObjectRid] = pydantic.Field(alias=str("objectRids"))  # type: ignore[literal-required]
    """The RIDs of the relevant object instances to include in the prompt."""

    property_type_rids: typing.List[ontologies_models.PropertyTypeRid] = pydantic.Field(alias=str("propertyTypeRids"))  # type: ignore[literal-required]
    """The RIDs of the property types for the given objects to include in the prompt."""

    type: typing.Literal["objectContext"] = "objectContext"


class ObjectSetParameter(core.ModelBase):
    """ObjectSetParameter"""

    expected_object_types: typing.List[ontologies_models.ObjectTypeId] = pydantic.Field(alias=str("expectedObjectTypes"))  # type: ignore[literal-required]
    """The types of objects that are expected in ObjectSet values passed for this variable."""

    type: typing.Literal["objectSet"] = "objectSet"


class ObjectSetParameterValue(core.ModelBase):
    """A value passed for `ObjectSetParameter` application variable types."""

    object_set: ontologies_models.ObjectSet = pydantic.Field(alias=str("objectSet"))  # type: ignore[literal-required]
    ontology: ontologies_models.OntologyIdentifier
    """
    The API name of the Ontology for the provided `ObjectSet`.
    To find the API name, use the `List ontologies` endpoint or check the [Ontology Manager](https://palantir.com/docs/foundry/ontology-manager/overview/).
    """

    type: typing.Literal["objectSet"] = "objectSet"


class ObjectSetParameterValueUpdate(core.ModelBase):
    """ObjectSetParameterValueUpdate"""

    value: ontologies_models.ObjectSetRid
    type: typing.Literal["objectSet"] = "objectSet"


class Parameter(core.ModelBase):
    """A variable configured in the application state of an Agent in [AIP Agent Studio](https://palantir.com/docs/foundry/agent-studio/overview/)."""

    parameter_type: ParameterType = pydantic.Field(alias=str("parameterType"))  # type: ignore[literal-required]
    """Details of the types of values accepted and defaults for this variable."""

    access: ParameterAccessMode
    """The access mode controls how the Agent is able to interact with the variable."""

    description: typing.Optional[str] = None
    """
    A description to explain the use of this variable.
    This description is injected into the Agent's prompt to provide context for when to use the variable.
    """


ParameterAccessMode = typing.Literal["READ_ONLY", "READ_WRITE"]
"""
READ_ONLY: Allows the variable to be read by the Agent, but the Agent cannot generate updates for it.
READ_WRITE: Allows the variable to be read and updated by the Agent.
"""


ParameterId = str
"""The unique identifier for a variable configured in the application state of an Agent in [AIP Agent Studio](https://palantir.com/docs/foundry/agent-studio/overview/)."""


ParameterType = typing_extensions.Annotated[
    typing.Union["StringParameter", ObjectSetParameter], pydantic.Field(discriminator="type")
]
"""ParameterType"""


ParameterValue = typing_extensions.Annotated[
    typing.Union["StringParameterValue", ObjectSetParameterValue],
    pydantic.Field(discriminator="type"),
]
"""The value provided for a variable configured in the [application state](https://palantir.com/docs/foundry/agent-studio/application-state/) of an Agent."""


ParameterValueUpdate = typing_extensions.Annotated[
    typing.Union["StringParameterValue", ObjectSetParameterValueUpdate],
    pydantic.Field(discriminator="type"),
]
"""
A value update for an [application variable](https://palantir.com/docs/foundry/agent-studio/application-state/) generated by the Agent.
For `StringParameter` types, this will be the updated string value.
For `ObjectSetParameter` types, this will be a Resource Identifier (RID) for the updated object set.
"""


class RidToolInputValue(core.ModelBase):
    """A Resource Identifier (RID) that was passed as input to a tool."""

    rid: core.RID
    type: typing.Literal["rid"] = "rid"


class RidToolOutputValue(core.ModelBase):
    """A Resource Identifier (RID) value that was returned from a tool."""

    rid: core.RID
    type: typing.Literal["rid"] = "rid"


class Session(core.ModelBase):
    """Session"""

    rid: SessionRid
    """The Resource Identifier (RID) of the conversation session."""

    metadata: SessionMetadata
    """Metadata about the session."""

    agent_rid: AgentRid = pydantic.Field(alias=str("agentRid"))  # type: ignore[literal-required]
    """The Resource Identifier (RID) of the Agent associated with the session."""

    agent_version: AgentVersionString = pydantic.Field(alias=str("agentVersion"))  # type: ignore[literal-required]
    """
    The version of the Agent associated with the session.
    This can be set by clients on session creation.
    If not specified, defaults to use the latest published version of the Agent at session creation time.
    """


class SessionExchange(core.ModelBase):
    """Represents an individual exchange between a user and an Agent in a conversation session."""

    user_input: UserTextInput = pydantic.Field(alias=str("userInput"))  # type: ignore[literal-required]
    """The user message that initiated the exchange."""

    contexts: typing.Optional[SessionExchangeContexts] = None
    """
    Additional retrieved context that was included in the prompt to the Agent.
    This may include context that was passed by the client with the user input, or relevant context that was automatically retrieved and added based on available data sources configured on the Agent.
    Empty if no additional context was included in the prompt.
    """

    result: SessionExchangeResult
    """The final result for the exchange."""


class SessionExchangeContexts(core.ModelBase):
    """Retrieved context which was passed to the Agent as input for the exchange."""

    object_contexts: typing.List[ObjectContext] = pydantic.Field(alias=str("objectContexts"))  # type: ignore[literal-required]
    """Relevant object context for the user's message that was included in the prompt to the Agent."""

    function_retrieved_contexts: typing.List[FunctionRetrievedContext] = pydantic.Field(alias=str("functionRetrievedContexts"))  # type: ignore[literal-required]
    """Context retrieved from running a function that was included as additional context in the prompt to the Agent."""


class SessionExchangeResult(core.ModelBase):
    """The returned result from the Agent for a session exchange."""

    agent_markdown_response: AgentMarkdownResponse = pydantic.Field(alias=str("agentMarkdownResponse"))  # type: ignore[literal-required]
    """The final text response generated by the Agent. Responses are formatted using markdown."""

    parameter_updates: typing.Dict[ParameterId, ParameterValueUpdate] = pydantic.Field(alias=str("parameterUpdates"))  # type: ignore[literal-required]
    """
    Any updates to application variable values which were generated by the Agent for this exchange.
    Updates can only be generated for application variables configured with `READ_WRITE` access on the Agent in AIP Agent Studio.
    """

    total_tokens_used: typing.Optional[int] = pydantic.Field(alias=str("totalTokensUsed"), default=None)  # type: ignore[literal-required]
    """Total tokens used to compute the result. Omitted if token usage information is not supported by the model used for the session."""

    interrupted_output: bool = pydantic.Field(alias=str("interruptedOutput"))  # type: ignore[literal-required]
    """
    True if the exchange was canceled.
    In that case, the response (if any) was provided by the client as part of the cancellation request rather than by the Agent.
    """

    session_trace_id: SessionTraceId = pydantic.Field(alias=str("sessionTraceId"))  # type: ignore[literal-required]
    """
    The unique identifier for the session trace. The session trace lists the sequence of steps that an Agent
    takes to arrive at an answer. For example, a trace may include steps such as context retrieval and tool calls.
    """


class SessionMetadata(core.ModelBase):
    """Metadata for a conversation session with an Agent."""

    title: str
    """The title of the session."""

    created_time: core.AwareDatetime = pydantic.Field(alias=str("createdTime"))  # type: ignore[literal-required]
    """The time the session was created."""

    updated_time: core.AwareDatetime = pydantic.Field(alias=str("updatedTime"))  # type: ignore[literal-required]
    """The time the session was last updated."""

    message_count: int = pydantic.Field(alias=str("messageCount"))  # type: ignore[literal-required]
    """
    The count of messages in the session.
    Includes both user messages and Agent replies, so each complete exchange counts as two messages.
    """

    estimated_expires_time: core.AwareDatetime = pydantic.Field(alias=str("estimatedExpiresTime"))  # type: ignore[literal-required]
    """
    The estimated time at which the session is due to expire.
    Once a session has expired, it can no longer be accessed and a new session must be created.
    The expiry time is automatically extended when new exchanges are added to the session.
    """


SessionRid = core.RID
"""The Resource Identifier (RID) of the conversation session."""


class SessionTrace(core.ModelBase):
    """SessionTrace"""

    id: SessionTraceId
    """The unique identifier for the trace."""

    status: SessionTraceStatus
    """
    This indicates whether the Agent has finished generating the final response. Clients should keep polling
    the `getSessionTrace` endpoint until the status is `COMPLETE`.
    """

    contexts: typing.Optional[SessionExchangeContexts] = None
    """
    Any additional context which was provided by the client or retrieved automatically by the agent, grouped
    by context type. Empty if no additional context was provided or configured to be automatically
    retrieved. A present SessionExchangeContexts object with empty lists indicates that context retrieval
    was attempted but no context was found.
    Note that this field will only be populated once the response generation has completed.
    """

    tool_call_groups: typing.List[ToolCallGroup] = pydantic.Field(alias=str("toolCallGroups"))  # type: ignore[literal-required]
    """
    List of tool call groups that were triggered at the same point in the trace for the agent response
    generation. The groups are returned in the same order as they were triggered by the agent.
    """


SessionTraceId = core.UUID
"""
The unique identifier for a trace. The trace lists the sequence of steps that an Agent took to arrive at an
answer. For example, a trace may include steps such as context retrieval and tool calls.
"""


SessionTraceStatus = typing.Literal["IN_PROGRESS", "COMPLETE"]
"""SessionTraceStatus"""


class StringParameter(core.ModelBase):
    """StringParameter"""

    default_value: typing.Optional[str] = pydantic.Field(alias=str("defaultValue"), default=None)  # type: ignore[literal-required]
    """The default value to use for this variable."""

    type: typing.Literal["string"] = "string"


class StringParameterValue(core.ModelBase):
    """A value passed for `StringParameter` application variable types."""

    value: str
    type: typing.Literal["string"] = "string"


class StringToolInputValue(core.ModelBase):
    """A string value that was passed as input to a tool."""

    value: str
    type: typing.Literal["string"] = "string"


class StringToolOutputValue(core.ModelBase):
    """A string value that was returned from a tool."""

    value: str
    type: typing.Literal["string"] = "string"


class SuccessToolCallOutput(core.ModelBase):
    """The successful output of a tool call."""

    output: ToolOutputValue
    type: typing.Literal["success"] = "success"


class ToolCall(core.ModelBase):
    """A tool call with its input and output."""

    tool_metadata: ToolMetadata = pydantic.Field(alias=str("toolMetadata"))  # type: ignore[literal-required]
    """Details about the tool that was called, including the name and type of the tool."""

    input: ToolCallInput
    output: typing.Optional[ToolCallOutput] = None
    """Empty if the tool call is in progress."""


class ToolCallGroup(core.ModelBase):
    """List of tool calls that were triggered at the same point in the trace for the agent response generation."""

    tool_calls: typing.List[ToolCall] = pydantic.Field(alias=str("toolCalls"))  # type: ignore[literal-required]


class ToolCallInput(core.ModelBase):
    """Input parameters for a tool call."""

    thought: typing.Optional[str] = None
    """Any additional message content that the Agent provided for why it chose to call the tool."""

    inputs: typing.Dict[ToolInputName, ToolInputValue]


ToolCallOutput = typing_extensions.Annotated[
    typing.Union[SuccessToolCallOutput, FailureToolCallOutput], pydantic.Field(discriminator="type")
]
"""The output of a tool call."""


ToolInputName = str
"""The name of a tool input parameter."""


ToolInputValue = typing_extensions.Annotated[
    typing.Union[StringToolInputValue, RidToolInputValue], pydantic.Field(discriminator="type")
]
"""A tool input value, which can be either a string or a Resource Identifier (RID)."""


class ToolMetadata(core.ModelBase):
    """Details about the used tool."""

    name: str
    """The name of the tool that was called, as configured on the Agent."""

    type: ToolType
    """The type of the tool that was called."""


ToolOutputValue = typing_extensions.Annotated[
    typing.Union[StringToolOutputValue, RidToolOutputValue], pydantic.Field(discriminator="type")
]
"""A tool output value, which can be either a string or a Resource Identifier (RID)."""


ToolType = typing.Literal[
    "FUNCTION",
    "ACTION",
    "ONTOLOGY_SEMANTIC_SEARCH",
    "OBJECT_QUERY",
    "UPDATE_APPLICATION_VARIABLE",
    "REQUEST_CLARIFICATION",
]
"""ToolType"""


class UserTextInput(core.ModelBase):
    """UserTextInput"""

    text: str
    """The user message text."""


core.resolve_forward_references(InputContext, globalns=globals(), localns=locals())
core.resolve_forward_references(ParameterType, globalns=globals(), localns=locals())
core.resolve_forward_references(ParameterValue, globalns=globals(), localns=locals())
core.resolve_forward_references(ParameterValueUpdate, globalns=globals(), localns=locals())
core.resolve_forward_references(ToolCallOutput, globalns=globals(), localns=locals())
core.resolve_forward_references(ToolInputValue, globalns=globals(), localns=locals())
core.resolve_forward_references(ToolOutputValue, globalns=globals(), localns=locals())

__all__ = [
    "Agent",
    "AgentMarkdownResponse",
    "AgentMetadata",
    "AgentRid",
    "AgentSessionRagContextResponse",
    "AgentVersion",
    "AgentVersionDetails",
    "AgentVersionString",
    "AgentsSessionsPage",
    "CancelSessionResponse",
    "Content",
    "FailureToolCallOutput",
    "FunctionRetrievedContext",
    "InputContext",
    "ListAgentVersionsResponse",
    "ListSessionsResponse",
    "MessageId",
    "ObjectContext",
    "ObjectSetParameter",
    "ObjectSetParameterValue",
    "ObjectSetParameterValueUpdate",
    "Parameter",
    "ParameterAccessMode",
    "ParameterId",
    "ParameterType",
    "ParameterValue",
    "ParameterValueUpdate",
    "RidToolInputValue",
    "RidToolOutputValue",
    "Session",
    "SessionExchange",
    "SessionExchangeContexts",
    "SessionExchangeResult",
    "SessionMetadata",
    "SessionRid",
    "SessionTrace",
    "SessionTraceId",
    "SessionTraceStatus",
    "StringParameter",
    "StringParameterValue",
    "StringToolInputValue",
    "StringToolOutputValue",
    "SuccessToolCallOutput",
    "ToolCall",
    "ToolCallGroup",
    "ToolCallInput",
    "ToolCallOutput",
    "ToolInputName",
    "ToolInputValue",
    "ToolMetadata",
    "ToolOutputValue",
    "ToolType",
    "UserTextInput",
]
