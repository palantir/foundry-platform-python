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
from datetime import datetime

import pydantic
import typing_extensions

from foundry import _core as core


class Agent(pydantic.BaseModel):
    """Agent"""

    rid: AgentRid
    """An RID identifying an AIP Agent created in [AIP Agent Studio](/docs/foundry/agent-studio/overview/)."""

    version: AgentVersionString
    """The version of this instance of the Agent."""

    metadata: AgentMetadata
    parameters: typing.Dict[ParameterId, Parameter]
    """
    The types and names of variables configured for the Agent in [AIP Agent Studio](/docs/foundry/agent-studio/overview/) in the [application state](/docs/foundry/agent-studio/application-state/).
    These variables can be used to send custom values in prompts sent to an Agent to customize and control the Agent's behavior.
    """

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "AgentDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(AgentDict, self.model_dump(by_alias=True, exclude_none=True))


class AgentDict(typing_extensions.TypedDict):
    """Agent"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    rid: AgentRid
    """An RID identifying an AIP Agent created in [AIP Agent Studio](/docs/foundry/agent-studio/overview/)."""

    version: AgentVersionString
    """The version of this instance of the Agent."""

    metadata: AgentMetadataDict
    parameters: typing.Dict[ParameterId, ParameterDict]
    """
    The types and names of variables configured for the Agent in [AIP Agent Studio](/docs/foundry/agent-studio/overview/) in the [application state](/docs/foundry/agent-studio/application-state/).
    These variables can be used to send custom values in prompts sent to an Agent to customize and control the Agent's behavior.
    """


AgentMarkdownResponse = str
"""The final answer for an exchange. Responses are formatted using markdown."""


class AgentMetadata(pydantic.BaseModel):
    """Metadata for an Agent."""

    display_name: str = pydantic.Field(alias=str("displayName"))  # type: ignore[literal-required]
    """The name of the Agent."""

    description: typing.Optional[str] = None
    """The description for the Agent."""

    input_placeholder: typing.Optional[str] = pydantic.Field(alias=str("inputPlaceholder"), default=None)  # type: ignore[literal-required]
    """The default text to show as the placeholder input for chats with the Agent."""

    suggested_prompts: typing.List[str] = pydantic.Field(alias=str("suggestedPrompts"))  # type: ignore[literal-required]
    """Prompts to show to the user as example messages to start a conversation with the Agent."""

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "AgentMetadataDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(AgentMetadataDict, self.model_dump(by_alias=True, exclude_none=True))


class AgentMetadataDict(typing_extensions.TypedDict):
    """Metadata for an Agent."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    displayName: str
    """The name of the Agent."""

    description: typing_extensions.NotRequired[str]
    """The description for the Agent."""

    inputPlaceholder: typing_extensions.NotRequired[str]
    """The default text to show as the placeholder input for chats with the Agent."""

    suggestedPrompts: typing.List[str]
    """Prompts to show to the user as example messages to start a conversation with the Agent."""


AgentRid = core.RID
"""An RID identifying an AIP Agent created in [AIP Agent Studio](/docs/foundry/agent-studio/overview/)."""


class AgentSessionRagContextResponse(pydantic.BaseModel):
    """Context retrieved from an Agent's configured context data sources which was relevant to the supplied user message."""

    object_contexts: typing.List[ObjectContext] = pydantic.Field(alias=str("objectContexts"))  # type: ignore[literal-required]
    function_retrieved_contexts: typing.List[FunctionRetrievedContext] = pydantic.Field(alias=str("functionRetrievedContexts"))  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "AgentSessionRagContextResponseDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            AgentSessionRagContextResponseDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class AgentSessionRagContextResponseDict(typing_extensions.TypedDict):
    """Context retrieved from an Agent's configured context data sources which was relevant to the supplied user message."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    objectContexts: typing.List[ObjectContextDict]
    functionRetrievedContexts: typing.List[FunctionRetrievedContextDict]


class AgentVersion(pydantic.BaseModel):
    """AgentVersion"""

    string: AgentVersionString
    """The semantic version of the Agent, formatted as "majorVersion.minorVersion"."""

    version: AgentVersionDetails
    """Semantic version details of the Agent."""

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "AgentVersionDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(AgentVersionDict, self.model_dump(by_alias=True, exclude_none=True))


class AgentVersionDetails(pydantic.BaseModel):
    """Semantic version details for an Agent."""

    major: int
    """The major version of the Agent. Incremented every time the Agent is published."""

    minor: int
    """The minor version of the Agent. Incremented every time the Agent is saved."""

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "AgentVersionDetailsDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            AgentVersionDetailsDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class AgentVersionDetailsDict(typing_extensions.TypedDict):
    """Semantic version details for an Agent."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    major: int
    """The major version of the Agent. Incremented every time the Agent is published."""

    minor: int
    """The minor version of the Agent. Incremented every time the Agent is saved."""


class AgentVersionDict(typing_extensions.TypedDict):
    """AgentVersion"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    string: AgentVersionString
    """The semantic version of the Agent, formatted as "majorVersion.minorVersion"."""

    version: AgentVersionDetailsDict
    """Semantic version details of the Agent."""


AgentVersionString = str
"""The semantic version of the Agent, formatted as "majorVersion.minorVersion"."""


class AgentsSessionsPage(pydantic.BaseModel):
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
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "AgentsSessionsPageDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            AgentsSessionsPageDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class AgentsSessionsPageDict(typing_extensions.TypedDict):
    """
    A page of results for sessions across all accessible Agents for the calling user.
    Sessions are returned in order of most recently updated first.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    nextPageToken: typing_extensions.NotRequired[core_models.PageToken]
    """
    The page token that should be used when requesting the next page of results.
    Empty if there are no more results to retrieve.
    """

    data: typing.List[SessionDict]


class CancelSessionResponse(pydantic.BaseModel):
    """CancelSessionResponse"""

    result: typing.Optional[SessionExchangeResult] = None
    """
    If the `response` field was specified, this returns the result that was added to the session for the canceled exchange, with the client-provided response.
    If no `response` was specified in the request, this returns an empty response, as no exchange was added to the session.
    """

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "CancelSessionResponseDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            CancelSessionResponseDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class CancelSessionResponseDict(typing_extensions.TypedDict):
    """CancelSessionResponse"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    result: typing_extensions.NotRequired[SessionExchangeResultDict]
    """
    If the `response` field was specified, this returns the result that was added to the session for the canceled exchange, with the client-provided response.
    If no `response` was specified in the request, this returns an empty response, as no exchange was added to the session.
    """


class Content(pydantic.BaseModel):
    """Content"""

    exchanges: typing.List[SessionExchange]
    """
    The conversation history for the session, represented as a list of exchanges.
    Each exchange represents an initiating message from the user and the Agent's response.
    Exchanges are returned in chronological order, starting with the first exchange.
    """

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ContentDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(ContentDict, self.model_dump(by_alias=True, exclude_none=True))


class ContentDict(typing_extensions.TypedDict):
    """Content"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    exchanges: typing.List[SessionExchangeDict]
    """
    The conversation history for the session, represented as a list of exchanges.
    Each exchange represents an initiating message from the user and the Agent's response.
    Exchanges are returned in chronological order, starting with the first exchange.
    """


class FunctionRetrievedContext(pydantic.BaseModel):
    """Context retrieved from running a function to include as additional context in the prompt to the Agent."""

    function_rid: functions_models.FunctionRid = pydantic.Field(alias=str("functionRid"))  # type: ignore[literal-required]
    function_version: functions_models.FunctionVersion = pydantic.Field(alias=str("functionVersion"))  # type: ignore[literal-required]
    retrieved_prompt: str = pydantic.Field(alias=str("retrievedPrompt"))  # type: ignore[literal-required]
    """String content returned from a context retrieval function."""

    type: typing.Literal["functionRetrievedContext"] = "functionRetrievedContext"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "FunctionRetrievedContextDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            FunctionRetrievedContextDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class FunctionRetrievedContextDict(typing_extensions.TypedDict):
    """Context retrieved from running a function to include as additional context in the prompt to the Agent."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    functionRid: functions_models.FunctionRid
    functionVersion: functions_models.FunctionVersion
    retrievedPrompt: str
    """String content returned from a context retrieval function."""

    type: typing.Literal["functionRetrievedContext"]


InputContext = typing_extensions.Annotated[
    typing.Union["FunctionRetrievedContext", "ObjectContext"], pydantic.Field(discriminator="type")
]
"""Custom retrieved [context](/docs/foundry/agent-studio/retrieval-context/) to provide to an Agent for continuing a session."""


InputContextDict = typing_extensions.Annotated[
    typing.Union["FunctionRetrievedContextDict", "ObjectContextDict"],
    pydantic.Field(discriminator="type"),
]
"""Custom retrieved [context](/docs/foundry/agent-studio/retrieval-context/) to provide to an Agent for continuing a session."""


class ListAgentVersionsResponse(pydantic.BaseModel):
    """ListAgentVersionsResponse"""

    data: typing.List[AgentVersion]
    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ListAgentVersionsResponseDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            ListAgentVersionsResponseDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class ListAgentVersionsResponseDict(typing_extensions.TypedDict):
    """ListAgentVersionsResponse"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    data: typing.List[AgentVersionDict]
    nextPageToken: typing_extensions.NotRequired[core_models.PageToken]


class ListSessionsResponse(pydantic.BaseModel):
    """ListSessionsResponse"""

    data: typing.List[Session]
    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ListSessionsResponseDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            ListSessionsResponseDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class ListSessionsResponseDict(typing_extensions.TypedDict):
    """ListSessionsResponse"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    data: typing.List[SessionDict]
    nextPageToken: typing_extensions.NotRequired[core_models.PageToken]


MessageId = core.UUID
"""
An ephemeral client-generated Universally Unique Identifier (UUID) to identify a message for streamed session responses.
This can be used by clients to cancel a streamed exchange.
"""


class ObjectContext(pydantic.BaseModel):
    """Details of relevant retrieved object instances for a user's message to include as additional context in the prompt to the Agent."""

    object_rids: typing.List[ontologies_models.ObjectRid] = pydantic.Field(alias=str("objectRids"))  # type: ignore[literal-required]
    """The RIDs of the relevant object instances to include in the prompt."""

    property_type_rids: typing.List[ontologies_models.PropertyTypeRid] = pydantic.Field(alias=str("propertyTypeRids"))  # type: ignore[literal-required]
    """The RIDs of the property types for the given objects to include in the prompt."""

    type: typing.Literal["objectContext"] = "objectContext"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ObjectContextDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(ObjectContextDict, self.model_dump(by_alias=True, exclude_none=True))


class ObjectContextDict(typing_extensions.TypedDict):
    """Details of relevant retrieved object instances for a user's message to include as additional context in the prompt to the Agent."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    objectRids: typing.List[ontologies_models.ObjectRid]
    """The RIDs of the relevant object instances to include in the prompt."""

    propertyTypeRids: typing.List[ontologies_models.PropertyTypeRid]
    """The RIDs of the property types for the given objects to include in the prompt."""

    type: typing.Literal["objectContext"]


class ObjectSetParameter(pydantic.BaseModel):
    """ObjectSetParameter"""

    expected_object_types: typing.List[ontologies_models.ObjectTypeId] = pydantic.Field(alias=str("expectedObjectTypes"))  # type: ignore[literal-required]
    """The types of objects that are expected in ObjectSet values passed for this variable."""

    type: typing.Literal["objectSet"] = "objectSet"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ObjectSetParameterDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            ObjectSetParameterDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class ObjectSetParameterDict(typing_extensions.TypedDict):
    """ObjectSetParameter"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    expectedObjectTypes: typing.List[ontologies_models.ObjectTypeId]
    """The types of objects that are expected in ObjectSet values passed for this variable."""

    type: typing.Literal["objectSet"]


class ObjectSetParameterValue(pydantic.BaseModel):
    """A value passed for `ObjectSetParameter` application variable types."""

    object_set: ontologies_models.ObjectSet = pydantic.Field(alias=str("objectSet"))  # type: ignore[literal-required]
    ontology: ontologies_models.OntologyIdentifier
    """
    The API name of the Ontology for the provided `ObjectSet`.
    To find the API name, use the `List ontologies` endpoint or check the [Ontology Manager](/docs/foundry/ontology-manager/overview/).
    """

    type: typing.Literal["objectSet"] = "objectSet"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ObjectSetParameterValueDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            ObjectSetParameterValueDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class ObjectSetParameterValueDict(typing_extensions.TypedDict):
    """A value passed for `ObjectSetParameter` application variable types."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    objectSet: ontologies_models.ObjectSetDict
    ontology: ontologies_models.OntologyIdentifier
    """
    The API name of the Ontology for the provided `ObjectSet`.
    To find the API name, use the `List ontologies` endpoint or check the [Ontology Manager](/docs/foundry/ontology-manager/overview/).
    """

    type: typing.Literal["objectSet"]


class ObjectSetParameterValueUpdate(pydantic.BaseModel):
    """ObjectSetParameterValueUpdate"""

    value: ontologies_models.ObjectSetRid
    type: typing.Literal["objectSet"] = "objectSet"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ObjectSetParameterValueUpdateDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            ObjectSetParameterValueUpdateDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class ObjectSetParameterValueUpdateDict(typing_extensions.TypedDict):
    """ObjectSetParameterValueUpdate"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    value: ontologies_models.ObjectSetRid
    type: typing.Literal["objectSet"]


class Parameter(pydantic.BaseModel):
    """A variable configured in the application state of an Agent in [AIP Agent Studio](/docs/foundry/agent-studio/overview/)."""

    parameter_type: ParameterType = pydantic.Field(alias=str("parameterType"))  # type: ignore[literal-required]
    """Details of the types of values accepted and defaults for this variable."""

    access: ParameterAccessMode
    """The access mode controls how the Agent is able to interact with the variable."""

    description: typing.Optional[str] = None
    """
    A description to explain the use of this variable.
    This description is injected into the Agent's prompt to provide context for when to use the variable.
    """

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ParameterDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(ParameterDict, self.model_dump(by_alias=True, exclude_none=True))


ParameterAccessMode = typing.Literal["READ_ONLY", "READ_WRITE"]
"""
READ_ONLY: Allows the variable to be read by the Agent, but the Agent cannot generate updates for it.
READ_WRITE: Allows the variable to be read and updated by the Agent.
"""


class ParameterDict(typing_extensions.TypedDict):
    """A variable configured in the application state of an Agent in [AIP Agent Studio](/docs/foundry/agent-studio/overview/)."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    parameterType: ParameterTypeDict
    """Details of the types of values accepted and defaults for this variable."""

    access: ParameterAccessMode
    """The access mode controls how the Agent is able to interact with the variable."""

    description: typing_extensions.NotRequired[str]
    """
    A description to explain the use of this variable.
    This description is injected into the Agent's prompt to provide context for when to use the variable.
    """


ParameterId = str
"""The unique identifier for a variable configured in the application state of an Agent in [AIP Agent Studio](/docs/foundry/agent-studio/overview/)."""


ParameterType = typing_extensions.Annotated[
    typing.Union["StringParameter", "ObjectSetParameter"], pydantic.Field(discriminator="type")
]
"""ParameterType"""


ParameterTypeDict = typing_extensions.Annotated[
    typing.Union["StringParameterDict", "ObjectSetParameterDict"],
    pydantic.Field(discriminator="type"),
]
"""ParameterType"""


ParameterValue = typing_extensions.Annotated[
    typing.Union["StringParameterValue", "ObjectSetParameterValue"],
    pydantic.Field(discriminator="type"),
]
"""The value provided for a variable configured in the [application state](/docs/foundry/agent-studio/application-state/) of an Agent."""


ParameterValueDict = typing_extensions.Annotated[
    typing.Union["StringParameterValueDict", "ObjectSetParameterValueDict"],
    pydantic.Field(discriminator="type"),
]
"""The value provided for a variable configured in the [application state](/docs/foundry/agent-studio/application-state/) of an Agent."""


ParameterValueUpdate = typing_extensions.Annotated[
    typing.Union["StringParameterValue", "ObjectSetParameterValueUpdate"],
    pydantic.Field(discriminator="type"),
]
"""
A value update for an [application variable](/docs/foundry/agent-studio/application-state/) generated by the Agent.
For `StringParameter` types, this will be the updated string value.
For `ObjectSetParameter` types, this will be a Resource Identifier (RID) for the updated object set.
"""


ParameterValueUpdateDict = typing_extensions.Annotated[
    typing.Union["StringParameterValueDict", "ObjectSetParameterValueUpdateDict"],
    pydantic.Field(discriminator="type"),
]
"""
A value update for an [application variable](/docs/foundry/agent-studio/application-state/) generated by the Agent.
For `StringParameter` types, this will be the updated string value.
For `ObjectSetParameter` types, this will be a Resource Identifier (RID) for the updated object set.
"""


class Session(pydantic.BaseModel):
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

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "SessionDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(SessionDict, self.model_dump(by_alias=True, exclude_none=True))


class SessionDict(typing_extensions.TypedDict):
    """Session"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    rid: SessionRid
    """The Resource Identifier (RID) of the conversation session."""

    metadata: SessionMetadataDict
    """Metadata about the session."""

    agentRid: AgentRid
    """The Resource Identifier (RID) of the Agent associated with the session."""

    agentVersion: AgentVersionString
    """
    The version of the Agent associated with the session.
    This can be set by clients on session creation.
    If not specified, defaults to use the latest published version of the Agent at session creation time.
    """


class SessionExchange(pydantic.BaseModel):
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

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "SessionExchangeDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(SessionExchangeDict, self.model_dump(by_alias=True, exclude_none=True))


class SessionExchangeContexts(pydantic.BaseModel):
    """Retrieved context which was passed to the Agent as input for the exchange."""

    object_contexts: typing.List[ObjectContext] = pydantic.Field(alias=str("objectContexts"))  # type: ignore[literal-required]
    """Relevant object context for the user's message that was included in the prompt to the Agent."""

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "SessionExchangeContextsDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            SessionExchangeContextsDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class SessionExchangeContextsDict(typing_extensions.TypedDict):
    """Retrieved context which was passed to the Agent as input for the exchange."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    objectContexts: typing.List[ObjectContextDict]
    """Relevant object context for the user's message that was included in the prompt to the Agent."""


class SessionExchangeDict(typing_extensions.TypedDict):
    """Represents an individual exchange between a user and an Agent in a conversation session."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    userInput: UserTextInputDict
    """The user message that initiated the exchange."""

    contexts: typing_extensions.NotRequired[SessionExchangeContextsDict]
    """
    Additional retrieved context that was included in the prompt to the Agent.
    This may include context that was passed by the client with the user input, or relevant context that was automatically retrieved and added based on available data sources configured on the Agent.
    Empty if no additional context was included in the prompt.
    """

    result: SessionExchangeResultDict
    """The final result for the exchange."""


class SessionExchangeResult(pydantic.BaseModel):
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

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "SessionExchangeResultDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            SessionExchangeResultDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class SessionExchangeResultDict(typing_extensions.TypedDict):
    """The returned result from the Agent for a session exchange."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    agentMarkdownResponse: AgentMarkdownResponse
    """The final text response generated by the Agent. Responses are formatted using markdown."""

    parameterUpdates: typing.Dict[ParameterId, ParameterValueUpdateDict]
    """
    Any updates to application variable values which were generated by the Agent for this exchange.
    Updates can only be generated for application variables configured with `READ_WRITE` access on the Agent in AIP Agent Studio.
    """

    totalTokensUsed: typing_extensions.NotRequired[int]
    """Total tokens used to compute the result. Omitted if token usage information is not supported by the model used for the session."""

    interruptedOutput: bool
    """
    True if the exchange was canceled.
    In that case, the response (if any) was provided by the client as part of the cancellation request rather than by the Agent.
    """


class SessionMetadata(pydantic.BaseModel):
    """Metadata for a conversation session with an Agent."""

    title: str
    """The title of the session."""

    created_time: datetime = pydantic.Field(alias=str("createdTime"))  # type: ignore[literal-required]
    """The time the session was created."""

    updated_time: datetime = pydantic.Field(alias=str("updatedTime"))  # type: ignore[literal-required]
    """The time the session was last updated."""

    message_count: int = pydantic.Field(alias=str("messageCount"))  # type: ignore[literal-required]
    """
    The count of messages in the session.
    Includes both user messages and Agent replies, so each complete exchange counts as two messages.
    """

    estimated_expires_time: datetime = pydantic.Field(alias=str("estimatedExpiresTime"))  # type: ignore[literal-required]
    """
    The estimated time at which the session is due to expire.
    Once a session has expired, it can no longer be accessed and a new session must be created.
    The expiry time is automatically extended when new exchanges are added to the session.
    """

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "SessionMetadataDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(SessionMetadataDict, self.model_dump(by_alias=True, exclude_none=True))


class SessionMetadataDict(typing_extensions.TypedDict):
    """Metadata for a conversation session with an Agent."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    title: str
    """The title of the session."""

    createdTime: datetime
    """The time the session was created."""

    updatedTime: datetime
    """The time the session was last updated."""

    messageCount: int
    """
    The count of messages in the session.
    Includes both user messages and Agent replies, so each complete exchange counts as two messages.
    """

    estimatedExpiresTime: datetime
    """
    The estimated time at which the session is due to expire.
    Once a session has expired, it can no longer be accessed and a new session must be created.
    The expiry time is automatically extended when new exchanges are added to the session.
    """


SessionRid = core.RID
"""The Resource Identifier (RID) of the conversation session."""


class StringParameter(pydantic.BaseModel):
    """StringParameter"""

    default_value: typing.Optional[str] = pydantic.Field(alias=str("defaultValue"), default=None)  # type: ignore[literal-required]
    """The default value to use for this variable."""

    type: typing.Literal["string"] = "string"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "StringParameterDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(StringParameterDict, self.model_dump(by_alias=True, exclude_none=True))


class StringParameterDict(typing_extensions.TypedDict):
    """StringParameter"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    defaultValue: typing_extensions.NotRequired[str]
    """The default value to use for this variable."""

    type: typing.Literal["string"]


class StringParameterValue(pydantic.BaseModel):
    """A value passed for `StringParameter` application variable types."""

    value: str
    type: typing.Literal["string"] = "string"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "StringParameterValueDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            StringParameterValueDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class StringParameterValueDict(typing_extensions.TypedDict):
    """A value passed for `StringParameter` application variable types."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    value: str
    type: typing.Literal["string"]


class UserTextInput(pydantic.BaseModel):
    """UserTextInput"""

    text: str
    """The user message text."""

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "UserTextInputDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(UserTextInputDict, self.model_dump(by_alias=True, exclude_none=True))


class UserTextInputDict(typing_extensions.TypedDict):
    """UserTextInput"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    text: str
    """The user message text."""


from foundry.v2.core import models as core_models  # noqa: E402
from foundry.v2.functions import models as functions_models  # noqa: E402
from foundry.v2.ontologies import models as ontologies_models  # noqa: E402

__all__ = [
    "Agent",
    "AgentDict",
    "AgentMarkdownResponse",
    "AgentMetadata",
    "AgentMetadataDict",
    "AgentRid",
    "AgentSessionRagContextResponse",
    "AgentSessionRagContextResponseDict",
    "AgentVersion",
    "AgentVersionDetails",
    "AgentVersionDetailsDict",
    "AgentVersionDict",
    "AgentVersionString",
    "AgentsSessionsPage",
    "AgentsSessionsPageDict",
    "CancelSessionResponse",
    "CancelSessionResponseDict",
    "Content",
    "ContentDict",
    "FunctionRetrievedContext",
    "FunctionRetrievedContextDict",
    "InputContext",
    "InputContextDict",
    "ListAgentVersionsResponse",
    "ListAgentVersionsResponseDict",
    "ListSessionsResponse",
    "ListSessionsResponseDict",
    "MessageId",
    "ObjectContext",
    "ObjectContextDict",
    "ObjectSetParameter",
    "ObjectSetParameterDict",
    "ObjectSetParameterValue",
    "ObjectSetParameterValueDict",
    "ObjectSetParameterValueUpdate",
    "ObjectSetParameterValueUpdateDict",
    "Parameter",
    "ParameterAccessMode",
    "ParameterDict",
    "ParameterId",
    "ParameterType",
    "ParameterTypeDict",
    "ParameterValue",
    "ParameterValueDict",
    "ParameterValueUpdate",
    "ParameterValueUpdateDict",
    "Session",
    "SessionDict",
    "SessionExchange",
    "SessionExchangeContexts",
    "SessionExchangeContextsDict",
    "SessionExchangeDict",
    "SessionExchangeResult",
    "SessionExchangeResultDict",
    "SessionMetadata",
    "SessionMetadataDict",
    "SessionRid",
    "StringParameter",
    "StringParameterDict",
    "StringParameterValue",
    "StringParameterValueDict",
    "UserTextInput",
    "UserTextInputDict",
]
