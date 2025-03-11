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

from foundry import _core as core
from foundry import _errors as errors
from foundry.v2.core import models as core_models
from foundry.v2.ontologies import models as ontologies_models


class OntologyObjectSetClient:
    """
    The API client for the OntologyObjectSet Resource.

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
        self.with_streaming_response = _OntologyObjectSetClientStreaming(
            auth=auth, hostname=hostname, config=config
        )
        self.with_raw_response = _OntologyObjectSetClientRaw(
            auth=auth, hostname=hostname, config=config
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def aggregate(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        *,
        aggregation: typing.List[
            typing.Union[ontologies_models.AggregationV2, ontologies_models.AggregationV2Dict]
        ],
        group_by: typing.List[
            typing.Union[
                ontologies_models.AggregationGroupByV2, ontologies_models.AggregationGroupByV2Dict
            ]
        ],
        object_set: typing.Union[ontologies_models.ObjectSet, ontologies_models.ObjectSetDict],
        accuracy: typing.Optional[ontologies_models.AggregationAccuracyRequest] = None,
        artifact_repository: typing.Optional[ontologies_models.ArtifactRepositoryRid] = None,
        package_name: typing.Optional[ontologies_models.SdkPackageName] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> ontologies_models.AggregateObjectsResponseV2:
        """
        Aggregates the ontology objects present in the `ObjectSet` from the provided object set definition.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

        :param ontology: The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.
        :type ontology: OntologyIdentifier
        :param aggregation:
        :type aggregation: List[Union[AggregationV2, AggregationV2Dict]]
        :param group_by:
        :type group_by: List[Union[AggregationGroupByV2, AggregationGroupByV2Dict]]
        :param object_set:
        :type object_set: Union[ObjectSet, ObjectSetDict]
        :param accuracy:
        :type accuracy: Optional[AggregationAccuracyRequest]
        :param artifact_repository: The repository associated with a marketplace installation.
        :type artifact_repository: Optional[ArtifactRepositoryRid]
        :param package_name: The package name of the generated SDK.
        :type package_name: Optional[SdkPackageName]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ontologies_models.AggregateObjectsResponseV2
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/ontologies/{ontology}/objectSets/aggregate",
                query_params={
                    "artifactRepository": artifact_repository,
                    "packageName": package_name,
                },
                path_params={
                    "ontology": ontology,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "aggregation": aggregation,
                    "objectSet": object_set,
                    "groupBy": group_by,
                    "accuracy": accuracy,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "aggregation": typing.List[
                            typing.Union[
                                ontologies_models.AggregationV2, ontologies_models.AggregationV2Dict
                            ]
                        ],
                        "objectSet": typing.Union[
                            ontologies_models.ObjectSet, ontologies_models.ObjectSetDict
                        ],
                        "groupBy": typing.List[
                            typing.Union[
                                ontologies_models.AggregationGroupByV2,
                                ontologies_models.AggregationGroupByV2Dict,
                            ]
                        ],
                        "accuracy": typing.Optional[ontologies_models.AggregationAccuracyRequest],
                    },
                ),
                response_type=ontologies_models.AggregateObjectsResponseV2,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        ).decode()

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def create_temporary(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        *,
        object_set: typing.Union[ontologies_models.ObjectSet, ontologies_models.ObjectSetDict],
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> ontologies_models.CreateTemporaryObjectSetResponseV2:
        """
        Creates a temporary `ObjectSet` from the given definition. This `ObjectSet` expires after one hour.

        Third-party applications using this endpoint via OAuth2 must request the
        following operation scopes: `api:ontologies-read api:ontologies-write`.

        :param ontology: The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.
        :type ontology: OntologyIdentifier
        :param object_set:
        :type object_set: Union[ObjectSet, ObjectSetDict]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ontologies_models.CreateTemporaryObjectSetResponseV2
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/ontologies/{ontology}/objectSets/createTemporary",
                query_params={},
                path_params={
                    "ontology": ontology,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "objectSet": object_set,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "objectSet": typing.Union[
                            ontologies_models.ObjectSet, ontologies_models.ObjectSetDict
                        ],
                    },
                ),
                response_type=ontologies_models.CreateTemporaryObjectSetResponseV2,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        ).decode()

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        object_set_rid: ontologies_models.ObjectSetRid,
        *,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> ontologies_models.ObjectSet:
        """
        Gets the definition of the `ObjectSet` with the given RID.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

        :param ontology: The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.
        :type ontology: OntologyIdentifier
        :param object_set_rid: The RID of the object set.
        :type object_set_rid: ObjectSetRid
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ontologies_models.ObjectSet
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/ontologies/{ontology}/objectSets/{objectSetRid}",
                query_params={},
                path_params={
                    "ontology": ontology,
                    "objectSetRid": object_set_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ontologies_models.ObjectSet,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        ).decode()

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def load(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        *,
        object_set: typing.Union[ontologies_models.ObjectSet, ontologies_models.ObjectSetDict],
        select: typing.List[ontologies_models.SelectedPropertyApiName],
        artifact_repository: typing.Optional[ontologies_models.ArtifactRepositoryRid] = None,
        exclude_rid: typing.Optional[bool] = None,
        order_by: typing.Optional[
            typing.Union[ontologies_models.SearchOrderByV2, ontologies_models.SearchOrderByV2Dict]
        ] = None,
        package_name: typing.Optional[ontologies_models.SdkPackageName] = None,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> ontologies_models.LoadObjectSetResponseV2:
        """
        Load the ontology objects present in the `ObjectSet` from the provided object set definition.

        For Object Storage V1 backed objects, this endpoint returns a maximum of 10,000 objects. After 10,000 objects have been returned and if more objects
        are available, attempting to load another page will result in an `ObjectsExceededLimit` error being returned. There is no limit on Object Storage V2 backed objects.

        Note that null value properties will not be returned.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

        :param ontology: The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.
        :type ontology: OntologyIdentifier
        :param object_set:
        :type object_set: Union[ObjectSet, ObjectSetDict]
        :param select:
        :type select: List[SelectedPropertyApiName]
        :param artifact_repository: The repository associated with a marketplace installation.
        :type artifact_repository: Optional[ArtifactRepositoryRid]
        :param exclude_rid: A flag to exclude the retrieval of the `__rid` property. Setting this to true may improve performance of this endpoint for object types in OSV2.
        :type exclude_rid: Optional[bool]
        :param order_by:
        :type order_by: Optional[Union[SearchOrderByV2, SearchOrderByV2Dict]]
        :param package_name: The package name of the generated SDK.
        :type package_name: Optional[SdkPackageName]
        :param page_size:
        :type page_size: Optional[PageSize]
        :param page_token:
        :type page_token: Optional[PageToken]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ontologies_models.LoadObjectSetResponseV2
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/ontologies/{ontology}/objectSets/loadObjects",
                query_params={
                    "artifactRepository": artifact_repository,
                    "packageName": package_name,
                },
                path_params={
                    "ontology": ontology,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "objectSet": object_set,
                    "orderBy": order_by,
                    "select": select,
                    "pageToken": page_token,
                    "pageSize": page_size,
                    "excludeRid": exclude_rid,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "objectSet": typing.Union[
                            ontologies_models.ObjectSet, ontologies_models.ObjectSetDict
                        ],
                        "orderBy": typing.Optional[
                            typing.Union[
                                ontologies_models.SearchOrderByV2,
                                ontologies_models.SearchOrderByV2Dict,
                            ]
                        ],
                        "select": typing.List[ontologies_models.SelectedPropertyApiName],
                        "pageToken": typing.Optional[core_models.PageToken],
                        "pageSize": typing.Optional[core_models.PageSize],
                        "excludeRid": typing.Optional[bool],
                    },
                ),
                response_type=ontologies_models.LoadObjectSetResponseV2,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        ).decode()


class _OntologyObjectSetClientRaw:
    """
    The API client for the OntologyObjectSet Resource.

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
    def aggregate(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        *,
        aggregation: typing.List[
            typing.Union[ontologies_models.AggregationV2, ontologies_models.AggregationV2Dict]
        ],
        group_by: typing.List[
            typing.Union[
                ontologies_models.AggregationGroupByV2, ontologies_models.AggregationGroupByV2Dict
            ]
        ],
        object_set: typing.Union[ontologies_models.ObjectSet, ontologies_models.ObjectSetDict],
        accuracy: typing.Optional[ontologies_models.AggregationAccuracyRequest] = None,
        artifact_repository: typing.Optional[ontologies_models.ArtifactRepositoryRid] = None,
        package_name: typing.Optional[ontologies_models.SdkPackageName] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[ontologies_models.AggregateObjectsResponseV2]:
        """
        Aggregates the ontology objects present in the `ObjectSet` from the provided object set definition.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

        :param ontology: The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.
        :type ontology: OntologyIdentifier
        :param aggregation:
        :type aggregation: List[Union[AggregationV2, AggregationV2Dict]]
        :param group_by:
        :type group_by: List[Union[AggregationGroupByV2, AggregationGroupByV2Dict]]
        :param object_set:
        :type object_set: Union[ObjectSet, ObjectSetDict]
        :param accuracy:
        :type accuracy: Optional[AggregationAccuracyRequest]
        :param artifact_repository: The repository associated with a marketplace installation.
        :type artifact_repository: Optional[ArtifactRepositoryRid]
        :param package_name: The package name of the generated SDK.
        :type package_name: Optional[SdkPackageName]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[ontologies_models.AggregateObjectsResponseV2]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/ontologies/{ontology}/objectSets/aggregate",
                query_params={
                    "artifactRepository": artifact_repository,
                    "packageName": package_name,
                },
                path_params={
                    "ontology": ontology,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "aggregation": aggregation,
                    "objectSet": object_set,
                    "groupBy": group_by,
                    "accuracy": accuracy,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "aggregation": typing.List[
                            typing.Union[
                                ontologies_models.AggregationV2, ontologies_models.AggregationV2Dict
                            ]
                        ],
                        "objectSet": typing.Union[
                            ontologies_models.ObjectSet, ontologies_models.ObjectSetDict
                        ],
                        "groupBy": typing.List[
                            typing.Union[
                                ontologies_models.AggregationGroupByV2,
                                ontologies_models.AggregationGroupByV2Dict,
                            ]
                        ],
                        "accuracy": typing.Optional[ontologies_models.AggregationAccuracyRequest],
                    },
                ),
                response_type=ontologies_models.AggregateObjectsResponseV2,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def create_temporary(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        *,
        object_set: typing.Union[ontologies_models.ObjectSet, ontologies_models.ObjectSetDict],
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[ontologies_models.CreateTemporaryObjectSetResponseV2]:
        """
        Creates a temporary `ObjectSet` from the given definition. This `ObjectSet` expires after one hour.

        Third-party applications using this endpoint via OAuth2 must request the
        following operation scopes: `api:ontologies-read api:ontologies-write`.

        :param ontology: The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.
        :type ontology: OntologyIdentifier
        :param object_set:
        :type object_set: Union[ObjectSet, ObjectSetDict]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[ontologies_models.CreateTemporaryObjectSetResponseV2]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/ontologies/{ontology}/objectSets/createTemporary",
                query_params={},
                path_params={
                    "ontology": ontology,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "objectSet": object_set,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "objectSet": typing.Union[
                            ontologies_models.ObjectSet, ontologies_models.ObjectSetDict
                        ],
                    },
                ),
                response_type=ontologies_models.CreateTemporaryObjectSetResponseV2,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        object_set_rid: ontologies_models.ObjectSetRid,
        *,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[ontologies_models.ObjectSet]:
        """
        Gets the definition of the `ObjectSet` with the given RID.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

        :param ontology: The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.
        :type ontology: OntologyIdentifier
        :param object_set_rid: The RID of the object set.
        :type object_set_rid: ObjectSetRid
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[ontologies_models.ObjectSet]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/ontologies/{ontology}/objectSets/{objectSetRid}",
                query_params={},
                path_params={
                    "ontology": ontology,
                    "objectSetRid": object_set_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ontologies_models.ObjectSet,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def load(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        *,
        object_set: typing.Union[ontologies_models.ObjectSet, ontologies_models.ObjectSetDict],
        select: typing.List[ontologies_models.SelectedPropertyApiName],
        artifact_repository: typing.Optional[ontologies_models.ArtifactRepositoryRid] = None,
        exclude_rid: typing.Optional[bool] = None,
        order_by: typing.Optional[
            typing.Union[ontologies_models.SearchOrderByV2, ontologies_models.SearchOrderByV2Dict]
        ] = None,
        package_name: typing.Optional[ontologies_models.SdkPackageName] = None,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[ontologies_models.LoadObjectSetResponseV2]:
        """
        Load the ontology objects present in the `ObjectSet` from the provided object set definition.

        For Object Storage V1 backed objects, this endpoint returns a maximum of 10,000 objects. After 10,000 objects have been returned and if more objects
        are available, attempting to load another page will result in an `ObjectsExceededLimit` error being returned. There is no limit on Object Storage V2 backed objects.

        Note that null value properties will not be returned.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

        :param ontology: The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.
        :type ontology: OntologyIdentifier
        :param object_set:
        :type object_set: Union[ObjectSet, ObjectSetDict]
        :param select:
        :type select: List[SelectedPropertyApiName]
        :param artifact_repository: The repository associated with a marketplace installation.
        :type artifact_repository: Optional[ArtifactRepositoryRid]
        :param exclude_rid: A flag to exclude the retrieval of the `__rid` property. Setting this to true may improve performance of this endpoint for object types in OSV2.
        :type exclude_rid: Optional[bool]
        :param order_by:
        :type order_by: Optional[Union[SearchOrderByV2, SearchOrderByV2Dict]]
        :param package_name: The package name of the generated SDK.
        :type package_name: Optional[SdkPackageName]
        :param page_size:
        :type page_size: Optional[PageSize]
        :param page_token:
        :type page_token: Optional[PageToken]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[ontologies_models.LoadObjectSetResponseV2]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/ontologies/{ontology}/objectSets/loadObjects",
                query_params={
                    "artifactRepository": artifact_repository,
                    "packageName": package_name,
                },
                path_params={
                    "ontology": ontology,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "objectSet": object_set,
                    "orderBy": order_by,
                    "select": select,
                    "pageToken": page_token,
                    "pageSize": page_size,
                    "excludeRid": exclude_rid,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "objectSet": typing.Union[
                            ontologies_models.ObjectSet, ontologies_models.ObjectSetDict
                        ],
                        "orderBy": typing.Optional[
                            typing.Union[
                                ontologies_models.SearchOrderByV2,
                                ontologies_models.SearchOrderByV2Dict,
                            ]
                        ],
                        "select": typing.List[ontologies_models.SelectedPropertyApiName],
                        "pageToken": typing.Optional[core_models.PageToken],
                        "pageSize": typing.Optional[core_models.PageSize],
                        "excludeRid": typing.Optional[bool],
                    },
                ),
                response_type=ontologies_models.LoadObjectSetResponseV2,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )


class _OntologyObjectSetClientStreaming:
    """
    The API client for the OntologyObjectSet Resource.

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
    def aggregate(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        *,
        aggregation: typing.List[
            typing.Union[ontologies_models.AggregationV2, ontologies_models.AggregationV2Dict]
        ],
        group_by: typing.List[
            typing.Union[
                ontologies_models.AggregationGroupByV2, ontologies_models.AggregationGroupByV2Dict
            ]
        ],
        object_set: typing.Union[ontologies_models.ObjectSet, ontologies_models.ObjectSetDict],
        accuracy: typing.Optional[ontologies_models.AggregationAccuracyRequest] = None,
        artifact_repository: typing.Optional[ontologies_models.ArtifactRepositoryRid] = None,
        package_name: typing.Optional[ontologies_models.SdkPackageName] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[ontologies_models.AggregateObjectsResponseV2]:
        """
        Aggregates the ontology objects present in the `ObjectSet` from the provided object set definition.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

        :param ontology: The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.
        :type ontology: OntologyIdentifier
        :param aggregation:
        :type aggregation: List[Union[AggregationV2, AggregationV2Dict]]
        :param group_by:
        :type group_by: List[Union[AggregationGroupByV2, AggregationGroupByV2Dict]]
        :param object_set:
        :type object_set: Union[ObjectSet, ObjectSetDict]
        :param accuracy:
        :type accuracy: Optional[AggregationAccuracyRequest]
        :param artifact_repository: The repository associated with a marketplace installation.
        :type artifact_repository: Optional[ArtifactRepositoryRid]
        :param package_name: The package name of the generated SDK.
        :type package_name: Optional[SdkPackageName]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[ontologies_models.AggregateObjectsResponseV2]
        """

        return self._api_client.stream_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/ontologies/{ontology}/objectSets/aggregate",
                query_params={
                    "artifactRepository": artifact_repository,
                    "packageName": package_name,
                },
                path_params={
                    "ontology": ontology,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "aggregation": aggregation,
                    "objectSet": object_set,
                    "groupBy": group_by,
                    "accuracy": accuracy,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "aggregation": typing.List[
                            typing.Union[
                                ontologies_models.AggregationV2, ontologies_models.AggregationV2Dict
                            ]
                        ],
                        "objectSet": typing.Union[
                            ontologies_models.ObjectSet, ontologies_models.ObjectSetDict
                        ],
                        "groupBy": typing.List[
                            typing.Union[
                                ontologies_models.AggregationGroupByV2,
                                ontologies_models.AggregationGroupByV2Dict,
                            ]
                        ],
                        "accuracy": typing.Optional[ontologies_models.AggregationAccuracyRequest],
                    },
                ),
                response_type=ontologies_models.AggregateObjectsResponseV2,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def create_temporary(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        *,
        object_set: typing.Union[ontologies_models.ObjectSet, ontologies_models.ObjectSetDict],
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[ontologies_models.CreateTemporaryObjectSetResponseV2]:
        """
        Creates a temporary `ObjectSet` from the given definition. This `ObjectSet` expires after one hour.

        Third-party applications using this endpoint via OAuth2 must request the
        following operation scopes: `api:ontologies-read api:ontologies-write`.

        :param ontology: The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.
        :type ontology: OntologyIdentifier
        :param object_set:
        :type object_set: Union[ObjectSet, ObjectSetDict]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[ontologies_models.CreateTemporaryObjectSetResponseV2]
        """

        return self._api_client.stream_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/ontologies/{ontology}/objectSets/createTemporary",
                query_params={},
                path_params={
                    "ontology": ontology,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "objectSet": object_set,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "objectSet": typing.Union[
                            ontologies_models.ObjectSet, ontologies_models.ObjectSetDict
                        ],
                    },
                ),
                response_type=ontologies_models.CreateTemporaryObjectSetResponseV2,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        object_set_rid: ontologies_models.ObjectSetRid,
        *,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[ontologies_models.ObjectSet]:
        """
        Gets the definition of the `ObjectSet` with the given RID.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

        :param ontology: The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.
        :type ontology: OntologyIdentifier
        :param object_set_rid: The RID of the object set.
        :type object_set_rid: ObjectSetRid
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[ontologies_models.ObjectSet]
        """

        return self._api_client.stream_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/ontologies/{ontology}/objectSets/{objectSetRid}",
                query_params={},
                path_params={
                    "ontology": ontology,
                    "objectSetRid": object_set_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ontologies_models.ObjectSet,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def load(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        *,
        object_set: typing.Union[ontologies_models.ObjectSet, ontologies_models.ObjectSetDict],
        select: typing.List[ontologies_models.SelectedPropertyApiName],
        artifact_repository: typing.Optional[ontologies_models.ArtifactRepositoryRid] = None,
        exclude_rid: typing.Optional[bool] = None,
        order_by: typing.Optional[
            typing.Union[ontologies_models.SearchOrderByV2, ontologies_models.SearchOrderByV2Dict]
        ] = None,
        package_name: typing.Optional[ontologies_models.SdkPackageName] = None,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[ontologies_models.LoadObjectSetResponseV2]:
        """
        Load the ontology objects present in the `ObjectSet` from the provided object set definition.

        For Object Storage V1 backed objects, this endpoint returns a maximum of 10,000 objects. After 10,000 objects have been returned and if more objects
        are available, attempting to load another page will result in an `ObjectsExceededLimit` error being returned. There is no limit on Object Storage V2 backed objects.

        Note that null value properties will not be returned.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

        :param ontology: The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.
        :type ontology: OntologyIdentifier
        :param object_set:
        :type object_set: Union[ObjectSet, ObjectSetDict]
        :param select:
        :type select: List[SelectedPropertyApiName]
        :param artifact_repository: The repository associated with a marketplace installation.
        :type artifact_repository: Optional[ArtifactRepositoryRid]
        :param exclude_rid: A flag to exclude the retrieval of the `__rid` property. Setting this to true may improve performance of this endpoint for object types in OSV2.
        :type exclude_rid: Optional[bool]
        :param order_by:
        :type order_by: Optional[Union[SearchOrderByV2, SearchOrderByV2Dict]]
        :param package_name: The package name of the generated SDK.
        :type package_name: Optional[SdkPackageName]
        :param page_size:
        :type page_size: Optional[PageSize]
        :param page_token:
        :type page_token: Optional[PageToken]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[ontologies_models.LoadObjectSetResponseV2]
        """

        return self._api_client.stream_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/ontologies/{ontology}/objectSets/loadObjects",
                query_params={
                    "artifactRepository": artifact_repository,
                    "packageName": package_name,
                },
                path_params={
                    "ontology": ontology,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "objectSet": object_set,
                    "orderBy": order_by,
                    "select": select,
                    "pageToken": page_token,
                    "pageSize": page_size,
                    "excludeRid": exclude_rid,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "objectSet": typing.Union[
                            ontologies_models.ObjectSet, ontologies_models.ObjectSetDict
                        ],
                        "orderBy": typing.Optional[
                            typing.Union[
                                ontologies_models.SearchOrderByV2,
                                ontologies_models.SearchOrderByV2Dict,
                            ]
                        ],
                        "select": typing.List[ontologies_models.SelectedPropertyApiName],
                        "pageToken": typing.Optional[core_models.PageToken],
                        "pageSize": typing.Optional[core_models.PageSize],
                        "excludeRid": typing.Optional[bool],
                    },
                ),
                response_type=ontologies_models.LoadObjectSetResponseV2,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )
