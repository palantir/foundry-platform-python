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

from typing import Any
from typing import Dict
from typing import List
from typing import Optional

import pydantic
from typing_extensions import Annotated
from typing_extensions import TypedDict

from foundry._core import ApiClient
from foundry._core import Auth
from foundry._core import RequestInfo
from foundry._core import ResourceIterator
from foundry._errors import handle_unexpected
from foundry.v2.aip_agents.content import ContentClient
from foundry.v2.aip_agents.models._agent_markdown_response import AgentMarkdownResponse
from foundry.v2.aip_agents.models._agent_rid import AgentRid
from foundry.v2.aip_agents.models._agent_session_rag_context_response import (
    AgentSessionRagContextResponse,
)  # NOQA
from foundry.v2.aip_agents.models._agent_version_string import AgentVersionString
from foundry.v2.aip_agents.models._cancel_session_response import CancelSessionResponse
from foundry.v2.aip_agents.models._input_context_dict import InputContextDict
from foundry.v2.aip_agents.models._list_sessions_response import ListSessionsResponse
from foundry.v2.aip_agents.models._message_id import MessageId
from foundry.v2.aip_agents.models._parameter_id import ParameterId
from foundry.v2.aip_agents.models._parameter_value_dict import ParameterValueDict
from foundry.v2.aip_agents.models._session import Session
from foundry.v2.aip_agents.models._session_exchange_result import SessionExchangeResult
from foundry.v2.aip_agents.models._session_rid import SessionRid
from foundry.v2.aip_agents.models._user_text_input_dict import UserTextInputDict
from foundry.v2.core.models._page_size import PageSize
from foundry.v2.core.models._page_token import PageToken
from foundry.v2.core.models._preview_mode import PreviewMode


class SessionClient:
    def __init__(self, auth: Auth, hostname: str) -> None:
        self._api_client = ApiClient(auth=auth, hostname=hostname)

        self.Content = ContentClient(auth=auth, hostname=hostname)

    @pydantic.validate_call
    @handle_unexpected
    def blocking_continue(
        self,
        agent_rid: AgentRid,
        session_rid: SessionRid,
        *,
        parameter_inputs: Dict[ParameterId, ParameterValueDict],
        user_input: UserTextInputDict,
        contexts_override: Optional[List[InputContextDict]] = None,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> SessionExchangeResult:
        """
        Continue a conversation session with an Agent, or add the first exchange to a session after creation.
        Adds a new exchange to the session with the provided inputs, and generates a response from the Agent.
        Blocks on returning the result of the added exchange until the response is fully generated.
        Streamed responses are also supported; see `streamingContinue` for details.
        Concurrent requests to continue the same session are not supported. Clients should wait
        to receive a response before sending the next message.

        :param agent_rid: agentRid
        :type agent_rid: AgentRid
        :param session_rid: sessionRid
        :type session_rid: SessionRid
        :param parameter_inputs: Any supplied [parameter values](/docs/foundry/agent-studio/parameters/) to pass to the Agent for the exchange.
        :type parameter_inputs: Dict[ParameterId, ParameterValueDict]
        :param user_input: The user message for the Agent to respond to.
        :type user_input: UserTextInputDict
        :param contexts_override: If set, automatic [context retrieval](/docs/foundry/agent-studio/retrieval-context/)  is skipped and the list of specified context is provided to the Agent instead. If omitted, relevant context  for the user message is automatically retrieved and included in the prompt, based on data sources configured  on the Agent for the session.
        :type contexts_override: Optional[List[InputContextDict]]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: SessionExchangeResult
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
                        "userInput": UserTextInputDict,
                        "parameterInputs": Dict[ParameterId, ParameterValueDict],
                        "contextsOverride": Optional[List[InputContextDict]],
                    },
                ),
                response_type=SessionExchangeResult,
                request_timeout=request_timeout,
            ),
        )

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
        Canceling an exchange allows clients to prevent the exchange from being added to the session,
        or to provide a response to replace the Agent-generated response.
        Note that canceling an exchange does not terminate the stream returned by `streamingContinue`;
        clients should close the stream on triggering the cancellation request to stop reading from the stream.

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
            ),
        )

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
        :param agent_version: The version of the Agent that the session is with. This can be set by clients on session creation. If not specified, defaults to use the latest published version of the Agent at session creation time.
        :type agent_version: Optional[AgentVersionString]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: Session
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
            ),
        )

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
        Get details of a conversation session between the calling user and an Agent.
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
            ),
        )

    @pydantic.validate_call
    @handle_unexpected
    def list(
        self,
        agent_rid: AgentRid,
        *,
        page_size: Optional[PageSize] = None,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ResourceIterator[Session]:
        """
        List all conversation sessions between the calling user and an Agent that were created by this client.
        This does not list sessions for the user created by other clients. For example, any sessions created by
        the user in AIP Agent Studio will not be listed here.
        Sessions are returned in order of most recently updated first.

        :param agent_rid: agentRid
        :type agent_rid: AgentRid
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
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
            ),
        )

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
        List all conversation sessions between the calling user and an Agent that were created by this client.
        This does not list sessions for the user created by other clients. For example, any sessions created by
        the user in AIP Agent Studio will not be listed here.
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
            ),
        )

    @pydantic.validate_call
    @handle_unexpected
    def rag_context(
        self,
        agent_rid: AgentRid,
        session_rid: SessionRid,
        *,
        parameter_inputs: Dict[ParameterId, ParameterValueDict],
        user_input: UserTextInputDict,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> AgentSessionRagContextResponse:
        """
        Retrieve relevant [context](/docs/foundry/agent-studio/core-concepts/#retrieval-context) for a user message
        from the data sources configured for the session. This allows clients to pre-retrieve context for a user
        message before sending it to the Agent with the `contextsOverride` option when continuing a session, to
        allow any pre-processing of the context before sending it to the Agent.

        :param agent_rid: agentRid
        :type agent_rid: AgentRid
        :param session_rid: sessionRid
        :type session_rid: SessionRid
        :param parameter_inputs: Any parameter values to use for the context retrieval.
        :type parameter_inputs: Dict[ParameterId, ParameterValueDict]
        :param user_input: The user message to retrieve relevant context for from the configured Agent data sources.
        :type user_input: UserTextInputDict
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: AgentSessionRagContextResponse
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
                        "userInput": UserTextInputDict,
                        "parameterInputs": Dict[ParameterId, ParameterValueDict],
                    },
                ),
                response_type=AgentSessionRagContextResponse,
                request_timeout=request_timeout,
            ),
        )

    @pydantic.validate_call
    @handle_unexpected
    def streaming_continue(
        self,
        agent_rid: AgentRid,
        session_rid: SessionRid,
        *,
        parameter_inputs: Dict[ParameterId, ParameterValueDict],
        user_input: UserTextInputDict,
        contexts_override: Optional[List[InputContextDict]] = None,
        message_id: Optional[MessageId] = None,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> bytes:
        """
        Continue a conversation session with an Agent, or add the first exchange to a session after creation.
        Adds a new exchange to the session with the provided inputs, and generates a response from the Agent.
        Returns a stream of the Agent response text (formatted using markdown) for clients to consume as
        the response is generated.
        On completion of the streamed response, clients can load the full details of the exchange that was
        added to the session by reloading the session content.
        Streamed exchanges also support cancellation; see `cancel` for details.
        Concurrent requests to continue the same session are not supported. Clients should wait to receive a
        response, or cancel the in-progress exchange, before sending the next message.

        :param agent_rid: agentRid
        :type agent_rid: AgentRid
        :param session_rid: sessionRid
        :type session_rid: SessionRid
        :param parameter_inputs: Any supplied [parameter](/docs/foundry/agent-studio/parameters/) values to pass to the Agent for the exchange.
        :type parameter_inputs: Dict[ParameterId, ParameterValueDict]
        :param user_input: The user message for the Agent to respond to.
        :type user_input: UserTextInputDict
        :param contexts_override: If set, automatic [context](/docs/foundry/agent-studio/retrieval-context/) retrieval is skipped and the list of specified context is provided to the Agent instead. If omitted, relevant context for the user message is automatically retrieved and included in the prompt, based on data sources configured on the Agent for the session.
        :type contexts_override: Optional[List[InputContextDict]]
        :param message_id: A client-generated Universally Unique Identifier (UUID) to identify the message, which the client can use to cancel the exchange before the streaming response is complete.
        :type message_id: Optional[MessageId]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: bytes
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
                        "userInput": UserTextInputDict,
                        "parameterInputs": Dict[ParameterId, ParameterValueDict],
                        "contextsOverride": Optional[List[InputContextDict]],
                        "messageId": Optional[MessageId],
                    },
                ),
                response_type=bytes,
                request_timeout=request_timeout,
            ),
        )
