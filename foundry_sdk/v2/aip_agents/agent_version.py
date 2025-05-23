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


class AgentVersionClient:
    """
    The API client for the AgentVersion Resource.

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

        self.with_streaming_response = _AgentVersionClientStreaming(self)
        self.with_raw_response = _AgentVersionClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        agent_rid: aip_agents_models.AgentRid,
        agent_version_string: aip_agents_models.AgentVersionString,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> aip_agents_models.AgentVersion:
        """
        Get version details for an AIP Agent.
        :param agent_rid: An RID identifying an AIP Agent created in [AIP Agent Studio](https://palantir.com/docs/foundry/agent-studio/overview/).
        :type agent_rid: AgentRid
        :param agent_version_string: The semantic version of the Agent, formatted as "majorVersion.minorVersion".
        :type agent_version_string: AgentVersionString
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: aip_agents_models.AgentVersion

        :raises AgentNotFound: The given Agent could not be found.
        :raises AgentVersionNotFound: The given AgentVersion could not be found.
        :raises InvalidAgentVersion: The provided version string is not a valid format for an Agent version.
        :raises NoPublishedAgentVersion: Failed to retrieve the latest published version of the Agent because the Agent has no published versions. Try publishing the Agent in AIP Agent Studio to use the latest published version, or specify the version of the Agent to use.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/aipAgents/agents/{agentRid}/agentVersions/{agentVersionString}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "agentRid": agent_rid,
                    "agentVersionString": agent_version_string,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=aip_agents_models.AgentVersion,
                request_timeout=request_timeout,
                throwable_errors={
                    "AgentNotFound": aip_agents_errors.AgentNotFound,
                    "AgentVersionNotFound": aip_agents_errors.AgentVersionNotFound,
                    "InvalidAgentVersion": aip_agents_errors.InvalidAgentVersion,
                    "NoPublishedAgentVersion": aip_agents_errors.NoPublishedAgentVersion,
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
    ) -> core.ResourceIterator[aip_agents_models.AgentVersion]:
        """
        List all versions for an AIP Agent.
        Versions are returned in descending order, by most recent versions first.

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
        :rtype: core.ResourceIterator[aip_agents_models.AgentVersion]

        :raises AgentNotFound: The given Agent could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/aipAgents/agents/{agentRid}/agentVersions",
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
                response_type=aip_agents_models.ListAgentVersionsResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "AgentNotFound": aip_agents_errors.AgentNotFound,
                },
                response_mode=_sdk_internal.get("response_mode", "ITERATOR"),
            ),
        )


class _AgentVersionClientRaw:
    def __init__(self, client: AgentVersionClient) -> None:
        def get(_: aip_agents_models.AgentVersion): ...
        def list(_: aip_agents_models.ListAgentVersionsResponse): ...

        self.get = core.with_raw_response(get, client.get)
        self.list = core.with_raw_response(list, client.list)


class _AgentVersionClientStreaming:
    def __init__(self, client: AgentVersionClient) -> None:
        def get(_: aip_agents_models.AgentVersion): ...
        def list(_: aip_agents_models.ListAgentVersionsResponse): ...

        self.get = core.with_streaming_response(get, client.get)
        self.list = core.with_streaming_response(list, client.list)


class AsyncAgentVersionClient:
    """
    The API client for the AgentVersion Resource.

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

        self.with_streaming_response = _AsyncAgentVersionClientStreaming(self)
        self.with_raw_response = _AsyncAgentVersionClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        agent_rid: aip_agents_models.AgentRid,
        agent_version_string: aip_agents_models.AgentVersionString,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[aip_agents_models.AgentVersion]:
        """
        Get version details for an AIP Agent.
        :param agent_rid: An RID identifying an AIP Agent created in [AIP Agent Studio](https://palantir.com/docs/foundry/agent-studio/overview/).
        :type agent_rid: AgentRid
        :param agent_version_string: The semantic version of the Agent, formatted as "majorVersion.minorVersion".
        :type agent_version_string: AgentVersionString
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[aip_agents_models.AgentVersion]

        :raises AgentNotFound: The given Agent could not be found.
        :raises AgentVersionNotFound: The given AgentVersion could not be found.
        :raises InvalidAgentVersion: The provided version string is not a valid format for an Agent version.
        :raises NoPublishedAgentVersion: Failed to retrieve the latest published version of the Agent because the Agent has no published versions. Try publishing the Agent in AIP Agent Studio to use the latest published version, or specify the version of the Agent to use.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/aipAgents/agents/{agentRid}/agentVersions/{agentVersionString}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "agentRid": agent_rid,
                    "agentVersionString": agent_version_string,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=aip_agents_models.AgentVersion,
                request_timeout=request_timeout,
                throwable_errors={
                    "AgentNotFound": aip_agents_errors.AgentNotFound,
                    "AgentVersionNotFound": aip_agents_errors.AgentVersionNotFound,
                    "InvalidAgentVersion": aip_agents_errors.InvalidAgentVersion,
                    "NoPublishedAgentVersion": aip_agents_errors.NoPublishedAgentVersion,
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
    ) -> core.AsyncResourceIterator[aip_agents_models.AgentVersion]:
        """
        List all versions for an AIP Agent.
        Versions are returned in descending order, by most recent versions first.

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
        :rtype: core.AsyncResourceIterator[aip_agents_models.AgentVersion]

        :raises AgentNotFound: The given Agent could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/aipAgents/agents/{agentRid}/agentVersions",
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
                response_type=aip_agents_models.ListAgentVersionsResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "AgentNotFound": aip_agents_errors.AgentNotFound,
                },
                response_mode=_sdk_internal.get("response_mode", "ITERATOR"),
            ),
        )


class _AsyncAgentVersionClientRaw:
    def __init__(self, client: AsyncAgentVersionClient) -> None:
        def get(_: aip_agents_models.AgentVersion): ...
        def list(_: aip_agents_models.ListAgentVersionsResponse): ...

        self.get = core.async_with_raw_response(get, client.get)
        self.list = core.async_with_raw_response(list, client.list)


class _AsyncAgentVersionClientStreaming:
    def __init__(self, client: AsyncAgentVersionClient) -> None:
        def get(_: aip_agents_models.AgentVersion): ...
        def list(_: aip_agents_models.ListAgentVersionsResponse): ...

        self.get = core.async_with_streaming_response(get, client.get)
        self.list = core.async_with_streaming_response(list, client.list)
