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
from functools import cached_property

import pydantic
import typing_extensions

from foundry_sdk import _core as core
from foundry_sdk import _errors as errors
from foundry_sdk.v2.aip_agents import errors as aip_agents_errors
from foundry_sdk.v2.aip_agents import models as aip_agents_models
from foundry_sdk.v2.core import models as core_models


class SessionClient:
    """
    The API client for the Session Resource.

    :param auth: Your auth configuration.
    :param hostname: Your Foundry hostname (for example, "myfoundry.palantirfoundry.com"). This can also include your API gateway service URI.
    :param config: Optionally specify the configuration for the HTTP session.
    """

    def __init__(
        self,
        auth: core.Auth,
        hostname: str,
        config: typing.Optional[core.Config] = None,
    ):
        self._auth = auth
        self._hostname = hostname
        self._config = config
        self._api_client = core.ApiClient(auth=auth, hostname=hostname, config=config)

        self.with_streaming_response = _SessionClientStreaming(self)
        self.with_raw_response = _SessionClientRaw(self)

    @cached_property
    def Content(self):
        from foundry_sdk.v2.aip_agents.content import ContentClient

        return ContentClient(
            auth=self._auth,
            hostname=self._hostname,
            config=self._config,
        )

    @cached_property
    def SessionTrace(self):
        from foundry_sdk.v2.aip_agents.session_trace import SessionTraceClient

        return SessionTraceClient(
            auth=self._auth,
            hostname=self._hostname,
            config=self._config,
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def blocking_continue(
        self,
        agent_rid: aip_agents_models.AgentRid,
        session_rid: aip_agents_models.SessionRid,
        *,
        parameter_inputs: typing.Dict[
            aip_agents_models.ParameterId, aip_agents_models.ParameterValue
        ],
        user_input: aip_agents_models.UserTextInput,
        contexts_override: typing.Optional[typing.List[aip_agents_models.InputContext]] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        session_trace_id: typing.Optional[aip_agents_models.SessionTraceId] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> aip_agents_models.SessionExchangeResult:
        """
        Continue a conversation session with an Agent, or add the first exchange to a session after creation.
        Adds a new exchange to the session with the provided inputs, and generates a response from the Agent.
        Blocks on returning the result of the added exchange until the response is fully generated.
        Streamed responses are also supported; see `streamingContinue` for details.
        Concurrent requests to continue the same session are not supported.
        Clients should wait to receive a response before sending the next message.

        :param agent_rid: An RID identifying an AIP Agent created in [AIP Agent Studio](https://palantir.com/docs/foundry/agent-studio/overview/).
        :type agent_rid: AgentRid
        :param session_rid: The Resource Identifier (RID) of the conversation session.
        :type session_rid: SessionRid
        :param parameter_inputs: Any supplied values for [application variables](https://palantir.com/docs/foundry/agent-studio/application-state/) to pass to the Agent for the exchange.
        :type parameter_inputs: Dict[ParameterId, ParameterValue]
        :param user_input: The user message for the Agent to respond to.
        :type user_input: UserTextInput
        :param contexts_override: If set, automatic [context retrieval](https://palantir.com/docs/foundry/agent-studio/retrieval-context/) is skipped and the list of specified context is provided to the Agent instead. If omitted, relevant context for the user message is automatically retrieved and included in the prompt, based on data sources configured on the Agent for the session.
        :type contexts_override: Optional[List[InputContext]]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param session_trace_id: The unique identifier to use for this continue session trace. By generating and passing this ID to the `blockingContinue` endpoint, clients can use this trace ID to separately load details of the trace used to generate a result, while the result is in progress. If omitted, it will be generated automatically. Clients can check the generated ID by inspecting the `sessionTraceId` in the `SessionExchangeResult`.
        :type session_trace_id: Optional[SessionTraceId]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: aip_agents_models.SessionExchangeResult

        :raises AgentIterationsExceededLimit: The Agent was unable to produce an answer in the set number of maximum iterations. This can happen if the Agent gets confused or stuck in a loop, or if the query is too complex. Try a different query or review the Agent configuration in AIP Agent Studio.
        :raises AgentNotFound: The given Agent could not be found.
        :raises BlockingContinueSessionPermissionDenied: Could not blockingContinue the Session.
        :raises ContextSizeExceededLimit: Failed to generate a response for a session because the context size of the LLM has been exceeded. Clients should either retry with a shorter message or create a new session and try re-sending the message.
        :raises FunctionLocatorNotFound: The specified function locator is configured for use by the Agent but could not be found. The function type or version may not exist or the client token does not have access.
        :raises InvalidParameter: The provided application variable is not valid for the Agent for this session. Check the available application variables for the Agent under the `parameters` property, and version through the API with `getAgent`, or in AIP Agent Studio. The Agent version used for the session can be checked through the API with `getSession`.
        :raises InvalidParameterType: The provided value does not match the expected type for the application variable configured on the Agent for this session. Check the available application variables for the Agent under the `parameters` property, and version through the API with `getAgent`, or in AIP Agent Studio. The Agent version used for the session can be checked through the API with `getSession`.
        :raises ObjectTypeIdsNotFound: Some object types are configured for use by the Agent but could not be found. The object types either do not exist or the client token does not have access. Object types can be checked by listing available object types through the API, or searching in [Ontology Manager](https://palantir.com/docs/foundry/ontology-manager/overview/).
        :raises ObjectTypeRidsNotFound: Some object types are configured for use by the Agent but could not be found. The object types either do not exist or the client token does not have access. Object types can be checked by listing available object types through the API, or searching in [Ontology Manager](https://palantir.com/docs/foundry/ontology-manager/overview/).
        :raises RateLimitExceeded: Failed to generate a response as the model rate limits were exceeded. Clients should wait and retry.
        :raises SessionExecutionFailed: Failed to generate a response for a session due to an unexpected error.
        :raises SessionNotFound: The given Session could not be found.
        :raises SessionTraceIdAlreadyExists: The provided trace ID already exists for the session and cannot be reused.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                    "sessionTraceId": session_trace_id,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "userInput": aip_agents_models.UserTextInput,
                        "parameterInputs": typing.Dict[
                            aip_agents_models.ParameterId, aip_agents_models.ParameterValue
                        ],
                        "contextsOverride": typing.Optional[
                            typing.List[aip_agents_models.InputContext]
                        ],
                        "sessionTraceId": typing.Optional[aip_agents_models.SessionTraceId],
                    },
                ),
                response_type=aip_agents_models.SessionExchangeResult,
                request_timeout=request_timeout,
                throwable_errors={
                    "AgentIterationsExceededLimit": aip_agents_errors.AgentIterationsExceededLimit,
                    "AgentNotFound": aip_agents_errors.AgentNotFound,
                    "BlockingContinueSessionPermissionDenied": aip_agents_errors.BlockingContinueSessionPermissionDenied,
                    "ContextSizeExceededLimit": aip_agents_errors.ContextSizeExceededLimit,
                    "FunctionLocatorNotFound": aip_agents_errors.FunctionLocatorNotFound,
                    "InvalidParameter": aip_agents_errors.InvalidParameter,
                    "InvalidParameterType": aip_agents_errors.InvalidParameterType,
                    "ObjectTypeIdsNotFound": aip_agents_errors.ObjectTypeIdsNotFound,
                    "ObjectTypeRidsNotFound": aip_agents_errors.ObjectTypeRidsNotFound,
                    "RateLimitExceeded": aip_agents_errors.RateLimitExceeded,
                    "SessionExecutionFailed": aip_agents_errors.SessionExecutionFailed,
                    "SessionNotFound": aip_agents_errors.SessionNotFound,
                    "SessionTraceIdAlreadyExists": aip_agents_errors.SessionTraceIdAlreadyExists,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def cancel(
        self,
        agent_rid: aip_agents_models.AgentRid,
        session_rid: aip_agents_models.SessionRid,
        *,
        message_id: aip_agents_models.MessageId,
        preview: typing.Optional[core_models.PreviewMode] = None,
        response: typing.Optional[aip_agents_models.AgentMarkdownResponse] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> aip_agents_models.CancelSessionResponse:
        """
        Cancel an in-progress streamed exchange with an Agent which was initiated with `streamingContinue`.
        Canceling an exchange allows clients to prevent the exchange from being added to the session, or to provide a response to replace the Agent-generated response.
        Note that canceling an exchange does not terminate the stream returned by `streamingContinue`; clients should close the stream on triggering the cancellation request to stop reading from the stream.

        :param agent_rid: An RID identifying an AIP Agent created in [AIP Agent Studio](https://palantir.com/docs/foundry/agent-studio/overview/).
        :type agent_rid: AgentRid
        :param session_rid: The Resource Identifier (RID) of the conversation session.
        :type session_rid: SessionRid
        :param message_id: The identifier for the in-progress exchange to cancel. This should match the `messageId` which was provided when initiating the exchange with `streamingContinue`.
        :type message_id: MessageId
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param response: When specified, the exchange is added to the session with the client-provided response as the result. When omitted, the exchange is not added to the session.
        :type response: Optional[AgentMarkdownResponse]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: aip_agents_models.CancelSessionResponse

        :raises AgentNotFound: The given Agent could not be found.
        :raises CancelSessionFailedMessageNotInProgress: Unable to cancel the requested session exchange as no in-progress exchange was found for the provided message identifier. This is expected if no exchange was initiated with the provided message identifier through a `streamingContinue` request, or if the exchange for this identifier has already completed and cannot be canceled, or if the exchange has already been canceled. This error can also occur if the cancellation was requested immediately after requesting the exchange through a `streamingContinue` request, and the exchange has not started yet. Clients should handle these errors gracefully, and can reload the session content to get the latest conversation state.
        :raises CancelSessionPermissionDenied: Could not cancel the Session.
        :raises SessionNotFound: The given Session could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "messageId": aip_agents_models.MessageId,
                        "response": typing.Optional[aip_agents_models.AgentMarkdownResponse],
                    },
                ),
                response_type=aip_agents_models.CancelSessionResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "AgentNotFound": aip_agents_errors.AgentNotFound,
                    "CancelSessionFailedMessageNotInProgress": aip_agents_errors.CancelSessionFailedMessageNotInProgress,
                    "CancelSessionPermissionDenied": aip_agents_errors.CancelSessionPermissionDenied,
                    "SessionNotFound": aip_agents_errors.SessionNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def create(
        self,
        agent_rid: aip_agents_models.AgentRid,
        *,
        agent_version: typing.Optional[aip_agents_models.AgentVersionString] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> aip_agents_models.Session:
        """
        Create a new conversation session between the calling user and an Agent.
        Use `blockingContinue` or `streamingContinue` to start adding exchanges to the session.

        :param agent_rid: An RID identifying an AIP Agent created in [AIP Agent Studio](https://palantir.com/docs/foundry/agent-studio/overview/).
        :type agent_rid: AgentRid
        :param agent_version: The version of the Agent associated with the session. This can be set by clients on session creation. If not specified, defaults to use the latest published version of the Agent at session creation time.
        :type agent_version: Optional[AgentVersionString]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: aip_agents_models.Session

        :raises AgentNotFound: The given Agent could not be found.
        :raises AgentVersionNotFound: The given AgentVersion could not be found.
        :raises CreateSessionPermissionDenied: Could not create the Session.
        :raises FunctionLocatorNotFound: The specified function locator is configured for use by the Agent but could not be found. The function type or version may not exist or the client token does not have access.
        :raises InvalidAgentVersion: The provided version string is not a valid format for an Agent version.
        :raises NoPublishedAgentVersion: Failed to retrieve the latest published version of the Agent because the Agent has no published versions. Try publishing the Agent in AIP Agent Studio to use the latest published version, or specify the version of the Agent to use.
        :raises ObjectTypeIdsNotFound: Some object types are configured for use by the Agent but could not be found. The object types either do not exist or the client token does not have access. Object types can be checked by listing available object types through the API, or searching in [Ontology Manager](https://palantir.com/docs/foundry/ontology-manager/overview/).
        :raises ObjectTypeRidsNotFound: Some object types are configured for use by the Agent but could not be found. The object types either do not exist or the client token does not have access. Object types can be checked by listing available object types through the API, or searching in [Ontology Manager](https://palantir.com/docs/foundry/ontology-manager/overview/).
        :raises SessionNotFound: The given Session could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "agentVersion": typing.Optional[aip_agents_models.AgentVersionString],
                    },
                ),
                response_type=aip_agents_models.Session,
                request_timeout=request_timeout,
                throwable_errors={
                    "AgentNotFound": aip_agents_errors.AgentNotFound,
                    "AgentVersionNotFound": aip_agents_errors.AgentVersionNotFound,
                    "CreateSessionPermissionDenied": aip_agents_errors.CreateSessionPermissionDenied,
                    "FunctionLocatorNotFound": aip_agents_errors.FunctionLocatorNotFound,
                    "InvalidAgentVersion": aip_agents_errors.InvalidAgentVersion,
                    "NoPublishedAgentVersion": aip_agents_errors.NoPublishedAgentVersion,
                    "ObjectTypeIdsNotFound": aip_agents_errors.ObjectTypeIdsNotFound,
                    "ObjectTypeRidsNotFound": aip_agents_errors.ObjectTypeRidsNotFound,
                    "SessionNotFound": aip_agents_errors.SessionNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        agent_rid: aip_agents_models.AgentRid,
        session_rid: aip_agents_models.SessionRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> aip_agents_models.Session:
        """
        Get the details of a conversation session between the calling user and an Agent.
        :param agent_rid: An RID identifying an AIP Agent created in [AIP Agent Studio](https://palantir.com/docs/foundry/agent-studio/overview/).
        :type agent_rid: AgentRid
        :param session_rid: The Resource Identifier (RID) of the conversation session.
        :type session_rid: SessionRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: aip_agents_models.Session

        :raises AgentNotFound: The given Agent could not be found.
        :raises SessionNotFound: The given Session could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                response_type=aip_agents_models.Session,
                request_timeout=request_timeout,
                throwable_errors={
                    "AgentNotFound": aip_agents_errors.AgentNotFound,
                    "SessionNotFound": aip_agents_errors.SessionNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def list(
        self,
        agent_rid: aip_agents_models.AgentRid,
        *,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> core.ResourceIterator[aip_agents_models.Session]:
        """
        List all conversation sessions between the calling user and an Agent that was created by this client.
        This does not list sessions for the user created by other clients.
        For example, any sessions created by the user in AIP Agent Studio will not be listed here.
        Sessions are returned in order of most recently updated first.

        :param agent_rid: An RID identifying an AIP Agent created in [AIP Agent Studio](https://palantir.com/docs/foundry/agent-studio/overview/).
        :type agent_rid: AgentRid
        :param page_size: The page size to use for the endpoint.
        :type page_size: Optional[PageSize]
        :param page_token: The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
        :type page_token: Optional[PageToken]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ResourceIterator[aip_agents_models.Session]

        :raises AgentNotFound: The given Agent could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                response_type=aip_agents_models.ListSessionsResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "AgentNotFound": aip_agents_errors.AgentNotFound,
                },
                response_mode=_sdk_internal.get("response_mode", "ITERATOR"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def rag_context(
        self,
        agent_rid: aip_agents_models.AgentRid,
        session_rid: aip_agents_models.SessionRid,
        *,
        parameter_inputs: typing.Dict[
            aip_agents_models.ParameterId, aip_agents_models.ParameterValue
        ],
        user_input: aip_agents_models.UserTextInput,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> aip_agents_models.AgentSessionRagContextResponse:
        """
        Retrieve relevant [context](https://palantir.com/docs/foundry/agent-studio/core-concepts/#retrieval-context) for a user message from the data sources configured for the session.
        This allows clients to pre-retrieve context for a user message before sending it to the Agent with the `contextsOverride` option when continuing a session, to allow any pre-processing of the context before sending it to the Agent.

        :param agent_rid: An RID identifying an AIP Agent created in [AIP Agent Studio](https://palantir.com/docs/foundry/agent-studio/overview/).
        :type agent_rid: AgentRid
        :param session_rid: The Resource Identifier (RID) of the conversation session.
        :type session_rid: SessionRid
        :param parameter_inputs: Any values for [application variables](https://palantir.com/docs/foundry/agent-studio/application-state/) to use for the context retrieval.
        :type parameter_inputs: Dict[ParameterId, ParameterValue]
        :param user_input: The user message to retrieve relevant context for from the configured Agent data sources.
        :type user_input: UserTextInput
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: aip_agents_models.AgentSessionRagContextResponse

        :raises AgentNotFound: The given Agent could not be found.
        :raises FunctionLocatorNotFound: The specified function locator is configured for use by the Agent but could not be found. The function type or version may not exist or the client token does not have access.
        :raises GetRagContextForSessionPermissionDenied: Could not ragContext the Session.
        :raises ObjectTypeIdsNotFound: Some object types are configured for use by the Agent but could not be found. The object types either do not exist or the client token does not have access. Object types can be checked by listing available object types through the API, or searching in [Ontology Manager](https://palantir.com/docs/foundry/ontology-manager/overview/).
        :raises ObjectTypeRidsNotFound: Some object types are configured for use by the Agent but could not be found. The object types either do not exist or the client token does not have access. Object types can be checked by listing available object types through the API, or searching in [Ontology Manager](https://palantir.com/docs/foundry/ontology-manager/overview/).
        :raises SessionNotFound: The given Session could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "userInput": aip_agents_models.UserTextInput,
                        "parameterInputs": typing.Dict[
                            aip_agents_models.ParameterId, aip_agents_models.ParameterValue
                        ],
                    },
                ),
                response_type=aip_agents_models.AgentSessionRagContextResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "AgentNotFound": aip_agents_errors.AgentNotFound,
                    "FunctionLocatorNotFound": aip_agents_errors.FunctionLocatorNotFound,
                    "GetRagContextForSessionPermissionDenied": aip_agents_errors.GetRagContextForSessionPermissionDenied,
                    "ObjectTypeIdsNotFound": aip_agents_errors.ObjectTypeIdsNotFound,
                    "ObjectTypeRidsNotFound": aip_agents_errors.ObjectTypeRidsNotFound,
                    "SessionNotFound": aip_agents_errors.SessionNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def streaming_continue(
        self,
        agent_rid: aip_agents_models.AgentRid,
        session_rid: aip_agents_models.SessionRid,
        *,
        parameter_inputs: typing.Dict[
            aip_agents_models.ParameterId, aip_agents_models.ParameterValue
        ],
        user_input: aip_agents_models.UserTextInput,
        contexts_override: typing.Optional[typing.List[aip_agents_models.InputContext]] = None,
        message_id: typing.Optional[aip_agents_models.MessageId] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        session_trace_id: typing.Optional[aip_agents_models.SessionTraceId] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> bytes:
        """
        Continue a conversation session with an Agent, or add the first exchange to a session after creation.
        Adds a new exchange to the session with the provided inputs, and generates a response from the Agent.
        Returns a stream of the Agent response text (formatted using markdown) for clients to consume as the response is generated.
        On completion of the streamed response, clients can load the full details of the exchange that was added to the session by reloading the session content.
        Streamed exchanges also support cancellation; see `cancel` for details.
        Concurrent requests to continue the same session are not supported.
        Clients should wait to receive a response, or cancel the in-progress exchange, before sending the next message.

        :param agent_rid: An RID identifying an AIP Agent created in [AIP Agent Studio](https://palantir.com/docs/foundry/agent-studio/overview/).
        :type agent_rid: AgentRid
        :param session_rid: The Resource Identifier (RID) of the conversation session.
        :type session_rid: SessionRid
        :param parameter_inputs: Any supplied values for [application variables](https://palantir.com/docs/foundry/agent-studio/application-state/) to pass to the Agent for the exchange.
        :type parameter_inputs: Dict[ParameterId, ParameterValue]
        :param user_input: The user message for the Agent to respond to.
        :type user_input: UserTextInput
        :param contexts_override: If set, automatic [context](https://palantir.com/docs/foundry/agent-studio/retrieval-context/) retrieval is skipped and the list of specified context is provided to the Agent instead. If omitted, relevant context for the user message is automatically retrieved and included in the prompt, based on data sources configured on the Agent for the session.
        :type contexts_override: Optional[List[InputContext]]
        :param message_id: A client-generated Universally Unique Identifier (UUID) to identify the message, which the client can use to cancel the exchange before the streaming response is complete.
        :type message_id: Optional[MessageId]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param session_trace_id: The unique identifier to use for this continue session trace. By generating and passing this ID to the `streamingContinue` endpoint, clients can use this trace ID to separately load details of the trace used to generate a result, while the result is in progress. If omitted, it will be generated automatically. Clients can check the generated ID by inspecting the `sessionTraceId` in the `SessionExchangeResult`, which can be loaded via the `getContent` endpoint.
        :type session_trace_id: Optional[SessionTraceId]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: bytes

        :raises AgentNotFound: The given Agent could not be found.
        :raises FunctionLocatorNotFound: The specified function locator is configured for use by the Agent but could not be found. The function type or version may not exist or the client token does not have access.
        :raises InvalidParameter: The provided application variable is not valid for the Agent for this session. Check the available application variables for the Agent under the `parameters` property, and version through the API with `getAgent`, or in AIP Agent Studio. The Agent version used for the session can be checked through the API with `getSession`.
        :raises InvalidParameterType: The provided value does not match the expected type for the application variable configured on the Agent for this session. Check the available application variables for the Agent under the `parameters` property, and version through the API with `getAgent`, or in AIP Agent Studio. The Agent version used for the session can be checked through the API with `getSession`.
        :raises ObjectTypeIdsNotFound: Some object types are configured for use by the Agent but could not be found. The object types either do not exist or the client token does not have access. Object types can be checked by listing available object types through the API, or searching in [Ontology Manager](https://palantir.com/docs/foundry/ontology-manager/overview/).
        :raises ObjectTypeRidsNotFound: Some object types are configured for use by the Agent but could not be found. The object types either do not exist or the client token does not have access. Object types can be checked by listing available object types through the API, or searching in [Ontology Manager](https://palantir.com/docs/foundry/ontology-manager/overview/).
        :raises SessionNotFound: The given Session could not be found.
        :raises SessionTraceIdAlreadyExists: The provided trace ID already exists for the session and cannot be reused.
        :raises StreamingContinueSessionPermissionDenied: Could not streamingContinue the Session.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                    "sessionTraceId": session_trace_id,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "userInput": aip_agents_models.UserTextInput,
                        "parameterInputs": typing.Dict[
                            aip_agents_models.ParameterId, aip_agents_models.ParameterValue
                        ],
                        "contextsOverride": typing.Optional[
                            typing.List[aip_agents_models.InputContext]
                        ],
                        "messageId": typing.Optional[aip_agents_models.MessageId],
                        "sessionTraceId": typing.Optional[aip_agents_models.SessionTraceId],
                    },
                ),
                response_type=bytes,
                request_timeout=request_timeout,
                throwable_errors={
                    "AgentNotFound": aip_agents_errors.AgentNotFound,
                    "FunctionLocatorNotFound": aip_agents_errors.FunctionLocatorNotFound,
                    "InvalidParameter": aip_agents_errors.InvalidParameter,
                    "InvalidParameterType": aip_agents_errors.InvalidParameterType,
                    "ObjectTypeIdsNotFound": aip_agents_errors.ObjectTypeIdsNotFound,
                    "ObjectTypeRidsNotFound": aip_agents_errors.ObjectTypeRidsNotFound,
                    "SessionNotFound": aip_agents_errors.SessionNotFound,
                    "SessionTraceIdAlreadyExists": aip_agents_errors.SessionTraceIdAlreadyExists,
                    "StreamingContinueSessionPermissionDenied": aip_agents_errors.StreamingContinueSessionPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def update_title(
        self,
        agent_rid: aip_agents_models.AgentRid,
        session_rid: aip_agents_models.SessionRid,
        *,
        title: str,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> None:
        """
        Update the title for a session.
        Use this to set a custom title for a session to help identify it in the list of sessions with an Agent.

        :param agent_rid: An RID identifying an AIP Agent created in [AIP Agent Studio](https://palantir.com/docs/foundry/agent-studio/overview/).
        :type agent_rid: AgentRid
        :param session_rid: The Resource Identifier (RID) of the conversation session.
        :type session_rid: SessionRid
        :param title: The new title for the session. The maximum title length is 200 characters. Titles are truncated if they exceed this length.
        :type title: str
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: None

        :raises AgentNotFound: The given Agent could not be found.
        :raises SessionNotFound: The given Session could not be found.
        :raises UpdateSessionTitlePermissionDenied: Could not updateTitle the Session.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="PUT",
                resource_path="/v2/aipAgents/agents/{agentRid}/sessions/{sessionRid}/updateTitle",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "agentRid": agent_rid,
                    "sessionRid": session_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                },
                body={
                    "title": title,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "title": str,
                    },
                ),
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "AgentNotFound": aip_agents_errors.AgentNotFound,
                    "SessionNotFound": aip_agents_errors.SessionNotFound,
                    "UpdateSessionTitlePermissionDenied": aip_agents_errors.UpdateSessionTitlePermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _SessionClientRaw:
    def __init__(self, client: SessionClient) -> None:
        def blocking_continue(_: aip_agents_models.SessionExchangeResult): ...
        def cancel(_: aip_agents_models.CancelSessionResponse): ...
        def create(_: aip_agents_models.Session): ...
        def get(_: aip_agents_models.Session): ...
        def list(_: aip_agents_models.ListSessionsResponse): ...
        def rag_context(_: aip_agents_models.AgentSessionRagContextResponse): ...
        def streaming_continue(_: bytes): ...
        def update_title(_: None): ...

        self.blocking_continue = core.with_raw_response(blocking_continue, client.blocking_continue)
        self.cancel = core.with_raw_response(cancel, client.cancel)
        self.create = core.with_raw_response(create, client.create)
        self.get = core.with_raw_response(get, client.get)
        self.list = core.with_raw_response(list, client.list)
        self.rag_context = core.with_raw_response(rag_context, client.rag_context)
        self.streaming_continue = core.with_raw_response(
            streaming_continue, client.streaming_continue
        )
        self.update_title = core.with_raw_response(update_title, client.update_title)


class _SessionClientStreaming:
    def __init__(self, client: SessionClient) -> None:
        def blocking_continue(_: aip_agents_models.SessionExchangeResult): ...
        def cancel(_: aip_agents_models.CancelSessionResponse): ...
        def create(_: aip_agents_models.Session): ...
        def get(_: aip_agents_models.Session): ...
        def list(_: aip_agents_models.ListSessionsResponse): ...
        def rag_context(_: aip_agents_models.AgentSessionRagContextResponse): ...
        def streaming_continue(_: bytes): ...

        self.blocking_continue = core.with_streaming_response(
            blocking_continue, client.blocking_continue
        )
        self.cancel = core.with_streaming_response(cancel, client.cancel)
        self.create = core.with_streaming_response(create, client.create)
        self.get = core.with_streaming_response(get, client.get)
        self.list = core.with_streaming_response(list, client.list)
        self.rag_context = core.with_streaming_response(rag_context, client.rag_context)
        self.streaming_continue = core.with_streaming_response(
            streaming_continue, client.streaming_continue
        )


class AsyncSessionClient:
    """
    The API client for the Session Resource.

    :param auth: Your auth configuration.
    :param hostname: Your Foundry hostname (for example, "myfoundry.palantirfoundry.com"). This can also include your API gateway service URI.
    :param config: Optionally specify the configuration for the HTTP session.
    """

    def __init__(
        self,
        auth: core.Auth,
        hostname: str,
        config: typing.Optional[core.Config] = None,
    ):
        self._auth = auth
        self._hostname = hostname
        self._config = config
        self._api_client = core.AsyncApiClient(auth=auth, hostname=hostname, config=config)

        self.with_streaming_response = _AsyncSessionClientStreaming(self)
        self.with_raw_response = _AsyncSessionClientRaw(self)

    @cached_property
    def Content(self):
        from foundry_sdk.v2.aip_agents.content import AsyncContentClient

        return AsyncContentClient(
            auth=self._auth,
            hostname=self._hostname,
            config=self._config,
        )

    @cached_property
    def SessionTrace(self):
        from foundry_sdk.v2.aip_agents.session_trace import AsyncSessionTraceClient

        return AsyncSessionTraceClient(
            auth=self._auth,
            hostname=self._hostname,
            config=self._config,
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def blocking_continue(
        self,
        agent_rid: aip_agents_models.AgentRid,
        session_rid: aip_agents_models.SessionRid,
        *,
        parameter_inputs: typing.Dict[
            aip_agents_models.ParameterId, aip_agents_models.ParameterValue
        ],
        user_input: aip_agents_models.UserTextInput,
        contexts_override: typing.Optional[typing.List[aip_agents_models.InputContext]] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        session_trace_id: typing.Optional[aip_agents_models.SessionTraceId] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[aip_agents_models.SessionExchangeResult]:
        """
        Continue a conversation session with an Agent, or add the first exchange to a session after creation.
        Adds a new exchange to the session with the provided inputs, and generates a response from the Agent.
        Blocks on returning the result of the added exchange until the response is fully generated.
        Streamed responses are also supported; see `streamingContinue` for details.
        Concurrent requests to continue the same session are not supported.
        Clients should wait to receive a response before sending the next message.

        :param agent_rid: An RID identifying an AIP Agent created in [AIP Agent Studio](https://palantir.com/docs/foundry/agent-studio/overview/).
        :type agent_rid: AgentRid
        :param session_rid: The Resource Identifier (RID) of the conversation session.
        :type session_rid: SessionRid
        :param parameter_inputs: Any supplied values for [application variables](https://palantir.com/docs/foundry/agent-studio/application-state/) to pass to the Agent for the exchange.
        :type parameter_inputs: Dict[ParameterId, ParameterValue]
        :param user_input: The user message for the Agent to respond to.
        :type user_input: UserTextInput
        :param contexts_override: If set, automatic [context retrieval](https://palantir.com/docs/foundry/agent-studio/retrieval-context/) is skipped and the list of specified context is provided to the Agent instead. If omitted, relevant context for the user message is automatically retrieved and included in the prompt, based on data sources configured on the Agent for the session.
        :type contexts_override: Optional[List[InputContext]]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param session_trace_id: The unique identifier to use for this continue session trace. By generating and passing this ID to the `blockingContinue` endpoint, clients can use this trace ID to separately load details of the trace used to generate a result, while the result is in progress. If omitted, it will be generated automatically. Clients can check the generated ID by inspecting the `sessionTraceId` in the `SessionExchangeResult`.
        :type session_trace_id: Optional[SessionTraceId]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[aip_agents_models.SessionExchangeResult]

        :raises AgentIterationsExceededLimit: The Agent was unable to produce an answer in the set number of maximum iterations. This can happen if the Agent gets confused or stuck in a loop, or if the query is too complex. Try a different query or review the Agent configuration in AIP Agent Studio.
        :raises AgentNotFound: The given Agent could not be found.
        :raises BlockingContinueSessionPermissionDenied: Could not blockingContinue the Session.
        :raises ContextSizeExceededLimit: Failed to generate a response for a session because the context size of the LLM has been exceeded. Clients should either retry with a shorter message or create a new session and try re-sending the message.
        :raises FunctionLocatorNotFound: The specified function locator is configured for use by the Agent but could not be found. The function type or version may not exist or the client token does not have access.
        :raises InvalidParameter: The provided application variable is not valid for the Agent for this session. Check the available application variables for the Agent under the `parameters` property, and version through the API with `getAgent`, or in AIP Agent Studio. The Agent version used for the session can be checked through the API with `getSession`.
        :raises InvalidParameterType: The provided value does not match the expected type for the application variable configured on the Agent for this session. Check the available application variables for the Agent under the `parameters` property, and version through the API with `getAgent`, or in AIP Agent Studio. The Agent version used for the session can be checked through the API with `getSession`.
        :raises ObjectTypeIdsNotFound: Some object types are configured for use by the Agent but could not be found. The object types either do not exist or the client token does not have access. Object types can be checked by listing available object types through the API, or searching in [Ontology Manager](https://palantir.com/docs/foundry/ontology-manager/overview/).
        :raises ObjectTypeRidsNotFound: Some object types are configured for use by the Agent but could not be found. The object types either do not exist or the client token does not have access. Object types can be checked by listing available object types through the API, or searching in [Ontology Manager](https://palantir.com/docs/foundry/ontology-manager/overview/).
        :raises RateLimitExceeded: Failed to generate a response as the model rate limits were exceeded. Clients should wait and retry.
        :raises SessionExecutionFailed: Failed to generate a response for a session due to an unexpected error.
        :raises SessionNotFound: The given Session could not be found.
        :raises SessionTraceIdAlreadyExists: The provided trace ID already exists for the session and cannot be reused.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                    "sessionTraceId": session_trace_id,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "userInput": aip_agents_models.UserTextInput,
                        "parameterInputs": typing.Dict[
                            aip_agents_models.ParameterId, aip_agents_models.ParameterValue
                        ],
                        "contextsOverride": typing.Optional[
                            typing.List[aip_agents_models.InputContext]
                        ],
                        "sessionTraceId": typing.Optional[aip_agents_models.SessionTraceId],
                    },
                ),
                response_type=aip_agents_models.SessionExchangeResult,
                request_timeout=request_timeout,
                throwable_errors={
                    "AgentIterationsExceededLimit": aip_agents_errors.AgentIterationsExceededLimit,
                    "AgentNotFound": aip_agents_errors.AgentNotFound,
                    "BlockingContinueSessionPermissionDenied": aip_agents_errors.BlockingContinueSessionPermissionDenied,
                    "ContextSizeExceededLimit": aip_agents_errors.ContextSizeExceededLimit,
                    "FunctionLocatorNotFound": aip_agents_errors.FunctionLocatorNotFound,
                    "InvalidParameter": aip_agents_errors.InvalidParameter,
                    "InvalidParameterType": aip_agents_errors.InvalidParameterType,
                    "ObjectTypeIdsNotFound": aip_agents_errors.ObjectTypeIdsNotFound,
                    "ObjectTypeRidsNotFound": aip_agents_errors.ObjectTypeRidsNotFound,
                    "RateLimitExceeded": aip_agents_errors.RateLimitExceeded,
                    "SessionExecutionFailed": aip_agents_errors.SessionExecutionFailed,
                    "SessionNotFound": aip_agents_errors.SessionNotFound,
                    "SessionTraceIdAlreadyExists": aip_agents_errors.SessionTraceIdAlreadyExists,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def cancel(
        self,
        agent_rid: aip_agents_models.AgentRid,
        session_rid: aip_agents_models.SessionRid,
        *,
        message_id: aip_agents_models.MessageId,
        preview: typing.Optional[core_models.PreviewMode] = None,
        response: typing.Optional[aip_agents_models.AgentMarkdownResponse] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[aip_agents_models.CancelSessionResponse]:
        """
        Cancel an in-progress streamed exchange with an Agent which was initiated with `streamingContinue`.
        Canceling an exchange allows clients to prevent the exchange from being added to the session, or to provide a response to replace the Agent-generated response.
        Note that canceling an exchange does not terminate the stream returned by `streamingContinue`; clients should close the stream on triggering the cancellation request to stop reading from the stream.

        :param agent_rid: An RID identifying an AIP Agent created in [AIP Agent Studio](https://palantir.com/docs/foundry/agent-studio/overview/).
        :type agent_rid: AgentRid
        :param session_rid: The Resource Identifier (RID) of the conversation session.
        :type session_rid: SessionRid
        :param message_id: The identifier for the in-progress exchange to cancel. This should match the `messageId` which was provided when initiating the exchange with `streamingContinue`.
        :type message_id: MessageId
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param response: When specified, the exchange is added to the session with the client-provided response as the result. When omitted, the exchange is not added to the session.
        :type response: Optional[AgentMarkdownResponse]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[aip_agents_models.CancelSessionResponse]

        :raises AgentNotFound: The given Agent could not be found.
        :raises CancelSessionFailedMessageNotInProgress: Unable to cancel the requested session exchange as no in-progress exchange was found for the provided message identifier. This is expected if no exchange was initiated with the provided message identifier through a `streamingContinue` request, or if the exchange for this identifier has already completed and cannot be canceled, or if the exchange has already been canceled. This error can also occur if the cancellation was requested immediately after requesting the exchange through a `streamingContinue` request, and the exchange has not started yet. Clients should handle these errors gracefully, and can reload the session content to get the latest conversation state.
        :raises CancelSessionPermissionDenied: Could not cancel the Session.
        :raises SessionNotFound: The given Session could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "messageId": aip_agents_models.MessageId,
                        "response": typing.Optional[aip_agents_models.AgentMarkdownResponse],
                    },
                ),
                response_type=aip_agents_models.CancelSessionResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "AgentNotFound": aip_agents_errors.AgentNotFound,
                    "CancelSessionFailedMessageNotInProgress": aip_agents_errors.CancelSessionFailedMessageNotInProgress,
                    "CancelSessionPermissionDenied": aip_agents_errors.CancelSessionPermissionDenied,
                    "SessionNotFound": aip_agents_errors.SessionNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def create(
        self,
        agent_rid: aip_agents_models.AgentRid,
        *,
        agent_version: typing.Optional[aip_agents_models.AgentVersionString] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[aip_agents_models.Session]:
        """
        Create a new conversation session between the calling user and an Agent.
        Use `blockingContinue` or `streamingContinue` to start adding exchanges to the session.

        :param agent_rid: An RID identifying an AIP Agent created in [AIP Agent Studio](https://palantir.com/docs/foundry/agent-studio/overview/).
        :type agent_rid: AgentRid
        :param agent_version: The version of the Agent associated with the session. This can be set by clients on session creation. If not specified, defaults to use the latest published version of the Agent at session creation time.
        :type agent_version: Optional[AgentVersionString]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[aip_agents_models.Session]

        :raises AgentNotFound: The given Agent could not be found.
        :raises AgentVersionNotFound: The given AgentVersion could not be found.
        :raises CreateSessionPermissionDenied: Could not create the Session.
        :raises FunctionLocatorNotFound: The specified function locator is configured for use by the Agent but could not be found. The function type or version may not exist or the client token does not have access.
        :raises InvalidAgentVersion: The provided version string is not a valid format for an Agent version.
        :raises NoPublishedAgentVersion: Failed to retrieve the latest published version of the Agent because the Agent has no published versions. Try publishing the Agent in AIP Agent Studio to use the latest published version, or specify the version of the Agent to use.
        :raises ObjectTypeIdsNotFound: Some object types are configured for use by the Agent but could not be found. The object types either do not exist or the client token does not have access. Object types can be checked by listing available object types through the API, or searching in [Ontology Manager](https://palantir.com/docs/foundry/ontology-manager/overview/).
        :raises ObjectTypeRidsNotFound: Some object types are configured for use by the Agent but could not be found. The object types either do not exist or the client token does not have access. Object types can be checked by listing available object types through the API, or searching in [Ontology Manager](https://palantir.com/docs/foundry/ontology-manager/overview/).
        :raises SessionNotFound: The given Session could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "agentVersion": typing.Optional[aip_agents_models.AgentVersionString],
                    },
                ),
                response_type=aip_agents_models.Session,
                request_timeout=request_timeout,
                throwable_errors={
                    "AgentNotFound": aip_agents_errors.AgentNotFound,
                    "AgentVersionNotFound": aip_agents_errors.AgentVersionNotFound,
                    "CreateSessionPermissionDenied": aip_agents_errors.CreateSessionPermissionDenied,
                    "FunctionLocatorNotFound": aip_agents_errors.FunctionLocatorNotFound,
                    "InvalidAgentVersion": aip_agents_errors.InvalidAgentVersion,
                    "NoPublishedAgentVersion": aip_agents_errors.NoPublishedAgentVersion,
                    "ObjectTypeIdsNotFound": aip_agents_errors.ObjectTypeIdsNotFound,
                    "ObjectTypeRidsNotFound": aip_agents_errors.ObjectTypeRidsNotFound,
                    "SessionNotFound": aip_agents_errors.SessionNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        agent_rid: aip_agents_models.AgentRid,
        session_rid: aip_agents_models.SessionRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[aip_agents_models.Session]:
        """
        Get the details of a conversation session between the calling user and an Agent.
        :param agent_rid: An RID identifying an AIP Agent created in [AIP Agent Studio](https://palantir.com/docs/foundry/agent-studio/overview/).
        :type agent_rid: AgentRid
        :param session_rid: The Resource Identifier (RID) of the conversation session.
        :type session_rid: SessionRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[aip_agents_models.Session]

        :raises AgentNotFound: The given Agent could not be found.
        :raises SessionNotFound: The given Session could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                response_type=aip_agents_models.Session,
                request_timeout=request_timeout,
                throwable_errors={
                    "AgentNotFound": aip_agents_errors.AgentNotFound,
                    "SessionNotFound": aip_agents_errors.SessionNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def list(
        self,
        agent_rid: aip_agents_models.AgentRid,
        *,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> core.AsyncResourceIterator[aip_agents_models.Session]:
        """
        List all conversation sessions between the calling user and an Agent that was created by this client.
        This does not list sessions for the user created by other clients.
        For example, any sessions created by the user in AIP Agent Studio will not be listed here.
        Sessions are returned in order of most recently updated first.

        :param agent_rid: An RID identifying an AIP Agent created in [AIP Agent Studio](https://palantir.com/docs/foundry/agent-studio/overview/).
        :type agent_rid: AgentRid
        :param page_size: The page size to use for the endpoint.
        :type page_size: Optional[PageSize]
        :param page_token: The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
        :type page_token: Optional[PageToken]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.AsyncResourceIterator[aip_agents_models.Session]

        :raises AgentNotFound: The given Agent could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                response_type=aip_agents_models.ListSessionsResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "AgentNotFound": aip_agents_errors.AgentNotFound,
                },
                response_mode=_sdk_internal.get("response_mode", "ITERATOR"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def rag_context(
        self,
        agent_rid: aip_agents_models.AgentRid,
        session_rid: aip_agents_models.SessionRid,
        *,
        parameter_inputs: typing.Dict[
            aip_agents_models.ParameterId, aip_agents_models.ParameterValue
        ],
        user_input: aip_agents_models.UserTextInput,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[aip_agents_models.AgentSessionRagContextResponse]:
        """
        Retrieve relevant [context](https://palantir.com/docs/foundry/agent-studio/core-concepts/#retrieval-context) for a user message from the data sources configured for the session.
        This allows clients to pre-retrieve context for a user message before sending it to the Agent with the `contextsOverride` option when continuing a session, to allow any pre-processing of the context before sending it to the Agent.

        :param agent_rid: An RID identifying an AIP Agent created in [AIP Agent Studio](https://palantir.com/docs/foundry/agent-studio/overview/).
        :type agent_rid: AgentRid
        :param session_rid: The Resource Identifier (RID) of the conversation session.
        :type session_rid: SessionRid
        :param parameter_inputs: Any values for [application variables](https://palantir.com/docs/foundry/agent-studio/application-state/) to use for the context retrieval.
        :type parameter_inputs: Dict[ParameterId, ParameterValue]
        :param user_input: The user message to retrieve relevant context for from the configured Agent data sources.
        :type user_input: UserTextInput
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[aip_agents_models.AgentSessionRagContextResponse]

        :raises AgentNotFound: The given Agent could not be found.
        :raises FunctionLocatorNotFound: The specified function locator is configured for use by the Agent but could not be found. The function type or version may not exist or the client token does not have access.
        :raises GetRagContextForSessionPermissionDenied: Could not ragContext the Session.
        :raises ObjectTypeIdsNotFound: Some object types are configured for use by the Agent but could not be found. The object types either do not exist or the client token does not have access. Object types can be checked by listing available object types through the API, or searching in [Ontology Manager](https://palantir.com/docs/foundry/ontology-manager/overview/).
        :raises ObjectTypeRidsNotFound: Some object types are configured for use by the Agent but could not be found. The object types either do not exist or the client token does not have access. Object types can be checked by listing available object types through the API, or searching in [Ontology Manager](https://palantir.com/docs/foundry/ontology-manager/overview/).
        :raises SessionNotFound: The given Session could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "userInput": aip_agents_models.UserTextInput,
                        "parameterInputs": typing.Dict[
                            aip_agents_models.ParameterId, aip_agents_models.ParameterValue
                        ],
                    },
                ),
                response_type=aip_agents_models.AgentSessionRagContextResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "AgentNotFound": aip_agents_errors.AgentNotFound,
                    "FunctionLocatorNotFound": aip_agents_errors.FunctionLocatorNotFound,
                    "GetRagContextForSessionPermissionDenied": aip_agents_errors.GetRagContextForSessionPermissionDenied,
                    "ObjectTypeIdsNotFound": aip_agents_errors.ObjectTypeIdsNotFound,
                    "ObjectTypeRidsNotFound": aip_agents_errors.ObjectTypeRidsNotFound,
                    "SessionNotFound": aip_agents_errors.SessionNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def streaming_continue(
        self,
        agent_rid: aip_agents_models.AgentRid,
        session_rid: aip_agents_models.SessionRid,
        *,
        parameter_inputs: typing.Dict[
            aip_agents_models.ParameterId, aip_agents_models.ParameterValue
        ],
        user_input: aip_agents_models.UserTextInput,
        contexts_override: typing.Optional[typing.List[aip_agents_models.InputContext]] = None,
        message_id: typing.Optional[aip_agents_models.MessageId] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        session_trace_id: typing.Optional[aip_agents_models.SessionTraceId] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[bytes]:
        """
        Continue a conversation session with an Agent, or add the first exchange to a session after creation.
        Adds a new exchange to the session with the provided inputs, and generates a response from the Agent.
        Returns a stream of the Agent response text (formatted using markdown) for clients to consume as the response is generated.
        On completion of the streamed response, clients can load the full details of the exchange that was added to the session by reloading the session content.
        Streamed exchanges also support cancellation; see `cancel` for details.
        Concurrent requests to continue the same session are not supported.
        Clients should wait to receive a response, or cancel the in-progress exchange, before sending the next message.

        :param agent_rid: An RID identifying an AIP Agent created in [AIP Agent Studio](https://palantir.com/docs/foundry/agent-studio/overview/).
        :type agent_rid: AgentRid
        :param session_rid: The Resource Identifier (RID) of the conversation session.
        :type session_rid: SessionRid
        :param parameter_inputs: Any supplied values for [application variables](https://palantir.com/docs/foundry/agent-studio/application-state/) to pass to the Agent for the exchange.
        :type parameter_inputs: Dict[ParameterId, ParameterValue]
        :param user_input: The user message for the Agent to respond to.
        :type user_input: UserTextInput
        :param contexts_override: If set, automatic [context](https://palantir.com/docs/foundry/agent-studio/retrieval-context/) retrieval is skipped and the list of specified context is provided to the Agent instead. If omitted, relevant context for the user message is automatically retrieved and included in the prompt, based on data sources configured on the Agent for the session.
        :type contexts_override: Optional[List[InputContext]]
        :param message_id: A client-generated Universally Unique Identifier (UUID) to identify the message, which the client can use to cancel the exchange before the streaming response is complete.
        :type message_id: Optional[MessageId]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param session_trace_id: The unique identifier to use for this continue session trace. By generating and passing this ID to the `streamingContinue` endpoint, clients can use this trace ID to separately load details of the trace used to generate a result, while the result is in progress. If omitted, it will be generated automatically. Clients can check the generated ID by inspecting the `sessionTraceId` in the `SessionExchangeResult`, which can be loaded via the `getContent` endpoint.
        :type session_trace_id: Optional[SessionTraceId]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[bytes]

        :raises AgentNotFound: The given Agent could not be found.
        :raises FunctionLocatorNotFound: The specified function locator is configured for use by the Agent but could not be found. The function type or version may not exist or the client token does not have access.
        :raises InvalidParameter: The provided application variable is not valid for the Agent for this session. Check the available application variables for the Agent under the `parameters` property, and version through the API with `getAgent`, or in AIP Agent Studio. The Agent version used for the session can be checked through the API with `getSession`.
        :raises InvalidParameterType: The provided value does not match the expected type for the application variable configured on the Agent for this session. Check the available application variables for the Agent under the `parameters` property, and version through the API with `getAgent`, or in AIP Agent Studio. The Agent version used for the session can be checked through the API with `getSession`.
        :raises ObjectTypeIdsNotFound: Some object types are configured for use by the Agent but could not be found. The object types either do not exist or the client token does not have access. Object types can be checked by listing available object types through the API, or searching in [Ontology Manager](https://palantir.com/docs/foundry/ontology-manager/overview/).
        :raises ObjectTypeRidsNotFound: Some object types are configured for use by the Agent but could not be found. The object types either do not exist or the client token does not have access. Object types can be checked by listing available object types through the API, or searching in [Ontology Manager](https://palantir.com/docs/foundry/ontology-manager/overview/).
        :raises SessionNotFound: The given Session could not be found.
        :raises SessionTraceIdAlreadyExists: The provided trace ID already exists for the session and cannot be reused.
        :raises StreamingContinueSessionPermissionDenied: Could not streamingContinue the Session.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                    "sessionTraceId": session_trace_id,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "userInput": aip_agents_models.UserTextInput,
                        "parameterInputs": typing.Dict[
                            aip_agents_models.ParameterId, aip_agents_models.ParameterValue
                        ],
                        "contextsOverride": typing.Optional[
                            typing.List[aip_agents_models.InputContext]
                        ],
                        "messageId": typing.Optional[aip_agents_models.MessageId],
                        "sessionTraceId": typing.Optional[aip_agents_models.SessionTraceId],
                    },
                ),
                response_type=bytes,
                request_timeout=request_timeout,
                throwable_errors={
                    "AgentNotFound": aip_agents_errors.AgentNotFound,
                    "FunctionLocatorNotFound": aip_agents_errors.FunctionLocatorNotFound,
                    "InvalidParameter": aip_agents_errors.InvalidParameter,
                    "InvalidParameterType": aip_agents_errors.InvalidParameterType,
                    "ObjectTypeIdsNotFound": aip_agents_errors.ObjectTypeIdsNotFound,
                    "ObjectTypeRidsNotFound": aip_agents_errors.ObjectTypeRidsNotFound,
                    "SessionNotFound": aip_agents_errors.SessionNotFound,
                    "SessionTraceIdAlreadyExists": aip_agents_errors.SessionTraceIdAlreadyExists,
                    "StreamingContinueSessionPermissionDenied": aip_agents_errors.StreamingContinueSessionPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def update_title(
        self,
        agent_rid: aip_agents_models.AgentRid,
        session_rid: aip_agents_models.SessionRid,
        *,
        title: str,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[None]:
        """
        Update the title for a session.
        Use this to set a custom title for a session to help identify it in the list of sessions with an Agent.

        :param agent_rid: An RID identifying an AIP Agent created in [AIP Agent Studio](https://palantir.com/docs/foundry/agent-studio/overview/).
        :type agent_rid: AgentRid
        :param session_rid: The Resource Identifier (RID) of the conversation session.
        :type session_rid: SessionRid
        :param title: The new title for the session. The maximum title length is 200 characters. Titles are truncated if they exceed this length.
        :type title: str
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[None]

        :raises AgentNotFound: The given Agent could not be found.
        :raises SessionNotFound: The given Session could not be found.
        :raises UpdateSessionTitlePermissionDenied: Could not updateTitle the Session.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="PUT",
                resource_path="/v2/aipAgents/agents/{agentRid}/sessions/{sessionRid}/updateTitle",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "agentRid": agent_rid,
                    "sessionRid": session_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                },
                body={
                    "title": title,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "title": str,
                    },
                ),
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "AgentNotFound": aip_agents_errors.AgentNotFound,
                    "SessionNotFound": aip_agents_errors.SessionNotFound,
                    "UpdateSessionTitlePermissionDenied": aip_agents_errors.UpdateSessionTitlePermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _AsyncSessionClientRaw:
    def __init__(self, client: AsyncSessionClient) -> None:
        def blocking_continue(_: aip_agents_models.SessionExchangeResult): ...
        def cancel(_: aip_agents_models.CancelSessionResponse): ...
        def create(_: aip_agents_models.Session): ...
        def get(_: aip_agents_models.Session): ...
        def list(_: aip_agents_models.ListSessionsResponse): ...
        def rag_context(_: aip_agents_models.AgentSessionRagContextResponse): ...
        def streaming_continue(_: bytes): ...
        def update_title(_: None): ...

        self.blocking_continue = core.async_with_raw_response(
            blocking_continue, client.blocking_continue
        )
        self.cancel = core.async_with_raw_response(cancel, client.cancel)
        self.create = core.async_with_raw_response(create, client.create)
        self.get = core.async_with_raw_response(get, client.get)
        self.list = core.async_with_raw_response(list, client.list)
        self.rag_context = core.async_with_raw_response(rag_context, client.rag_context)
        self.streaming_continue = core.async_with_raw_response(
            streaming_continue, client.streaming_continue
        )
        self.update_title = core.async_with_raw_response(update_title, client.update_title)


class _AsyncSessionClientStreaming:
    def __init__(self, client: AsyncSessionClient) -> None:
        def blocking_continue(_: aip_agents_models.SessionExchangeResult): ...
        def cancel(_: aip_agents_models.CancelSessionResponse): ...
        def create(_: aip_agents_models.Session): ...
        def get(_: aip_agents_models.Session): ...
        def list(_: aip_agents_models.ListSessionsResponse): ...
        def rag_context(_: aip_agents_models.AgentSessionRagContextResponse): ...
        def streaming_continue(_: bytes): ...

        self.blocking_continue = core.async_with_streaming_response(
            blocking_continue, client.blocking_continue
        )
        self.cancel = core.async_with_streaming_response(cancel, client.cancel)
        self.create = core.async_with_streaming_response(create, client.create)
        self.get = core.async_with_streaming_response(get, client.get)
        self.list = core.async_with_streaming_response(list, client.list)
        self.rag_context = core.async_with_streaming_response(rag_context, client.rag_context)
        self.streaming_continue = core.async_with_streaming_response(
            streaming_continue, client.streaming_continue
        )
