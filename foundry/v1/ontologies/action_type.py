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

import pydantic
import typing_extensions

from foundry import _core as core
from foundry import _errors as errors
from foundry.v1.core import models as core_models
from foundry.v1.ontologies import models as ontologies_models


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
        self.with_streaming_response = _ActionTypeClientStreaming(
            auth=auth, hostname=hostname, config=config
        )
        self.with_raw_response = _ActionTypeClientRaw(auth=auth, hostname=hostname, config=config)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        ontology_rid: ontologies_models.OntologyRid,
        action_type_api_name: ontologies_models.ActionTypeApiName,
        *,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> ontologies_models.ActionType:
        """
        Gets a specific action type with the given API name.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

        :param ontology_rid: The unique Resource Identifier (RID) of the Ontology that contains the action type.
        :type ontology_rid: OntologyRid
        :param action_type_api_name: The name of the action type in the API.
        :type action_type_api_name: ActionTypeApiName
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ontologies_models.ActionType
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v1/ontologies/{ontologyRid}/actionTypes/{actionTypeApiName}",
                query_params={},
                path_params={
                    "ontologyRid": ontology_rid,
                    "actionTypeApiName": action_type_api_name,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ontologies_models.ActionType,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        ).decode()

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def list(
        self,
        ontology_rid: ontologies_models.OntologyRid,
        *,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ResourceIterator[ontologies_models.ActionType]:
        """
        Lists the action types for the given Ontology.

        Each page may be smaller than the requested page size. However, it is guaranteed that if there are more
        results available, at least one result will be present in the response.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

        :param ontology_rid: The unique Resource Identifier (RID) of the Ontology that contains the action types. To look up your Ontology RID, please use the **List ontologies** endpoint or check the **Ontology Manager**.
        :type ontology_rid: OntologyRid
        :param page_size: The desired size of the page to be returned. Defaults to 500. See [page sizes](/docs/foundry/api/general/overview/paging/#page-sizes) for details.
        :type page_size: Optional[PageSize]
        :param page_token:
        :type page_token: Optional[PageToken]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ResourceIterator[ontologies_models.ActionType]
        """

        return self._api_client.iterate_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v1/ontologies/{ontologyRid}/actionTypes",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
                },
                path_params={
                    "ontologyRid": ontology_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ontologies_models.ListActionTypesResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def page(
        self,
        ontology_rid: ontologies_models.OntologyRid,
        *,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> ontologies_models.ListActionTypesResponse:
        """
        Lists the action types for the given Ontology.

        Each page may be smaller than the requested page size. However, it is guaranteed that if there are more
        results available, at least one result will be present in the response.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

        :param ontology_rid: The unique Resource Identifier (RID) of the Ontology that contains the action types. To look up your Ontology RID, please use the **List ontologies** endpoint or check the **Ontology Manager**.
        :type ontology_rid: OntologyRid
        :param page_size: The desired size of the page to be returned. Defaults to 500. See [page sizes](/docs/foundry/api/general/overview/paging/#page-sizes) for details.
        :type page_size: Optional[PageSize]
        :param page_token:
        :type page_token: Optional[PageToken]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ontologies_models.ListActionTypesResponse
        """

        warnings.warn(
            "The client.ontologies.ActionType.page(...) method has been deprecated. Please use client.ontologies.ActionType.list(...) instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v1/ontologies/{ontologyRid}/actionTypes",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
                },
                path_params={
                    "ontologyRid": ontology_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ontologies_models.ListActionTypesResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        ).decode()


class _ActionTypeClientRaw:
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

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        ontology_rid: ontologies_models.OntologyRid,
        action_type_api_name: ontologies_models.ActionTypeApiName,
        *,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[ontologies_models.ActionType]:
        """
        Gets a specific action type with the given API name.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

        :param ontology_rid: The unique Resource Identifier (RID) of the Ontology that contains the action type.
        :type ontology_rid: OntologyRid
        :param action_type_api_name: The name of the action type in the API.
        :type action_type_api_name: ActionTypeApiName
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[ontologies_models.ActionType]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v1/ontologies/{ontologyRid}/actionTypes/{actionTypeApiName}",
                query_params={},
                path_params={
                    "ontologyRid": ontology_rid,
                    "actionTypeApiName": action_type_api_name,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ontologies_models.ActionType,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def list(
        self,
        ontology_rid: ontologies_models.OntologyRid,
        *,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[ontologies_models.ListActionTypesResponse]:
        """
        Lists the action types for the given Ontology.

        Each page may be smaller than the requested page size. However, it is guaranteed that if there are more
        results available, at least one result will be present in the response.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

        :param ontology_rid: The unique Resource Identifier (RID) of the Ontology that contains the action types. To look up your Ontology RID, please use the **List ontologies** endpoint or check the **Ontology Manager**.
        :type ontology_rid: OntologyRid
        :param page_size: The desired size of the page to be returned. Defaults to 500. See [page sizes](/docs/foundry/api/general/overview/paging/#page-sizes) for details.
        :type page_size: Optional[PageSize]
        :param page_token:
        :type page_token: Optional[PageToken]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[ontologies_models.ListActionTypesResponse]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v1/ontologies/{ontologyRid}/actionTypes",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
                },
                path_params={
                    "ontologyRid": ontology_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ontologies_models.ListActionTypesResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def page(
        self,
        ontology_rid: ontologies_models.OntologyRid,
        *,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[ontologies_models.ListActionTypesResponse]:
        """
        Lists the action types for the given Ontology.

        Each page may be smaller than the requested page size. However, it is guaranteed that if there are more
        results available, at least one result will be present in the response.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

        :param ontology_rid: The unique Resource Identifier (RID) of the Ontology that contains the action types. To look up your Ontology RID, please use the **List ontologies** endpoint or check the **Ontology Manager**.
        :type ontology_rid: OntologyRid
        :param page_size: The desired size of the page to be returned. Defaults to 500. See [page sizes](/docs/foundry/api/general/overview/paging/#page-sizes) for details.
        :type page_size: Optional[PageSize]
        :param page_token:
        :type page_token: Optional[PageToken]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[ontologies_models.ListActionTypesResponse]
        """

        warnings.warn(
            "The client.ontologies.ActionType.page(...) method has been deprecated. Please use client.ontologies.ActionType.list(...) instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v1/ontologies/{ontologyRid}/actionTypes",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
                },
                path_params={
                    "ontologyRid": ontology_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ontologies_models.ListActionTypesResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )


class _ActionTypeClientStreaming:
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

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        ontology_rid: ontologies_models.OntologyRid,
        action_type_api_name: ontologies_models.ActionTypeApiName,
        *,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[ontologies_models.ActionType]:
        """
        Gets a specific action type with the given API name.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

        :param ontology_rid: The unique Resource Identifier (RID) of the Ontology that contains the action type.
        :type ontology_rid: OntologyRid
        :param action_type_api_name: The name of the action type in the API.
        :type action_type_api_name: ActionTypeApiName
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[ontologies_models.ActionType]
        """

        return self._api_client.stream_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v1/ontologies/{ontologyRid}/actionTypes/{actionTypeApiName}",
                query_params={},
                path_params={
                    "ontologyRid": ontology_rid,
                    "actionTypeApiName": action_type_api_name,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ontologies_models.ActionType,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def list(
        self,
        ontology_rid: ontologies_models.OntologyRid,
        *,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[ontologies_models.ListActionTypesResponse]:
        """
        Lists the action types for the given Ontology.

        Each page may be smaller than the requested page size. However, it is guaranteed that if there are more
        results available, at least one result will be present in the response.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

        :param ontology_rid: The unique Resource Identifier (RID) of the Ontology that contains the action types. To look up your Ontology RID, please use the **List ontologies** endpoint or check the **Ontology Manager**.
        :type ontology_rid: OntologyRid
        :param page_size: The desired size of the page to be returned. Defaults to 500. See [page sizes](/docs/foundry/api/general/overview/paging/#page-sizes) for details.
        :type page_size: Optional[PageSize]
        :param page_token:
        :type page_token: Optional[PageToken]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[ontologies_models.ListActionTypesResponse]
        """

        return self._api_client.stream_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v1/ontologies/{ontologyRid}/actionTypes",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
                },
                path_params={
                    "ontologyRid": ontology_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ontologies_models.ListActionTypesResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def page(
        self,
        ontology_rid: ontologies_models.OntologyRid,
        *,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[ontologies_models.ListActionTypesResponse]:
        """
        Lists the action types for the given Ontology.

        Each page may be smaller than the requested page size. However, it is guaranteed that if there are more
        results available, at least one result will be present in the response.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

        :param ontology_rid: The unique Resource Identifier (RID) of the Ontology that contains the action types. To look up your Ontology RID, please use the **List ontologies** endpoint or check the **Ontology Manager**.
        :type ontology_rid: OntologyRid
        :param page_size: The desired size of the page to be returned. Defaults to 500. See [page sizes](/docs/foundry/api/general/overview/paging/#page-sizes) for details.
        :type page_size: Optional[PageSize]
        :param page_token:
        :type page_token: Optional[PageToken]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[ontologies_models.ListActionTypesResponse]
        """

        warnings.warn(
            "The client.ontologies.ActionType.page(...) method has been deprecated. Please use client.ontologies.ActionType.list(...) instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        return self._api_client.stream_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v1/ontologies/{ontologyRid}/actionTypes",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
                },
                path_params={
                    "ontologyRid": ontology_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ontologies_models.ListActionTypesResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )
