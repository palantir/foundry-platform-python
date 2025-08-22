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


class ActionTypeClient:
    """
    The API client for the ActionType Resource.

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
        :param branch: The Foundry branch to load the action type definition from. If not specified, the default branch will be used.
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
                body_type=None,
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
        :param branch: The Foundry branch to load the action type definition from. If not specified, the default branch will be used.
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
                body_type=None,
                response_type=ontologies_models.ActionTypeV2,
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
        :param branch: The Foundry branch to list the action types from. If not specified, the default branch will be used.
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
                body_type=None,
                response_type=ontologies_models.ListActionTypesResponseV2,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode", "ITERATOR"),
            ),
        )


class _ActionTypeClientRaw:
    def __init__(self, client: ActionTypeClient) -> None:
        def get(_: ontologies_models.ActionTypeV2): ...
        def get_by_rid(_: ontologies_models.ActionTypeV2): ...
        def list(_: ontologies_models.ListActionTypesResponseV2): ...

        self.get = core.with_raw_response(get, client.get)
        self.get_by_rid = core.with_raw_response(get_by_rid, client.get_by_rid)
        self.list = core.with_raw_response(list, client.list)


class _ActionTypeClientStreaming:
    def __init__(self, client: ActionTypeClient) -> None:
        def get(_: ontologies_models.ActionTypeV2): ...
        def get_by_rid(_: ontologies_models.ActionTypeV2): ...
        def list(_: ontologies_models.ListActionTypesResponseV2): ...

        self.get = core.with_streaming_response(get, client.get)
        self.get_by_rid = core.with_streaming_response(get_by_rid, client.get_by_rid)
        self.list = core.with_streaming_response(list, client.list)


class AsyncActionTypeClient:
    """
    The API client for the ActionType Resource.

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
        :param branch: The Foundry branch to load the action type definition from. If not specified, the default branch will be used.
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
                body_type=None,
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
        :param branch: The Foundry branch to load the action type definition from. If not specified, the default branch will be used.
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
                body_type=None,
                response_type=ontologies_models.ActionTypeV2,
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
        :param branch: The Foundry branch to list the action types from. If not specified, the default branch will be used.
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
                body_type=None,
                response_type=ontologies_models.ListActionTypesResponseV2,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode", "ITERATOR"),
            ),
        )


class _AsyncActionTypeClientRaw:
    def __init__(self, client: AsyncActionTypeClient) -> None:
        def get(_: ontologies_models.ActionTypeV2): ...
        def get_by_rid(_: ontologies_models.ActionTypeV2): ...
        def list(_: ontologies_models.ListActionTypesResponseV2): ...

        self.get = core.async_with_raw_response(get, client.get)
        self.get_by_rid = core.async_with_raw_response(get_by_rid, client.get_by_rid)
        self.list = core.async_with_raw_response(list, client.list)


class _AsyncActionTypeClientStreaming:
    def __init__(self, client: AsyncActionTypeClient) -> None:
        def get(_: ontologies_models.ActionTypeV2): ...
        def get_by_rid(_: ontologies_models.ActionTypeV2): ...
        def list(_: ontologies_models.ListActionTypesResponseV2): ...

        self.get = core.async_with_streaming_response(get, client.get)
        self.get_by_rid = core.async_with_streaming_response(get_by_rid, client.get_by_rid)
        self.list = core.async_with_streaming_response(list, client.list)
