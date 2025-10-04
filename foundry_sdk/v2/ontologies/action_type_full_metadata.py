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
from foundry_sdk.v2.core import models as core_models
from foundry_sdk.v2.ontologies import models as ontologies_models


class ActionTypeFullMetadataClient:
    """
    The API client for the ActionTypeFullMetadata Resource.

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

        self.with_streaming_response = _ActionTypeFullMetadataClientStreaming(self)
        self.with_raw_response = _ActionTypeFullMetadataClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        action_type: ontologies_models.ActionTypeApiName,
        *,
        branch: typing.Optional[core_models.FoundryBranch] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> ontologies_models.ActionTypeFullMetadata:
        """
        Gets the full metadata associated with an action type.

        :param ontology: The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.
        :type ontology: OntologyIdentifier
        :param action_type: The name of the action type in the API.
        :type action_type: ActionTypeApiName
        :param branch: The Foundry branch to load the action type definition from. If not specified, the default branch will be used.
        :type branch: Optional[FoundryBranch]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ontologies_models.ActionTypeFullMetadata
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/ontologies/{ontology}/actionTypes/{actionType}/fullMetadata",
                query_params={
                    "branch": branch,
                },
                path_params={
                    "ontology": ontology,
                    "actionType": action_type,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=ontologies_models.ActionTypeFullMetadata,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _ActionTypeFullMetadataClientRaw:
    def __init__(self, client: ActionTypeFullMetadataClient) -> None:
        def get(_: ontologies_models.ActionTypeFullMetadata): ...

        self.get = core.with_raw_response(get, client.get)


class _ActionTypeFullMetadataClientStreaming:
    def __init__(self, client: ActionTypeFullMetadataClient) -> None:
        def get(_: ontologies_models.ActionTypeFullMetadata): ...

        self.get = core.with_streaming_response(get, client.get)


class AsyncActionTypeFullMetadataClient:
    """
    The API client for the ActionTypeFullMetadata Resource.

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

        self.with_streaming_response = _AsyncActionTypeFullMetadataClientStreaming(self)
        self.with_raw_response = _AsyncActionTypeFullMetadataClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        action_type: ontologies_models.ActionTypeApiName,
        *,
        branch: typing.Optional[core_models.FoundryBranch] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[ontologies_models.ActionTypeFullMetadata]:
        """
        Gets the full metadata associated with an action type.

        :param ontology: The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.
        :type ontology: OntologyIdentifier
        :param action_type: The name of the action type in the API.
        :type action_type: ActionTypeApiName
        :param branch: The Foundry branch to load the action type definition from. If not specified, the default branch will be used.
        :type branch: Optional[FoundryBranch]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[ontologies_models.ActionTypeFullMetadata]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/ontologies/{ontology}/actionTypes/{actionType}/fullMetadata",
                query_params={
                    "branch": branch,
                },
                path_params={
                    "ontology": ontology,
                    "actionType": action_type,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=ontologies_models.ActionTypeFullMetadata,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _AsyncActionTypeFullMetadataClientRaw:
    def __init__(self, client: AsyncActionTypeFullMetadataClient) -> None:
        def get(_: ontologies_models.ActionTypeFullMetadata): ...

        self.get = core.async_with_raw_response(get, client.get)


class _AsyncActionTypeFullMetadataClientStreaming:
    def __init__(self, client: AsyncActionTypeFullMetadataClient) -> None:
        def get(_: ontologies_models.ActionTypeFullMetadata): ...

        self.get = core.async_with_streaming_response(get, client.get)
