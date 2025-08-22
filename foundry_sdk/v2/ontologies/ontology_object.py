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


class OntologyObjectClient:
    """
    The API client for the OntologyObject Resource.

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

        self.with_streaming_response = _OntologyObjectClientStreaming(self)
        self.with_raw_response = _OntologyObjectClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def aggregate(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        object_type: ontologies_models.ObjectTypeApiName,
        *,
        aggregation: typing.List[ontologies_models.AggregationV2],
        group_by: typing.List[ontologies_models.AggregationGroupByV2],
        accuracy: typing.Optional[ontologies_models.AggregationAccuracyRequest] = None,
        branch: typing.Optional[core_models.FoundryBranch] = None,
        sdk_package_rid: typing.Optional[ontologies_models.SdkPackageRid] = None,
        sdk_version: typing.Optional[ontologies_models.SdkVersion] = None,
        where: typing.Optional[ontologies_models.SearchJsonQueryV2] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> ontologies_models.AggregateObjectsResponseV2:
        """
        Perform functions on object fields in the specified ontology and object type.

        :param ontology:
        :type ontology: OntologyIdentifier
        :param object_type: The type of the object to aggregate on.
        :type object_type: ObjectTypeApiName
        :param aggregation:
        :type aggregation: List[AggregationV2]
        :param group_by:
        :type group_by: List[AggregationGroupByV2]
        :param accuracy:
        :type accuracy: Optional[AggregationAccuracyRequest]
        :param branch: The Foundry branch to aggregate objects from. If not specified, the default branch will be used.
        :type branch: Optional[FoundryBranch]
        :param sdk_package_rid: The package rid of the generated SDK.
        :type sdk_package_rid: Optional[SdkPackageRid]
        :param sdk_version: The version of the generated SDK.
        :type sdk_version: Optional[SdkVersion]
        :param where:
        :type where: Optional[SearchJsonQueryV2]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ontologies_models.AggregateObjectsResponseV2
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/ontologies/{ontology}/objects/{objectType}/aggregate",
                query_params={
                    "branch": branch,
                    "sdkPackageRid": sdk_package_rid,
                    "sdkVersion": sdk_version,
                },
                path_params={
                    "ontology": ontology,
                    "objectType": object_type,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "aggregation": aggregation,
                    "where": where,
                    "groupBy": group_by,
                    "accuracy": accuracy,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "aggregation": typing.List[ontologies_models.AggregationV2],
                        "where": typing.Optional[ontologies_models.SearchJsonQueryV2],
                        "groupBy": typing.List[ontologies_models.AggregationGroupByV2],
                        "accuracy": typing.Optional[ontologies_models.AggregationAccuracyRequest],
                    },
                ),
                response_type=ontologies_models.AggregateObjectsResponseV2,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def count(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        object_type: ontologies_models.ObjectTypeApiName,
        *,
        branch: typing.Optional[core_models.FoundryBranch] = None,
        sdk_package_rid: typing.Optional[ontologies_models.SdkPackageRid] = None,
        sdk_version: typing.Optional[ontologies_models.SdkVersion] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> ontologies_models.CountObjectsResponseV2:
        """
        Returns a count of the objects of the given object type.

        :param ontology:
        :type ontology: OntologyIdentifier
        :param object_type: The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**.
        :type object_type: ObjectTypeApiName
        :param branch: The Foundry branch to count the objects from. If not specified, the default branch is used.
        :type branch: Optional[FoundryBranch]
        :param sdk_package_rid: The package rid of the generated SDK.
        :type sdk_package_rid: Optional[SdkPackageRid]
        :param sdk_version: The package version of the generated SDK.
        :type sdk_version: Optional[SdkVersion]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ontologies_models.CountObjectsResponseV2
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/ontologies/{ontology}/objects/{objectType}/count",
                query_params={
                    "branch": branch,
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
                body_type=None,
                response_type=ontologies_models.CountObjectsResponseV2,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        object_type: ontologies_models.ObjectTypeApiName,
        primary_key: ontologies_models.PropertyValueEscapedString,
        *,
        branch: typing.Optional[core_models.FoundryBranch] = None,
        exclude_rid: typing.Optional[bool] = None,
        sdk_package_rid: typing.Optional[ontologies_models.SdkPackageRid] = None,
        sdk_version: typing.Optional[ontologies_models.SdkVersion] = None,
        select: typing.Optional[typing.List[ontologies_models.SelectedPropertyApiName]] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> ontologies_models.OntologyObjectV2:
        """
        Gets a specific object with the given primary key.

        :param ontology:
        :type ontology: OntologyIdentifier
        :param object_type: The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**.
        :type object_type: ObjectTypeApiName
        :param primary_key: The primary key of the requested object. To look up the expected primary key for your object type, use the `Get object type` endpoint or the **Ontology Manager**.
        :type primary_key: PropertyValueEscapedString
        :param branch: The Foundry branch to get the object from. If not specified, the default branch is used.
        :type branch: Optional[FoundryBranch]
        :param exclude_rid: A flag to exclude the retrieval of the `__rid` property.  Setting this to true may improve performance of this endpoint for object types in OSV2.
        :type exclude_rid: Optional[bool]
        :param sdk_package_rid: The package rid of the generated SDK.
        :type sdk_package_rid: Optional[SdkPackageRid]
        :param sdk_version: The version of the generated SDK.
        :type sdk_version: Optional[SdkVersion]
        :param select: The properties of the object type that should be included in the response. Omit this parameter to get all the properties.
        :type select: Optional[List[SelectedPropertyApiName]]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ontologies_models.OntologyObjectV2
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}",
                query_params={
                    "branch": branch,
                    "excludeRid": exclude_rid,
                    "sdkPackageRid": sdk_package_rid,
                    "sdkVersion": sdk_version,
                    "select": select,
                },
                path_params={
                    "ontology": ontology,
                    "objectType": object_type,
                    "primaryKey": primary_key,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ontologies_models.OntologyObjectV2,
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
        object_type: ontologies_models.ObjectTypeApiName,
        *,
        branch: typing.Optional[core_models.FoundryBranch] = None,
        exclude_rid: typing.Optional[bool] = None,
        order_by: typing.Optional[ontologies_models.OrderBy] = None,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        sdk_package_rid: typing.Optional[ontologies_models.SdkPackageRid] = None,
        sdk_version: typing.Optional[ontologies_models.SdkVersion] = None,
        select: typing.Optional[typing.List[ontologies_models.SelectedPropertyApiName]] = None,
        snapshot: typing.Optional[bool] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> core.ResourceIterator[ontologies_models.OntologyObjectV2]:
        """
        Lists the objects for the given Ontology and object type.

        Note that this endpoint does not guarantee consistency. Changes to the data could result in missing or
        repeated objects in the response pages.

        For Object Storage V1 backed objects, this endpoint returns a maximum of 10,000 objects. After 10,000 objects have been returned and if more objects
        are available, attempting to load another page will result in an `ObjectsExceededLimit` error being returned. There is no limit on Object Storage V2 backed objects.

        Each page may be smaller or larger than the requested page size. However, it
        is guaranteed that if there are more results available, at least one result will be present
        in the response.

        Note that null value properties will not be returned.

        :param ontology:
        :type ontology: OntologyIdentifier
        :param object_type: The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**.
        :type object_type: ObjectTypeApiName
        :param branch: The Foundry branch to list objects from. If not specified, the default branch will be used.
        :type branch: Optional[FoundryBranch]
        :param exclude_rid: A flag to exclude the retrieval of the `__rid` property.  Setting this to true may improve performance of this endpoint for object types in OSV2.
        :type exclude_rid: Optional[bool]
        :param order_by:
        :type order_by: Optional[OrderBy]
        :param page_size: The desired size of the page to be returned. Defaults to 1,000. See [page sizes](https://palantir.com/docs/foundry/api/general/overview/paging/#page-sizes) for details.
        :type page_size: Optional[PageSize]
        :param page_token:
        :type page_token: Optional[PageToken]
        :param sdk_package_rid: The package rid of the generated SDK.
        :type sdk_package_rid: Optional[SdkPackageRid]
        :param sdk_version: The version of the generated SDK.
        :type sdk_version: Optional[SdkVersion]
        :param select: The properties of the object type that should be included in the response. Omit this parameter to get all the properties.
        :type select: Optional[List[SelectedPropertyApiName]]
        :param snapshot: A flag to use snapshot consistency when paging. Setting this to true will give you a consistent view from before you start paging through the results, ensuring you do not get duplicate or missing items. Setting this to false will let new results enter as you page, but you may encounter duplicate or missing items. This defaults to false if not specified, which means you will always get the latest results.
        :type snapshot: Optional[bool]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ResourceIterator[ontologies_models.OntologyObjectV2]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/ontologies/{ontology}/objects/{objectType}",
                query_params={
                    "branch": branch,
                    "excludeRid": exclude_rid,
                    "orderBy": order_by,
                    "pageSize": page_size,
                    "pageToken": page_token,
                    "sdkPackageRid": sdk_package_rid,
                    "sdkVersion": sdk_version,
                    "select": select,
                    "snapshot": snapshot,
                },
                path_params={
                    "ontology": ontology,
                    "objectType": object_type,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ontologies_models.ListObjectsResponseV2,
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
        object_type: ontologies_models.ObjectTypeApiName,
        *,
        select: typing.List[ontologies_models.PropertyApiName],
        branch: typing.Optional[core_models.FoundryBranch] = None,
        exclude_rid: typing.Optional[bool] = None,
        order_by: typing.Optional[ontologies_models.SearchOrderByV2] = None,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        sdk_package_rid: typing.Optional[ontologies_models.SdkPackageRid] = None,
        sdk_version: typing.Optional[ontologies_models.SdkVersion] = None,
        snapshot: typing.Optional[bool] = None,
        where: typing.Optional[ontologies_models.SearchJsonQueryV2] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> ontologies_models.SearchObjectsResponseV2:
        """
        Search for objects in the specified ontology and object type. The request body is used
        to filter objects based on the specified query. The supported queries are:

        | Query type                              | Description                                                                                                       | Supported Types                 |
        |-----------------------------------------|-------------------------------------------------------------------------------------------------------------------|---------------------------------|
        | lt                                      | The provided property is less than the provided value.                                                            | number, string, date, timestamp |
        | gt                                      | The provided property is greater than the provided value.                                                         | number, string, date, timestamp |
        | lte                                     | The provided property is less than or equal to the provided value.                                                | number, string, date, timestamp |
        | gte                                     | The provided property is greater than or equal to the provided value.                                             | number, string, date, timestamp |
        | eq                                      | The provided property is exactly equal to the provided value.                                                     | number, string, date, timestamp |
        | isNull                                  | The provided property is (or is not) null.                                                                        | all                             |
        | contains                                | The provided property contains the provided value.                                                                | array                           |
        | not                                     | The sub-query does not match.                                                                                     | N/A (applied on a query)        |
        | and                                     | All the sub-queries match.                                                                                        | N/A (applied on queries)        |
        | or                                      | At least one of the sub-queries match.                                                                            | N/A (applied on queries)        |
        | containsAllTermsInOrderPrefixLastTerm   | The provided property contains all the terms provided in order. The last term can be a partial prefix match.      | string                          |
        | containsAllTermsInOrder                 | The provided property contains the provided term as a substring.                                                  | string                          |
        | containsAnyTerm                         | The provided property contains at least one of the terms separated by whitespace.                                 | string                          |
        | containsAllTerms                        | The provided property contains all the terms separated by whitespace.                                             | string                          |
        | startsWith                              | Deprecated alias for containsAllTermsInOrderPrefixLastTerm.                                                       | string                          |

        Queries can be at most three levels deep. By default, terms are separated by whitespace or punctuation (`?!,:;-[](){}'"~`). Periods (`.`) on their own are ignored.
        Partial terms are not matched by terms filters except where explicitly noted.

        :param ontology:
        :type ontology: OntologyIdentifier
        :param object_type: The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**.
        :type object_type: ObjectTypeApiName
        :param select: The API names of the object type properties to include in the response.
        :type select: List[PropertyApiName]
        :param branch: The Foundry branch to search objects from. If not specified, the default branch will be used.
        :type branch: Optional[FoundryBranch]
        :param exclude_rid: A flag to exclude the retrieval of the `__rid` property. Setting this to true may improve performance of this endpoint for object types in OSV2.
        :type exclude_rid: Optional[bool]
        :param order_by:
        :type order_by: Optional[SearchOrderByV2]
        :param page_size:
        :type page_size: Optional[PageSize]
        :param page_token:
        :type page_token: Optional[PageToken]
        :param sdk_package_rid: The package rid of the generated SDK.
        :type sdk_package_rid: Optional[SdkPackageRid]
        :param sdk_version: The version of the generated SDK.
        :type sdk_version: Optional[SdkVersion]
        :param snapshot: A flag to use snapshot consistency when paging. Setting this to true will give you a consistent view from before you start paging through the results, ensuring you do not get duplicate or missing items. Setting this to false will let new results enter as you page, but you may encounter duplicate or missing items. This defaults to false if not specified, which means you will always get the latest results.
        :type snapshot: Optional[bool]
        :param where:
        :type where: Optional[SearchJsonQueryV2]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ontologies_models.SearchObjectsResponseV2
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/ontologies/{ontology}/objects/{objectType}/search",
                query_params={
                    "branch": branch,
                    "sdkPackageRid": sdk_package_rid,
                    "sdkVersion": sdk_version,
                },
                path_params={
                    "ontology": ontology,
                    "objectType": object_type,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "where": where,
                    "orderBy": order_by,
                    "pageSize": page_size,
                    "pageToken": page_token,
                    "select": select,
                    "excludeRid": exclude_rid,
                    "snapshot": snapshot,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "where": typing.Optional[ontologies_models.SearchJsonQueryV2],
                        "orderBy": typing.Optional[ontologies_models.SearchOrderByV2],
                        "pageSize": typing.Optional[core_models.PageSize],
                        "pageToken": typing.Optional[core_models.PageToken],
                        "select": typing.List[ontologies_models.PropertyApiName],
                        "excludeRid": typing.Optional[bool],
                        "snapshot": typing.Optional[bool],
                    },
                ),
                response_type=ontologies_models.SearchObjectsResponseV2,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _OntologyObjectClientRaw:
    def __init__(self, client: OntologyObjectClient) -> None:
        def aggregate(_: ontologies_models.AggregateObjectsResponseV2): ...
        def count(_: ontologies_models.CountObjectsResponseV2): ...
        def get(_: ontologies_models.OntologyObjectV2): ...
        def list(_: ontologies_models.ListObjectsResponseV2): ...
        def search(_: ontologies_models.SearchObjectsResponseV2): ...

        self.aggregate = core.with_raw_response(aggregate, client.aggregate)
        self.count = core.with_raw_response(count, client.count)
        self.get = core.with_raw_response(get, client.get)
        self.list = core.with_raw_response(list, client.list)
        self.search = core.with_raw_response(search, client.search)


class _OntologyObjectClientStreaming:
    def __init__(self, client: OntologyObjectClient) -> None:
        def aggregate(_: ontologies_models.AggregateObjectsResponseV2): ...
        def count(_: ontologies_models.CountObjectsResponseV2): ...
        def get(_: ontologies_models.OntologyObjectV2): ...
        def list(_: ontologies_models.ListObjectsResponseV2): ...
        def search(_: ontologies_models.SearchObjectsResponseV2): ...

        self.aggregate = core.with_streaming_response(aggregate, client.aggregate)
        self.count = core.with_streaming_response(count, client.count)
        self.get = core.with_streaming_response(get, client.get)
        self.list = core.with_streaming_response(list, client.list)
        self.search = core.with_streaming_response(search, client.search)


class AsyncOntologyObjectClient:
    """
    The API client for the OntologyObject Resource.

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

        self.with_streaming_response = _AsyncOntologyObjectClientStreaming(self)
        self.with_raw_response = _AsyncOntologyObjectClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def aggregate(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        object_type: ontologies_models.ObjectTypeApiName,
        *,
        aggregation: typing.List[ontologies_models.AggregationV2],
        group_by: typing.List[ontologies_models.AggregationGroupByV2],
        accuracy: typing.Optional[ontologies_models.AggregationAccuracyRequest] = None,
        branch: typing.Optional[core_models.FoundryBranch] = None,
        sdk_package_rid: typing.Optional[ontologies_models.SdkPackageRid] = None,
        sdk_version: typing.Optional[ontologies_models.SdkVersion] = None,
        where: typing.Optional[ontologies_models.SearchJsonQueryV2] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[ontologies_models.AggregateObjectsResponseV2]:
        """
        Perform functions on object fields in the specified ontology and object type.

        :param ontology:
        :type ontology: OntologyIdentifier
        :param object_type: The type of the object to aggregate on.
        :type object_type: ObjectTypeApiName
        :param aggregation:
        :type aggregation: List[AggregationV2]
        :param group_by:
        :type group_by: List[AggregationGroupByV2]
        :param accuracy:
        :type accuracy: Optional[AggregationAccuracyRequest]
        :param branch: The Foundry branch to aggregate objects from. If not specified, the default branch will be used.
        :type branch: Optional[FoundryBranch]
        :param sdk_package_rid: The package rid of the generated SDK.
        :type sdk_package_rid: Optional[SdkPackageRid]
        :param sdk_version: The version of the generated SDK.
        :type sdk_version: Optional[SdkVersion]
        :param where:
        :type where: Optional[SearchJsonQueryV2]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[ontologies_models.AggregateObjectsResponseV2]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/ontologies/{ontology}/objects/{objectType}/aggregate",
                query_params={
                    "branch": branch,
                    "sdkPackageRid": sdk_package_rid,
                    "sdkVersion": sdk_version,
                },
                path_params={
                    "ontology": ontology,
                    "objectType": object_type,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "aggregation": aggregation,
                    "where": where,
                    "groupBy": group_by,
                    "accuracy": accuracy,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "aggregation": typing.List[ontologies_models.AggregationV2],
                        "where": typing.Optional[ontologies_models.SearchJsonQueryV2],
                        "groupBy": typing.List[ontologies_models.AggregationGroupByV2],
                        "accuracy": typing.Optional[ontologies_models.AggregationAccuracyRequest],
                    },
                ),
                response_type=ontologies_models.AggregateObjectsResponseV2,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def count(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        object_type: ontologies_models.ObjectTypeApiName,
        *,
        branch: typing.Optional[core_models.FoundryBranch] = None,
        sdk_package_rid: typing.Optional[ontologies_models.SdkPackageRid] = None,
        sdk_version: typing.Optional[ontologies_models.SdkVersion] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[ontologies_models.CountObjectsResponseV2]:
        """
        Returns a count of the objects of the given object type.

        :param ontology:
        :type ontology: OntologyIdentifier
        :param object_type: The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**.
        :type object_type: ObjectTypeApiName
        :param branch: The Foundry branch to count the objects from. If not specified, the default branch is used.
        :type branch: Optional[FoundryBranch]
        :param sdk_package_rid: The package rid of the generated SDK.
        :type sdk_package_rid: Optional[SdkPackageRid]
        :param sdk_version: The package version of the generated SDK.
        :type sdk_version: Optional[SdkVersion]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[ontologies_models.CountObjectsResponseV2]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/ontologies/{ontology}/objects/{objectType}/count",
                query_params={
                    "branch": branch,
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
                body_type=None,
                response_type=ontologies_models.CountObjectsResponseV2,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        object_type: ontologies_models.ObjectTypeApiName,
        primary_key: ontologies_models.PropertyValueEscapedString,
        *,
        branch: typing.Optional[core_models.FoundryBranch] = None,
        exclude_rid: typing.Optional[bool] = None,
        sdk_package_rid: typing.Optional[ontologies_models.SdkPackageRid] = None,
        sdk_version: typing.Optional[ontologies_models.SdkVersion] = None,
        select: typing.Optional[typing.List[ontologies_models.SelectedPropertyApiName]] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[ontologies_models.OntologyObjectV2]:
        """
        Gets a specific object with the given primary key.

        :param ontology:
        :type ontology: OntologyIdentifier
        :param object_type: The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**.
        :type object_type: ObjectTypeApiName
        :param primary_key: The primary key of the requested object. To look up the expected primary key for your object type, use the `Get object type` endpoint or the **Ontology Manager**.
        :type primary_key: PropertyValueEscapedString
        :param branch: The Foundry branch to get the object from. If not specified, the default branch is used.
        :type branch: Optional[FoundryBranch]
        :param exclude_rid: A flag to exclude the retrieval of the `__rid` property.  Setting this to true may improve performance of this endpoint for object types in OSV2.
        :type exclude_rid: Optional[bool]
        :param sdk_package_rid: The package rid of the generated SDK.
        :type sdk_package_rid: Optional[SdkPackageRid]
        :param sdk_version: The version of the generated SDK.
        :type sdk_version: Optional[SdkVersion]
        :param select: The properties of the object type that should be included in the response. Omit this parameter to get all the properties.
        :type select: Optional[List[SelectedPropertyApiName]]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[ontologies_models.OntologyObjectV2]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}",
                query_params={
                    "branch": branch,
                    "excludeRid": exclude_rid,
                    "sdkPackageRid": sdk_package_rid,
                    "sdkVersion": sdk_version,
                    "select": select,
                },
                path_params={
                    "ontology": ontology,
                    "objectType": object_type,
                    "primaryKey": primary_key,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ontologies_models.OntologyObjectV2,
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
        object_type: ontologies_models.ObjectTypeApiName,
        *,
        branch: typing.Optional[core_models.FoundryBranch] = None,
        exclude_rid: typing.Optional[bool] = None,
        order_by: typing.Optional[ontologies_models.OrderBy] = None,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        sdk_package_rid: typing.Optional[ontologies_models.SdkPackageRid] = None,
        sdk_version: typing.Optional[ontologies_models.SdkVersion] = None,
        select: typing.Optional[typing.List[ontologies_models.SelectedPropertyApiName]] = None,
        snapshot: typing.Optional[bool] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> core.AsyncResourceIterator[ontologies_models.OntologyObjectV2]:
        """
        Lists the objects for the given Ontology and object type.

        Note that this endpoint does not guarantee consistency. Changes to the data could result in missing or
        repeated objects in the response pages.

        For Object Storage V1 backed objects, this endpoint returns a maximum of 10,000 objects. After 10,000 objects have been returned and if more objects
        are available, attempting to load another page will result in an `ObjectsExceededLimit` error being returned. There is no limit on Object Storage V2 backed objects.

        Each page may be smaller or larger than the requested page size. However, it
        is guaranteed that if there are more results available, at least one result will be present
        in the response.

        Note that null value properties will not be returned.

        :param ontology:
        :type ontology: OntologyIdentifier
        :param object_type: The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**.
        :type object_type: ObjectTypeApiName
        :param branch: The Foundry branch to list objects from. If not specified, the default branch will be used.
        :type branch: Optional[FoundryBranch]
        :param exclude_rid: A flag to exclude the retrieval of the `__rid` property.  Setting this to true may improve performance of this endpoint for object types in OSV2.
        :type exclude_rid: Optional[bool]
        :param order_by:
        :type order_by: Optional[OrderBy]
        :param page_size: The desired size of the page to be returned. Defaults to 1,000. See [page sizes](https://palantir.com/docs/foundry/api/general/overview/paging/#page-sizes) for details.
        :type page_size: Optional[PageSize]
        :param page_token:
        :type page_token: Optional[PageToken]
        :param sdk_package_rid: The package rid of the generated SDK.
        :type sdk_package_rid: Optional[SdkPackageRid]
        :param sdk_version: The version of the generated SDK.
        :type sdk_version: Optional[SdkVersion]
        :param select: The properties of the object type that should be included in the response. Omit this parameter to get all the properties.
        :type select: Optional[List[SelectedPropertyApiName]]
        :param snapshot: A flag to use snapshot consistency when paging. Setting this to true will give you a consistent view from before you start paging through the results, ensuring you do not get duplicate or missing items. Setting this to false will let new results enter as you page, but you may encounter duplicate or missing items. This defaults to false if not specified, which means you will always get the latest results.
        :type snapshot: Optional[bool]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.AsyncResourceIterator[ontologies_models.OntologyObjectV2]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/ontologies/{ontology}/objects/{objectType}",
                query_params={
                    "branch": branch,
                    "excludeRid": exclude_rid,
                    "orderBy": order_by,
                    "pageSize": page_size,
                    "pageToken": page_token,
                    "sdkPackageRid": sdk_package_rid,
                    "sdkVersion": sdk_version,
                    "select": select,
                    "snapshot": snapshot,
                },
                path_params={
                    "ontology": ontology,
                    "objectType": object_type,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ontologies_models.ListObjectsResponseV2,
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
        object_type: ontologies_models.ObjectTypeApiName,
        *,
        select: typing.List[ontologies_models.PropertyApiName],
        branch: typing.Optional[core_models.FoundryBranch] = None,
        exclude_rid: typing.Optional[bool] = None,
        order_by: typing.Optional[ontologies_models.SearchOrderByV2] = None,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        sdk_package_rid: typing.Optional[ontologies_models.SdkPackageRid] = None,
        sdk_version: typing.Optional[ontologies_models.SdkVersion] = None,
        snapshot: typing.Optional[bool] = None,
        where: typing.Optional[ontologies_models.SearchJsonQueryV2] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[ontologies_models.SearchObjectsResponseV2]:
        """
        Search for objects in the specified ontology and object type. The request body is used
        to filter objects based on the specified query. The supported queries are:

        | Query type                              | Description                                                                                                       | Supported Types                 |
        |-----------------------------------------|-------------------------------------------------------------------------------------------------------------------|---------------------------------|
        | lt                                      | The provided property is less than the provided value.                                                            | number, string, date, timestamp |
        | gt                                      | The provided property is greater than the provided value.                                                         | number, string, date, timestamp |
        | lte                                     | The provided property is less than or equal to the provided value.                                                | number, string, date, timestamp |
        | gte                                     | The provided property is greater than or equal to the provided value.                                             | number, string, date, timestamp |
        | eq                                      | The provided property is exactly equal to the provided value.                                                     | number, string, date, timestamp |
        | isNull                                  | The provided property is (or is not) null.                                                                        | all                             |
        | contains                                | The provided property contains the provided value.                                                                | array                           |
        | not                                     | The sub-query does not match.                                                                                     | N/A (applied on a query)        |
        | and                                     | All the sub-queries match.                                                                                        | N/A (applied on queries)        |
        | or                                      | At least one of the sub-queries match.                                                                            | N/A (applied on queries)        |
        | containsAllTermsInOrderPrefixLastTerm   | The provided property contains all the terms provided in order. The last term can be a partial prefix match.      | string                          |
        | containsAllTermsInOrder                 | The provided property contains the provided term as a substring.                                                  | string                          |
        | containsAnyTerm                         | The provided property contains at least one of the terms separated by whitespace.                                 | string                          |
        | containsAllTerms                        | The provided property contains all the terms separated by whitespace.                                             | string                          |
        | startsWith                              | Deprecated alias for containsAllTermsInOrderPrefixLastTerm.                                                       | string                          |

        Queries can be at most three levels deep. By default, terms are separated by whitespace or punctuation (`?!,:;-[](){}'"~`). Periods (`.`) on their own are ignored.
        Partial terms are not matched by terms filters except where explicitly noted.

        :param ontology:
        :type ontology: OntologyIdentifier
        :param object_type: The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**.
        :type object_type: ObjectTypeApiName
        :param select: The API names of the object type properties to include in the response.
        :type select: List[PropertyApiName]
        :param branch: The Foundry branch to search objects from. If not specified, the default branch will be used.
        :type branch: Optional[FoundryBranch]
        :param exclude_rid: A flag to exclude the retrieval of the `__rid` property. Setting this to true may improve performance of this endpoint for object types in OSV2.
        :type exclude_rid: Optional[bool]
        :param order_by:
        :type order_by: Optional[SearchOrderByV2]
        :param page_size:
        :type page_size: Optional[PageSize]
        :param page_token:
        :type page_token: Optional[PageToken]
        :param sdk_package_rid: The package rid of the generated SDK.
        :type sdk_package_rid: Optional[SdkPackageRid]
        :param sdk_version: The version of the generated SDK.
        :type sdk_version: Optional[SdkVersion]
        :param snapshot: A flag to use snapshot consistency when paging. Setting this to true will give you a consistent view from before you start paging through the results, ensuring you do not get duplicate or missing items. Setting this to false will let new results enter as you page, but you may encounter duplicate or missing items. This defaults to false if not specified, which means you will always get the latest results.
        :type snapshot: Optional[bool]
        :param where:
        :type where: Optional[SearchJsonQueryV2]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[ontologies_models.SearchObjectsResponseV2]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/ontologies/{ontology}/objects/{objectType}/search",
                query_params={
                    "branch": branch,
                    "sdkPackageRid": sdk_package_rid,
                    "sdkVersion": sdk_version,
                },
                path_params={
                    "ontology": ontology,
                    "objectType": object_type,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "where": where,
                    "orderBy": order_by,
                    "pageSize": page_size,
                    "pageToken": page_token,
                    "select": select,
                    "excludeRid": exclude_rid,
                    "snapshot": snapshot,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "where": typing.Optional[ontologies_models.SearchJsonQueryV2],
                        "orderBy": typing.Optional[ontologies_models.SearchOrderByV2],
                        "pageSize": typing.Optional[core_models.PageSize],
                        "pageToken": typing.Optional[core_models.PageToken],
                        "select": typing.List[ontologies_models.PropertyApiName],
                        "excludeRid": typing.Optional[bool],
                        "snapshot": typing.Optional[bool],
                    },
                ),
                response_type=ontologies_models.SearchObjectsResponseV2,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _AsyncOntologyObjectClientRaw:
    def __init__(self, client: AsyncOntologyObjectClient) -> None:
        def aggregate(_: ontologies_models.AggregateObjectsResponseV2): ...
        def count(_: ontologies_models.CountObjectsResponseV2): ...
        def get(_: ontologies_models.OntologyObjectV2): ...
        def list(_: ontologies_models.ListObjectsResponseV2): ...
        def search(_: ontologies_models.SearchObjectsResponseV2): ...

        self.aggregate = core.async_with_raw_response(aggregate, client.aggregate)
        self.count = core.async_with_raw_response(count, client.count)
        self.get = core.async_with_raw_response(get, client.get)
        self.list = core.async_with_raw_response(list, client.list)
        self.search = core.async_with_raw_response(search, client.search)


class _AsyncOntologyObjectClientStreaming:
    def __init__(self, client: AsyncOntologyObjectClient) -> None:
        def aggregate(_: ontologies_models.AggregateObjectsResponseV2): ...
        def count(_: ontologies_models.CountObjectsResponseV2): ...
        def get(_: ontologies_models.OntologyObjectV2): ...
        def list(_: ontologies_models.ListObjectsResponseV2): ...
        def search(_: ontologies_models.SearchObjectsResponseV2): ...

        self.aggregate = core.async_with_streaming_response(aggregate, client.aggregate)
        self.count = core.async_with_streaming_response(count, client.count)
        self.get = core.async_with_streaming_response(get, client.get)
        self.list = core.async_with_streaming_response(list, client.list)
        self.search = core.async_with_streaming_response(search, client.search)
