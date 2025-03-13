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
import warnings
from functools import cached_property

import pydantic
import typing_extensions

from foundry import _core as core
from foundry import _errors as errors
from foundry.v2.aip_agents import errors as aip_agents_errors
from foundry.v2.aip_agents import models as aip_agents_models
from foundry.v2.core import models as core_models


class AgentClient:
    """
    The API client for the Agent Resource.

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

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def all_sessions(
        self,
        *,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ResourceIterator[aip_agents_models.Session]:
        """
        List all conversation sessions between the calling user and all accessible Agents that were created by this client.
        Sessions are returned in order of most recently updated first.

        :param page_size: The maximum number of sessions to return in a single page. The maximum allowed value is 100. Defaults to 100 if not specified.
        :type page_size: Optional[PageSize]
        :param page_token:
        :type page_token: Optional[PageToken]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ResourceIterator[aip_agents_models.Session]

        :raises ListSessionsForAgentsPermissionDenied: Could not allSessions the Agent.
        """

        return self._api_client.iterate_api(
            core.RequestInfo(
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
                response_type=aip_agents_models.AgentsSessionsPage,
                request_timeout=request_timeout,
                throwable_errors={
                    "ListSessionsForAgentsPermissionDenied": aip_agents_errors.ListSessionsForAgentsPermissionDenied,
                },
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def all_sessions_page(
        self,
        *,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> aip_agents_models.AgentsSessionsPage:
        """
        List all conversation sessions between the calling user and all accessible Agents that were created by this client.
        Sessions are returned in order of most recently updated first.

        :param page_size: The maximum number of sessions to return in a single page. The maximum allowed value is 100. Defaults to 100 if not specified.
        :type page_size: Optional[PageSize]
        :param page_token:
        :type page_token: Optional[PageToken]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: aip_agents_models.AgentsSessionsPage

        :raises ListSessionsForAgentsPermissionDenied: Could not allSessions the Agent.
        """

        warnings.warn(
            "The client.aip_agents.Agent.all_sessions_page(...) method has been deprecated. Please use client.aip_agents.Agent.all_sessions(...) instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        return self._api_client.call_api(
            core.RequestInfo(
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
                response_type=aip_agents_models.AgentsSessionsPage,
                request_timeout=request_timeout,
                throwable_errors={
                    "ListSessionsForAgentsPermissionDenied": aip_agents_errors.ListSessionsForAgentsPermissionDenied,
                },
            ),
        ).decode()

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        agent_rid: aip_agents_models.AgentRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        version: typing.Optional[aip_agents_models.AgentVersionString] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> aip_agents_models.Agent:
        """
        Get details for an AIP Agent.
        :param agent_rid: An RID identifying an AIP Agent created in [AIP Agent Studio](/docs/foundry/agent-studio/overview/).
        :type agent_rid: AgentRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param version: The version of the Agent to retrieve. If not specified, the latest published version will be returned.
        :type version: Optional[AgentVersionString]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: aip_agents_models.Agent

        :raises AgentNotFound: The given Agent could not be found.
        :raises AgentVersionNotFound: The given AgentVersion could not be found.
        :raises InvalidAgentVersion: The provided version string is not a valid format for an Agent version.
        :raises NoPublishedAgentVersion: Failed to retrieve the latest published version of the Agent because the Agent has no published versions. Try publishing the Agent in AIP Agent Studio to use the latest published version, or specify the version of the Agent to use.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                response_type=aip_agents_models.Agent,
                request_timeout=request_timeout,
                throwable_errors={
                    "AgentNotFound": aip_agents_errors.AgentNotFound,
                    "AgentVersionNotFound": aip_agents_errors.AgentVersionNotFound,
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
        auth: core.Auth,
        hostname: str,
        config: typing.Optional[core.Config] = None,
    ):
        self._auth = auth
        self._hostname = hostname
        self._config = config
        self._api_client = core.ApiClient(auth=auth, hostname=hostname, config=config)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def all_sessions(
        self,
        *,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[aip_agents_models.AgentsSessionsPage]:
        """
        List all conversation sessions between the calling user and all accessible Agents that were created by this client.
        Sessions are returned in order of most recently updated first.

        :param page_size: The maximum number of sessions to return in a single page. The maximum allowed value is 100. Defaults to 100 if not specified.
        :type page_size: Optional[PageSize]
        :param page_token:
        :type page_token: Optional[PageToken]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[aip_agents_models.AgentsSessionsPage]

        :raises ListSessionsForAgentsPermissionDenied: Could not allSessions the Agent.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                response_type=aip_agents_models.AgentsSessionsPage,
                request_timeout=request_timeout,
                throwable_errors={
                    "ListSessionsForAgentsPermissionDenied": aip_agents_errors.ListSessionsForAgentsPermissionDenied,
                },
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def all_sessions_page(
        self,
        *,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[aip_agents_models.AgentsSessionsPage]:
        """
        List all conversation sessions between the calling user and all accessible Agents that were created by this client.
        Sessions are returned in order of most recently updated first.

        :param page_size: The maximum number of sessions to return in a single page. The maximum allowed value is 100. Defaults to 100 if not specified.
        :type page_size: Optional[PageSize]
        :param page_token:
        :type page_token: Optional[PageToken]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[aip_agents_models.AgentsSessionsPage]

        :raises ListSessionsForAgentsPermissionDenied: Could not allSessions the Agent.
        """

        warnings.warn(
            "The client.aip_agents.Agent.all_sessions_page(...) method has been deprecated. Please use client.aip_agents.Agent.all_sessions(...) instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        return self._api_client.call_api(
            core.RequestInfo(
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
                response_type=aip_agents_models.AgentsSessionsPage,
                request_timeout=request_timeout,
                throwable_errors={
                    "ListSessionsForAgentsPermissionDenied": aip_agents_errors.ListSessionsForAgentsPermissionDenied,
                },
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        agent_rid: aip_agents_models.AgentRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        version: typing.Optional[aip_agents_models.AgentVersionString] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[aip_agents_models.Agent]:
        """
        Get details for an AIP Agent.
        :param agent_rid: An RID identifying an AIP Agent created in [AIP Agent Studio](/docs/foundry/agent-studio/overview/).
        :type agent_rid: AgentRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param version: The version of the Agent to retrieve. If not specified, the latest published version will be returned.
        :type version: Optional[AgentVersionString]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[aip_agents_models.Agent]

        :raises AgentNotFound: The given Agent could not be found.
        :raises AgentVersionNotFound: The given AgentVersion could not be found.
        :raises InvalidAgentVersion: The provided version string is not a valid format for an Agent version.
        :raises NoPublishedAgentVersion: Failed to retrieve the latest published version of the Agent because the Agent has no published versions. Try publishing the Agent in AIP Agent Studio to use the latest published version, or specify the version of the Agent to use.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                response_type=aip_agents_models.Agent,
                request_timeout=request_timeout,
                throwable_errors={
                    "AgentNotFound": aip_agents_errors.AgentNotFound,
                    "AgentVersionNotFound": aip_agents_errors.AgentVersionNotFound,
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
        auth: core.Auth,
        hostname: str,
        config: typing.Optional[core.Config] = None,
    ):
        self._auth = auth
        self._hostname = hostname
        self._config = config
        self._api_client = core.ApiClient(auth=auth, hostname=hostname, config=config)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def all_sessions(
        self,
        *,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[aip_agents_models.AgentsSessionsPage]:
        """
        List all conversation sessions between the calling user and all accessible Agents that were created by this client.
        Sessions are returned in order of most recently updated first.

        :param page_size: The maximum number of sessions to return in a single page. The maximum allowed value is 100. Defaults to 100 if not specified.
        :type page_size: Optional[PageSize]
        :param page_token:
        :type page_token: Optional[PageToken]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[aip_agents_models.AgentsSessionsPage]

        :raises ListSessionsForAgentsPermissionDenied: Could not allSessions the Agent.
        """

        return self._api_client.stream_api(
            core.RequestInfo(
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
                response_type=aip_agents_models.AgentsSessionsPage,
                request_timeout=request_timeout,
                throwable_errors={
                    "ListSessionsForAgentsPermissionDenied": aip_agents_errors.ListSessionsForAgentsPermissionDenied,
                },
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def all_sessions_page(
        self,
        *,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[aip_agents_models.AgentsSessionsPage]:
        """
        List all conversation sessions between the calling user and all accessible Agents that were created by this client.
        Sessions are returned in order of most recently updated first.

        :param page_size: The maximum number of sessions to return in a single page. The maximum allowed value is 100. Defaults to 100 if not specified.
        :type page_size: Optional[PageSize]
        :param page_token:
        :type page_token: Optional[PageToken]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[aip_agents_models.AgentsSessionsPage]

        :raises ListSessionsForAgentsPermissionDenied: Could not allSessions the Agent.
        """

        warnings.warn(
            "The client.aip_agents.Agent.all_sessions_page(...) method has been deprecated. Please use client.aip_agents.Agent.all_sessions(...) instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        return self._api_client.stream_api(
            core.RequestInfo(
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
                response_type=aip_agents_models.AgentsSessionsPage,
                request_timeout=request_timeout,
                throwable_errors={
                    "ListSessionsForAgentsPermissionDenied": aip_agents_errors.ListSessionsForAgentsPermissionDenied,
                },
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        agent_rid: aip_agents_models.AgentRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        version: typing.Optional[aip_agents_models.AgentVersionString] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[aip_agents_models.Agent]:
        """
        Get details for an AIP Agent.
        :param agent_rid: An RID identifying an AIP Agent created in [AIP Agent Studio](/docs/foundry/agent-studio/overview/).
        :type agent_rid: AgentRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param version: The version of the Agent to retrieve. If not specified, the latest published version will be returned.
        :type version: Optional[AgentVersionString]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[aip_agents_models.Agent]

        :raises AgentNotFound: The given Agent could not be found.
        :raises AgentVersionNotFound: The given AgentVersion could not be found.
        :raises InvalidAgentVersion: The provided version string is not a valid format for an Agent version.
        :raises NoPublishedAgentVersion: Failed to retrieve the latest published version of the Agent because the Agent has no published versions. Try publishing the Agent in AIP Agent Studio to use the latest published version, or specify the version of the Agent to use.
        """

        return self._api_client.stream_api(
            core.RequestInfo(
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
                response_type=aip_agents_models.Agent,
                request_timeout=request_timeout,
                throwable_errors={
                    "AgentNotFound": aip_agents_errors.AgentNotFound,
                    "AgentVersionNotFound": aip_agents_errors.AgentVersionNotFound,
                    "InvalidAgentVersion": aip_agents_errors.InvalidAgentVersion,
                    "NoPublishedAgentVersion": aip_agents_errors.NoPublishedAgentVersion,
                },
            ),
        )
