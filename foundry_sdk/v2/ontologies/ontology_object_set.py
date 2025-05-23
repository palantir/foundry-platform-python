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

        self.with_streaming_response = _OntologyObjectSetClientStreaming(self)
        self.with_raw_response = _OntologyObjectSetClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def aggregate(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        *,
        aggregation: typing.List[ontologies_models.AggregationV2],
        group_by: typing.List[ontologies_models.AggregationGroupByV2],
        object_set: ontologies_models.ObjectSet,
        accuracy: typing.Optional[ontologies_models.AggregationAccuracyRequest] = None,
        artifact_repository: typing.Optional[ontologies_models.ArtifactRepositoryRid] = None,
        package_name: typing.Optional[ontologies_models.SdkPackageName] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> ontologies_models.AggregateObjectsResponseV2:
        """
        Aggregates the ontology objects present in the `ObjectSet` from the provided object set definition.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

        :param ontology: The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.
        :type ontology: OntologyIdentifier
        :param aggregation:
        :type aggregation: List[AggregationV2]
        :param group_by:
        :type group_by: List[AggregationGroupByV2]
        :param object_set:
        :type object_set: ObjectSet
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
                        "aggregation": typing.List[ontologies_models.AggregationV2],
                        "objectSet": ontologies_models.ObjectSet,
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
    def create_temporary(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        *,
        object_set: ontologies_models.ObjectSet,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> ontologies_models.CreateTemporaryObjectSetResponseV2:
        """
        Creates a temporary `ObjectSet` from the given definition. This `ObjectSet` expires after one hour.

        Third-party applications using this endpoint via OAuth2 must request the
        following operation scopes: `api:ontologies-read api:ontologies-write`.

        :param ontology: The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.
        :type ontology: OntologyIdentifier
        :param object_set:
        :type object_set: ObjectSet
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
                        "objectSet": ontologies_models.ObjectSet,
                    },
                ),
                response_type=ontologies_models.CreateTemporaryObjectSetResponseV2,
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
        object_set_rid: ontologies_models.ObjectSetRid,
        *,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
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
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def load(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        *,
        object_set: ontologies_models.ObjectSet,
        select: typing.List[ontologies_models.SelectedPropertyApiName],
        artifact_repository: typing.Optional[ontologies_models.ArtifactRepositoryRid] = None,
        exclude_rid: typing.Optional[bool] = None,
        order_by: typing.Optional[ontologies_models.SearchOrderByV2] = None,
        package_name: typing.Optional[ontologies_models.SdkPackageName] = None,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> ontologies_models.LoadObjectSetResponseV2:
        """
        Load the ontology objects present in the `ObjectSet` from the provided object set definition.

        For Object Storage V1 backed objects, this endpoint returns a maximum of 10,000 objects. After 10,000 objects have been returned and if more objects
        are available, attempting to load another page will result in an `ObjectsExceededLimit` error being returned. There is no limit on Object Storage V2 backed objects.

        Note that null value properties will not be returned.

        Vector properties will not be returned unless included in the `select` parameter.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

        :param ontology: The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.
        :type ontology: OntologyIdentifier
        :param object_set:
        :type object_set: ObjectSet
        :param select:
        :type select: List[SelectedPropertyApiName]
        :param artifact_repository: The repository associated with a marketplace installation.
        :type artifact_repository: Optional[ArtifactRepositoryRid]
        :param exclude_rid: A flag to exclude the retrieval of the `__rid` property. Setting this to true may improve performance of this endpoint for object types in OSV2.
        :type exclude_rid: Optional[bool]
        :param order_by:
        :type order_by: Optional[SearchOrderByV2]
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
                        "objectSet": ontologies_models.ObjectSet,
                        "orderBy": typing.Optional[ontologies_models.SearchOrderByV2],
                        "select": typing.List[ontologies_models.SelectedPropertyApiName],
                        "pageToken": typing.Optional[core_models.PageToken],
                        "pageSize": typing.Optional[core_models.PageSize],
                        "excludeRid": typing.Optional[bool],
                    },
                ),
                response_type=ontologies_models.LoadObjectSetResponseV2,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def load_multiple_object_types(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        *,
        object_set: ontologies_models.ObjectSet,
        select: typing.List[ontologies_models.SelectedPropertyApiName],
        artifact_repository: typing.Optional[ontologies_models.ArtifactRepositoryRid] = None,
        exclude_rid: typing.Optional[bool] = None,
        order_by: typing.Optional[ontologies_models.SearchOrderByV2] = None,
        package_name: typing.Optional[ontologies_models.SdkPackageName] = None,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> ontologies_models.LoadObjectSetV2MultipleObjectTypesResponse:
        """
        Load the ontology objects present in the `ObjectSet` from the provided object set definition. The resulting
        objects may be scoped to an object type, in which all the selected properties on the object type are returned, or scoped
        to an interface, in which only the object type properties that implement the properties of any interfaces in its
        scope are returned. For objects that are scoped to an interface in the result, a mapping from interface to
        object implementation is returned in order to interpret the objects as the interfaces that they implement.

        For Object Storage V1 backed objects, this endpoint returns a maximum of 10,000 objects. After 10,000 objects have been returned and if more objects
        are available, attempting to load another page will result in an `ObjectsExceededLimit` error being returned. There is no limit on Object Storage V2 backed objects.

        Note that null value properties will not be returned. In addition, property metadata (rid, apiName, and primaryKey)
        will be prefixed with '$' instead of '__' as is the case in `loadObjects`.

        Vector properties will not be returned unless included in the `select` parameter.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

        :param ontology: The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.
        :type ontology: OntologyIdentifier
        :param object_set:
        :type object_set: ObjectSet
        :param select:
        :type select: List[SelectedPropertyApiName]
        :param artifact_repository: The repository associated with a marketplace installation.
        :type artifact_repository: Optional[ArtifactRepositoryRid]
        :param exclude_rid: A flag to exclude the retrieval of the `$rid` property. Setting this to true may improve performance of this endpoint for object types in OSV2.
        :type exclude_rid: Optional[bool]
        :param order_by:
        :type order_by: Optional[SearchOrderByV2]
        :param package_name: The package name of the generated SDK.
        :type package_name: Optional[SdkPackageName]
        :param page_size:
        :type page_size: Optional[PageSize]
        :param page_token:
        :type page_token: Optional[PageToken]
        :param preview: A boolean flag that, when set to true, enables the use of beta features in preview mode.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ontologies_models.LoadObjectSetV2MultipleObjectTypesResponse
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/ontologies/{ontology}/objectSets/loadObjectsMultipleObjectTypes",
                query_params={
                    "artifactRepository": artifact_repository,
                    "packageName": package_name,
                    "preview": preview,
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
                        "objectSet": ontologies_models.ObjectSet,
                        "orderBy": typing.Optional[ontologies_models.SearchOrderByV2],
                        "select": typing.List[ontologies_models.SelectedPropertyApiName],
                        "pageToken": typing.Optional[core_models.PageToken],
                        "pageSize": typing.Optional[core_models.PageSize],
                        "excludeRid": typing.Optional[bool],
                    },
                ),
                response_type=ontologies_models.LoadObjectSetV2MultipleObjectTypesResponse,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def load_objects_or_interfaces(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        *,
        object_set: ontologies_models.ObjectSet,
        select: typing.List[ontologies_models.SelectedPropertyApiName],
        artifact_repository: typing.Optional[ontologies_models.ArtifactRepositoryRid] = None,
        exclude_rid: typing.Optional[bool] = None,
        order_by: typing.Optional[ontologies_models.SearchOrderByV2] = None,
        package_name: typing.Optional[ontologies_models.SdkPackageName] = None,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> ontologies_models.LoadObjectSetV2ObjectsOrInterfacesResponse:
        """
        Load the ontology objects present in the `ObjectSet` from the provided object set definition. If the requested
        object set contains interfaces and the object can be viewed as an interface, it will contain the properties
        defined by the interface. If not, it will contain the properties defined by its object type. This allows directly
        loading all objects of an interface where all objects are viewed as the interface, for example.

        Note that the result object set cannot contain a mix of objects with "interface" properties and "object type"
        properties. Attempting to load an object set like this will result in an error.

        For Object Storage V1 backed objects, this endpoint returns a maximum of 10,000 objects. After 10,000 objects have been returned and if more objects
        are available, attempting to load another page will result in an `ObjectsExceededLimit` error being returned. There is no limit on Object Storage V2 backed objects.

        Note that null value properties will not be returned. In addition, property metadata (rid, apiName, and primaryKey)
        will be prefixed with '$' instead of '__' as is the case in `/loadObjects`.

        Vector properties will not be returned unless included in the `select` parameter.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

        :param ontology: The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.
        :type ontology: OntologyIdentifier
        :param object_set:
        :type object_set: ObjectSet
        :param select:
        :type select: List[SelectedPropertyApiName]
        :param artifact_repository: The repository associated with a marketplace installation.
        :type artifact_repository: Optional[ArtifactRepositoryRid]
        :param exclude_rid: A flag to exclude the retrieval of the `$rid` property. Setting this to true may improve performance of this endpoint for object types in OSV2.
        :type exclude_rid: Optional[bool]
        :param order_by:
        :type order_by: Optional[SearchOrderByV2]
        :param package_name: The package name of the generated SDK.
        :type package_name: Optional[SdkPackageName]
        :param page_size:
        :type page_size: Optional[PageSize]
        :param page_token:
        :type page_token: Optional[PageToken]
        :param preview: A boolean flag that, when set to true, enables the use of beta features in preview mode.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ontologies_models.LoadObjectSetV2ObjectsOrInterfacesResponse
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/ontologies/{ontology}/objectSets/loadObjectsOrInterfaces",
                query_params={
                    "artifactRepository": artifact_repository,
                    "packageName": package_name,
                    "preview": preview,
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
                        "objectSet": ontologies_models.ObjectSet,
                        "orderBy": typing.Optional[ontologies_models.SearchOrderByV2],
                        "select": typing.List[ontologies_models.SelectedPropertyApiName],
                        "pageToken": typing.Optional[core_models.PageToken],
                        "pageSize": typing.Optional[core_models.PageSize],
                        "excludeRid": typing.Optional[bool],
                    },
                ),
                response_type=ontologies_models.LoadObjectSetV2ObjectsOrInterfacesResponse,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _OntologyObjectSetClientRaw:
    def __init__(self, client: OntologyObjectSetClient) -> None:
        def aggregate(_: ontologies_models.AggregateObjectsResponseV2): ...
        def create_temporary(_: ontologies_models.CreateTemporaryObjectSetResponseV2): ...
        def get(_: ontologies_models.ObjectSet): ...
        def load(_: ontologies_models.LoadObjectSetResponseV2): ...
        def load_multiple_object_types(
            _: ontologies_models.LoadObjectSetV2MultipleObjectTypesResponse,
        ): ...
        def load_objects_or_interfaces(
            _: ontologies_models.LoadObjectSetV2ObjectsOrInterfacesResponse,
        ): ...

        self.aggregate = core.with_raw_response(aggregate, client.aggregate)
        self.create_temporary = core.with_raw_response(create_temporary, client.create_temporary)
        self.get = core.with_raw_response(get, client.get)
        self.load = core.with_raw_response(load, client.load)
        self.load_multiple_object_types = core.with_raw_response(
            load_multiple_object_types, client.load_multiple_object_types
        )
        self.load_objects_or_interfaces = core.with_raw_response(
            load_objects_or_interfaces, client.load_objects_or_interfaces
        )


class _OntologyObjectSetClientStreaming:
    def __init__(self, client: OntologyObjectSetClient) -> None:
        def aggregate(_: ontologies_models.AggregateObjectsResponseV2): ...
        def create_temporary(_: ontologies_models.CreateTemporaryObjectSetResponseV2): ...
        def get(_: ontologies_models.ObjectSet): ...
        def load(_: ontologies_models.LoadObjectSetResponseV2): ...
        def load_multiple_object_types(
            _: ontologies_models.LoadObjectSetV2MultipleObjectTypesResponse,
        ): ...
        def load_objects_or_interfaces(
            _: ontologies_models.LoadObjectSetV2ObjectsOrInterfacesResponse,
        ): ...

        self.aggregate = core.with_streaming_response(aggregate, client.aggregate)
        self.create_temporary = core.with_streaming_response(
            create_temporary, client.create_temporary
        )
        self.get = core.with_streaming_response(get, client.get)
        self.load = core.with_streaming_response(load, client.load)
        self.load_multiple_object_types = core.with_streaming_response(
            load_multiple_object_types, client.load_multiple_object_types
        )
        self.load_objects_or_interfaces = core.with_streaming_response(
            load_objects_or_interfaces, client.load_objects_or_interfaces
        )


class AsyncOntologyObjectSetClient:
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
        self._api_client = core.AsyncApiClient(auth=auth, hostname=hostname, config=config)

        self.with_streaming_response = _AsyncOntologyObjectSetClientStreaming(self)
        self.with_raw_response = _AsyncOntologyObjectSetClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def aggregate(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        *,
        aggregation: typing.List[ontologies_models.AggregationV2],
        group_by: typing.List[ontologies_models.AggregationGroupByV2],
        object_set: ontologies_models.ObjectSet,
        accuracy: typing.Optional[ontologies_models.AggregationAccuracyRequest] = None,
        artifact_repository: typing.Optional[ontologies_models.ArtifactRepositoryRid] = None,
        package_name: typing.Optional[ontologies_models.SdkPackageName] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[ontologies_models.AggregateObjectsResponseV2]:
        """
        Aggregates the ontology objects present in the `ObjectSet` from the provided object set definition.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

        :param ontology: The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.
        :type ontology: OntologyIdentifier
        :param aggregation:
        :type aggregation: List[AggregationV2]
        :param group_by:
        :type group_by: List[AggregationGroupByV2]
        :param object_set:
        :type object_set: ObjectSet
        :param accuracy:
        :type accuracy: Optional[AggregationAccuracyRequest]
        :param artifact_repository: The repository associated with a marketplace installation.
        :type artifact_repository: Optional[ArtifactRepositoryRid]
        :param package_name: The package name of the generated SDK.
        :type package_name: Optional[SdkPackageName]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[ontologies_models.AggregateObjectsResponseV2]
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
                        "aggregation": typing.List[ontologies_models.AggregationV2],
                        "objectSet": ontologies_models.ObjectSet,
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
    def create_temporary(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        *,
        object_set: ontologies_models.ObjectSet,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[ontologies_models.CreateTemporaryObjectSetResponseV2]:
        """
        Creates a temporary `ObjectSet` from the given definition. This `ObjectSet` expires after one hour.

        Third-party applications using this endpoint via OAuth2 must request the
        following operation scopes: `api:ontologies-read api:ontologies-write`.

        :param ontology: The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.
        :type ontology: OntologyIdentifier
        :param object_set:
        :type object_set: ObjectSet
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[ontologies_models.CreateTemporaryObjectSetResponseV2]
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
                        "objectSet": ontologies_models.ObjectSet,
                    },
                ),
                response_type=ontologies_models.CreateTemporaryObjectSetResponseV2,
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
        object_set_rid: ontologies_models.ObjectSetRid,
        *,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[ontologies_models.ObjectSet]:
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
        :rtype: typing.Awaitable[ontologies_models.ObjectSet]
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
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def load(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        *,
        object_set: ontologies_models.ObjectSet,
        select: typing.List[ontologies_models.SelectedPropertyApiName],
        artifact_repository: typing.Optional[ontologies_models.ArtifactRepositoryRid] = None,
        exclude_rid: typing.Optional[bool] = None,
        order_by: typing.Optional[ontologies_models.SearchOrderByV2] = None,
        package_name: typing.Optional[ontologies_models.SdkPackageName] = None,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[ontologies_models.LoadObjectSetResponseV2]:
        """
        Load the ontology objects present in the `ObjectSet` from the provided object set definition.

        For Object Storage V1 backed objects, this endpoint returns a maximum of 10,000 objects. After 10,000 objects have been returned and if more objects
        are available, attempting to load another page will result in an `ObjectsExceededLimit` error being returned. There is no limit on Object Storage V2 backed objects.

        Note that null value properties will not be returned.

        Vector properties will not be returned unless included in the `select` parameter.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

        :param ontology: The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.
        :type ontology: OntologyIdentifier
        :param object_set:
        :type object_set: ObjectSet
        :param select:
        :type select: List[SelectedPropertyApiName]
        :param artifact_repository: The repository associated with a marketplace installation.
        :type artifact_repository: Optional[ArtifactRepositoryRid]
        :param exclude_rid: A flag to exclude the retrieval of the `__rid` property. Setting this to true may improve performance of this endpoint for object types in OSV2.
        :type exclude_rid: Optional[bool]
        :param order_by:
        :type order_by: Optional[SearchOrderByV2]
        :param package_name: The package name of the generated SDK.
        :type package_name: Optional[SdkPackageName]
        :param page_size:
        :type page_size: Optional[PageSize]
        :param page_token:
        :type page_token: Optional[PageToken]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[ontologies_models.LoadObjectSetResponseV2]
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
                        "objectSet": ontologies_models.ObjectSet,
                        "orderBy": typing.Optional[ontologies_models.SearchOrderByV2],
                        "select": typing.List[ontologies_models.SelectedPropertyApiName],
                        "pageToken": typing.Optional[core_models.PageToken],
                        "pageSize": typing.Optional[core_models.PageSize],
                        "excludeRid": typing.Optional[bool],
                    },
                ),
                response_type=ontologies_models.LoadObjectSetResponseV2,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def load_multiple_object_types(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        *,
        object_set: ontologies_models.ObjectSet,
        select: typing.List[ontologies_models.SelectedPropertyApiName],
        artifact_repository: typing.Optional[ontologies_models.ArtifactRepositoryRid] = None,
        exclude_rid: typing.Optional[bool] = None,
        order_by: typing.Optional[ontologies_models.SearchOrderByV2] = None,
        package_name: typing.Optional[ontologies_models.SdkPackageName] = None,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[ontologies_models.LoadObjectSetV2MultipleObjectTypesResponse]:
        """
        Load the ontology objects present in the `ObjectSet` from the provided object set definition. The resulting
        objects may be scoped to an object type, in which all the selected properties on the object type are returned, or scoped
        to an interface, in which only the object type properties that implement the properties of any interfaces in its
        scope are returned. For objects that are scoped to an interface in the result, a mapping from interface to
        object implementation is returned in order to interpret the objects as the interfaces that they implement.

        For Object Storage V1 backed objects, this endpoint returns a maximum of 10,000 objects. After 10,000 objects have been returned and if more objects
        are available, attempting to load another page will result in an `ObjectsExceededLimit` error being returned. There is no limit on Object Storage V2 backed objects.

        Note that null value properties will not be returned. In addition, property metadata (rid, apiName, and primaryKey)
        will be prefixed with '$' instead of '__' as is the case in `loadObjects`.

        Vector properties will not be returned unless included in the `select` parameter.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

        :param ontology: The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.
        :type ontology: OntologyIdentifier
        :param object_set:
        :type object_set: ObjectSet
        :param select:
        :type select: List[SelectedPropertyApiName]
        :param artifact_repository: The repository associated with a marketplace installation.
        :type artifact_repository: Optional[ArtifactRepositoryRid]
        :param exclude_rid: A flag to exclude the retrieval of the `$rid` property. Setting this to true may improve performance of this endpoint for object types in OSV2.
        :type exclude_rid: Optional[bool]
        :param order_by:
        :type order_by: Optional[SearchOrderByV2]
        :param package_name: The package name of the generated SDK.
        :type package_name: Optional[SdkPackageName]
        :param page_size:
        :type page_size: Optional[PageSize]
        :param page_token:
        :type page_token: Optional[PageToken]
        :param preview: A boolean flag that, when set to true, enables the use of beta features in preview mode.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[ontologies_models.LoadObjectSetV2MultipleObjectTypesResponse]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/ontologies/{ontology}/objectSets/loadObjectsMultipleObjectTypes",
                query_params={
                    "artifactRepository": artifact_repository,
                    "packageName": package_name,
                    "preview": preview,
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
                        "objectSet": ontologies_models.ObjectSet,
                        "orderBy": typing.Optional[ontologies_models.SearchOrderByV2],
                        "select": typing.List[ontologies_models.SelectedPropertyApiName],
                        "pageToken": typing.Optional[core_models.PageToken],
                        "pageSize": typing.Optional[core_models.PageSize],
                        "excludeRid": typing.Optional[bool],
                    },
                ),
                response_type=ontologies_models.LoadObjectSetV2MultipleObjectTypesResponse,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def load_objects_or_interfaces(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        *,
        object_set: ontologies_models.ObjectSet,
        select: typing.List[ontologies_models.SelectedPropertyApiName],
        artifact_repository: typing.Optional[ontologies_models.ArtifactRepositoryRid] = None,
        exclude_rid: typing.Optional[bool] = None,
        order_by: typing.Optional[ontologies_models.SearchOrderByV2] = None,
        package_name: typing.Optional[ontologies_models.SdkPackageName] = None,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[ontologies_models.LoadObjectSetV2ObjectsOrInterfacesResponse]:
        """
        Load the ontology objects present in the `ObjectSet` from the provided object set definition. If the requested
        object set contains interfaces and the object can be viewed as an interface, it will contain the properties
        defined by the interface. If not, it will contain the properties defined by its object type. This allows directly
        loading all objects of an interface where all objects are viewed as the interface, for example.

        Note that the result object set cannot contain a mix of objects with "interface" properties and "object type"
        properties. Attempting to load an object set like this will result in an error.

        For Object Storage V1 backed objects, this endpoint returns a maximum of 10,000 objects. After 10,000 objects have been returned and if more objects
        are available, attempting to load another page will result in an `ObjectsExceededLimit` error being returned. There is no limit on Object Storage V2 backed objects.

        Note that null value properties will not be returned. In addition, property metadata (rid, apiName, and primaryKey)
        will be prefixed with '$' instead of '__' as is the case in `/loadObjects`.

        Vector properties will not be returned unless included in the `select` parameter.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

        :param ontology: The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.
        :type ontology: OntologyIdentifier
        :param object_set:
        :type object_set: ObjectSet
        :param select:
        :type select: List[SelectedPropertyApiName]
        :param artifact_repository: The repository associated with a marketplace installation.
        :type artifact_repository: Optional[ArtifactRepositoryRid]
        :param exclude_rid: A flag to exclude the retrieval of the `$rid` property. Setting this to true may improve performance of this endpoint for object types in OSV2.
        :type exclude_rid: Optional[bool]
        :param order_by:
        :type order_by: Optional[SearchOrderByV2]
        :param package_name: The package name of the generated SDK.
        :type package_name: Optional[SdkPackageName]
        :param page_size:
        :type page_size: Optional[PageSize]
        :param page_token:
        :type page_token: Optional[PageToken]
        :param preview: A boolean flag that, when set to true, enables the use of beta features in preview mode.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[ontologies_models.LoadObjectSetV2ObjectsOrInterfacesResponse]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/ontologies/{ontology}/objectSets/loadObjectsOrInterfaces",
                query_params={
                    "artifactRepository": artifact_repository,
                    "packageName": package_name,
                    "preview": preview,
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
                        "objectSet": ontologies_models.ObjectSet,
                        "orderBy": typing.Optional[ontologies_models.SearchOrderByV2],
                        "select": typing.List[ontologies_models.SelectedPropertyApiName],
                        "pageToken": typing.Optional[core_models.PageToken],
                        "pageSize": typing.Optional[core_models.PageSize],
                        "excludeRid": typing.Optional[bool],
                    },
                ),
                response_type=ontologies_models.LoadObjectSetV2ObjectsOrInterfacesResponse,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _AsyncOntologyObjectSetClientRaw:
    def __init__(self, client: AsyncOntologyObjectSetClient) -> None:
        def aggregate(_: ontologies_models.AggregateObjectsResponseV2): ...
        def create_temporary(_: ontologies_models.CreateTemporaryObjectSetResponseV2): ...
        def get(_: ontologies_models.ObjectSet): ...
        def load(_: ontologies_models.LoadObjectSetResponseV2): ...
        def load_multiple_object_types(
            _: ontologies_models.LoadObjectSetV2MultipleObjectTypesResponse,
        ): ...
        def load_objects_or_interfaces(
            _: ontologies_models.LoadObjectSetV2ObjectsOrInterfacesResponse,
        ): ...

        self.aggregate = core.async_with_raw_response(aggregate, client.aggregate)
        self.create_temporary = core.async_with_raw_response(
            create_temporary, client.create_temporary
        )
        self.get = core.async_with_raw_response(get, client.get)
        self.load = core.async_with_raw_response(load, client.load)
        self.load_multiple_object_types = core.async_with_raw_response(
            load_multiple_object_types, client.load_multiple_object_types
        )
        self.load_objects_or_interfaces = core.async_with_raw_response(
            load_objects_or_interfaces, client.load_objects_or_interfaces
        )


class _AsyncOntologyObjectSetClientStreaming:
    def __init__(self, client: AsyncOntologyObjectSetClient) -> None:
        def aggregate(_: ontologies_models.AggregateObjectsResponseV2): ...
        def create_temporary(_: ontologies_models.CreateTemporaryObjectSetResponseV2): ...
        def get(_: ontologies_models.ObjectSet): ...
        def load(_: ontologies_models.LoadObjectSetResponseV2): ...
        def load_multiple_object_types(
            _: ontologies_models.LoadObjectSetV2MultipleObjectTypesResponse,
        ): ...
        def load_objects_or_interfaces(
            _: ontologies_models.LoadObjectSetV2ObjectsOrInterfacesResponse,
        ): ...

        self.aggregate = core.async_with_streaming_response(aggregate, client.aggregate)
        self.create_temporary = core.async_with_streaming_response(
            create_temporary, client.create_temporary
        )
        self.get = core.async_with_streaming_response(get, client.get)
        self.load = core.async_with_streaming_response(load, client.load)
        self.load_multiple_object_types = core.async_with_streaming_response(
            load_multiple_object_types, client.load_multiple_object_types
        )
        self.load_objects_or_interfaces = core.async_with_streaming_response(
            load_objects_or_interfaces, client.load_objects_or_interfaces
        )
