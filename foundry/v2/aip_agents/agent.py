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
from typing import Optional

import pydantic
from typing_extensions import Annotated

from foundry._core import ApiClient
from foundry._core import ApiResponse
from foundry._core import Auth
from foundry._core import Config
from foundry._core import RequestInfo
from foundry._core import ResourceIterator
from foundry._core import StreamingContextManager
from foundry._core.utils import maybe_ignore_preview
from foundry._errors import handle_unexpected
from foundry.v2.aip_agents import errors as aip_agents_errors
from foundry.v2.aip_agents.models._agent import Agent
from foundry.v2.aip_agents.models._agent_rid import AgentRid
from foundry.v2.aip_agents.models._agent_version_string import AgentVersionString
from foundry.v2.aip_agents.models._agents_sessions_page import AgentsSessionsPage
from foundry.v2.aip_agents.models._session import Session
from foundry.v2.core.models._page_size import PageSize
from foundry.v2.core.models._page_token import PageToken
from foundry.v2.core.models._preview_mode import PreviewMode


class AgentClient:
    """
    The API client for the Agent Resource.

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
        self.with_streaming_response = _AgentClientStreaming(
            auth=auth, hostname=hostname, config=config
        )
        self.with_raw_response = _AgentClientRaw(auth=auth, hostname=hostname, config=config)

    @cached_property
    def AgentVersion(self):
        from foundry.v2.aip_agents.agent_version import AgentVersionClient

        return AgentVersionClient(
            auth=self._auth,
            hostname=self._hostname,
            config=self._config,
        )

    @cached_property
    def Session(self):
        from foundry.v2.aip_agents.session import SessionClient

        return SessionClient(
            auth=self._auth,
            hostname=self._hostname,
            config=self._config,
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def all_sessions(
        self,
        *,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ResourceIterator[Session]:
        """
        List all conversation sessions between the calling user and all accessible Agents that were created by this client.
        Sessions are returned in order of most recently updated first.

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

        :raises ListSessionsForAgentsPermissionDenied: Could not allSessions the Agent.
        """

        return self._api_client.iterate_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/aipAgents/agents/allSessions",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=AgentsSessionsPage,
                request_timeout=request_timeout,
                throwable_errors={
                    "ListSessionsForAgentsPermissionDenied": aip_agents_errors.ListSessionsForAgentsPermissionDenied,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def all_sessions_page(
        self,
        *,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> AgentsSessionsPage:
        """
        List all conversation sessions between the calling user and all accessible Agents that were created by this client.
        Sessions are returned in order of most recently updated first.

        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param page_token: pageToken
        :type page_token: Optional[PageToken]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: AgentsSessionsPage

        :raises ListSessionsForAgentsPermissionDenied: Could not allSessions the Agent.
        """

        warnings.warn(
            "The client.aip_agents.Agent.all_sessions_page(...) method has been deprecated. Please use client.aip_agents.Agent.all_sessions(...) instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/aipAgents/agents/allSessions",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=AgentsSessionsPage,
                request_timeout=request_timeout,
                throwable_errors={
                    "ListSessionsForAgentsPermissionDenied": aip_agents_errors.ListSessionsForAgentsPermissionDenied,
                },
            ),
        ).decode()

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def get(
        self,
        agent_rid: AgentRid,
        *,
        preview: Optional[PreviewMode] = None,
        version: Optional[AgentVersionString] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> Agent:
        """
        Get details for an AIP Agent.
        :param agent_rid: agentRid
        :type agent_rid: AgentRid
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param version: version
        :type version: Optional[AgentVersionString]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: Agent

        :raises AgentNotFound: The given Agent could not be found.
        :raises InvalidAgentVersion: The provided version string is not a valid format for an Agent version.
        :raises NoPublishedAgentVersion: Failed to retrieve the latest published version of the Agent because the Agent has no published versions. Try publishing the Agent in AIP Agent Studio to use the latest published version, or specify the version of the Agent to use.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/aipAgents/agents/{agentRid}",
                query_params={
                    "preview": preview,
                    "version": version,
                },
                path_params={
                    "agentRid": agent_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=Agent,
                request_timeout=request_timeout,
                throwable_errors={
                    "AgentNotFound": aip_agents_errors.AgentNotFound,
                    "InvalidAgentVersion": aip_agents_errors.InvalidAgentVersion,
                    "NoPublishedAgentVersion": aip_agents_errors.NoPublishedAgentVersion,
                },
            ),
        ).decode()


class _AgentClientRaw:
    """
    The API client for the Agent Resource.

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
    def all_sessions(
        self,
        *,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[AgentsSessionsPage]:
        """
        List all conversation sessions between the calling user and all accessible Agents that were created by this client.
        Sessions are returned in order of most recently updated first.

        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param page_token: pageToken
        :type page_token: Optional[PageToken]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[AgentsSessionsPage]

        :raises ListSessionsForAgentsPermissionDenied: Could not allSessions the Agent.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/aipAgents/agents/allSessions",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=AgentsSessionsPage,
                request_timeout=request_timeout,
                throwable_errors={
                    "ListSessionsForAgentsPermissionDenied": aip_agents_errors.ListSessionsForAgentsPermissionDenied,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def all_sessions_page(
        self,
        *,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[AgentsSessionsPage]:
        """
        List all conversation sessions between the calling user and all accessible Agents that were created by this client.
        Sessions are returned in order of most recently updated first.

        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param page_token: pageToken
        :type page_token: Optional[PageToken]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[AgentsSessionsPage]

        :raises ListSessionsForAgentsPermissionDenied: Could not allSessions the Agent.
        """

        warnings.warn(
            "The client.aip_agents.Agent.all_sessions_page(...) method has been deprecated. Please use client.aip_agents.Agent.all_sessions(...) instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/aipAgents/agents/allSessions",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=AgentsSessionsPage,
                request_timeout=request_timeout,
                throwable_errors={
                    "ListSessionsForAgentsPermissionDenied": aip_agents_errors.ListSessionsForAgentsPermissionDenied,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def get(
        self,
        agent_rid: AgentRid,
        *,
        preview: Optional[PreviewMode] = None,
        version: Optional[AgentVersionString] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[Agent]:
        """
        Get details for an AIP Agent.
        :param agent_rid: agentRid
        :type agent_rid: AgentRid
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param version: version
        :type version: Optional[AgentVersionString]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[Agent]

        :raises AgentNotFound: The given Agent could not be found.
        :raises InvalidAgentVersion: The provided version string is not a valid format for an Agent version.
        :raises NoPublishedAgentVersion: Failed to retrieve the latest published version of the Agent because the Agent has no published versions. Try publishing the Agent in AIP Agent Studio to use the latest published version, or specify the version of the Agent to use.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/aipAgents/agents/{agentRid}",
                query_params={
                    "preview": preview,
                    "version": version,
                },
                path_params={
                    "agentRid": agent_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=Agent,
                request_timeout=request_timeout,
                throwable_errors={
                    "AgentNotFound": aip_agents_errors.AgentNotFound,
                    "InvalidAgentVersion": aip_agents_errors.InvalidAgentVersion,
                    "NoPublishedAgentVersion": aip_agents_errors.NoPublishedAgentVersion,
                },
            ),
        )


class _AgentClientStreaming:
    """
    The API client for the Agent Resource.

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
    def all_sessions(
        self,
        *,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[AgentsSessionsPage]:
        """
        List all conversation sessions between the calling user and all accessible Agents that were created by this client.
        Sessions are returned in order of most recently updated first.

        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param page_token: pageToken
        :type page_token: Optional[PageToken]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[AgentsSessionsPage]

        :raises ListSessionsForAgentsPermissionDenied: Could not allSessions the Agent.
        """

        return self._api_client.stream_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/aipAgents/agents/allSessions",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=AgentsSessionsPage,
                request_timeout=request_timeout,
                throwable_errors={
                    "ListSessionsForAgentsPermissionDenied": aip_agents_errors.ListSessionsForAgentsPermissionDenied,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def all_sessions_page(
        self,
        *,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[AgentsSessionsPage]:
        """
        List all conversation sessions between the calling user and all accessible Agents that were created by this client.
        Sessions are returned in order of most recently updated first.

        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param page_token: pageToken
        :type page_token: Optional[PageToken]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[AgentsSessionsPage]

        :raises ListSessionsForAgentsPermissionDenied: Could not allSessions the Agent.
        """

        warnings.warn(
            "The client.aip_agents.Agent.all_sessions_page(...) method has been deprecated. Please use client.aip_agents.Agent.all_sessions(...) instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        return self._api_client.stream_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/aipAgents/agents/allSessions",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=AgentsSessionsPage,
                request_timeout=request_timeout,
                throwable_errors={
                    "ListSessionsForAgentsPermissionDenied": aip_agents_errors.ListSessionsForAgentsPermissionDenied,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def get(
        self,
        agent_rid: AgentRid,
        *,
        preview: Optional[PreviewMode] = None,
        version: Optional[AgentVersionString] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[Agent]:
        """
        Get details for an AIP Agent.
        :param agent_rid: agentRid
        :type agent_rid: AgentRid
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param version: version
        :type version: Optional[AgentVersionString]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[Agent]

        :raises AgentNotFound: The given Agent could not be found.
        :raises InvalidAgentVersion: The provided version string is not a valid format for an Agent version.
        :raises NoPublishedAgentVersion: Failed to retrieve the latest published version of the Agent because the Agent has no published versions. Try publishing the Agent in AIP Agent Studio to use the latest published version, or specify the version of the Agent to use.
        """

        return self._api_client.stream_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/aipAgents/agents/{agentRid}",
                query_params={
                    "preview": preview,
                    "version": version,
                },
                path_params={
                    "agentRid": agent_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=Agent,
                request_timeout=request_timeout,
                throwable_errors={
                    "AgentNotFound": aip_agents_errors.AgentNotFound,
                    "InvalidAgentVersion": aip_agents_errors.InvalidAgentVersion,
                    "NoPublishedAgentVersion": aip_agents_errors.NoPublishedAgentVersion,
                },
            ),
        )
