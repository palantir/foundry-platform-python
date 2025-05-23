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

import pydantic
import typing_extensions

from foundry_sdk import _core as core
from foundry_sdk import _errors as errors
from foundry_sdk.v2.aip_agents import errors as aip_agents_errors
from foundry_sdk.v2.aip_agents import models as aip_agents_models
from foundry_sdk.v2.core import models as core_models


class SessionTraceClient:
    """
    The API client for the SessionTrace Resource.

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

        self.with_streaming_response = _SessionTraceClientStreaming(self)
        self.with_raw_response = _SessionTraceClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        agent_rid: aip_agents_models.AgentRid,
        session_rid: aip_agents_models.SessionRid,
        session_trace_id: aip_agents_models.SessionTraceId,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> aip_agents_models.SessionTrace:
        """
        Get the trace of an Agent response. The trace lists the sequence of steps that an Agent took to arrive at
        an answer. For example, a trace may include steps such as context retrieval and tool calls. Clients should
        poll this endpoint to check the realtime progress of a response until the trace is completed.

        :param agent_rid: An RID identifying an AIP Agent created in [AIP Agent Studio](https://palantir.com/docs/foundry/agent-studio/overview/).
        :type agent_rid: AgentRid
        :param session_rid: The Resource Identifier (RID) of the conversation session.
        :type session_rid: SessionRid
        :param session_trace_id: The unique identifier for the trace.
        :type session_trace_id: SessionTraceId
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: aip_agents_models.SessionTrace

        :raises AgentNotFound: The given Agent could not be found.
        :raises SessionNotFound: The given Session could not be found.
        :raises SessionTraceNotFound: The given SessionTrace could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/aipAgents/agents/{agentRid}/sessions/{sessionRid}/sessionTraces/{sessionTraceId}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "agentRid": agent_rid,
                    "sessionRid": session_rid,
                    "sessionTraceId": session_trace_id,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=aip_agents_models.SessionTrace,
                request_timeout=request_timeout,
                throwable_errors={
                    "AgentNotFound": aip_agents_errors.AgentNotFound,
                    "SessionNotFound": aip_agents_errors.SessionNotFound,
                    "SessionTraceNotFound": aip_agents_errors.SessionTraceNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _SessionTraceClientRaw:
    def __init__(self, client: SessionTraceClient) -> None:
        def get(_: aip_agents_models.SessionTrace): ...

        self.get = core.with_raw_response(get, client.get)


class _SessionTraceClientStreaming:
    def __init__(self, client: SessionTraceClient) -> None:
        def get(_: aip_agents_models.SessionTrace): ...

        self.get = core.with_streaming_response(get, client.get)


class AsyncSessionTraceClient:
    """
    The API client for the SessionTrace Resource.

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

        self.with_streaming_response = _AsyncSessionTraceClientStreaming(self)
        self.with_raw_response = _AsyncSessionTraceClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        agent_rid: aip_agents_models.AgentRid,
        session_rid: aip_agents_models.SessionRid,
        session_trace_id: aip_agents_models.SessionTraceId,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[aip_agents_models.SessionTrace]:
        """
        Get the trace of an Agent response. The trace lists the sequence of steps that an Agent took to arrive at
        an answer. For example, a trace may include steps such as context retrieval and tool calls. Clients should
        poll this endpoint to check the realtime progress of a response until the trace is completed.

        :param agent_rid: An RID identifying an AIP Agent created in [AIP Agent Studio](https://palantir.com/docs/foundry/agent-studio/overview/).
        :type agent_rid: AgentRid
        :param session_rid: The Resource Identifier (RID) of the conversation session.
        :type session_rid: SessionRid
        :param session_trace_id: The unique identifier for the trace.
        :type session_trace_id: SessionTraceId
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[aip_agents_models.SessionTrace]

        :raises AgentNotFound: The given Agent could not be found.
        :raises SessionNotFound: The given Session could not be found.
        :raises SessionTraceNotFound: The given SessionTrace could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/aipAgents/agents/{agentRid}/sessions/{sessionRid}/sessionTraces/{sessionTraceId}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "agentRid": agent_rid,
                    "sessionRid": session_rid,
                    "sessionTraceId": session_trace_id,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=aip_agents_models.SessionTrace,
                request_timeout=request_timeout,
                throwable_errors={
                    "AgentNotFound": aip_agents_errors.AgentNotFound,
                    "SessionNotFound": aip_agents_errors.SessionNotFound,
                    "SessionTraceNotFound": aip_agents_errors.SessionTraceNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _AsyncSessionTraceClientRaw:
    def __init__(self, client: AsyncSessionTraceClient) -> None:
        def get(_: aip_agents_models.SessionTrace): ...

        self.get = core.async_with_raw_response(get, client.get)


class _AsyncSessionTraceClientStreaming:
    def __init__(self, client: AsyncSessionTraceClient) -> None:
        def get(_: aip_agents_models.SessionTrace): ...

        self.get = core.async_with_streaming_response(get, client.get)
