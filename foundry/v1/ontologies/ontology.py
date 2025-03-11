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

from foundry import _core as core
from foundry import _errors as errors
from foundry.v1.ontologies import models as ontologies_models


class OntologyClient:
    """
    The API client for the Ontology Resource.

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
        self.with_streaming_response = _OntologyClientStreaming(
            auth=auth, hostname=hostname, config=config
        )
        self.with_raw_response = _OntologyClientRaw(auth=auth, hostname=hostname, config=config)

    @cached_property
    def ActionType(self):
        from foundry.v1.ontologies.action_type import ActionTypeClient

        return ActionTypeClient(
            auth=self._auth,
            hostname=self._hostname,
            config=self._config,
        )

    @cached_property
    def ObjectType(self):
        from foundry.v1.ontologies.object_type import ObjectTypeClient

        return ObjectTypeClient(
            auth=self._auth,
            hostname=self._hostname,
            config=self._config,
        )

    @cached_property
    def QueryType(self):
        from foundry.v1.ontologies.query_type import QueryTypeClient

        return QueryTypeClient(
            auth=self._auth,
            hostname=self._hostname,
            config=self._config,
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        ontology_rid: ontologies_models.OntologyRid,
        *,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> ontologies_models.Ontology:
        """
        Gets a specific ontology with the given Ontology RID.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

        :param ontology_rid: The unique Resource Identifier (RID) of the Ontology. To look up your Ontology RID, please use the **List ontologies** endpoint or check the **Ontology Manager**.
        :type ontology_rid: OntologyRid
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ontologies_models.Ontology
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v1/ontologies/{ontologyRid}",
                query_params={},
                path_params={
                    "ontologyRid": ontology_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ontologies_models.Ontology,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        ).decode()

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def list(
        self,
        *,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> ontologies_models.ListOntologiesResponse:
        """
        Lists the Ontologies visible to the current user.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ontologies_models.ListOntologiesResponse
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v1/ontologies",
                query_params={},
                path_params={},
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ontologies_models.ListOntologiesResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        ).decode()


class _OntologyClientRaw:
    """
    The API client for the Ontology Resource.

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
    def get(
        self,
        ontology_rid: ontologies_models.OntologyRid,
        *,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[ontologies_models.Ontology]:
        """
        Gets a specific ontology with the given Ontology RID.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

        :param ontology_rid: The unique Resource Identifier (RID) of the Ontology. To look up your Ontology RID, please use the **List ontologies** endpoint or check the **Ontology Manager**.
        :type ontology_rid: OntologyRid
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[ontologies_models.Ontology]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v1/ontologies/{ontologyRid}",
                query_params={},
                path_params={
                    "ontologyRid": ontology_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ontologies_models.Ontology,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def list(
        self,
        *,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[ontologies_models.ListOntologiesResponse]:
        """
        Lists the Ontologies visible to the current user.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[ontologies_models.ListOntologiesResponse]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v1/ontologies",
                query_params={},
                path_params={},
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ontologies_models.ListOntologiesResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )


class _OntologyClientStreaming:
    """
    The API client for the Ontology Resource.

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
    def get(
        self,
        ontology_rid: ontologies_models.OntologyRid,
        *,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[ontologies_models.Ontology]:
        """
        Gets a specific ontology with the given Ontology RID.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

        :param ontology_rid: The unique Resource Identifier (RID) of the Ontology. To look up your Ontology RID, please use the **List ontologies** endpoint or check the **Ontology Manager**.
        :type ontology_rid: OntologyRid
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[ontologies_models.Ontology]
        """

        return self._api_client.stream_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v1/ontologies/{ontologyRid}",
                query_params={},
                path_params={
                    "ontologyRid": ontology_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ontologies_models.Ontology,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def list(
        self,
        *,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[ontologies_models.ListOntologiesResponse]:
        """
        Lists the Ontologies visible to the current user.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[ontologies_models.ListOntologiesResponse]
        """

        return self._api_client.stream_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v1/ontologies",
                query_params={},
                path_params={},
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ontologies_models.ListOntologiesResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )
