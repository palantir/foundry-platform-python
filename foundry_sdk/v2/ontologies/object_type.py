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

import annotated_types
import pydantic
import typing_extensions

from foundry_sdk import _core as core
from foundry_sdk import _errors as errors
from foundry_sdk.v2.core import models as core_models
from foundry_sdk.v2.ontologies import models as ontologies_models


class ObjectTypeClient:
    """
    The API client for the ObjectType Resource.

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

        self.with_streaming_response = _ObjectTypeClientStreaming(self)
        self.with_raw_response = _ObjectTypeClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        object_type: ontologies_models.ObjectTypeApiName,
        *,
        branch: typing.Optional[core_models.FoundryBranch] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> ontologies_models.ObjectTypeV2:
        """
        Gets a specific object type with the given API name.

        :param ontology:
        :type ontology: OntologyIdentifier
        :param object_type: The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**.
        :type object_type: ObjectTypeApiName
        :param branch: The Foundry branch to load the object type definition from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported.
        :type branch: Optional[FoundryBranch]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ontologies_models.ObjectTypeV2
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/ontologies/{ontology}/objectTypes/{objectType}",
                query_params={
                    "branch": branch,
                },
                path_params={
                    "ontology": ontology,
                    "objectType": object_type,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=ontologies_models.ObjectTypeV2,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get_by_rid_batch(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        *,
        requests: typing_extensions.Annotated[
            typing.List[ontologies_models.GetObjectTypeByRidBatchRequestElement],
            annotated_types.Len(min_length=1, max_length=100),
        ],
        branch: typing.Optional[core_models.FoundryBranch] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> ontologies_models.GetObjectTypeByRidBatchResponse:
        """
        Gets a list of object types by RID in bulk.

        Object types are filtered from the response if they don't exist or the requesting token lacks the required
        permissions.

        The maximum batch size for this endpoint is 100.

        :param ontology:
        :type ontology: OntologyIdentifier
        :param requests:
        :type requests: List[GetObjectTypeByRidBatchRequestElement]
        :param branch: The Foundry branch to load the object type definitions from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported.
        :type branch: Optional[FoundryBranch]
        :param preview: A boolean flag that, when set to true, enables the use of beta features in preview mode.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ontologies_models.GetObjectTypeByRidBatchResponse
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/ontologies/{ontology}/objectTypes/getByRidBatch",
                query_params={
                    "branch": branch,
                    "preview": preview,
                },
                path_params={
                    "ontology": ontology,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body=ontologies_models.GetObjectTypeByRidBatchRequest(
                    requests=requests,
                ),
                response_type=ontologies_models.GetObjectTypeByRidBatchResponse,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get_edits_history(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        object_type: ontologies_models.ObjectTypeApiName,
        *,
        branch: typing.Optional[core_models.FoundryBranch] = None,
        filters: typing.Optional[ontologies_models.EditsHistoryFilter] = None,
        include_all_previous_properties: typing.Optional[bool] = None,
        object_primary_key: typing.Optional[ontologies_models.ObjectPrimaryKeyV2] = None,
        page_size: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        scenario_rid: typing.Optional[ontologies_models.OntologyScenarioRid] = None,
        sort_order: typing.Optional[ontologies_models.EditsHistorySortOrder] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> ontologies_models.ObjectTypeEditsHistoryResponse:
        """
        Returns the history of edits (additions, modifications, deletions) for objects of a
        specific object type. This endpoint provides visibility into all actions that have
        modified objects of this type.

        The edits are returned in reverse chronological order (most recent first) by default.

        Note that filters are ignored for OSv1 object types.

        :param ontology: The ontology RID or API name
        :type ontology: OntologyIdentifier
        :param object_type: The API name of the object type
        :type object_type: ObjectTypeApiName
        :param branch: The Foundry branch from which we will get edits history. If not specified, the default branch is used. Branches are an experimental feature and not all workflows are supported.
        :type branch: Optional[FoundryBranch]
        :param filters:
        :type filters: Optional[EditsHistoryFilter]
        :param include_all_previous_properties:
        :type include_all_previous_properties: Optional[bool]
        :param object_primary_key:
        :type object_primary_key: Optional[ObjectPrimaryKeyV2]
        :param page_size: The maximum number of edits to return per page. Defaults to 100.
        :type page_size: Optional[int]
        :param page_token: Token for retrieving the next page of results
        :type page_token: Optional[str]
        :param preview: A boolean flag that, when set to true, enables the use of beta features in preview mode.
        :type preview: Optional[PreviewMode]
        :param scenario_rid: The resource identifier of an ontology scenario to get edits history from.
        :type scenario_rid: Optional[OntologyScenarioRid]
        :param sort_order:
        :type sort_order: Optional[EditsHistorySortOrder]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ontologies_models.ObjectTypeEditsHistoryResponse
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/ontologies/{ontology}/objectTypes/{objectType}/editsHistory",
                query_params={
                    "branch": branch,
                    "preview": preview,
                    "scenarioRid": scenario_rid,
                },
                path_params={
                    "ontology": ontology,
                    "objectType": object_type,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body=ontologies_models.ObjectTypeEditsHistoryRequest(
                    object_primary_key=object_primary_key,
                    filters=filters,
                    sort_order=sort_order,
                    include_all_previous_properties=include_all_previous_properties,
                    page_size=page_size,
                    page_token=page_token,
                ),
                response_type=ontologies_models.ObjectTypeEditsHistoryResponse,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get_full_metadata(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        object_type: ontologies_models.ObjectTypeApiName,
        *,
        branch: typing.Optional[core_models.FoundryBranch] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        sdk_package_rid: typing.Optional[ontologies_models.SdkPackageRid] = None,
        sdk_version: typing.Optional[ontologies_models.SdkVersion] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> ontologies_models.ObjectTypeFullMetadata:
        """
        Gets the full metadata for a specific object type with the given API name.

        :param ontology:
        :type ontology: OntologyIdentifier
        :param object_type: The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**.
        :type object_type: ObjectTypeApiName
        :param branch: The Foundry branch to load the action type definition from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported.
        :type branch: Optional[FoundryBranch]
        :param preview: A boolean flag that, when set to true, enables the use of beta features in preview mode.
        :type preview: Optional[PreviewMode]
        :param sdk_package_rid: The package rid of the generated SDK.
        :type sdk_package_rid: Optional[SdkPackageRid]
        :param sdk_version: The version of the generated SDK.
        :type sdk_version: Optional[SdkVersion]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ontologies_models.ObjectTypeFullMetadata
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/ontologies/{ontology}/objectTypes/{objectType}/fullMetadata",
                query_params={
                    "branch": branch,
                    "preview": preview,
                    "sdkPackageRid": sdk_package_rid,
                    "sdkVersion": sdk_version,
                },
                path_params={
                    "ontology": ontology,
                    "objectType": object_type,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=ontologies_models.ObjectTypeFullMetadata,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get_outgoing_link_type(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        object_type: ontologies_models.ObjectTypeApiName,
        link_type: ontologies_models.LinkTypeApiName,
        *,
        branch: typing.Optional[core_models.FoundryBranch] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> ontologies_models.LinkTypeSideV2:
        """
        Get an outgoing link for an object type.

        :param ontology:
        :type ontology: OntologyIdentifier
        :param object_type: The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager** application.
        :type object_type: ObjectTypeApiName
        :param link_type: The API name of the outgoing link. To find the API name for your link type, check the **Ontology Manager**.
        :type link_type: LinkTypeApiName
        :param branch: The Foundry branch to get the outgoing link types for an object type from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported.
        :type branch: Optional[FoundryBranch]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ontologies_models.LinkTypeSideV2
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/ontologies/{ontology}/objectTypes/{objectType}/outgoingLinkTypes/{linkType}",
                query_params={
                    "branch": branch,
                },
                path_params={
                    "ontology": ontology,
                    "objectType": object_type,
                    "linkType": link_type,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=ontologies_models.LinkTypeSideV2,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get_outgoing_link_types_by_object_type_rid_batch(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        *,
        filter_link_type_rids: typing.List[ontologies_models.LinkTypeRid],
        requests: typing_extensions.Annotated[
            typing.List[ontologies_models.GetOutgoingLinkTypesByObjectTypeRidBatchRequestElement],
            annotated_types.Len(min_length=1, max_length=100),
        ],
        branch: typing.Optional[core_models.FoundryBranch] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> ontologies_models.GetOutgoingLinkTypesByObjectTypeRidBatchResponse:
        """
        Gets outgoing link types for a batch of object types, identified by their RIDs.

        For each requested object type, returns the list of outgoing link types visible to the
        requesting token. Optionally, results can be filtered to only include specific link type RIDs.

        Object types that don't exist or that the requesting token lacks permissions for are
        silently omitted from the response.

        The maximum batch size for this endpoint is 100.

        :param ontology:
        :type ontology: OntologyIdentifier
        :param filter_link_type_rids: If provided, only return outgoing link types with RIDs in this list. If omitted, all outgoing link types for each requested object type are returned.
        :type filter_link_type_rids: List[LinkTypeRid]
        :param requests:
        :type requests: List[GetOutgoingLinkTypesByObjectTypeRidBatchRequestElement]
        :param branch: The Foundry branch to load the outgoing link type definitions from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported.
        :type branch: Optional[FoundryBranch]
        :param preview: A boolean flag that, when set to true, enables the use of beta features in preview mode.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ontologies_models.GetOutgoingLinkTypesByObjectTypeRidBatchResponse
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/ontologies/{ontology}/outgoingLinkTypes/getByRidBatch",
                query_params={
                    "branch": branch,
                    "preview": preview,
                },
                path_params={
                    "ontology": ontology,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body=ontologies_models.GetOutgoingLinkTypesByObjectTypeRidBatchRequest(
                    requests=requests,
                    filter_link_type_rids=filter_link_type_rids,
                ),
                response_type=ontologies_models.GetOutgoingLinkTypesByObjectTypeRidBatchResponse,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def list(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        *,
        branch: typing.Optional[core_models.FoundryBranch] = None,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> core.ResourceIterator[ontologies_models.ObjectTypeV2]:
        """
        Lists the object types for the given Ontology.

        Each page may be smaller or larger than the requested page size. However, it is guaranteed that if there are
        more results available, at least one result will be present in the
        response.

        :param ontology:
        :type ontology: OntologyIdentifier
        :param branch: The Foundry branch to list the object types from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported.
        :type branch: Optional[FoundryBranch]
        :param page_size: The desired size of the page to be returned. Defaults to 500. See [page sizes](https://palantir.com/docs/foundry/api/general/overview/paging/#page-sizes) for details.
        :type page_size: Optional[PageSize]
        :param page_token:
        :type page_token: Optional[PageToken]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ResourceIterator[ontologies_models.ObjectTypeV2]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/ontologies/{ontology}/objectTypes",
                query_params={
                    "branch": branch,
                    "pageSize": page_size,
                    "pageToken": page_token,
                },
                path_params={
                    "ontology": ontology,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=ontologies_models.ListObjectTypesV2Response,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode", "ITERATOR"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def list_outgoing_link_types(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        object_type: ontologies_models.ObjectTypeApiName,
        *,
        branch: typing.Optional[core_models.FoundryBranch] = None,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> core.ResourceIterator[ontologies_models.LinkTypeSideV2]:
        """
        List the outgoing links for an object type.

        :param ontology:
        :type ontology: OntologyIdentifier
        :param object_type: The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager** application.
        :type object_type: ObjectTypeApiName
        :param branch: The Foundry branch to load the outgoing link types from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported.
        :type branch: Optional[FoundryBranch]
        :param page_size: The desired size of the page to be returned.
        :type page_size: Optional[PageSize]
        :param page_token:
        :type page_token: Optional[PageToken]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ResourceIterator[ontologies_models.LinkTypeSideV2]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/ontologies/{ontology}/objectTypes/{objectType}/outgoingLinkTypes",
                query_params={
                    "branch": branch,
                    "pageSize": page_size,
                    "pageToken": page_token,
                },
                path_params={
                    "ontology": ontology,
                    "objectType": object_type,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=ontologies_models.ListOutgoingLinkTypesResponseV2,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode", "ITERATOR"),
            ),
        )


class _ObjectTypeClientRaw:
    def __init__(self, client: ObjectTypeClient) -> None:
        def get(_: ontologies_models.ObjectTypeV2): ...
        def get_by_rid_batch(_: ontologies_models.GetObjectTypeByRidBatchResponse): ...
        def get_edits_history(_: ontologies_models.ObjectTypeEditsHistoryResponse): ...
        def get_full_metadata(_: ontologies_models.ObjectTypeFullMetadata): ...
        def get_outgoing_link_type(_: ontologies_models.LinkTypeSideV2): ...
        def get_outgoing_link_types_by_object_type_rid_batch(
            _: ontologies_models.GetOutgoingLinkTypesByObjectTypeRidBatchResponse,
        ): ...
        def list(_: ontologies_models.ListObjectTypesV2Response): ...
        def list_outgoing_link_types(_: ontologies_models.ListOutgoingLinkTypesResponseV2): ...

        self.get = core.with_raw_response(get, client.get)
        self.get_by_rid_batch = core.with_raw_response(get_by_rid_batch, client.get_by_rid_batch)
        self.get_edits_history = core.with_raw_response(get_edits_history, client.get_edits_history)
        self.get_full_metadata = core.with_raw_response(get_full_metadata, client.get_full_metadata)
        self.get_outgoing_link_type = core.with_raw_response(
            get_outgoing_link_type, client.get_outgoing_link_type
        )
        self.get_outgoing_link_types_by_object_type_rid_batch = core.with_raw_response(
            get_outgoing_link_types_by_object_type_rid_batch,
            client.get_outgoing_link_types_by_object_type_rid_batch,
        )
        self.list = core.with_raw_response(list, client.list)
        self.list_outgoing_link_types = core.with_raw_response(
            list_outgoing_link_types, client.list_outgoing_link_types
        )


class _ObjectTypeClientStreaming:
    def __init__(self, client: ObjectTypeClient) -> None:
        def get(_: ontologies_models.ObjectTypeV2): ...
        def get_by_rid_batch(_: ontologies_models.GetObjectTypeByRidBatchResponse): ...
        def get_edits_history(_: ontologies_models.ObjectTypeEditsHistoryResponse): ...
        def get_full_metadata(_: ontologies_models.ObjectTypeFullMetadata): ...
        def get_outgoing_link_type(_: ontologies_models.LinkTypeSideV2): ...
        def get_outgoing_link_types_by_object_type_rid_batch(
            _: ontologies_models.GetOutgoingLinkTypesByObjectTypeRidBatchResponse,
        ): ...
        def list(_: ontologies_models.ListObjectTypesV2Response): ...
        def list_outgoing_link_types(_: ontologies_models.ListOutgoingLinkTypesResponseV2): ...

        self.get = core.with_streaming_response(get, client.get)
        self.get_by_rid_batch = core.with_streaming_response(
            get_by_rid_batch, client.get_by_rid_batch
        )
        self.get_edits_history = core.with_streaming_response(
            get_edits_history, client.get_edits_history
        )
        self.get_full_metadata = core.with_streaming_response(
            get_full_metadata, client.get_full_metadata
        )
        self.get_outgoing_link_type = core.with_streaming_response(
            get_outgoing_link_type, client.get_outgoing_link_type
        )
        self.get_outgoing_link_types_by_object_type_rid_batch = core.with_streaming_response(
            get_outgoing_link_types_by_object_type_rid_batch,
            client.get_outgoing_link_types_by_object_type_rid_batch,
        )
        self.list = core.with_streaming_response(list, client.list)
        self.list_outgoing_link_types = core.with_streaming_response(
            list_outgoing_link_types, client.list_outgoing_link_types
        )


class AsyncObjectTypeClient:
    """
    The API client for the ObjectType Resource.

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

        self.with_streaming_response = _AsyncObjectTypeClientStreaming(self)
        self.with_raw_response = _AsyncObjectTypeClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        object_type: ontologies_models.ObjectTypeApiName,
        *,
        branch: typing.Optional[core_models.FoundryBranch] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[ontologies_models.ObjectTypeV2]:
        """
        Gets a specific object type with the given API name.

        :param ontology:
        :type ontology: OntologyIdentifier
        :param object_type: The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**.
        :type object_type: ObjectTypeApiName
        :param branch: The Foundry branch to load the object type definition from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported.
        :type branch: Optional[FoundryBranch]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[ontologies_models.ObjectTypeV2]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/ontologies/{ontology}/objectTypes/{objectType}",
                query_params={
                    "branch": branch,
                },
                path_params={
                    "ontology": ontology,
                    "objectType": object_type,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=ontologies_models.ObjectTypeV2,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get_by_rid_batch(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        *,
        requests: typing_extensions.Annotated[
            typing.List[ontologies_models.GetObjectTypeByRidBatchRequestElement],
            annotated_types.Len(min_length=1, max_length=100),
        ],
        branch: typing.Optional[core_models.FoundryBranch] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[ontologies_models.GetObjectTypeByRidBatchResponse]:
        """
        Gets a list of object types by RID in bulk.

        Object types are filtered from the response if they don't exist or the requesting token lacks the required
        permissions.

        The maximum batch size for this endpoint is 100.

        :param ontology:
        :type ontology: OntologyIdentifier
        :param requests:
        :type requests: List[GetObjectTypeByRidBatchRequestElement]
        :param branch: The Foundry branch to load the object type definitions from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported.
        :type branch: Optional[FoundryBranch]
        :param preview: A boolean flag that, when set to true, enables the use of beta features in preview mode.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[ontologies_models.GetObjectTypeByRidBatchResponse]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/ontologies/{ontology}/objectTypes/getByRidBatch",
                query_params={
                    "branch": branch,
                    "preview": preview,
                },
                path_params={
                    "ontology": ontology,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body=ontologies_models.GetObjectTypeByRidBatchRequest(
                    requests=requests,
                ),
                response_type=ontologies_models.GetObjectTypeByRidBatchResponse,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get_edits_history(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        object_type: ontologies_models.ObjectTypeApiName,
        *,
        branch: typing.Optional[core_models.FoundryBranch] = None,
        filters: typing.Optional[ontologies_models.EditsHistoryFilter] = None,
        include_all_previous_properties: typing.Optional[bool] = None,
        object_primary_key: typing.Optional[ontologies_models.ObjectPrimaryKeyV2] = None,
        page_size: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        scenario_rid: typing.Optional[ontologies_models.OntologyScenarioRid] = None,
        sort_order: typing.Optional[ontologies_models.EditsHistorySortOrder] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[ontologies_models.ObjectTypeEditsHistoryResponse]:
        """
        Returns the history of edits (additions, modifications, deletions) for objects of a
        specific object type. This endpoint provides visibility into all actions that have
        modified objects of this type.

        The edits are returned in reverse chronological order (most recent first) by default.

        Note that filters are ignored for OSv1 object types.

        :param ontology: The ontology RID or API name
        :type ontology: OntologyIdentifier
        :param object_type: The API name of the object type
        :type object_type: ObjectTypeApiName
        :param branch: The Foundry branch from which we will get edits history. If not specified, the default branch is used. Branches are an experimental feature and not all workflows are supported.
        :type branch: Optional[FoundryBranch]
        :param filters:
        :type filters: Optional[EditsHistoryFilter]
        :param include_all_previous_properties:
        :type include_all_previous_properties: Optional[bool]
        :param object_primary_key:
        :type object_primary_key: Optional[ObjectPrimaryKeyV2]
        :param page_size: The maximum number of edits to return per page. Defaults to 100.
        :type page_size: Optional[int]
        :param page_token: Token for retrieving the next page of results
        :type page_token: Optional[str]
        :param preview: A boolean flag that, when set to true, enables the use of beta features in preview mode.
        :type preview: Optional[PreviewMode]
        :param scenario_rid: The resource identifier of an ontology scenario to get edits history from.
        :type scenario_rid: Optional[OntologyScenarioRid]
        :param sort_order:
        :type sort_order: Optional[EditsHistorySortOrder]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[ontologies_models.ObjectTypeEditsHistoryResponse]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/ontologies/{ontology}/objectTypes/{objectType}/editsHistory",
                query_params={
                    "branch": branch,
                    "preview": preview,
                    "scenarioRid": scenario_rid,
                },
                path_params={
                    "ontology": ontology,
                    "objectType": object_type,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body=ontologies_models.ObjectTypeEditsHistoryRequest(
                    object_primary_key=object_primary_key,
                    filters=filters,
                    sort_order=sort_order,
                    include_all_previous_properties=include_all_previous_properties,
                    page_size=page_size,
                    page_token=page_token,
                ),
                response_type=ontologies_models.ObjectTypeEditsHistoryResponse,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get_full_metadata(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        object_type: ontologies_models.ObjectTypeApiName,
        *,
        branch: typing.Optional[core_models.FoundryBranch] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        sdk_package_rid: typing.Optional[ontologies_models.SdkPackageRid] = None,
        sdk_version: typing.Optional[ontologies_models.SdkVersion] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[ontologies_models.ObjectTypeFullMetadata]:
        """
        Gets the full metadata for a specific object type with the given API name.

        :param ontology:
        :type ontology: OntologyIdentifier
        :param object_type: The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**.
        :type object_type: ObjectTypeApiName
        :param branch: The Foundry branch to load the action type definition from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported.
        :type branch: Optional[FoundryBranch]
        :param preview: A boolean flag that, when set to true, enables the use of beta features in preview mode.
        :type preview: Optional[PreviewMode]
        :param sdk_package_rid: The package rid of the generated SDK.
        :type sdk_package_rid: Optional[SdkPackageRid]
        :param sdk_version: The version of the generated SDK.
        :type sdk_version: Optional[SdkVersion]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[ontologies_models.ObjectTypeFullMetadata]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/ontologies/{ontology}/objectTypes/{objectType}/fullMetadata",
                query_params={
                    "branch": branch,
                    "preview": preview,
                    "sdkPackageRid": sdk_package_rid,
                    "sdkVersion": sdk_version,
                },
                path_params={
                    "ontology": ontology,
                    "objectType": object_type,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=ontologies_models.ObjectTypeFullMetadata,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get_outgoing_link_type(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        object_type: ontologies_models.ObjectTypeApiName,
        link_type: ontologies_models.LinkTypeApiName,
        *,
        branch: typing.Optional[core_models.FoundryBranch] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[ontologies_models.LinkTypeSideV2]:
        """
        Get an outgoing link for an object type.

        :param ontology:
        :type ontology: OntologyIdentifier
        :param object_type: The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager** application.
        :type object_type: ObjectTypeApiName
        :param link_type: The API name of the outgoing link. To find the API name for your link type, check the **Ontology Manager**.
        :type link_type: LinkTypeApiName
        :param branch: The Foundry branch to get the outgoing link types for an object type from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported.
        :type branch: Optional[FoundryBranch]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[ontologies_models.LinkTypeSideV2]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/ontologies/{ontology}/objectTypes/{objectType}/outgoingLinkTypes/{linkType}",
                query_params={
                    "branch": branch,
                },
                path_params={
                    "ontology": ontology,
                    "objectType": object_type,
                    "linkType": link_type,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=ontologies_models.LinkTypeSideV2,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get_outgoing_link_types_by_object_type_rid_batch(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        *,
        filter_link_type_rids: typing.List[ontologies_models.LinkTypeRid],
        requests: typing_extensions.Annotated[
            typing.List[ontologies_models.GetOutgoingLinkTypesByObjectTypeRidBatchRequestElement],
            annotated_types.Len(min_length=1, max_length=100),
        ],
        branch: typing.Optional[core_models.FoundryBranch] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[ontologies_models.GetOutgoingLinkTypesByObjectTypeRidBatchResponse]:
        """
        Gets outgoing link types for a batch of object types, identified by their RIDs.

        For each requested object type, returns the list of outgoing link types visible to the
        requesting token. Optionally, results can be filtered to only include specific link type RIDs.

        Object types that don't exist or that the requesting token lacks permissions for are
        silently omitted from the response.

        The maximum batch size for this endpoint is 100.

        :param ontology:
        :type ontology: OntologyIdentifier
        :param filter_link_type_rids: If provided, only return outgoing link types with RIDs in this list. If omitted, all outgoing link types for each requested object type are returned.
        :type filter_link_type_rids: List[LinkTypeRid]
        :param requests:
        :type requests: List[GetOutgoingLinkTypesByObjectTypeRidBatchRequestElement]
        :param branch: The Foundry branch to load the outgoing link type definitions from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported.
        :type branch: Optional[FoundryBranch]
        :param preview: A boolean flag that, when set to true, enables the use of beta features in preview mode.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[ontologies_models.GetOutgoingLinkTypesByObjectTypeRidBatchResponse]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/ontologies/{ontology}/outgoingLinkTypes/getByRidBatch",
                query_params={
                    "branch": branch,
                    "preview": preview,
                },
                path_params={
                    "ontology": ontology,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body=ontologies_models.GetOutgoingLinkTypesByObjectTypeRidBatchRequest(
                    requests=requests,
                    filter_link_type_rids=filter_link_type_rids,
                ),
                response_type=ontologies_models.GetOutgoingLinkTypesByObjectTypeRidBatchResponse,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def list(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        *,
        branch: typing.Optional[core_models.FoundryBranch] = None,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> core.AsyncResourceIterator[ontologies_models.ObjectTypeV2]:
        """
        Lists the object types for the given Ontology.

        Each page may be smaller or larger than the requested page size. However, it is guaranteed that if there are
        more results available, at least one result will be present in the
        response.

        :param ontology:
        :type ontology: OntologyIdentifier
        :param branch: The Foundry branch to list the object types from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported.
        :type branch: Optional[FoundryBranch]
        :param page_size: The desired size of the page to be returned. Defaults to 500. See [page sizes](https://palantir.com/docs/foundry/api/general/overview/paging/#page-sizes) for details.
        :type page_size: Optional[PageSize]
        :param page_token:
        :type page_token: Optional[PageToken]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.AsyncResourceIterator[ontologies_models.ObjectTypeV2]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/ontologies/{ontology}/objectTypes",
                query_params={
                    "branch": branch,
                    "pageSize": page_size,
                    "pageToken": page_token,
                },
                path_params={
                    "ontology": ontology,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=ontologies_models.ListObjectTypesV2Response,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode", "ITERATOR"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def list_outgoing_link_types(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        object_type: ontologies_models.ObjectTypeApiName,
        *,
        branch: typing.Optional[core_models.FoundryBranch] = None,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> core.AsyncResourceIterator[ontologies_models.LinkTypeSideV2]:
        """
        List the outgoing links for an object type.

        :param ontology:
        :type ontology: OntologyIdentifier
        :param object_type: The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager** application.
        :type object_type: ObjectTypeApiName
        :param branch: The Foundry branch to load the outgoing link types from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported.
        :type branch: Optional[FoundryBranch]
        :param page_size: The desired size of the page to be returned.
        :type page_size: Optional[PageSize]
        :param page_token:
        :type page_token: Optional[PageToken]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.AsyncResourceIterator[ontologies_models.LinkTypeSideV2]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/ontologies/{ontology}/objectTypes/{objectType}/outgoingLinkTypes",
                query_params={
                    "branch": branch,
                    "pageSize": page_size,
                    "pageToken": page_token,
                },
                path_params={
                    "ontology": ontology,
                    "objectType": object_type,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=ontologies_models.ListOutgoingLinkTypesResponseV2,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode", "ITERATOR"),
            ),
        )


class _AsyncObjectTypeClientRaw:
    def __init__(self, client: AsyncObjectTypeClient) -> None:
        def get(_: ontologies_models.ObjectTypeV2): ...
        def get_by_rid_batch(_: ontologies_models.GetObjectTypeByRidBatchResponse): ...
        def get_edits_history(_: ontologies_models.ObjectTypeEditsHistoryResponse): ...
        def get_full_metadata(_: ontologies_models.ObjectTypeFullMetadata): ...
        def get_outgoing_link_type(_: ontologies_models.LinkTypeSideV2): ...
        def get_outgoing_link_types_by_object_type_rid_batch(
            _: ontologies_models.GetOutgoingLinkTypesByObjectTypeRidBatchResponse,
        ): ...
        def list(_: ontologies_models.ListObjectTypesV2Response): ...
        def list_outgoing_link_types(_: ontologies_models.ListOutgoingLinkTypesResponseV2): ...

        self.get = core.async_with_raw_response(get, client.get)
        self.get_by_rid_batch = core.async_with_raw_response(
            get_by_rid_batch, client.get_by_rid_batch
        )
        self.get_edits_history = core.async_with_raw_response(
            get_edits_history, client.get_edits_history
        )
        self.get_full_metadata = core.async_with_raw_response(
            get_full_metadata, client.get_full_metadata
        )
        self.get_outgoing_link_type = core.async_with_raw_response(
            get_outgoing_link_type, client.get_outgoing_link_type
        )
        self.get_outgoing_link_types_by_object_type_rid_batch = core.async_with_raw_response(
            get_outgoing_link_types_by_object_type_rid_batch,
            client.get_outgoing_link_types_by_object_type_rid_batch,
        )
        self.list = core.async_with_raw_response(list, client.list)
        self.list_outgoing_link_types = core.async_with_raw_response(
            list_outgoing_link_types, client.list_outgoing_link_types
        )


class _AsyncObjectTypeClientStreaming:
    def __init__(self, client: AsyncObjectTypeClient) -> None:
        def get(_: ontologies_models.ObjectTypeV2): ...
        def get_by_rid_batch(_: ontologies_models.GetObjectTypeByRidBatchResponse): ...
        def get_edits_history(_: ontologies_models.ObjectTypeEditsHistoryResponse): ...
        def get_full_metadata(_: ontologies_models.ObjectTypeFullMetadata): ...
        def get_outgoing_link_type(_: ontologies_models.LinkTypeSideV2): ...
        def get_outgoing_link_types_by_object_type_rid_batch(
            _: ontologies_models.GetOutgoingLinkTypesByObjectTypeRidBatchResponse,
        ): ...
        def list(_: ontologies_models.ListObjectTypesV2Response): ...
        def list_outgoing_link_types(_: ontologies_models.ListOutgoingLinkTypesResponseV2): ...

        self.get = core.async_with_streaming_response(get, client.get)
        self.get_by_rid_batch = core.async_with_streaming_response(
            get_by_rid_batch, client.get_by_rid_batch
        )
        self.get_edits_history = core.async_with_streaming_response(
            get_edits_history, client.get_edits_history
        )
        self.get_full_metadata = core.async_with_streaming_response(
            get_full_metadata, client.get_full_metadata
        )
        self.get_outgoing_link_type = core.async_with_streaming_response(
            get_outgoing_link_type, client.get_outgoing_link_type
        )
        self.get_outgoing_link_types_by_object_type_rid_batch = core.async_with_streaming_response(
            get_outgoing_link_types_by_object_type_rid_batch,
            client.get_outgoing_link_types_by_object_type_rid_batch,
        )
        self.list = core.async_with_streaming_response(list, client.list)
        self.list_outgoing_link_types = core.async_with_streaming_response(
            list_outgoing_link_types, client.list_outgoing_link_types
        )
