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
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> ontologies_models.CreateOntologyScenarioResponse:
        """
        Creates an ontology scenario.

        :param ontology:
        :type ontology: OntologyIdentifier
        :param base:
        :type base: Optional[OntologyBase]
        :param preview: A boolean flag that, when set to true, enables the use of beta features in preview mode.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ontologies_models.CreateOntologyScenarioResponse
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/ontologies/{ontology}/scenarios/create",
                query_params={
                    "preview": preview,
                },
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

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def list_scenario_edited_entity_types(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        scenario_rid: ontologies_models.OntologyScenarioRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> ontologies_models.ListScenarioEditedEntityTypesResponse:
        """
        Returns the object types and link types that have been modified within a given scenario.

        The response contains the list of object type API names that have been modified, and the list of
        many-to-many link types that have been modified, grouped by their source object type. One-to-many
        link type edits are surfaced as object edits on the object type that owns the foreign key property.

        :param ontology:
        :type ontology: OntologyIdentifier
        :param scenario_rid: The unique resource identifier of the scenario.
        :type scenario_rid: OntologyScenarioRid
        :param preview: A boolean flag that, when set to true, enables the use of beta features in preview mode.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ontologies_models.ListScenarioEditedEntityTypesResponse
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/ontologies/{ontology}/scenarios/{scenarioRid}/editedEntityTypes",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "ontology": ontology,
                    "scenarioRid": scenario_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=ontologies_models.ListScenarioEditedEntityTypesResponse,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def list_scenario_edited_link_types(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        scenario_rid: ontologies_models.OntologyScenarioRid,
        object_type: ontologies_models.ObjectTypeApiName,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> ontologies_models.ListScenarioEditedLinkTypesResponse:
        """
        Returns the list of outgoing links that have been modified within a given scenario for an object type.

        Note that only many-to-many link type are returned by this endpoint. One-to-many link type edits are
        surfaced as object edits on the object type that owns the foreign key property.

        :param ontology:
        :type ontology: OntologyIdentifier
        :param scenario_rid: The unique resource identifier of the scenario.
        :type scenario_rid: OntologyScenarioRid
        :param object_type: The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager** application.
        :type object_type: ObjectTypeApiName
        :param preview: A boolean flag that, when set to true, enables the use of beta features in preview mode.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ontologies_models.ListScenarioEditedLinkTypesResponse
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/ontologies/{ontology}/scenarios/{scenarioRid}/objectTypes/{objectType}/outgoingLinkTypes/edited",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "ontology": ontology,
                    "scenarioRid": scenario_rid,
                    "objectType": object_type,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=ontologies_models.ListScenarioEditedLinkTypesResponse,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def list_scenario_edited_links(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        scenario_rid: ontologies_models.OntologyScenarioRid,
        object_type: ontologies_models.ObjectTypeApiName,
        link_type: ontologies_models.LinkTypeApiName,
        *,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> core.ResourceIterator[ontologies_models.LinksFromObject]:
        """
        Returns the list of edited links within a given scenario for a specific object type and link type, grouped
        by source object. Only works for many-to-many link types. Only links where the user has permission to view
        both objects are returned.

        Each page may be smaller than the requested page size.

        :param ontology:
        :type ontology: OntologyIdentifier
        :param scenario_rid: The unique resource identifier of the scenario.
        :type scenario_rid: OntologyScenarioRid
        :param object_type: The API name of the object type.
        :type object_type: ObjectTypeApiName
        :param link_type: The API name of the link type.
        :type link_type: LinkTypeApiName
        :param page_size: The maximum number of links to return per page.
        :type page_size: Optional[PageSize]
        :param page_token: The page token to use for pagination.
        :type page_token: Optional[PageToken]
        :param preview: A boolean flag that, when set to true, enables the use of beta features in preview mode.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ResourceIterator[ontologies_models.LinksFromObject]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/ontologies/{ontology}/scenarios/{scenarioRid}/objects/{objectType}/links/{linkType}/edited",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
                    "preview": preview,
                },
                path_params={
                    "ontology": ontology,
                    "scenarioRid": scenario_rid,
                    "objectType": object_type,
                    "linkType": link_type,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=ontologies_models.ListScenarioEditedLinksResponse,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode", "ITERATOR"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def list_scenario_edited_object_types(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        scenario_rid: ontologies_models.OntologyScenarioRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> ontologies_models.ListScenarioEditedObjectTypesResponse:
        """
        Returns the list of object type API names that have been modified within a given scenario.

        :param ontology:
        :type ontology: OntologyIdentifier
        :param scenario_rid: The unique resource identifier of the scenario.
        :type scenario_rid: OntologyScenarioRid
        :param preview: A boolean flag that, when set to true, enables the use of beta features in preview mode.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ontologies_models.ListScenarioEditedObjectTypesResponse
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/ontologies/{ontology}/scenarios/{scenarioRid}/objectTypes/edited",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "ontology": ontology,
                    "scenarioRid": scenario_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=ontologies_models.ListScenarioEditedObjectTypesResponse,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def list_scenario_edited_objects(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        scenario_rid: ontologies_models.OntologyScenarioRid,
        object_type: ontologies_models.ObjectTypeApiName,
        *,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> core.ResourceIterator[ontologies_models.OntologyObjectV2]:
        """
        Returns the list of objects that have been edited within a given scenario for a specific object type.
        Only objects that the user has permission to view are returned.

        Each page may be smaller than the requested page size.

        :param ontology:
        :type ontology: OntologyIdentifier
        :param scenario_rid: The unique resource identifier of the scenario.
        :type scenario_rid: OntologyScenarioRid
        :param object_type: The API name of the object type.
        :type object_type: ObjectTypeApiName
        :param page_size: The maximum number of objects to return per page.
        :type page_size: Optional[PageSize]
        :param page_token: The page token to use for pagination.
        :type page_token: Optional[PageToken]
        :param preview: A boolean flag that, when set to true, enables the use of beta features in preview mode.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ResourceIterator[ontologies_models.OntologyObjectV2]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/ontologies/{ontology}/scenarios/{scenarioRid}/objects/{objectType}/edited",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
                    "preview": preview,
                },
                path_params={
                    "ontology": ontology,
                    "scenarioRid": scenario_rid,
                    "objectType": object_type,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=ontologies_models.ListScenarioEditedObjectsResponse,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode", "ITERATOR"),
            ),
        )


class _OntologyScenarioClientRaw:
    def __init__(self, client: OntologyScenarioClient) -> None:
        def create_scenario(_: ontologies_models.CreateOntologyScenarioResponse): ...
        def list_scenario_edited_entity_types(
            _: ontologies_models.ListScenarioEditedEntityTypesResponse,
        ): ...
        def list_scenario_edited_link_types(
            _: ontologies_models.ListScenarioEditedLinkTypesResponse,
        ): ...
        def list_scenario_edited_links(_: ontologies_models.ListScenarioEditedLinksResponse): ...
        def list_scenario_edited_object_types(
            _: ontologies_models.ListScenarioEditedObjectTypesResponse,
        ): ...
        def list_scenario_edited_objects(
            _: ontologies_models.ListScenarioEditedObjectsResponse,
        ): ...

        self.create_scenario = core.with_raw_response(create_scenario, client.create_scenario)
        self.list_scenario_edited_entity_types = core.with_raw_response(
            list_scenario_edited_entity_types, client.list_scenario_edited_entity_types
        )
        self.list_scenario_edited_link_types = core.with_raw_response(
            list_scenario_edited_link_types, client.list_scenario_edited_link_types
        )
        self.list_scenario_edited_links = core.with_raw_response(
            list_scenario_edited_links, client.list_scenario_edited_links
        )
        self.list_scenario_edited_object_types = core.with_raw_response(
            list_scenario_edited_object_types, client.list_scenario_edited_object_types
        )
        self.list_scenario_edited_objects = core.with_raw_response(
            list_scenario_edited_objects, client.list_scenario_edited_objects
        )


class _OntologyScenarioClientStreaming:
    def __init__(self, client: OntologyScenarioClient) -> None:
        def create_scenario(_: ontologies_models.CreateOntologyScenarioResponse): ...
        def list_scenario_edited_entity_types(
            _: ontologies_models.ListScenarioEditedEntityTypesResponse,
        ): ...
        def list_scenario_edited_link_types(
            _: ontologies_models.ListScenarioEditedLinkTypesResponse,
        ): ...
        def list_scenario_edited_links(_: ontologies_models.ListScenarioEditedLinksResponse): ...
        def list_scenario_edited_object_types(
            _: ontologies_models.ListScenarioEditedObjectTypesResponse,
        ): ...
        def list_scenario_edited_objects(
            _: ontologies_models.ListScenarioEditedObjectsResponse,
        ): ...

        self.create_scenario = core.with_streaming_response(create_scenario, client.create_scenario)
        self.list_scenario_edited_entity_types = core.with_streaming_response(
            list_scenario_edited_entity_types, client.list_scenario_edited_entity_types
        )
        self.list_scenario_edited_link_types = core.with_streaming_response(
            list_scenario_edited_link_types, client.list_scenario_edited_link_types
        )
        self.list_scenario_edited_links = core.with_streaming_response(
            list_scenario_edited_links, client.list_scenario_edited_links
        )
        self.list_scenario_edited_object_types = core.with_streaming_response(
            list_scenario_edited_object_types, client.list_scenario_edited_object_types
        )
        self.list_scenario_edited_objects = core.with_streaming_response(
            list_scenario_edited_objects, client.list_scenario_edited_objects
        )


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
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[ontologies_models.CreateOntologyScenarioResponse]:
        """
        Creates an ontology scenario.

        :param ontology:
        :type ontology: OntologyIdentifier
        :param base:
        :type base: Optional[OntologyBase]
        :param preview: A boolean flag that, when set to true, enables the use of beta features in preview mode.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[ontologies_models.CreateOntologyScenarioResponse]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/ontologies/{ontology}/scenarios/create",
                query_params={
                    "preview": preview,
                },
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

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def list_scenario_edited_entity_types(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        scenario_rid: ontologies_models.OntologyScenarioRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[ontologies_models.ListScenarioEditedEntityTypesResponse]:
        """
        Returns the object types and link types that have been modified within a given scenario.

        The response contains the list of object type API names that have been modified, and the list of
        many-to-many link types that have been modified, grouped by their source object type. One-to-many
        link type edits are surfaced as object edits on the object type that owns the foreign key property.

        :param ontology:
        :type ontology: OntologyIdentifier
        :param scenario_rid: The unique resource identifier of the scenario.
        :type scenario_rid: OntologyScenarioRid
        :param preview: A boolean flag that, when set to true, enables the use of beta features in preview mode.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[ontologies_models.ListScenarioEditedEntityTypesResponse]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/ontologies/{ontology}/scenarios/{scenarioRid}/editedEntityTypes",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "ontology": ontology,
                    "scenarioRid": scenario_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=ontologies_models.ListScenarioEditedEntityTypesResponse,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def list_scenario_edited_link_types(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        scenario_rid: ontologies_models.OntologyScenarioRid,
        object_type: ontologies_models.ObjectTypeApiName,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[ontologies_models.ListScenarioEditedLinkTypesResponse]:
        """
        Returns the list of outgoing links that have been modified within a given scenario for an object type.

        Note that only many-to-many link type are returned by this endpoint. One-to-many link type edits are
        surfaced as object edits on the object type that owns the foreign key property.

        :param ontology:
        :type ontology: OntologyIdentifier
        :param scenario_rid: The unique resource identifier of the scenario.
        :type scenario_rid: OntologyScenarioRid
        :param object_type: The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager** application.
        :type object_type: ObjectTypeApiName
        :param preview: A boolean flag that, when set to true, enables the use of beta features in preview mode.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[ontologies_models.ListScenarioEditedLinkTypesResponse]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/ontologies/{ontology}/scenarios/{scenarioRid}/objectTypes/{objectType}/outgoingLinkTypes/edited",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "ontology": ontology,
                    "scenarioRid": scenario_rid,
                    "objectType": object_type,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=ontologies_models.ListScenarioEditedLinkTypesResponse,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def list_scenario_edited_links(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        scenario_rid: ontologies_models.OntologyScenarioRid,
        object_type: ontologies_models.ObjectTypeApiName,
        link_type: ontologies_models.LinkTypeApiName,
        *,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> core.AsyncResourceIterator[ontologies_models.LinksFromObject]:
        """
        Returns the list of edited links within a given scenario for a specific object type and link type, grouped
        by source object. Only works for many-to-many link types. Only links where the user has permission to view
        both objects are returned.

        Each page may be smaller than the requested page size.

        :param ontology:
        :type ontology: OntologyIdentifier
        :param scenario_rid: The unique resource identifier of the scenario.
        :type scenario_rid: OntologyScenarioRid
        :param object_type: The API name of the object type.
        :type object_type: ObjectTypeApiName
        :param link_type: The API name of the link type.
        :type link_type: LinkTypeApiName
        :param page_size: The maximum number of links to return per page.
        :type page_size: Optional[PageSize]
        :param page_token: The page token to use for pagination.
        :type page_token: Optional[PageToken]
        :param preview: A boolean flag that, when set to true, enables the use of beta features in preview mode.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.AsyncResourceIterator[ontologies_models.LinksFromObject]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/ontologies/{ontology}/scenarios/{scenarioRid}/objects/{objectType}/links/{linkType}/edited",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
                    "preview": preview,
                },
                path_params={
                    "ontology": ontology,
                    "scenarioRid": scenario_rid,
                    "objectType": object_type,
                    "linkType": link_type,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=ontologies_models.ListScenarioEditedLinksResponse,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode", "ITERATOR"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def list_scenario_edited_object_types(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        scenario_rid: ontologies_models.OntologyScenarioRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[ontologies_models.ListScenarioEditedObjectTypesResponse]:
        """
        Returns the list of object type API names that have been modified within a given scenario.

        :param ontology:
        :type ontology: OntologyIdentifier
        :param scenario_rid: The unique resource identifier of the scenario.
        :type scenario_rid: OntologyScenarioRid
        :param preview: A boolean flag that, when set to true, enables the use of beta features in preview mode.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[ontologies_models.ListScenarioEditedObjectTypesResponse]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/ontologies/{ontology}/scenarios/{scenarioRid}/objectTypes/edited",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "ontology": ontology,
                    "scenarioRid": scenario_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=ontologies_models.ListScenarioEditedObjectTypesResponse,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def list_scenario_edited_objects(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        scenario_rid: ontologies_models.OntologyScenarioRid,
        object_type: ontologies_models.ObjectTypeApiName,
        *,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> core.AsyncResourceIterator[ontologies_models.OntologyObjectV2]:
        """
        Returns the list of objects that have been edited within a given scenario for a specific object type.
        Only objects that the user has permission to view are returned.

        Each page may be smaller than the requested page size.

        :param ontology:
        :type ontology: OntologyIdentifier
        :param scenario_rid: The unique resource identifier of the scenario.
        :type scenario_rid: OntologyScenarioRid
        :param object_type: The API name of the object type.
        :type object_type: ObjectTypeApiName
        :param page_size: The maximum number of objects to return per page.
        :type page_size: Optional[PageSize]
        :param page_token: The page token to use for pagination.
        :type page_token: Optional[PageToken]
        :param preview: A boolean flag that, when set to true, enables the use of beta features in preview mode.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.AsyncResourceIterator[ontologies_models.OntologyObjectV2]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/ontologies/{ontology}/scenarios/{scenarioRid}/objects/{objectType}/edited",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
                    "preview": preview,
                },
                path_params={
                    "ontology": ontology,
                    "scenarioRid": scenario_rid,
                    "objectType": object_type,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=ontologies_models.ListScenarioEditedObjectsResponse,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode", "ITERATOR"),
            ),
        )


class _AsyncOntologyScenarioClientRaw:
    def __init__(self, client: AsyncOntologyScenarioClient) -> None:
        def create_scenario(_: ontologies_models.CreateOntologyScenarioResponse): ...
        def list_scenario_edited_entity_types(
            _: ontologies_models.ListScenarioEditedEntityTypesResponse,
        ): ...
        def list_scenario_edited_link_types(
            _: ontologies_models.ListScenarioEditedLinkTypesResponse,
        ): ...
        def list_scenario_edited_links(_: ontologies_models.ListScenarioEditedLinksResponse): ...
        def list_scenario_edited_object_types(
            _: ontologies_models.ListScenarioEditedObjectTypesResponse,
        ): ...
        def list_scenario_edited_objects(
            _: ontologies_models.ListScenarioEditedObjectsResponse,
        ): ...

        self.create_scenario = core.async_with_raw_response(create_scenario, client.create_scenario)
        self.list_scenario_edited_entity_types = core.async_with_raw_response(
            list_scenario_edited_entity_types, client.list_scenario_edited_entity_types
        )
        self.list_scenario_edited_link_types = core.async_with_raw_response(
            list_scenario_edited_link_types, client.list_scenario_edited_link_types
        )
        self.list_scenario_edited_links = core.async_with_raw_response(
            list_scenario_edited_links, client.list_scenario_edited_links
        )
        self.list_scenario_edited_object_types = core.async_with_raw_response(
            list_scenario_edited_object_types, client.list_scenario_edited_object_types
        )
        self.list_scenario_edited_objects = core.async_with_raw_response(
            list_scenario_edited_objects, client.list_scenario_edited_objects
        )


