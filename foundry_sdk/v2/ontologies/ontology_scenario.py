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
from foundry_sdk.v2.ontologies import models as ontologies_models


class OntologyScenarioClient:
    """
    The API client for the OntologyScenario Resource.

    :param auth: Your auth configuration.
    :param hostname: The hostname supplier for resolving base URLs.
    :param config: Optionally specify the configuration for the HTTP session.
    """

    def __init__(
        self,
        auth: core.Auth,
        hostname: typing.Union[str, core.HostnameSupplier],
        config: typing.Optional[core.Config] = None,
    ):
        self._auth = auth
        if isinstance(hostname, core.HostnameSupplier):
            self._hostname_supplier = hostname
        else:
            self._hostname_supplier = core.create_hostname_supplier(hostname, config)
        self._hostname = self._hostname_supplier.get_hostname()
        self._config = config
        self._api_client = core.ApiClient(
            auth=auth, hostname=self._hostname_supplier, config=config
        )

        self.with_streaming_response = _OntologyScenarioClientStreaming(self)
        self.with_raw_response = _OntologyScenarioClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def create_scenario(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        *,
        base: typing.Optional[ontologies_models.OntologyBase] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> ontologies_models.CreateOntologyScenarioResponse:
        """
        Creates an ontology scenario.

        :param ontology:
        :type ontology: OntologyIdentifier
        :param base:
        :type base: Optional[OntologyBase]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ontologies_models.CreateOntologyScenarioResponse
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/ontologies/{ontology}/scenarios/create",
                query_params={},
                path_params={
                    "ontology": ontology,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body=ontologies_models.CreateOntologyScenarioRequest(
                    base=base,
                ),
                response_type=ontologies_models.CreateOntologyScenarioResponse,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _OntologyScenarioClientRaw:
    def __init__(self, client: OntologyScenarioClient) -> None:
        def create_scenario(_: ontologies_models.CreateOntologyScenarioResponse): ...

        self.create_scenario = core.with_raw_response(create_scenario, client.create_scenario)


class _OntologyScenarioClientStreaming:
    def __init__(self, client: OntologyScenarioClient) -> None:
        def create_scenario(_: ontologies_models.CreateOntologyScenarioResponse): ...

        self.create_scenario = core.with_streaming_response(create_scenario, client.create_scenario)


class AsyncOntologyScenarioClient:
    """
    The API client for the OntologyScenario Resource.

    :param auth: Your auth configuration.
    :param hostname: The hostname supplier for resolving base URLs.
    :param config: Optionally specify the configuration for the HTTP session.
    """

    def __init__(
        self,
        auth: core.Auth,
        hostname: typing.Union[str, core.HostnameSupplier],
        config: typing.Optional[core.Config] = None,
    ):
        self._auth = auth
        if isinstance(hostname, core.HostnameSupplier):
            self._hostname_supplier = hostname
        else:
            self._hostname_supplier = core.create_hostname_supplier(hostname, config)
        self._hostname = self._hostname_supplier.get_hostname()
        self._config = config
        self._api_client = core.AsyncApiClient(
            auth=auth, hostname=self._hostname_supplier, config=config
        )

        self.with_streaming_response = _AsyncOntologyScenarioClientStreaming(self)
        self.with_raw_response = _AsyncOntologyScenarioClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def create_scenario(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        *,
        base: typing.Optional[ontologies_models.OntologyBase] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[ontologies_models.CreateOntologyScenarioResponse]:
        """
        Creates an ontology scenario.

        :param ontology:
        :type ontology: OntologyIdentifier
        :param base:
        :type base: Optional[OntologyBase]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[ontologies_models.CreateOntologyScenarioResponse]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/ontologies/{ontology}/scenarios/create",
                query_params={},
                path_params={
                    "ontology": ontology,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body=ontologies_models.CreateOntologyScenarioRequest(
                    base=base,
                ),
                response_type=ontologies_models.CreateOntologyScenarioResponse,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _AsyncOntologyScenarioClientRaw:
    def __init__(self, client: AsyncOntologyScenarioClient) -> None:
        def create_scenario(_: ontologies_models.CreateOntologyScenarioResponse): ...

        self.create_scenario = core.async_with_raw_response(create_scenario, client.create_scenario)


class _AsyncOntologyScenarioClientStreaming:
    def __init__(self, client: AsyncOntologyScenarioClient) -> None:
        def create_scenario(_: ontologies_models.CreateOntologyScenarioResponse): ...

        self.create_scenario = core.async_with_streaming_response(
            create_scenario, client.create_scenario
        )
