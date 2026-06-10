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


class ActionTypeClient:
    """
    The API client for the ActionType Resource.

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

        self.with_streaming_response = _ActionTypeClientStreaming(self)
        self.with_raw_response = _ActionTypeClientRaw(self)

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
    ) -> ontologies_models.ActionTypeV2:
        """
        Gets a specific action type with the given API name.

        :param ontology:
        :type ontology: OntologyIdentifier
        :param action_type: The name of the action type in the API.
        :type action_type: ActionTypeApiName
        :param branch: The Foundry branch to load the action type definition from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported.
        :type branch: Optional[FoundryBranch]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ontologies_models.ActionTypeV2
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/ontologies/{ontology}/actionTypes/{actionType}",
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
                response_type=ontologies_models.ActionTypeV2,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get_by_rid(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        action_type_rid: ontologies_models.ActionTypeRid,
        *,
        branch: typing.Optional[core_models.FoundryBranch] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> ontologies_models.ActionTypeV2:
        """
        Gets a specific action type with the given RID.

        :param ontology:
        :type ontology: OntologyIdentifier
        :param action_type_rid: The RID of the action type.
        :type action_type_rid: ActionTypeRid
        :param branch: The Foundry branch to load the action type definition from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported.
        :type branch: Optional[FoundryBranch]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ontologies_models.ActionTypeV2
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/ontologies/{ontology}/actionTypes/byRid/{actionTypeRid}",
                query_params={
                    "branch": branch,
                },
                path_params={
                    "ontology": ontology,
                    "actionTypeRid": action_type_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=ontologies_models.ActionTypeV2,
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
            typing.List[ontologies_models.GetActionTypeByRidBatchRequestElement],
            annotated_types.Len(min_length=1, max_length=100),
        ],
        branch: typing.Optional[core_models.FoundryBranch] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> ontologies_models.GetActionTypeByRidBatchResponse:
        """
        Gets a list of action types by RID in bulk.

        Action types are filtered from the response if they don't exist or the requesting token lacks the required
        permissions.

        The maximum batch size for this endpoint is 100.

        :param ontology:
        :type ontology: OntologyIdentifier
        :param requests:
        :type requests: List[GetActionTypeByRidBatchRequestElement]
        :param branch: The Foundry branch to load the action type definitions from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported.
        :type branch: Optional[FoundryBranch]
        :param preview: A boolean flag that, when set to true, enables the use of beta features in preview mode.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ontologies_models.GetActionTypeByRidBatchResponse
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/ontologies/{ontology}/actionTypes/getByRidBatch",
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
                body=ontologies_models.GetActionTypeByRidBatchRequest(
                    requests=requests,
                ),
                response_type=ontologies_models.GetActionTypeByRidBatchResponse,
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
    ) -> core.ResourceIterator[ontologies_models.ActionTypeV2]:
        """
        Lists the action types for the given Ontology.

        Each page may be smaller than the requested page size. However, it is guaranteed that if there are more
        results available, at least one result will be present in the response.

        :param ontology:
        :type ontology: OntologyIdentifier
        :param branch: The Foundry branch to list the action types from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported.
        :type branch: Optional[FoundryBranch]
        :param page_size: The desired size of the page to be returned. Defaults to 500. See [page sizes](https://palantir.com/docs/foundry/api/general/overview/paging/#page-sizes) for details.
        :type page_size: Optional[PageSize]
        :param page_token:
        :type page_token: Optional[PageToken]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ResourceIterator[ontologies_models.ActionTypeV2]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/ontologies/{ontology}/actionTypes",
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
                response_type=ontologies_models.ListActionTypesResponseV2,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode", "ITERATOR"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def search(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        *,
        branch: typing.Optional[core_models.FoundryBranch] = None,
        fuzziness: typing.Optional[ontologies_models.ActionTypeFuzziness] = None,
        order_by: typing.Optional[ontologies_models.SearchActionTypesOrderByV2] = None,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        where: typing.Optional[ontologies_models.ActionTypeSearchJsonQueryV2] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> ontologies_models.SearchActionTypesResponseV2:
        """
        Search for action types in the given Ontology that match the provided filters. Results are returned by
        relevance of the match unless an explicit `orderBy` is provided.

        Each page may be smaller than the requested page size. However, it is guaranteed that if there are more
        results available, at least one result will be present in the response. Search results are eventually
        consistent with the latest Ontology version and may lag slightly behind the last Ontology modification.

        :param ontology:
        :type ontology: OntologyIdentifier
        :param branch: The Foundry branch to search the action types from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported.
        :type branch: Optional[FoundryBranch]
        :param fuzziness:
        :type fuzziness: Optional[ActionTypeFuzziness]
        :param order_by:
        :type order_by: Optional[SearchActionTypesOrderByV2]
        :param page_size:
        :type page_size: Optional[PageSize]
        :param page_token:
        :type page_token: Optional[PageToken]
        :param preview: A boolean flag that, when set to true, enables the use of beta features in preview mode.
        :type preview: Optional[PreviewMode]
        :param where:
        :type where: Optional[ActionTypeSearchJsonQueryV2]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ontologies_models.SearchActionTypesResponseV2
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/ontologies/{ontology}/actionTypes/search",
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
                body=ontologies_models.SearchActionTypesRequestV2(
                    where=where,
                    order_by=order_by,
                    fuzziness=fuzziness,
                    page_size=page_size,
                    page_token=page_token,
                ),
                response_type=ontologies_models.SearchActionTypesResponseV2,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _ActionTypeClientRaw:
    def __init__(self, client: ActionTypeClient) -> None:
        def get(_: ontologies_models.ActionTypeV2): ...
        def get_by_rid(_: ontologies_models.ActionTypeV2): ...
        def get_by_rid_batch(_: ontologies_models.GetActionTypeByRidBatchResponse): ...
        def list(_: ontologies_models.ListActionTypesResponseV2): ...
        def search(_: ontologies_models.SearchActionTypesResponseV2): ...

        self.get = core.with_raw_response(get, client.get)
        self.get_by_rid = core.with_raw_response(get_by_rid, client.get_by_rid)
        self.get_by_rid_batch = core.with_raw_response(get_by_rid_batch, client.get_by_rid_batch)
        self.list = core.with_raw_response(list, client.list)
        self.search = core.with_raw_response(search, client.search)


class _ActionTypeClientStreaming:
    def __init__(self, client: ActionTypeClient) -> None:
        def get(_: ontologies_models.ActionTypeV2): ...
        def get_by_rid(_: ontologies_models.ActionTypeV2): ...
        def get_by_rid_batch(_: ontologies_models.GetActionTypeByRidBatchResponse): ...
        def list(_: ontologies_models.ListActionTypesResponseV2): ...
        def search(_: ontologies_models.SearchActionTypesResponseV2): ...

        self.get = core.with_streaming_response(get, client.get)
        self.get_by_rid = core.with_streaming_response(get_by_rid, client.get_by_rid)
        self.get_by_rid_batch = core.with_streaming_response(
            get_by_rid_batch, client.get_by_rid_batch
        )
        self.list = core.with_streaming_response(list, client.list)
        self.search = core.with_streaming_response(search, client.search)


class AsyncActionTypeClient:
    """
    The API client for the ActionType Resource.

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

        self.with_streaming_response = _AsyncActionTypeClientStreaming(self)
        self.with_raw_response = _AsyncActionTypeClientRaw(self)

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
    ) -> typing.Awaitable[ontologies_models.ActionTypeV2]:
        """
        Gets a specific action type with the given API name.

        :param ontology:
        :type ontology: OntologyIdentifier
        :param action_type: The name of the action type in the API.
        :type action_type: ActionTypeApiName
        :param branch: The Foundry branch to load the action type definition from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported.
        :type branch: Optional[FoundryBranch]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[ontologies_models.ActionTypeV2]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/ontologies/{ontology}/actionTypes/{actionType}",
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
                response_type=ontologies_models.ActionTypeV2,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get_by_rid(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        action_type_rid: ontologies_models.ActionTypeRid,
        *,
        branch: typing.Optional[core_models.FoundryBranch] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[ontologies_models.ActionTypeV2]:
        """
        Gets a specific action type with the given RID.

        :param ontology:
        :type ontology: OntologyIdentifier
        :param action_type_rid: The RID of the action type.
        :type action_type_rid: ActionTypeRid
        :param branch: The Foundry branch to load the action type definition from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported.
        :type branch: Optional[FoundryBranch]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[ontologies_models.ActionTypeV2]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/ontologies/{ontology}/actionTypes/byRid/{actionTypeRid}",
                query_params={
                    "branch": branch,
                },
                path_params={
                    "ontology": ontology,
                    "actionTypeRid": action_type_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=ontologies_models.ActionTypeV2,
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
            typing.List[ontologies_models.GetActionTypeByRidBatchRequestElement],
            annotated_types.Len(min_length=1, max_length=100),
        ],
        branch: typing.Optional[core_models.FoundryBranch] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[ontologies_models.GetActionTypeByRidBatchResponse]:
        """
        Gets a list of action types by RID in bulk.

        Action types are filtered from the response if they don't exist or the requesting token lacks the required
        permissions.

        The maximum batch size for this endpoint is 100.

        :param ontology:
        :type ontology: OntologyIdentifier
        :param requests:
        :type requests: List[GetActionTypeByRidBatchRequestElement]
        :param branch: The Foundry branch to load the action type definitions from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported.
        :type branch: Optional[FoundryBranch]
        :param preview: A boolean flag that, when set to true, enables the use of beta features in preview mode.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[ontologies_models.GetActionTypeByRidBatchResponse]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/ontologies/{ontology}/actionTypes/getByRidBatch",
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
                body=ontologies_models.GetActionTypeByRidBatchRequest(
                    requests=requests,
                ),
                response_type=ontologies_models.GetActionTypeByRidBatchResponse,
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
    ) -> core.AsyncResourceIterator[ontologies_models.ActionTypeV2]:
        """
        Lists the action types for the given Ontology.

        Each page may be smaller than the requested page size. However, it is guaranteed that if there are more
        results available, at least one result will be present in the response.

        :param ontology:
        :type ontology: OntologyIdentifier
        :param branch: The Foundry branch to list the action types from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported.
        :type branch: Optional[FoundryBranch]
        :param page_size: The desired size of the page to be returned. Defaults to 500. See [page sizes](https://palantir.com/docs/foundry/api/general/overview/paging/#page-sizes) for details.
        :type page_size: Optional[PageSize]
        :param page_token:
        :type page_token: Optional[PageToken]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.AsyncResourceIterator[ontologies_models.ActionTypeV2]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/ontologies/{ontology}/actionTypes",
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
                response_type=ontologies_models.ListActionTypesResponseV2,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode", "ITERATOR"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def search(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        *,
        branch: typing.Optional[core_models.FoundryBranch] = None,
        fuzziness: typing.Optional[ontologies_models.ActionTypeFuzziness] = None,
        order_by: typing.Optional[ontologies_models.SearchActionTypesOrderByV2] = None,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        where: typing.Optional[ontologies_models.ActionTypeSearchJsonQueryV2] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[ontologies_models.SearchActionTypesResponseV2]:
        """
        Search for action types in the given Ontology that match the provided filters. Results are returned by
        relevance of the match unless an explicit `orderBy` is provided.

        Each page may be smaller than the requested page size. However, it is guaranteed that if there are more
        results available, at least one result will be present in the response. Search results are eventually
        consistent with the latest Ontology version and may lag slightly behind the last Ontology modification.

        :param ontology:
        :type ontology: OntologyIdentifier
        :param branch: The Foundry branch to search the action types from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported.
        :type branch: Optional[FoundryBranch]
        :param fuzziness:
        :type fuzziness: Optional[ActionTypeFuzziness]
        :param order_by:
        :type order_by: Optional[SearchActionTypesOrderByV2]
        :param page_size:
        :type page_size: Optional[PageSize]
        :param page_token:
        :type page_token: Optional[PageToken]
        :param preview: A boolean flag that, when set to true, enables the use of beta features in preview mode.
        :type preview: Optional[PreviewMode]
        :param where:
        :type where: Optional[ActionTypeSearchJsonQueryV2]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[ontologies_models.SearchActionTypesResponseV2]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/ontologies/{ontology}/actionTypes/search",
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
                body=ontologies_models.SearchActionTypesRequestV2(
                    where=where,
                    order_by=order_by,
                    fuzziness=fuzziness,
                    page_size=page_size,
                    page_token=page_token,
                ),
                response_type=ontologies_models.SearchActionTypesResponseV2,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _AsyncActionTypeClientRaw:
    def __init__(self, client: AsyncActionTypeClient) -> None:
        def get(_: ontologies_models.ActionTypeV2): ...
        def get_by_rid(_: ontologies_models.ActionTypeV2): ...
        def get_by_rid_batch(_: ontologies_models.GetActionTypeByRidBatchResponse): ...
        def list(_: ontologies_models.ListActionTypesResponseV2): ...
        def search(_: ontologies_models.SearchActionTypesResponseV2): ...

        self.get = core.async_with_raw_response(get, client.get)
        self.get_by_rid = core.async_with_raw_response(get_by_rid, client.get_by_rid)
        self.get_by_rid_batch = core.async_with_raw_response(
            get_by_rid_batch, client.get_by_rid_batch
        )
        self.list = core.async_with_raw_response(list, client.list)
        self.search = core.async_with_raw_response(search, client.search)


class _AsyncActionTypeClientStreaming:
    def __init__(self, client: AsyncActionTypeClient) -> None:
        def get(_: ontologies_models.ActionTypeV2): ...
        def get_by_rid(_: ontologies_models.ActionTypeV2): ...
        def get_by_rid_batch(_: ontologies_models.GetActionTypeByRidBatchResponse): ...
        def list(_: ontologies_models.ListActionTypesResponseV2): ...
        def search(_: ontologies_models.SearchActionTypesResponseV2): ...

        self.get = core.async_with_streaming_response(get, client.get)
        self.get_by_rid = core.async_with_streaming_response(get_by_rid, client.get_by_rid)
        self.get_by_rid_batch = core.async_with_streaming_response(
            get_by_rid_batch, client.get_by_rid_batch
        )
        self.list = core.async_with_streaming_response(list, client.list)
        self.search = core.async_with_streaming_response(search, client.search)