class _AsyncOntologyScenarioClientStreaming:
    def __init__(self, client: AsyncOntologyScenarioClient) -> None:
        def create_scenario(_: ontologies_models.CreateOntologyScenarioResponse): ...
        def list_scenario_edited_entity_types(
            _: ontologies_models.ListScenarioEditedEntityTypesResponse,
        ): ...
        def list_scenario_edited_link_types(
            _: ontologies_models.ListScenarioEditedLinkTypesResponse,
        ): ...
        def list_scenario_edited_links(_: ontologies_models.ListScenarioEditedLinksResponse): ...
        def list_scenario_edited_object_types(
            _: ontologies_models.ListScenarioEditedObjectTypesResponse,
        ): ...
        def list_scenario_edited_objects(
            _: ontologies_models.ListScenarioEditedObjectsResponse,
        ): ...

        self.create_scenario = core.async_with_streaming_response(
            create_scenario, client.create_scenario
        )
        self.list_scenario_edited_entity_types = core.async_with_streaming_response(
            list_scenario_edited_entity_types, client.list_scenario_edited_entity_types
        )
        self.list_scenario_edited_link_types = core.async_with_streaming_response(
            list_scenario_edited_link_types, client.list_scenario_edited_link_types
        )
        self.list_scenario_edited_links = core.async_with_streaming_response(
            list_scenario_edited_links, client.list_scenario_edited_links
        )
        self.list_scenario_edited_object_types = core.async_with_streaming_response(
            list_scenario_edited_object_types, client.list_scenario_edited_object_types
        )
        self.list_scenario_edited_objects = core.async_with_streaming_response(
            list_scenario_edited_objects, client.list_scenario_edited_objects
        )
