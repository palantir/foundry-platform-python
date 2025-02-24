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

import warnings
from functools import cached_property
from typing import Any
from typing import Dict
from typing import List
from typing import Literal
from typing import Optional
from typing import Union

import pydantic
from typing_extensions import Annotated
from typing_extensions import TypedDict
from typing_extensions import deprecated
from typing_extensions import overload

from foundry._core import ApiClient
from foundry._core import ApiResponse
from foundry._core import Auth
from foundry._core import BinaryStream
from foundry._core import Config
from foundry._core import RequestInfo
from foundry._core import ResourceIterator
from foundry._core import StreamingContextManager
from foundry._core.utils import maybe_ignore_preview
from foundry._errors import handle_unexpected
from foundry.v2.aip_agents import errors as aip_agents_errors
from foundry.v2.aip_agents.models._agent_markdown_response import AgentMarkdownResponse
from foundry.v2.aip_agents.models._agent_rid import AgentRid
from foundry.v2.aip_agents.models._agent_session_rag_context_response import (
    AgentSessionRagContextResponse,
)  # NOQA
from foundry.v2.aip_agents.models._agent_version_string import AgentVersionString
from foundry.v2.aip_agents.models._cancel_session_response import CancelSessionResponse
from foundry.v2.aip_agents.models._input_context import InputContext
from foundry.v2.aip_agents.models._input_context_dict import InputContextDict
from foundry.v2.aip_agents.models._list_sessions_response import ListSessionsResponse
from foundry.v2.aip_agents.models._message_id import MessageId
from foundry.v2.aip_agents.models._parameter_id import ParameterId
from foundry.v2.aip_agents.models._parameter_value import ParameterValue
from foundry.v2.aip_agents.models._parameter_value_dict import ParameterValueDict
from foundry.v2.aip_agents.models._session import Session
from foundry.v2.aip_agents.models._session_exchange_result import SessionExchangeResult
from foundry.v2.aip_agents.models._session_rid import SessionRid
from foundry.v2.aip_agents.models._user_text_input import UserTextInput
from foundry.v2.aip_agents.models._user_text_input_dict import UserTextInputDict
from foundry.v2.core.models._page_size import PageSize
from foundry.v2.core.models._page_token import PageToken
from foundry.v2.core.models._preview_mode import PreviewMode


class SessionClient:
    """
    The API client for the Session Resource.

    :param auth: Your auth configuration.
    :param hostname: Your Foundry hostname (for example, "myfoundry.palantirfoundry.com"). This can also include your API gateway service URI.
    :param config: Optionally specify the configuration for the HTTP session.
    """

    def __init__(
        self,
        auth: Auth,
        hostname: str,
        config: Optional[Config] = None,
    ):
        self._auth = auth
        self._hostname = hostname
        self._config = config
        self._api_client = ApiClient(auth=auth, hostname=hostname, config=config)
        self.with_streaming_response = _SessionClientStreaming(
            auth=auth, hostname=hostname, config=config
        )
        self.with_raw_response = _SessionClientRaw(auth=auth, hostname=hostname, config=config)

    @cached_property
    def Content(self):
        from foundry.v2.aip_agents.content import ContentClient

        return ContentClient(
            auth=self._auth,
            hostname=self._hostname,
            config=self._config,
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def blocking_continue(
        self,
        agent_rid: AgentRid,
        session_rid: SessionRid,
        *,
        parameter_inputs: Dict[ParameterId, Union[ParameterValue, ParameterValueDict]],
        user_input: Union[UserTextInput, UserTextInputDict],
        contexts_override: Optional[List[Union[InputContext, InputContextDict]]] = None,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> SessionExchangeResult:
        """
        Continue a conversation session with an Agent, or add the first exchange to a session after creation.
        Adds a new exchange to the session with the provided inputs, and generates a response from the Agent.
        Blocks on returning the result of the added exchange until the response is fully generated.
        Streamed responses are also supported; see `streamingContinue` for details.
        Concurrent requests to continue the same session are not supported.
        Clients should wait to receive a response before sending the next message.

        :param agent_rid: agentRid
        :type agent_rid: AgentRid
        :param session_rid: sessionRid
        :type session_rid: SessionRid
        :param parameter_inputs: Any supplied values for [application variables](/docs/foundry/agent-studio/application-state/) to pass to the Agent for the exchange.
        :type parameter_inputs: Dict[ParameterId, Union[ParameterValue, ParameterValueDict]]
        :param user_input: The user message for the Agent to respond to.
        :type user_input: Union[UserTextInput, UserTextInputDict]
        :param contexts_override: If set, automatic [context retrieval](/docs/foundry/agent-studio/retrieval-context/) is skipped and the list of specified context is provided to the Agent instead. If omitted, relevant context for the user message is automatically retrieved and included in the prompt, based on data sources configured on the Agent for the session.
        :type contexts_override: Optional[List[Union[InputContext, InputContextDict]]]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: SessionExchangeResult

        :raises AgentIterationsExceededLimit: The Agent was unable to produce an answer in the set number of maximum iterations. This can happen if the Agent gets confused or stuck in a loop, or if the query is too complex. Try a different query or review the Agent configuration in AIP Agent Studio.
        :raises BlockingContinueSessionPermissionDenied: Could not blockingContinue the Session.
        :raises ContextSizeExceededLimit: Failed to generate a response for a session because the context size of the LLM has been exceeded. Clients should either retry with a shorter message or create a new session and try re-sending the message.
        :raises FunctionLocatorNotFound: The specified function locator is configured for use by the Agent but could not be found. The function type or version may not exist or the client token does not have access.
        :raises InvalidParameter: The provided application variable is not valid for the Agent for this session. Check the available application variables for the Agent under the `parameters` property, and version through the API with `getAgent`, or in AIP Agent Studio. The Agent version used for the session can be checked through the API with `getSession`.
        :raises InvalidParameterType: The provided value does not match the expected type for the application variable configured on the Agent for this session. Check the available application variables for the Agent under the `parameters` property, and version through the API with `getAgent`, or in AIP Agent Studio. The Agent version used for the session can be checked through the API with `getSession`.
        :raises ObjectTypeIdsNotFound: Some object types are configured for use by the Agent but could not be found. The object types either do not exist or the client token does not have access. Object types can be checked by listing available object types through the API, or searching in [Ontology Manager](/docs/foundry/ontology-manager/overview/).
        :raises ObjectTypeRidsNotFound: Some object types are configured for use by the Agent but could not be found. The object types either do not exist or the client token does not have access. Object types can be checked by listing available object types through the API, or searching in [Ontology Manager](/docs/foundry/ontology-manager/overview/).
        :raises RateLimitExceeded: Failed to generate a response as the model rate limits were exceeded. Clients should wait and retry.
        :raises SessionExecutionFailed: Failed to generate a response for a session due to an unexpected error.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/aipAgents/agents/{agentRid}/sessions/{sessionRid}/blockingContinue",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "agentRid": agent_rid,
                    "sessionRid": session_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "userInput": user_input,
                    "parameterInputs": parameter_inputs,
                    "contextsOverride": contexts_override,
                },
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "userInput": Union[UserTextInput, UserTextInputDict],
                        "parameterInputs": Dict[
                            ParameterId, Union[ParameterValue, ParameterValueDict]
                        ],
                        "contextsOverride": Optional[List[Union[InputContext, InputContextDict]]],
                    },
                ),
                response_type=SessionExchangeResult,
                request_timeout=request_timeout,
                throwable_errors={
                    "AgentIterationsExceededLimit": aip_agents_errors.AgentIterationsExceededLimit,
                    "BlockingContinueSessionPermissionDenied": aip_agents_errors.BlockingContinueSessionPermissionDenied,
                    "ContextSizeExceededLimit": aip_agents_errors.ContextSizeExceededLimit,
                    "FunctionLocatorNotFound": aip_agents_errors.FunctionLocatorNotFound,
                    "InvalidParameter": aip_agents_errors.InvalidParameter,
                    "InvalidParameterType": aip_agents_errors.InvalidParameterType,
                    "ObjectTypeIdsNotFound": aip_agents_errors.ObjectTypeIdsNotFound,
                    "ObjectTypeRidsNotFound": aip_agents_errors.ObjectTypeRidsNotFound,
                    "RateLimitExceeded": aip_agents_errors.RateLimitExceeded,
                    "SessionExecutionFailed": aip_agents_errors.SessionExecutionFailed,
                },
            ),
        ).decode()

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def cancel(
        self,
        agent_rid: AgentRid,
        session_rid: SessionRid,
        *,
        message_id: MessageId,
        preview: Optional[PreviewMode] = None,
        response: Optional[AgentMarkdownResponse] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> CancelSessionResponse:
        """
        Cancel an in-progress streamed exchange with an Agent which was initiated with `streamingContinue`.
        Canceling an exchange allows clients to prevent the exchange from being added to the session, or to provide a response to replace the Agent-generated response.
        Note that canceling an exchange does not terminate the stream returned by `streamingContinue`; clients should close the stream on triggering the cancellation request to stop reading from the stream.

        :param agent_rid: agentRid
        :type agent_rid: AgentRid
        :param session_rid: sessionRid
        :type session_rid: SessionRid
        :param message_id: The identifier for the in-progress exchange to cancel. This should match the `messageId` which was provided when initiating the exchange with `streamingContinue`.
        :type message_id: MessageId
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param response: When specified, the exchange is added to the session with the client-provided response as the result. When omitted, the exchange is not added to the session.
        :type response: Optional[AgentMarkdownResponse]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: CancelSessionResponse

        :raises CancelSessionFailedMessageNotInProgress: Unable to cancel the requested session exchange as no in-progress exchange was found for the provided message identifier. This is expected if no exchange was initiated with the provided message identifier through a `streamingContinue` request, or if the exchange for this identifier has already completed and cannot be canceled, or if the exchange has already been canceled. This error can also occur if the cancellation was requested immediately after requesting the exchange through a `streamingContinue` request, and the exchange has not started yet. Clients should handle these errors gracefully, and can reload the session content to get the latest conversation state.
        :raises CancelSessionPermissionDenied: Could not cancel the Session.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/aipAgents/agents/{agentRid}/sessions/{sessionRid}/cancel",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "agentRid": agent_rid,
                    "sessionRid": session_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "messageId": message_id,
                    "response": response,
                },
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "messageId": MessageId,
                        "response": Optional[AgentMarkdownResponse],
                    },
                ),
                response_type=CancelSessionResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "CancelSessionFailedMessageNotInProgress": aip_agents_errors.CancelSessionFailedMessageNotInProgress,
                    "CancelSessionPermissionDenied": aip_agents_errors.CancelSessionPermissionDenied,
                },
            ),
        ).decode()

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def create(
        self,
        agent_rid: AgentRid,
        *,
        agent_version: Optional[AgentVersionString] = None,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> Session:
        """
        Create a new conversation session between the calling user and an Agent.
        Use `blockingContinue` or `streamingContinue` to start adding exchanges to the session.

        :param agent_rid: agentRid
        :type agent_rid: AgentRid
        :param agent_version: The version of the Agent associated with the session. This can be set by clients on session creation. If not specified, defaults to use the latest published version of the Agent at session creation time.
        :type agent_version: Optional[AgentVersionString]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: Session

        :raises CreateSessionPermissionDenied: Could not create the Session.
        :raises FunctionLocatorNotFound: The specified function locator is configured for use by the Agent but could not be found. The function type or version may not exist or the client token does not have access.
        :raises NoPublishedAgentVersion: Failed to retrieve the latest published version of the Agent because the Agent has no published versions. Try publishing the Agent in AIP Agent Studio to use the latest published version, or specify the version of the Agent to use.
        :raises ObjectTypeIdsNotFound: Some object types are configured for use by the Agent but could not be found. The object types either do not exist or the client token does not have access. Object types can be checked by listing available object types through the API, or searching in [Ontology Manager](/docs/foundry/ontology-manager/overview/).
        :raises ObjectTypeRidsNotFound: Some object types are configured for use by the Agent but could not be found. The object types either do not exist or the client token does not have access. Object types can be checked by listing available object types through the API, or searching in [Ontology Manager](/docs/foundry/ontology-manager/overview/).
        """

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/aipAgents/agents/{agentRid}/sessions",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "agentRid": agent_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "agentVersion": agent_version,
                },
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "agentVersion": Optional[AgentVersionString],
                    },
                ),
                response_type=Session,
                request_timeout=request_timeout,
                throwable_errors={
                    "CreateSessionPermissionDenied": aip_agents_errors.CreateSessionPermissionDenied,
                    "FunctionLocatorNotFound": aip_agents_errors.FunctionLocatorNotFound,
                    "NoPublishedAgentVersion": aip_agents_errors.NoPublishedAgentVersion,
                    "ObjectTypeIdsNotFound": aip_agents_errors.ObjectTypeIdsNotFound,
                    "ObjectTypeRidsNotFound": aip_agents_errors.ObjectTypeRidsNotFound,
                },
            ),
        ).decode()

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def get(
        self,
        agent_rid: AgentRid,
        session_rid: SessionRid,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> Session:
        """
        Get the details of a conversation session between the calling user and an Agent.
        :param agent_rid: agentRid
        :type agent_rid: AgentRid
        :param session_rid: sessionRid
        :type session_rid: SessionRid
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: Session

        :raises SessionNotFound: The given Session could not be found.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/aipAgents/agents/{agentRid}/sessions/{sessionRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "agentRid": agent_rid,
                    "sessionRid": session_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=Session,
                request_timeout=request_timeout,
                throwable_errors={
                    "SessionNotFound": aip_agents_errors.SessionNotFound,
                },
            ),
        ).decode()

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def list(
        self,
        agent_rid: AgentRid,
        *,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ResourceIterator[Session]:
        """
        List all conversation sessions between the calling user and an Agent that was created by this client.
        This does not list sessions for the user created by other clients.
        For example, any sessions created by the user in AIP Agent Studio will not be listed here.
        Sessions are returned in order of most recently updated first.

        :param agent_rid: agentRid
        :type agent_rid: AgentRid
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param page_token: pageToken
        :type page_token: Optional[PageToken]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ResourceIterator[Session]
        """

        return self._api_client.iterate_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/aipAgents/agents/{agentRid}/sessions",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
                    "preview": preview,
                },
                path_params={
                    "agentRid": agent_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ListSessionsResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def page(
        self,
        agent_rid: AgentRid,
        *,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ListSessionsResponse:
        """
        List all conversation sessions between the calling user and an Agent that was created by this client.
        This does not list sessions for the user created by other clients.
        For example, any sessions created by the user in AIP Agent Studio will not be listed here.
        Sessions are returned in order of most recently updated first.

        :param agent_rid: agentRid
        :type agent_rid: AgentRid
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param page_token: pageToken
        :type page_token: Optional[PageToken]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ListSessionsResponse
        """

        warnings.warn(
            "The client.aip_agents.Session.page(...) method has been deprecated. Please use client.aip_agents.Session.list(...) instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/aipAgents/agents/{agentRid}/sessions",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
                    "preview": preview,
                },
                path_params={
                    "agentRid": agent_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ListSessionsResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        ).decode()

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def rag_context(
        self,
        agent_rid: AgentRid,
        session_rid: SessionRid,
        *,
        parameter_inputs: Dict[ParameterId, Union[ParameterValue, ParameterValueDict]],
        user_input: Union[UserTextInput, UserTextInputDict],
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> AgentSessionRagContextResponse:
        """
        Retrieve relevant [context](/docs/foundry/agent-studio/core-concepts/#retrieval-context) for a user message from the data sources configured for the session.
        This allows clients to pre-retrieve context for a user message before sending it to the Agent with the `contextsOverride` option when continuing a session, to allow any pre-processing of the context before sending it to the Agent.

        :param agent_rid: agentRid
        :type agent_rid: AgentRid
        :param session_rid: sessionRid
        :type session_rid: SessionRid
        :param parameter_inputs: Any values for [application variables](/docs/foundry/agent-studio/application-state/) to use for the context retrieval.
        :type parameter_inputs: Dict[ParameterId, Union[ParameterValue, ParameterValueDict]]
        :param user_input: The user message to retrieve relevant context for from the configured Agent data sources.
        :type user_input: Union[UserTextInput, UserTextInputDict]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: AgentSessionRagContextResponse

        :raises FunctionLocatorNotFound: The specified function locator is configured for use by the Agent but could not be found. The function type or version may not exist or the client token does not have access.
        :raises GetRagContextForSessionPermissionDenied: Could not ragContext the Session.
        :raises ObjectTypeIdsNotFound: Some object types are configured for use by the Agent but could not be found. The object types either do not exist or the client token does not have access. Object types can be checked by listing available object types through the API, or searching in [Ontology Manager](/docs/foundry/ontology-manager/overview/).
        :raises ObjectTypeRidsNotFound: Some object types are configured for use by the Agent but could not be found. The object types either do not exist or the client token does not have access. Object types can be checked by listing available object types through the API, or searching in [Ontology Manager](/docs/foundry/ontology-manager/overview/).
        """

        return self._api_client.call_api(
            RequestInfo(
                method="PUT",
                resource_path="/v2/aipAgents/agents/{agentRid}/sessions/{sessionRid}/ragContext",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "agentRid": agent_rid,
                    "sessionRid": session_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "userInput": user_input,
                    "parameterInputs": parameter_inputs,
                },
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "userInput": Union[UserTextInput, UserTextInputDict],
                        "parameterInputs": Dict[
                            ParameterId, Union[ParameterValue, ParameterValueDict]
                        ],
                    },
                ),
                response_type=AgentSessionRagContextResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "FunctionLocatorNotFound": aip_agents_errors.FunctionLocatorNotFound,
                    "GetRagContextForSessionPermissionDenied": aip_agents_errors.GetRagContextForSessionPermissionDenied,
                    "ObjectTypeIdsNotFound": aip_agents_errors.ObjectTypeIdsNotFound,
                    "ObjectTypeRidsNotFound": aip_agents_errors.ObjectTypeRidsNotFound,
                },
            ),
        ).decode()

    @overload
    @deprecated(
        "Using the `stream` parameter is deprecated. Please use the `with_streaming_response` instead."
    )
    def streaming_continue(
        self,
        agent_rid: AgentRid,
        session_rid: SessionRid,
        *,
        stream: Literal[True],
        parameter_inputs: Dict[ParameterId, Union[ParameterValue, ParameterValueDict]],
        user_input: Union[UserTextInput, UserTextInputDict],
        contexts_override: Optional[List[Union[InputContext, InputContextDict]]] = None,
        message_id: Optional[MessageId] = None,
        preview: Optional[PreviewMode] = None,
        chunk_size: Optional[int] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> BinaryStream:
        """
        Continue a conversation session with an Agent, or add the first exchange to a session after creation.
        Adds a new exchange to the session with the provided inputs, and generates a response from the Agent.
        Returns a stream of the Agent response text (formatted using markdown) for clients to consume as the response is generated.
        On completion of the streamed response, clients can load the full details of the exchange that was added to the session by reloading the session content.
        Streamed exchanges also support cancellation; see `cancel` for details.
        Concurrent requests to continue the same session are not supported.
        Clients should wait to receive a response, or cancel the in-progress exchange, before sending the next message.

        :param agent_rid: agentRid
        :type agent_rid: AgentRid
        :param session_rid: sessionRid
        :type session_rid: SessionRid
        :param parameter_inputs: Any supplied values for [application variables](/docs/foundry/agent-studio/application-state/) to pass to the Agent for the exchange.
        :type parameter_inputs: Dict[ParameterId, Union[ParameterValue, ParameterValueDict]]
        :param user_input: The user message for the Agent to respond to.
        :type user_input: Union[UserTextInput, UserTextInputDict]
        :param contexts_override: If set, automatic [context](/docs/foundry/agent-studio/retrieval-context/) retrieval is skipped and the list of specified context is provided to the Agent instead. If omitted, relevant context for the user message is automatically retrieved and included in the prompt, based on data sources configured on the Agent for the session.
        :type contexts_override: Optional[List[Union[InputContext, InputContextDict]]]
        :param message_id: A client-generated Universally Unique Identifier (UUID) to identify the message, which the client can use to cancel the exchange before the streaming response is complete.
        :type message_id: Optional[MessageId]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param stream: Whether to stream back the binary data in an iterator. This avoids reading the entire content of the response into memory at once.
        :type stream: bool
        :param chunk_size: The number of bytes that should be read into memory for each chunk. If set to None, the data will become available as it arrives in whatever size is sent from the host.
        :type chunk_size: Optional[int]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: BinaryStream

        :raises FunctionLocatorNotFound: The specified function locator is configured for use by the Agent but could not be found. The function type or version may not exist or the client token does not have access.
        :raises InvalidParameter: The provided application variable is not valid for the Agent for this session. Check the available application variables for the Agent under the `parameters` property, and version through the API with `getAgent`, or in AIP Agent Studio. The Agent version used for the session can be checked through the API with `getSession`.
        :raises InvalidParameterType: The provided value does not match the expected type for the application variable configured on the Agent for this session. Check the available application variables for the Agent under the `parameters` property, and version through the API with `getAgent`, or in AIP Agent Studio. The Agent version used for the session can be checked through the API with `getSession`.
        :raises ObjectTypeIdsNotFound: Some object types are configured for use by the Agent but could not be found. The object types either do not exist or the client token does not have access. Object types can be checked by listing available object types through the API, or searching in [Ontology Manager](/docs/foundry/ontology-manager/overview/).
        :raises ObjectTypeRidsNotFound: Some object types are configured for use by the Agent but could not be found. The object types either do not exist or the client token does not have access. Object types can be checked by listing available object types through the API, or searching in [Ontology Manager](/docs/foundry/ontology-manager/overview/).
        :raises StreamingContinueSessionPermissionDenied: Could not streamingContinue the Session.
        """
        ...

    @overload
    def streaming_continue(
        self,
        agent_rid: AgentRid,
        session_rid: SessionRid,
        *,
        parameter_inputs: Dict[ParameterId, Union[ParameterValue, ParameterValueDict]],
        user_input: Union[UserTextInput, UserTextInputDict],
        contexts_override: Optional[List[Union[InputContext, InputContextDict]]] = None,
        message_id: Optional[MessageId] = None,
        preview: Optional[PreviewMode] = None,
        stream: Literal[False] = False,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> bytes:
        """
        Continue a conversation session with an Agent, or add the first exchange to a session after creation.
        Adds a new exchange to the session with the provided inputs, and generates a response from the Agent.
        Returns a stream of the Agent response text (formatted using markdown) for clients to consume as the response is generated.
        On completion of the streamed response, clients can load the full details of the exchange that was added to the session by reloading the session content.
        Streamed exchanges also support cancellation; see `cancel` for details.
        Concurrent requests to continue the same session are not supported.
        Clients should wait to receive a response, or cancel the in-progress exchange, before sending the next message.

        :param agent_rid: agentRid
        :type agent_rid: AgentRid
        :param session_rid: sessionRid
        :type session_rid: SessionRid
        :param parameter_inputs: Any supplied values for [application variables](/docs/foundry/agent-studio/application-state/) to pass to the Agent for the exchange.
        :type parameter_inputs: Dict[ParameterId, Union[ParameterValue, ParameterValueDict]]
        :param user_input: The user message for the Agent to respond to.
        :type user_input: Union[UserTextInput, UserTextInputDict]
        :param contexts_override: If set, automatic [context](/docs/foundry/agent-studio/retrieval-context/) retrieval is skipped and the list of specified context is provided to the Agent instead. If omitted, relevant context for the user message is automatically retrieved and included in the prompt, based on data sources configured on the Agent for the session.
        :type contexts_override: Optional[List[Union[InputContext, InputContextDict]]]
        :param message_id: A client-generated Universally Unique Identifier (UUID) to identify the message, which the client can use to cancel the exchange before the streaming response is complete.
        :type message_id: Optional[MessageId]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param stream: Whether to stream back the binary data in an iterator. This avoids reading the entire content of the response into memory at once.
        :type stream: bool
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: bytes

        :raises FunctionLocatorNotFound: The specified function locator is configured for use by the Agent but could not be found. The function type or version may not exist or the client token does not have access.
        :raises InvalidParameter: The provided application variable is not valid for the Agent for this session. Check the available application variables for the Agent under the `parameters` property, and version through the API with `getAgent`, or in AIP Agent Studio. The Agent version used for the session can be checked through the API with `getSession`.
        :raises InvalidParameterType: The provided value does not match the expected type for the application variable configured on the Agent for this session. Check the available application variables for the Agent under the `parameters` property, and version through the API with `getAgent`, or in AIP Agent Studio. The Agent version used for the session can be checked through the API with `getSession`.
        :raises ObjectTypeIdsNotFound: Some object types are configured for use by the Agent but could not be found. The object types either do not exist or the client token does not have access. Object types can be checked by listing available object types through the API, or searching in [Ontology Manager](/docs/foundry/ontology-manager/overview/).
        :raises ObjectTypeRidsNotFound: Some object types are configured for use by the Agent but could not be found. The object types either do not exist or the client token does not have access. Object types can be checked by listing available object types through the API, or searching in [Ontology Manager](/docs/foundry/ontology-manager/overview/).
        :raises StreamingContinueSessionPermissionDenied: Could not streamingContinue the Session.
        """
        ...

    @overload
    @deprecated(
        "Using the `stream` parameter is deprecated. Please use the `with_streaming_response` instead."
    )
    def streaming_continue(
        self,
        agent_rid: AgentRid,
        session_rid: SessionRid,
        *,
        stream: bool,
        parameter_inputs: Dict[ParameterId, Union[ParameterValue, ParameterValueDict]],
        user_input: Union[UserTextInput, UserTextInputDict],
        contexts_override: Optional[List[Union[InputContext, InputContextDict]]] = None,
        message_id: Optional[MessageId] = None,
        preview: Optional[PreviewMode] = None,
        chunk_size: Optional[int] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> Union[bytes, BinaryStream]:
        """
        Continue a conversation session with an Agent, or add the first exchange to a session after creation.
        Adds a new exchange to the session with the provided inputs, and generates a response from the Agent.
        Returns a stream of the Agent response text (formatted using markdown) for clients to consume as the response is generated.
        On completion of the streamed response, clients can load the full details of the exchange that was added to the session by reloading the session content.
        Streamed exchanges also support cancellation; see `cancel` for details.
        Concurrent requests to continue the same session are not supported.
        Clients should wait to receive a response, or cancel the in-progress exchange, before sending the next message.

        :param agent_rid: agentRid
        :type agent_rid: AgentRid
        :param session_rid: sessionRid
        :type session_rid: SessionRid
        :param parameter_inputs: Any supplied values for [application variables](/docs/foundry/agent-studio/application-state/) to pass to the Agent for the exchange.
        :type parameter_inputs: Dict[ParameterId, Union[ParameterValue, ParameterValueDict]]
        :param user_input: The user message for the Agent to respond to.
        :type user_input: Union[UserTextInput, UserTextInputDict]
        :param contexts_override: If set, automatic [context](/docs/foundry/agent-studio/retrieval-context/) retrieval is skipped and the list of specified context is provided to the Agent instead. If omitted, relevant context for the user message is automatically retrieved and included in the prompt, based on data sources configured on the Agent for the session.
        :type contexts_override: Optional[List[Union[InputContext, InputContextDict]]]
        :param message_id: A client-generated Universally Unique Identifier (UUID) to identify the message, which the client can use to cancel the exchange before the streaming response is complete.
        :type message_id: Optional[MessageId]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param stream: Whether to stream back the binary data in an iterator. This avoids reading the entire content of the response into memory at once.
        :type stream: bool
        :param chunk_size: The number of bytes that should be read into memory for each chunk. If set to None, the data will become available as it arrives in whatever size is sent from the host.
        :type chunk_size: Optional[int]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: Union[bytes, BinaryStream]

        :raises FunctionLocatorNotFound: The specified function locator is configured for use by the Agent but could not be found. The function type or version may not exist or the client token does not have access.
        :raises InvalidParameter: The provided application variable is not valid for the Agent for this session. Check the available application variables for the Agent under the `parameters` property, and version through the API with `getAgent`, or in AIP Agent Studio. The Agent version used for the session can be checked through the API with `getSession`.
        :raises InvalidParameterType: The provided value does not match the expected type for the application variable configured on the Agent for this session. Check the available application variables for the Agent under the `parameters` property, and version through the API with `getAgent`, or in AIP Agent Studio. The Agent version used for the session can be checked through the API with `getSession`.
        :raises ObjectTypeIdsNotFound: Some object types are configured for use by the Agent but could not be found. The object types either do not exist or the client token does not have access. Object types can be checked by listing available object types through the API, or searching in [Ontology Manager](/docs/foundry/ontology-manager/overview/).
        :raises ObjectTypeRidsNotFound: Some object types are configured for use by the Agent but could not be found. The object types either do not exist or the client token does not have access. Object types can be checked by listing available object types through the API, or searching in [Ontology Manager](/docs/foundry/ontology-manager/overview/).
        :raises StreamingContinueSessionPermissionDenied: Could not streamingContinue the Session.
        """
        ...

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def streaming_continue(
        self,
        agent_rid: AgentRid,
        session_rid: SessionRid,
        *,
        parameter_inputs: Dict[ParameterId, Union[ParameterValue, ParameterValueDict]],
        user_input: Union[UserTextInput, UserTextInputDict],
        contexts_override: Optional[List[Union[InputContext, InputContextDict]]] = None,
        message_id: Optional[MessageId] = None,
        preview: Optional[PreviewMode] = None,
        stream: bool = False,
        chunk_size: Optional[int] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> Union[bytes, BinaryStream]:
        """
        Continue a conversation session with an Agent, or add the first exchange to a session after creation.
        Adds a new exchange to the session with the provided inputs, and generates a response from the Agent.
        Returns a stream of the Agent response text (formatted using markdown) for clients to consume as the response is generated.
        On completion of the streamed response, clients can load the full details of the exchange that was added to the session by reloading the session content.
        Streamed exchanges also support cancellation; see `cancel` for details.
        Concurrent requests to continue the same session are not supported.
        Clients should wait to receive a response, or cancel the in-progress exchange, before sending the next message.

        :param agent_rid: agentRid
        :type agent_rid: AgentRid
        :param session_rid: sessionRid
        :type session_rid: SessionRid
        :param parameter_inputs: Any supplied values for [application variables](/docs/foundry/agent-studio/application-state/) to pass to the Agent for the exchange.
        :type parameter_inputs: Dict[ParameterId, Union[ParameterValue, ParameterValueDict]]
        :param user_input: The user message for the Agent to respond to.
        :type user_input: Union[UserTextInput, UserTextInputDict]
        :param contexts_override: If set, automatic [context](/docs/foundry/agent-studio/retrieval-context/) retrieval is skipped and the list of specified context is provided to the Agent instead. If omitted, relevant context for the user message is automatically retrieved and included in the prompt, based on data sources configured on the Agent for the session.
        :type contexts_override: Optional[List[Union[InputContext, InputContextDict]]]
        :param message_id: A client-generated Universally Unique Identifier (UUID) to identify the message, which the client can use to cancel the exchange before the streaming response is complete.
        :type message_id: Optional[MessageId]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param stream: Whether to stream back the binary data in an iterator. This avoids reading the entire content of the response into memory at once.
        :type stream: bool
        :param chunk_size: The number of bytes that should be read into memory for each chunk. If set to None, the data will become available as it arrives in whatever size is sent from the host.
        :type chunk_size: Optional[int]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: Union[bytes, BinaryStream]

        :raises FunctionLocatorNotFound: The specified function locator is configured for use by the Agent but could not be found. The function type or version may not exist or the client token does not have access.
        :raises InvalidParameter: The provided application variable is not valid for the Agent for this session. Check the available application variables for the Agent under the `parameters` property, and version through the API with `getAgent`, or in AIP Agent Studio. The Agent version used for the session can be checked through the API with `getSession`.
        :raises InvalidParameterType: The provided value does not match the expected type for the application variable configured on the Agent for this session. Check the available application variables for the Agent under the `parameters` property, and version through the API with `getAgent`, or in AIP Agent Studio. The Agent version used for the session can be checked through the API with `getSession`.
        :raises ObjectTypeIdsNotFound: Some object types are configured for use by the Agent but could not be found. The object types either do not exist or the client token does not have access. Object types can be checked by listing available object types through the API, or searching in [Ontology Manager](/docs/foundry/ontology-manager/overview/).
        :raises ObjectTypeRidsNotFound: Some object types are configured for use by the Agent but could not be found. The object types either do not exist or the client token does not have access. Object types can be checked by listing available object types through the API, or searching in [Ontology Manager](/docs/foundry/ontology-manager/overview/).
        :raises StreamingContinueSessionPermissionDenied: Could not streamingContinue the Session.
        """

        if stream:
            warnings.warn(
                f"client.aip_agents.Agent.Session.streaming_continue(..., stream=True, chunk_size={chunk_size}) is deprecated. Please use:\n\nwith client.aip_agents.Agent.Session.with_streaming_response.streaming_continue(...) as response:\n    response.iter_bytes(chunk_size={chunk_size})\n",
                DeprecationWarning,
                stacklevel=2,
            )

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/aipAgents/agents/{agentRid}/sessions/{sessionRid}/streamingContinue",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "agentRid": agent_rid,
                    "sessionRid": session_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/octet-stream",
                },
                body={
                    "userInput": user_input,
                    "parameterInputs": parameter_inputs,
                    "contextsOverride": contexts_override,
                    "messageId": message_id,
                },
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "userInput": Union[UserTextInput, UserTextInputDict],
                        "parameterInputs": Dict[
                            ParameterId, Union[ParameterValue, ParameterValueDict]
                        ],
                        "contextsOverride": Optional[List[Union[InputContext, InputContextDict]]],
                        "messageId": Optional[MessageId],
                    },
                ),
                response_type=bytes,
                stream=stream,
                chunk_size=chunk_size,
                request_timeout=request_timeout,
                throwable_errors={
                    "FunctionLocatorNotFound": aip_agents_errors.FunctionLocatorNotFound,
                    "InvalidParameter": aip_agents_errors.InvalidParameter,
                    "InvalidParameterType": aip_agents_errors.InvalidParameterType,
                    "ObjectTypeIdsNotFound": aip_agents_errors.ObjectTypeIdsNotFound,
                    "ObjectTypeRidsNotFound": aip_agents_errors.ObjectTypeRidsNotFound,
                    "StreamingContinueSessionPermissionDenied": aip_agents_errors.StreamingContinueSessionPermissionDenied,
                },
            ),
        ).decode()


class _SessionClientRaw:
    """
    The API client for the Session Resource.

    :param auth: Your auth configuration.
    :param hostname: Your Foundry hostname (for example, "myfoundry.palantirfoundry.com"). This can also include your API gateway service URI.
    :param config: Optionally specify the configuration for the HTTP session.
    """

    def __init__(
        self,
        auth: Auth,
        hostname: str,
        config: Optional[Config] = None,
    ):
        self._auth = auth
        self._hostname = hostname
        self._config = config
        self._api_client = ApiClient(auth=auth, hostname=hostname, config=config)

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def blocking_continue(
        self,
        agent_rid: AgentRid,
        session_rid: SessionRid,
        *,
        parameter_inputs: Dict[ParameterId, Union[ParameterValue, ParameterValueDict]],
        user_input: Union[UserTextInput, UserTextInputDict],
        contexts_override: Optional[List[Union[InputContext, InputContextDict]]] = None,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[SessionExchangeResult]:
        """
        Continue a conversation session with an Agent, or add the first exchange to a session after creation.
        Adds a new exchange to the session with the provided inputs, and generates a response from the Agent.
        Blocks on returning the result of the added exchange until the response is fully generated.
        Streamed responses are also supported; see `streamingContinue` for details.
        Concurrent requests to continue the same session are not supported.
        Clients should wait to receive a response before sending the next message.

        :param agent_rid: agentRid
        :type agent_rid: AgentRid
        :param session_rid: sessionRid
        :type session_rid: SessionRid
        :param parameter_inputs: Any supplied values for [application variables](/docs/foundry/agent-studio/application-state/) to pass to the Agent for the exchange.
        :type parameter_inputs: Dict[ParameterId, Union[ParameterValue, ParameterValueDict]]
        :param user_input: The user message for the Agent to respond to.
        :type user_input: Union[UserTextInput, UserTextInputDict]
        :param contexts_override: If set, automatic [context retrieval](/docs/foundry/agent-studio/retrieval-context/) is skipped and the list of specified context is provided to the Agent instead. If omitted, relevant context for the user message is automatically retrieved and included in the prompt, based on data sources configured on the Agent for the session.
        :type contexts_override: Optional[List[Union[InputContext, InputContextDict]]]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[SessionExchangeResult]

        :raises AgentIterationsExceededLimit: The Agent was unable to produce an answer in the set number of maximum iterations. This can happen if the Agent gets confused or stuck in a loop, or if the query is too complex. Try a different query or review the Agent configuration in AIP Agent Studio.
        :raises BlockingContinueSessionPermissionDenied: Could not blockingContinue the Session.
        :raises ContextSizeExceededLimit: Failed to generate a response for a session because the context size of the LLM has been exceeded. Clients should either retry with a shorter message or create a new session and try re-sending the message.
        :raises FunctionLocatorNotFound: The specified function locator is configured for use by the Agent but could not be found. The function type or version may not exist or the client token does not have access.
        :raises InvalidParameter: The provided application variable is not valid for the Agent for this session. Check the available application variables for the Agent under the `parameters` property, and version through the API with `getAgent`, or in AIP Agent Studio. The Agent version used for the session can be checked through the API with `getSession`.
        :raises InvalidParameterType: The provided value does not match the expected type for the application variable configured on the Agent for this session. Check the available application variables for the Agent under the `parameters` property, and version through the API with `getAgent`, or in AIP Agent Studio. The Agent version used for the session can be checked through the API with `getSession`.
        :raises ObjectTypeIdsNotFound: Some object types are configured for use by the Agent but could not be found. The object types either do not exist or the client token does not have access. Object types can be checked by listing available object types through the API, or searching in [Ontology Manager](/docs/foundry/ontology-manager/overview/).
        :raises ObjectTypeRidsNotFound: Some object types are configured for use by the Agent but could not be found. The object types either do not exist or the client token does not have access. Object types can be checked by listing available object types through the API, or searching in [Ontology Manager](/docs/foundry/ontology-manager/overview/).
        :raises RateLimitExceeded: Failed to generate a response as the model rate limits were exceeded. Clients should wait and retry.
        :raises SessionExecutionFailed: Failed to generate a response for a session due to an unexpected error.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/aipAgents/agents/{agentRid}/sessions/{sessionRid}/blockingContinue",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "agentRid": agent_rid,
                    "sessionRid": session_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "userInput": user_input,
                    "parameterInputs": parameter_inputs,
                    "contextsOverride": contexts_override,
                },
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "userInput": Union[UserTextInput, UserTextInputDict],
                        "parameterInputs": Dict[
                            ParameterId, Union[ParameterValue, ParameterValueDict]
                        ],
                        "contextsOverride": Optional[List[Union[InputContext, InputContextDict]]],
                    },
                ),
                response_type=SessionExchangeResult,
                request_timeout=request_timeout,
                throwable_errors={
                    "AgentIterationsExceededLimit": aip_agents_errors.AgentIterationsExceededLimit,
                    "BlockingContinueSessionPermissionDenied": aip_agents_errors.BlockingContinueSessionPermissionDenied,
                    "ContextSizeExceededLimit": aip_agents_errors.ContextSizeExceededLimit,
                    "FunctionLocatorNotFound": aip_agents_errors.FunctionLocatorNotFound,
                    "InvalidParameter": aip_agents_errors.InvalidParameter,
                    "InvalidParameterType": aip_agents_errors.InvalidParameterType,
                    "ObjectTypeIdsNotFound": aip_agents_errors.ObjectTypeIdsNotFound,
                    "ObjectTypeRidsNotFound": aip_agents_errors.ObjectTypeRidsNotFound,
                    "RateLimitExceeded": aip_agents_errors.RateLimitExceeded,
                    "SessionExecutionFailed": aip_agents_errors.SessionExecutionFailed,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def cancel(
        self,
        agent_rid: AgentRid,
        session_rid: SessionRid,
        *,
        message_id: MessageId,
        preview: Optional[PreviewMode] = None,
        response: Optional[AgentMarkdownResponse] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[CancelSessionResponse]:
        """
        Cancel an in-progress streamed exchange with an Agent which was initiated with `streamingContinue`.
        Canceling an exchange allows clients to prevent the exchange from being added to the session, or to provide a response to replace the Agent-generated response.
        Note that canceling an exchange does not terminate the stream returned by `streamingContinue`; clients should close the stream on triggering the cancellation request to stop reading from the stream.

        :param agent_rid: agentRid
        :type agent_rid: AgentRid
        :param session_rid: sessionRid
        :type session_rid: SessionRid
        :param message_id: The identifier for the in-progress exchange to cancel. This should match the `messageId` which was provided when initiating the exchange with `streamingContinue`.
        :type message_id: MessageId
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param response: When specified, the exchange is added to the session with the client-provided response as the result. When omitted, the exchange is not added to the session.
        :type response: Optional[AgentMarkdownResponse]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[CancelSessionResponse]

        :raises CancelSessionFailedMessageNotInProgress: Unable to cancel the requested session exchange as no in-progress exchange was found for the provided message identifier. This is expected if no exchange was initiated with the provided message identifier through a `streamingContinue` request, or if the exchange for this identifier has already completed and cannot be canceled, or if the exchange has already been canceled. This error can also occur if the cancellation was requested immediately after requesting the exchange through a `streamingContinue` request, and the exchange has not started yet. Clients should handle these errors gracefully, and can reload the session content to get the latest conversation state.
        :raises CancelSessionPermissionDenied: Could not cancel the Session.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/aipAgents/agents/{agentRid}/sessions/{sessionRid}/cancel",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "agentRid": agent_rid,
                    "sessionRid": session_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "messageId": message_id,
                    "response": response,
                },
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "messageId": MessageId,
                        "response": Optional[AgentMarkdownResponse],
                    },
                ),
                response_type=CancelSessionResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "CancelSessionFailedMessageNotInProgress": aip_agents_errors.CancelSessionFailedMessageNotInProgress,
                    "CancelSessionPermissionDenied": aip_agents_errors.CancelSessionPermissionDenied,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def create(
        self,
        agent_rid: AgentRid,
        *,
        agent_version: Optional[AgentVersionString] = None,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[Session]:
        """
        Create a new conversation session between the calling user and an Agent.
        Use `blockingContinue` or `streamingContinue` to start adding exchanges to the session.

        :param agent_rid: agentRid
        :type agent_rid: AgentRid
        :param agent_version: The version of the Agent associated with the session. This can be set by clients on session creation. If not specified, defaults to use the latest published version of the Agent at session creation time.
        :type agent_version: Optional[AgentVersionString]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[Session]

        :raises CreateSessionPermissionDenied: Could not create the Session.
        :raises FunctionLocatorNotFound: The specified function locator is configured for use by the Agent but could not be found. The function type or version may not exist or the client token does not have access.
        :raises NoPublishedAgentVersion: Failed to retrieve the latest published version of the Agent because the Agent has no published versions. Try publishing the Agent in AIP Agent Studio to use the latest published version, or specify the version of the Agent to use.
        :raises ObjectTypeIdsNotFound: Some object types are configured for use by the Agent but could not be found. The object types either do not exist or the client token does not have access. Object types can be checked by listing available object types through the API, or searching in [Ontology Manager](/docs/foundry/ontology-manager/overview/).
        :raises ObjectTypeRidsNotFound: Some object types are configured for use by the Agent but could not be found. The object types either do not exist or the client token does not have access. Object types can be checked by listing available object types through the API, or searching in [Ontology Manager](/docs/foundry/ontology-manager/overview/).
        """

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/aipAgents/agents/{agentRid}/sessions",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "agentRid": agent_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "agentVersion": agent_version,
                },
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "agentVersion": Optional[AgentVersionString],
                    },
                ),
                response_type=Session,
                request_timeout=request_timeout,
                throwable_errors={
                    "CreateSessionPermissionDenied": aip_agents_errors.CreateSessionPermissionDenied,
                    "FunctionLocatorNotFound": aip_agents_errors.FunctionLocatorNotFound,
                    "NoPublishedAgentVersion": aip_agents_errors.NoPublishedAgentVersion,
                    "ObjectTypeIdsNotFound": aip_agents_errors.ObjectTypeIdsNotFound,
                    "ObjectTypeRidsNotFound": aip_agents_errors.ObjectTypeRidsNotFound,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def get(
        self,
        agent_rid: AgentRid,
        session_rid: SessionRid,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[Session]:
        """
        Get the details of a conversation session between the calling user and an Agent.
        :param agent_rid: agentRid
        :type agent_rid: AgentRid
        :param session_rid: sessionRid
        :type session_rid: SessionRid
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[Session]

        :raises SessionNotFound: The given Session could not be found.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/aipAgents/agents/{agentRid}/sessions/{sessionRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "agentRid": agent_rid,
                    "sessionRid": session_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=Session,
                request_timeout=request_timeout,
                throwable_errors={
                    "SessionNotFound": aip_agents_errors.SessionNotFound,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def list(
        self,
        agent_rid: AgentRid,
        *,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[ListSessionsResponse]:
        """
        List all conversation sessions between the calling user and an Agent that was created by this client.
        This does not list sessions for the user created by other clients.
        For example, any sessions created by the user in AIP Agent Studio will not be listed here.
        Sessions are returned in order of most recently updated first.

        :param agent_rid: agentRid
        :type agent_rid: AgentRid
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param page_token: pageToken
        :type page_token: Optional[PageToken]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[ListSessionsResponse]
        """

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/aipAgents/agents/{agentRid}/sessions",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
                    "preview": preview,
                },
                path_params={
                    "agentRid": agent_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ListSessionsResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def page(
        self,
        agent_rid: AgentRid,
        *,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[ListSessionsResponse]:
        """
        List all conversation sessions between the calling user and an Agent that was created by this client.
        This does not list sessions for the user created by other clients.
        For example, any sessions created by the user in AIP Agent Studio will not be listed here.
        Sessions are returned in order of most recently updated first.

        :param agent_rid: agentRid
        :type agent_rid: AgentRid
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param page_token: pageToken
        :type page_token: Optional[PageToken]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[ListSessionsResponse]
        """

        warnings.warn(
            "The client.aip_agents.Session.page(...) method has been deprecated. Please use client.aip_agents.Session.list(...) instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/aipAgents/agents/{agentRid}/sessions",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
                    "preview": preview,
                },
                path_params={
                    "agentRid": agent_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ListSessionsResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def rag_context(
        self,
        agent_rid: AgentRid,
        session_rid: SessionRid,
        *,
        parameter_inputs: Dict[ParameterId, Union[ParameterValue, ParameterValueDict]],
        user_input: Union[UserTextInput, UserTextInputDict],
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[AgentSessionRagContextResponse]:
        """
        Retrieve relevant [context](/docs/foundry/agent-studio/core-concepts/#retrieval-context) for a user message from the data sources configured for the session.
        This allows clients to pre-retrieve context for a user message before sending it to the Agent with the `contextsOverride` option when continuing a session, to allow any pre-processing of the context before sending it to the Agent.

        :param agent_rid: agentRid
        :type agent_rid: AgentRid
        :param session_rid: sessionRid
        :type session_rid: SessionRid
        :param parameter_inputs: Any values for [application variables](/docs/foundry/agent-studio/application-state/) to use for the context retrieval.
        :type parameter_inputs: Dict[ParameterId, Union[ParameterValue, ParameterValueDict]]
        :param user_input: The user message to retrieve relevant context for from the configured Agent data sources.
        :type user_input: Union[UserTextInput, UserTextInputDict]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[AgentSessionRagContextResponse]

        :raises FunctionLocatorNotFound: The specified function locator is configured for use by the Agent but could not be found. The function type or version may not exist or the client token does not have access.
        :raises GetRagContextForSessionPermissionDenied: Could not ragContext the Session.
        :raises ObjectTypeIdsNotFound: Some object types are configured for use by the Agent but could not be found. The object types either do not exist or the client token does not have access. Object types can be checked by listing available object types through the API, or searching in [Ontology Manager](/docs/foundry/ontology-manager/overview/).
        :raises ObjectTypeRidsNotFound: Some object types are configured for use by the Agent but could not be found. The object types either do not exist or the client token does not have access. Object types can be checked by listing available object types through the API, or searching in [Ontology Manager](/docs/foundry/ontology-manager/overview/).
        """

        return self._api_client.call_api(
            RequestInfo(
                method="PUT",
                resource_path="/v2/aipAgents/agents/{agentRid}/sessions/{sessionRid}/ragContext",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "agentRid": agent_rid,
                    "sessionRid": session_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "userInput": user_input,
                    "parameterInputs": parameter_inputs,
                },
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "userInput": Union[UserTextInput, UserTextInputDict],
                        "parameterInputs": Dict[
                            ParameterId, Union[ParameterValue, ParameterValueDict]
                        ],
                    },
                ),
                response_type=AgentSessionRagContextResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "FunctionLocatorNotFound": aip_agents_errors.FunctionLocatorNotFound,
                    "GetRagContextForSessionPermissionDenied": aip_agents_errors.GetRagContextForSessionPermissionDenied,
                    "ObjectTypeIdsNotFound": aip_agents_errors.ObjectTypeIdsNotFound,
                    "ObjectTypeRidsNotFound": aip_agents_errors.ObjectTypeRidsNotFound,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def streaming_continue(
        self,
        agent_rid: AgentRid,
        session_rid: SessionRid,
        *,
        parameter_inputs: Dict[ParameterId, Union[ParameterValue, ParameterValueDict]],
        user_input: Union[UserTextInput, UserTextInputDict],
        contexts_override: Optional[List[Union[InputContext, InputContextDict]]] = None,
        message_id: Optional[MessageId] = None,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[bytes]:
        """
        Continue a conversation session with an Agent, or add the first exchange to a session after creation.
        Adds a new exchange to the session with the provided inputs, and generates a response from the Agent.
        Returns a stream of the Agent response text (formatted using markdown) for clients to consume as the response is generated.
        On completion of the streamed response, clients can load the full details of the exchange that was added to the session by reloading the session content.
        Streamed exchanges also support cancellation; see `cancel` for details.
        Concurrent requests to continue the same session are not supported.
        Clients should wait to receive a response, or cancel the in-progress exchange, before sending the next message.

        :param agent_rid: agentRid
        :type agent_rid: AgentRid
        :param session_rid: sessionRid
        :type session_rid: SessionRid
        :param parameter_inputs: Any supplied values for [application variables](/docs/foundry/agent-studio/application-state/) to pass to the Agent for the exchange.
        :type parameter_inputs: Dict[ParameterId, Union[ParameterValue, ParameterValueDict]]
        :param user_input: The user message for the Agent to respond to.
        :type user_input: Union[UserTextInput, UserTextInputDict]
        :param contexts_override: If set, automatic [context](/docs/foundry/agent-studio/retrieval-context/) retrieval is skipped and the list of specified context is provided to the Agent instead. If omitted, relevant context for the user message is automatically retrieved and included in the prompt, based on data sources configured on the Agent for the session.
        :type contexts_override: Optional[List[Union[InputContext, InputContextDict]]]
        :param message_id: A client-generated Universally Unique Identifier (UUID) to identify the message, which the client can use to cancel the exchange before the streaming response is complete.
        :type message_id: Optional[MessageId]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[bytes]

        :raises FunctionLocatorNotFound: The specified function locator is configured for use by the Agent but could not be found. The function type or version may not exist or the client token does not have access.
        :raises InvalidParameter: The provided application variable is not valid for the Agent for this session. Check the available application variables for the Agent under the `parameters` property, and version through the API with `getAgent`, or in AIP Agent Studio. The Agent version used for the session can be checked through the API with `getSession`.
        :raises InvalidParameterType: The provided value does not match the expected type for the application variable configured on the Agent for this session. Check the available application variables for the Agent under the `parameters` property, and version through the API with `getAgent`, or in AIP Agent Studio. The Agent version used for the session can be checked through the API with `getSession`.
        :raises ObjectTypeIdsNotFound: Some object types are configured for use by the Agent but could not be found. The object types either do not exist or the client token does not have access. Object types can be checked by listing available object types through the API, or searching in [Ontology Manager](/docs/foundry/ontology-manager/overview/).
        :raises ObjectTypeRidsNotFound: Some object types are configured for use by the Agent but could not be found. The object types either do not exist or the client token does not have access. Object types can be checked by listing available object types through the API, or searching in [Ontology Manager](/docs/foundry/ontology-manager/overview/).
        :raises StreamingContinueSessionPermissionDenied: Could not streamingContinue the Session.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/aipAgents/agents/{agentRid}/sessions/{sessionRid}/streamingContinue",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "agentRid": agent_rid,
                    "sessionRid": session_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/octet-stream",
                },
                body={
                    "userInput": user_input,
                    "parameterInputs": parameter_inputs,
                    "contextsOverride": contexts_override,
                    "messageId": message_id,
                },
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "userInput": Union[UserTextInput, UserTextInputDict],
                        "parameterInputs": Dict[
                            ParameterId, Union[ParameterValue, ParameterValueDict]
                        ],
                        "contextsOverride": Optional[List[Union[InputContext, InputContextDict]]],
                        "messageId": Optional[MessageId],
                    },
                ),
                response_type=bytes,
                request_timeout=request_timeout,
                throwable_errors={
                    "FunctionLocatorNotFound": aip_agents_errors.FunctionLocatorNotFound,
                    "InvalidParameter": aip_agents_errors.InvalidParameter,
                    "InvalidParameterType": aip_agents_errors.InvalidParameterType,
                    "ObjectTypeIdsNotFound": aip_agents_errors.ObjectTypeIdsNotFound,
                    "ObjectTypeRidsNotFound": aip_agents_errors.ObjectTypeRidsNotFound,
                    "StreamingContinueSessionPermissionDenied": aip_agents_errors.StreamingContinueSessionPermissionDenied,
                },
            ),
        )


class _SessionClientStreaming:
    """
    The API client for the Session Resource.

    :param auth: Your auth configuration.
    :param hostname: Your Foundry hostname (for example, "myfoundry.palantirfoundry.com"). This can also include your API gateway service URI.
    :param config: Optionally specify the configuration for the HTTP session.
    """

    def __init__(
        self,
        auth: Auth,
        hostname: str,
        config: Optional[Config] = None,
    ):
        self._auth = auth
        self._hostname = hostname
        self._config = config
        self._api_client = ApiClient(auth=auth, hostname=hostname, config=config)

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def blocking_continue(
        self,
        agent_rid: AgentRid,
        session_rid: SessionRid,
        *,
        parameter_inputs: Dict[ParameterId, Union[ParameterValue, ParameterValueDict]],
        user_input: Union[UserTextInput, UserTextInputDict],
        contexts_override: Optional[List[Union[InputContext, InputContextDict]]] = None,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[SessionExchangeResult]:
        """
        Continue a conversation session with an Agent, or add the first exchange to a session after creation.
        Adds a new exchange to the session with the provided inputs, and generates a response from the Agent.
        Blocks on returning the result of the added exchange until the response is fully generated.
        Streamed responses are also supported; see `streamingContinue` for details.
        Concurrent requests to continue the same session are not supported.
        Clients should wait to receive a response before sending the next message.

        :param agent_rid: agentRid
        :type agent_rid: AgentRid
        :param session_rid: sessionRid
        :type session_rid: SessionRid
        :param parameter_inputs: Any supplied values for [application variables](/docs/foundry/agent-studio/application-state/) to pass to the Agent for the exchange.
        :type parameter_inputs: Dict[ParameterId, Union[ParameterValue, ParameterValueDict]]
        :param user_input: The user message for the Agent to respond to.
        :type user_input: Union[UserTextInput, UserTextInputDict]
        :param contexts_override: If set, automatic [context retrieval](/docs/foundry/agent-studio/retrieval-context/) is skipped and the list of specified context is provided to the Agent instead. If omitted, relevant context for the user message is automatically retrieved and included in the prompt, based on data sources configured on the Agent for the session.
        :type contexts_override: Optional[List[Union[InputContext, InputContextDict]]]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[SessionExchangeResult]

        :raises AgentIterationsExceededLimit: The Agent was unable to produce an answer in the set number of maximum iterations. This can happen if the Agent gets confused or stuck in a loop, or if the query is too complex. Try a different query or review the Agent configuration in AIP Agent Studio.
        :raises BlockingContinueSessionPermissionDenied: Could not blockingContinue the Session.
        :raises ContextSizeExceededLimit: Failed to generate a response for a session because the context size of the LLM has been exceeded. Clients should either retry with a shorter message or create a new session and try re-sending the message.
        :raises FunctionLocatorNotFound: The specified function locator is configured for use by the Agent but could not be found. The function type or version may not exist or the client token does not have access.
        :raises InvalidParameter: The provided application variable is not valid for the Agent for this session. Check the available application variables for the Agent under the `parameters` property, and version through the API with `getAgent`, or in AIP Agent Studio. The Agent version used for the session can be checked through the API with `getSession`.
        :raises InvalidParameterType: The provided value does not match the expected type for the application variable configured on the Agent for this session. Check the available application variables for the Agent under the `parameters` property, and version through the API with `getAgent`, or in AIP Agent Studio. The Agent version used for the session can be checked through the API with `getSession`.
        :raises ObjectTypeIdsNotFound: Some object types are configured for use by the Agent but could not be found. The object types either do not exist or the client token does not have access. Object types can be checked by listing available object types through the API, or searching in [Ontology Manager](/docs/foundry/ontology-manager/overview/).
        :raises ObjectTypeRidsNotFound: Some object types are configured for use by the Agent but could not be found. The object types either do not exist or the client token does not have access. Object types can be checked by listing available object types through the API, or searching in [Ontology Manager](/docs/foundry/ontology-manager/overview/).
        :raises RateLimitExceeded: Failed to generate a response as the model rate limits were exceeded. Clients should wait and retry.
        :raises SessionExecutionFailed: Failed to generate a response for a session due to an unexpected error.
        """

        return self._api_client.stream_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/aipAgents/agents/{agentRid}/sessions/{sessionRid}/blockingContinue",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "agentRid": agent_rid,
                    "sessionRid": session_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "userInput": user_input,
                    "parameterInputs": parameter_inputs,
                    "contextsOverride": contexts_override,
                },
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "userInput": Union[UserTextInput, UserTextInputDict],
                        "parameterInputs": Dict[
                            ParameterId, Union[ParameterValue, ParameterValueDict]
                        ],
                        "contextsOverride": Optional[List[Union[InputContext, InputContextDict]]],
                    },
                ),
                response_type=SessionExchangeResult,
                request_timeout=request_timeout,
                throwable_errors={
                    "AgentIterationsExceededLimit": aip_agents_errors.AgentIterationsExceededLimit,
                    "BlockingContinueSessionPermissionDenied": aip_agents_errors.BlockingContinueSessionPermissionDenied,
                    "ContextSizeExceededLimit": aip_agents_errors.ContextSizeExceededLimit,
                    "FunctionLocatorNotFound": aip_agents_errors.FunctionLocatorNotFound,
                    "InvalidParameter": aip_agents_errors.InvalidParameter,
                    "InvalidParameterType": aip_agents_errors.InvalidParameterType,
                    "ObjectTypeIdsNotFound": aip_agents_errors.ObjectTypeIdsNotFound,
                    "ObjectTypeRidsNotFound": aip_agents_errors.ObjectTypeRidsNotFound,
                    "RateLimitExceeded": aip_agents_errors.RateLimitExceeded,
                    "SessionExecutionFailed": aip_agents_errors.SessionExecutionFailed,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def cancel(
        self,
        agent_rid: AgentRid,
        session_rid: SessionRid,
        *,
        message_id: MessageId,
        preview: Optional[PreviewMode] = None,
        response: Optional[AgentMarkdownResponse] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[CancelSessionResponse]:
        """
        Cancel an in-progress streamed exchange with an Agent which was initiated with `streamingContinue`.
        Canceling an exchange allows clients to prevent the exchange from being added to the session, or to provide a response to replace the Agent-generated response.
        Note that canceling an exchange does not terminate the stream returned by `streamingContinue`; clients should close the stream on triggering the cancellation request to stop reading from the stream.

        :param agent_rid: agentRid
        :type agent_rid: AgentRid
        :param session_rid: sessionRid
        :type session_rid: SessionRid
        :param message_id: The identifier for the in-progress exchange to cancel. This should match the `messageId` which was provided when initiating the exchange with `streamingContinue`.
        :type message_id: MessageId
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param response: When specified, the exchange is added to the session with the client-provided response as the result. When omitted, the exchange is not added to the session.
        :type response: Optional[AgentMarkdownResponse]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[CancelSessionResponse]

        :raises CancelSessionFailedMessageNotInProgress: Unable to cancel the requested session exchange as no in-progress exchange was found for the provided message identifier. This is expected if no exchange was initiated with the provided message identifier through a `streamingContinue` request, or if the exchange for this identifier has already completed and cannot be canceled, or if the exchange has already been canceled. This error can also occur if the cancellation was requested immediately after requesting the exchange through a `streamingContinue` request, and the exchange has not started yet. Clients should handle these errors gracefully, and can reload the session content to get the latest conversation state.
        :raises CancelSessionPermissionDenied: Could not cancel the Session.
        """

        return self._api_client.stream_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/aipAgents/agents/{agentRid}/sessions/{sessionRid}/cancel",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "agentRid": agent_rid,
                    "sessionRid": session_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "messageId": message_id,
                    "response": response,
                },
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "messageId": MessageId,
                        "response": Optional[AgentMarkdownResponse],
                    },
                ),
                response_type=CancelSessionResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "CancelSessionFailedMessageNotInProgress": aip_agents_errors.CancelSessionFailedMessageNotInProgress,
                    "CancelSessionPermissionDenied": aip_agents_errors.CancelSessionPermissionDenied,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def create(
        self,
        agent_rid: AgentRid,
        *,
        agent_version: Optional[AgentVersionString] = None,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[Session]:
        """
        Create a new conversation session between the calling user and an Agent.
        Use `blockingContinue` or `streamingContinue` to start adding exchanges to the session.

        :param agent_rid: agentRid
        :type agent_rid: AgentRid
        :param agent_version: The version of the Agent associated with the session. This can be set by clients on session creation. If not specified, defaults to use the latest published version of the Agent at session creation time.
        :type agent_version: Optional[AgentVersionString]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[Session]

        :raises CreateSessionPermissionDenied: Could not create the Session.
        :raises FunctionLocatorNotFound: The specified function locator is configured for use by the Agent but could not be found. The function type or version may not exist or the client token does not have access.
        :raises NoPublishedAgentVersion: Failed to retrieve the latest published version of the Agent because the Agent has no published versions. Try publishing the Agent in AIP Agent Studio to use the latest published version, or specify the version of the Agent to use.
        :raises ObjectTypeIdsNotFound: Some object types are configured for use by the Agent but could not be found. The object types either do not exist or the client token does not have access. Object types can be checked by listing available object types through the API, or searching in [Ontology Manager](/docs/foundry/ontology-manager/overview/).
        :raises ObjectTypeRidsNotFound: Some object types are configured for use by the Agent but could not be found. The object types either do not exist or the client token does not have access. Object types can be checked by listing available object types through the API, or searching in [Ontology Manager](/docs/foundry/ontology-manager/overview/).
        """

        return self._api_client.stream_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/aipAgents/agents/{agentRid}/sessions",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "agentRid": agent_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "agentVersion": agent_version,
                },
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "agentVersion": Optional[AgentVersionString],
                    },
                ),
                response_type=Session,
                request_timeout=request_timeout,
                throwable_errors={
                    "CreateSessionPermissionDenied": aip_agents_errors.CreateSessionPermissionDenied,
                    "FunctionLocatorNotFound": aip_agents_errors.FunctionLocatorNotFound,
                    "NoPublishedAgentVersion": aip_agents_errors.NoPublishedAgentVersion,
                    "ObjectTypeIdsNotFound": aip_agents_errors.ObjectTypeIdsNotFound,
                    "ObjectTypeRidsNotFound": aip_agents_errors.ObjectTypeRidsNotFound,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def get(
        self,
        agent_rid: AgentRid,
        session_rid: SessionRid,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[Session]:
        """
        Get the details of a conversation session between the calling user and an Agent.
        :param agent_rid: agentRid
        :type agent_rid: AgentRid
        :param session_rid: sessionRid
        :type session_rid: SessionRid
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[Session]

        :raises SessionNotFound: The given Session could not be found.
        """

        return self._api_client.stream_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/aipAgents/agents/{agentRid}/sessions/{sessionRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "agentRid": agent_rid,
                    "sessionRid": session_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=Session,
                request_timeout=request_timeout,
                throwable_errors={
                    "SessionNotFound": aip_agents_errors.SessionNotFound,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def list(
        self,
        agent_rid: AgentRid,
        *,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[ListSessionsResponse]:
        """
        List all conversation sessions between the calling user and an Agent that was created by this client.
        This does not list sessions for the user created by other clients.
        For example, any sessions created by the user in AIP Agent Studio will not be listed here.
        Sessions are returned in order of most recently updated first.

        :param agent_rid: agentRid
        :type agent_rid: AgentRid
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param page_token: pageToken
        :type page_token: Optional[PageToken]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[ListSessionsResponse]
        """

        return self._api_client.stream_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/aipAgents/agents/{agentRid}/sessions",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
                    "preview": preview,
                },
                path_params={
                    "agentRid": agent_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ListSessionsResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def page(
        self,
        agent_rid: AgentRid,
        *,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[ListSessionsResponse]:
        """
        List all conversation sessions between the calling user and an Agent that was created by this client.
        This does not list sessions for the user created by other clients.
        For example, any sessions created by the user in AIP Agent Studio will not be listed here.
        Sessions are returned in order of most recently updated first.

        :param agent_rid: agentRid
        :type agent_rid: AgentRid
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param page_token: pageToken
        :type page_token: Optional[PageToken]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[ListSessionsResponse]
        """

        warnings.warn(
            "The client.aip_agents.Session.page(...) method has been deprecated. Please use client.aip_agents.Session.list(...) instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        return self._api_client.stream_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/aipAgents/agents/{agentRid}/sessions",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
                    "preview": preview,
                },
                path_params={
                    "agentRid": agent_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ListSessionsResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def rag_context(
        self,
        agent_rid: AgentRid,
        session_rid: SessionRid,
        *,
        parameter_inputs: Dict[ParameterId, Union[ParameterValue, ParameterValueDict]],
        user_input: Union[UserTextInput, UserTextInputDict],
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[AgentSessionRagContextResponse]:
        """
        Retrieve relevant [context](/docs/foundry/agent-studio/core-concepts/#retrieval-context) for a user message from the data sources configured for the session.
        This allows clients to pre-retrieve context for a user message before sending it to the Agent with the `contextsOverride` option when continuing a session, to allow any pre-processing of the context before sending it to the Agent.

        :param agent_rid: agentRid
        :type agent_rid: AgentRid
        :param session_rid: sessionRid
        :type session_rid: SessionRid
        :param parameter_inputs: Any values for [application variables](/docs/foundry/agent-studio/application-state/) to use for the context retrieval.
        :type parameter_inputs: Dict[ParameterId, Union[ParameterValue, ParameterValueDict]]
        :param user_input: The user message to retrieve relevant context for from the configured Agent data sources.
        :type user_input: Union[UserTextInput, UserTextInputDict]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[AgentSessionRagContextResponse]

        :raises FunctionLocatorNotFound: The specified function locator is configured for use by the Agent but could not be found. The function type or version may not exist or the client token does not have access.
        :raises GetRagContextForSessionPermissionDenied: Could not ragContext the Session.
        :raises ObjectTypeIdsNotFound: Some object types are configured for use by the Agent but could not be found. The object types either do not exist or the client token does not have access. Object types can be checked by listing available object types through the API, or searching in [Ontology Manager](/docs/foundry/ontology-manager/overview/).
        :raises ObjectTypeRidsNotFound: Some object types are configured for use by the Agent but could not be found. The object types either do not exist or the client token does not have access. Object types can be checked by listing available object types through the API, or searching in [Ontology Manager](/docs/foundry/ontology-manager/overview/).
        """

        return self._api_client.stream_api(
            RequestInfo(
                method="PUT",
                resource_path="/v2/aipAgents/agents/{agentRid}/sessions/{sessionRid}/ragContext",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "agentRid": agent_rid,
                    "sessionRid": session_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "userInput": user_input,
                    "parameterInputs": parameter_inputs,
                },
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "userInput": Union[UserTextInput, UserTextInputDict],
                        "parameterInputs": Dict[
                            ParameterId, Union[ParameterValue, ParameterValueDict]
                        ],
                    },
                ),
                response_type=AgentSessionRagContextResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "FunctionLocatorNotFound": aip_agents_errors.FunctionLocatorNotFound,
                    "GetRagContextForSessionPermissionDenied": aip_agents_errors.GetRagContextForSessionPermissionDenied,
                    "ObjectTypeIdsNotFound": aip_agents_errors.ObjectTypeIdsNotFound,
                    "ObjectTypeRidsNotFound": aip_agents_errors.ObjectTypeRidsNotFound,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def streaming_continue(
        self,
        agent_rid: AgentRid,
        session_rid: SessionRid,
        *,
        parameter_inputs: Dict[ParameterId, Union[ParameterValue, ParameterValueDict]],
        user_input: Union[UserTextInput, UserTextInputDict],
        contexts_override: Optional[List[Union[InputContext, InputContextDict]]] = None,
        message_id: Optional[MessageId] = None,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[bytes]:
        """
        Continue a conversation session with an Agent, or add the first exchange to a session after creation.
        Adds a new exchange to the session with the provided inputs, and generates a response from the Agent.
        Returns a stream of the Agent response text (formatted using markdown) for clients to consume as the response is generated.
        On completion of the streamed response, clients can load the full details of the exchange that was added to the session by reloading the session content.
        Streamed exchanges also support cancellation; see `cancel` for details.
        Concurrent requests to continue the same session are not supported.
        Clients should wait to receive a response, or cancel the in-progress exchange, before sending the next message.

        :param agent_rid: agentRid
        :type agent_rid: AgentRid
        :param session_rid: sessionRid
        :type session_rid: SessionRid
        :param parameter_inputs: Any supplied values for [application variables](/docs/foundry/agent-studio/application-state/) to pass to the Agent for the exchange.
        :type parameter_inputs: Dict[ParameterId, Union[ParameterValue, ParameterValueDict]]
        :param user_input: The user message for the Agent to respond to.
        :type user_input: Union[UserTextInput, UserTextInputDict]
        :param contexts_override: If set, automatic [context](/docs/foundry/agent-studio/retrieval-context/) retrieval is skipped and the list of specified context is provided to the Agent instead. If omitted, relevant context for the user message is automatically retrieved and included in the prompt, based on data sources configured on the Agent for the session.
        :type contexts_override: Optional[List[Union[InputContext, InputContextDict]]]
        :param message_id: A client-generated Universally Unique Identifier (UUID) to identify the message, which the client can use to cancel the exchange before the streaming response is complete.
        :type message_id: Optional[MessageId]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[bytes]

        :raises FunctionLocatorNotFound: The specified function locator is configured for use by the Agent but could not be found. The function type or version may not exist or the client token does not have access.
        :raises InvalidParameter: The provided application variable is not valid for the Agent for this session. Check the available application variables for the Agent under the `parameters` property, and version through the API with `getAgent`, or in AIP Agent Studio. The Agent version used for the session can be checked through the API with `getSession`.
        :raises InvalidParameterType: The provided value does not match the expected type for the application variable configured on the Agent for this session. Check the available application variables for the Agent under the `parameters` property, and version through the API with `getAgent`, or in AIP Agent Studio. The Agent version used for the session can be checked through the API with `getSession`.
        :raises ObjectTypeIdsNotFound: Some object types are configured for use by the Agent but could not be found. The object types either do not exist or the client token does not have access. Object types can be checked by listing available object types through the API, or searching in [Ontology Manager](/docs/foundry/ontology-manager/overview/).
        :raises ObjectTypeRidsNotFound: Some object types are configured for use by the Agent but could not be found. The object types either do not exist or the client token does not have access. Object types can be checked by listing available object types through the API, or searching in [Ontology Manager](/docs/foundry/ontology-manager/overview/).
        :raises StreamingContinueSessionPermissionDenied: Could not streamingContinue the Session.
        """

        return self._api_client.stream_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/aipAgents/agents/{agentRid}/sessions/{sessionRid}/streamingContinue",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "agentRid": agent_rid,
                    "sessionRid": session_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/octet-stream",
                },
                body={
                    "userInput": user_input,
                    "parameterInputs": parameter_inputs,
                    "contextsOverride": contexts_override,
                    "messageId": message_id,
                },
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "userInput": Union[UserTextInput, UserTextInputDict],
                        "parameterInputs": Dict[
                            ParameterId, Union[ParameterValue, ParameterValueDict]
                        ],
                        "contextsOverride": Optional[List[Union[InputContext, InputContextDict]]],
                        "messageId": Optional[MessageId],
                    },
                ),
                response_type=bytes,
                request_timeout=request_timeout,
                throwable_errors={
                    "FunctionLocatorNotFound": aip_agents_errors.FunctionLocatorNotFound,
                    "InvalidParameter": aip_agents_errors.InvalidParameter,
                    "InvalidParameterType": aip_agents_errors.InvalidParameterType,
                    "ObjectTypeIdsNotFound": aip_agents_errors.ObjectTypeIdsNotFound,
                    "ObjectTypeRidsNotFound": aip_agents_errors.ObjectTypeRidsNotFound,
                    "StreamingContinueSessionPermissionDenied": aip_agents_errors.StreamingContinueSessionPermissionDenied,
                },
            ),
        )
