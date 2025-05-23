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


class LinkedObjectClient:
    """
    The API client for the LinkedObject Resource.

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

        self.with_streaming_response = _LinkedObjectClientStreaming(self)
        self.with_raw_response = _LinkedObjectClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get_linked_object(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        object_type: ontologies_models.ObjectTypeApiName,
        primary_key: ontologies_models.PropertyValueEscapedString,
        link_type: ontologies_models.LinkTypeApiName,
        linked_object_primary_key: ontologies_models.PropertyValueEscapedString,
        *,
        artifact_repository: typing.Optional[ontologies_models.ArtifactRepositoryRid] = None,
        exclude_rid: typing.Optional[bool] = None,
        package_name: typing.Optional[ontologies_models.SdkPackageName] = None,
        select: typing.Optional[typing.List[ontologies_models.SelectedPropertyApiName]] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> ontologies_models.OntologyObjectV2:
        """
        Get a specific linked object that originates from another object.

        If there is no link between the two objects, `LinkedObjectNotFound` is thrown.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

        :param ontology: The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.
        :type ontology: OntologyIdentifier
        :param object_type: The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**.
        :type object_type: ObjectTypeApiName
        :param primary_key: The primary key of the object from which the links originate. To look up the expected primary key for your object type, use the `Get object type` endpoint or the **Ontology Manager**.
        :type primary_key: PropertyValueEscapedString
        :param link_type: The API name of the link that exists between the object and the requested objects. To find the API name for your link type, check the **Ontology Manager**.
        :type link_type: LinkTypeApiName
        :param linked_object_primary_key: The primary key of the requested linked object. To look up the expected primary key for your object type, use the `Get object type` endpoint (passing the linked object type) or the **Ontology Manager**.
        :type linked_object_primary_key: PropertyValueEscapedString
        :param artifact_repository: The repository associated with a marketplace installation.
        :type artifact_repository: Optional[ArtifactRepositoryRid]
        :param exclude_rid: A flag to exclude the retrieval of the `__rid` property.  Setting this to true may improve performance of this endpoint for object types in OSV2.
        :type exclude_rid: Optional[bool]
        :param package_name: The package name of the generated SDK.
        :type package_name: Optional[SdkPackageName]
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
                resource_path="/v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/links/{linkType}/{linkedObjectPrimaryKey}",
                query_params={
                    "artifactRepository": artifact_repository,
                    "excludeRid": exclude_rid,
                    "packageName": package_name,
                    "select": select,
                },
                path_params={
                    "ontology": ontology,
                    "objectType": object_type,
                    "primaryKey": primary_key,
                    "linkType": link_type,
                    "linkedObjectPrimaryKey": linked_object_primary_key,
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
    def list_linked_objects(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        object_type: ontologies_models.ObjectTypeApiName,
        primary_key: ontologies_models.PropertyValueEscapedString,
        link_type: ontologies_models.LinkTypeApiName,
        *,
        artifact_repository: typing.Optional[ontologies_models.ArtifactRepositoryRid] = None,
        exclude_rid: typing.Optional[bool] = None,
        order_by: typing.Optional[ontologies_models.OrderBy] = None,
        package_name: typing.Optional[ontologies_models.SdkPackageName] = None,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        select: typing.Optional[typing.List[ontologies_models.SelectedPropertyApiName]] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> core.ResourceIterator[ontologies_models.OntologyObjectV2]:
        """
        Lists the linked objects for a specific object and the given link type.

        Note that this endpoint does not guarantee consistency. Changes to the data could result in missing or
        repeated objects in the response pages.

        For Object Storage V1 backed objects, this endpoint returns a maximum of 10,000 objects. After 10,000 objects have been returned and if more objects
        are available, attempting to load another page will result in an `ObjectsExceededLimit` error being returned. There is no limit on Object Storage V2 backed objects.

        Each page may be smaller or larger than the requested page size. However, it
        is guaranteed that if there are more results available, at least one result will be present
        in the response.

        Note that null value properties will not be returned.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

        :param ontology: The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.
        :type ontology: OntologyIdentifier
        :param object_type: The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**.
        :type object_type: ObjectTypeApiName
        :param primary_key: The primary key of the object from which the links originate. To look up the expected primary key for your object type, use the `Get object type` endpoint or the **Ontology Manager**.
        :type primary_key: PropertyValueEscapedString
        :param link_type: The API name of the link that exists between the object and the requested objects. To find the API name for your link type, check the **Ontology Manager**.
        :type link_type: LinkTypeApiName
        :param artifact_repository: The repository associated with a marketplace installation.
        :type artifact_repository: Optional[ArtifactRepositoryRid]
        :param exclude_rid: A flag to exclude the retrieval of the `__rid` property.  Setting this to true may improve performance of this endpoint for object types in OSV2.
        :type exclude_rid: Optional[bool]
        :param order_by:
        :type order_by: Optional[OrderBy]
        :param package_name: The package name of the generated SDK.
        :type package_name: Optional[SdkPackageName]
        :param page_size: The desired size of the page to be returned. Defaults to 1,000. See [page sizes](https://palantir.com/docs/foundry/api/general/overview/paging/#page-sizes) for details.
        :type page_size: Optional[PageSize]
        :param page_token:
        :type page_token: Optional[PageToken]
        :param select: The properties of the object type that should be included in the response. Omit this parameter to get all the properties.
        :type select: Optional[List[SelectedPropertyApiName]]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ResourceIterator[ontologies_models.OntologyObjectV2]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/links/{linkType}",
                query_params={
                    "artifactRepository": artifact_repository,
                    "excludeRid": exclude_rid,
                    "orderBy": order_by,
                    "packageName": package_name,
                    "pageSize": page_size,
                    "pageToken": page_token,
                    "select": select,
                },
                path_params={
                    "ontology": ontology,
                    "objectType": object_type,
                    "primaryKey": primary_key,
                    "linkType": link_type,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ontologies_models.ListLinkedObjectsResponseV2,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode", "ITERATOR"),
            ),
        )


class _LinkedObjectClientRaw:
    def __init__(self, client: LinkedObjectClient) -> None:
        def get_linked_object(_: ontologies_models.OntologyObjectV2): ...
        def list_linked_objects(_: ontologies_models.ListLinkedObjectsResponseV2): ...

        self.get_linked_object = core.with_raw_response(get_linked_object, client.get_linked_object)
        self.list_linked_objects = core.with_raw_response(
            list_linked_objects, client.list_linked_objects
        )


class _LinkedObjectClientStreaming:
    def __init__(self, client: LinkedObjectClient) -> None:
        def get_linked_object(_: ontologies_models.OntologyObjectV2): ...
        def list_linked_objects(_: ontologies_models.ListLinkedObjectsResponseV2): ...

        self.get_linked_object = core.with_streaming_response(
            get_linked_object, client.get_linked_object
        )
        self.list_linked_objects = core.with_streaming_response(
            list_linked_objects, client.list_linked_objects
        )


class AsyncLinkedObjectClient:
    """
    The API client for the LinkedObject Resource.

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

        self.with_streaming_response = _AsyncLinkedObjectClientStreaming(self)
        self.with_raw_response = _AsyncLinkedObjectClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get_linked_object(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        object_type: ontologies_models.ObjectTypeApiName,
        primary_key: ontologies_models.PropertyValueEscapedString,
        link_type: ontologies_models.LinkTypeApiName,
        linked_object_primary_key: ontologies_models.PropertyValueEscapedString,
        *,
        artifact_repository: typing.Optional[ontologies_models.ArtifactRepositoryRid] = None,
        exclude_rid: typing.Optional[bool] = None,
        package_name: typing.Optional[ontologies_models.SdkPackageName] = None,
        select: typing.Optional[typing.List[ontologies_models.SelectedPropertyApiName]] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[ontologies_models.OntologyObjectV2]:
        """
        Get a specific linked object that originates from another object.

        If there is no link between the two objects, `LinkedObjectNotFound` is thrown.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

        :param ontology: The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.
        :type ontology: OntologyIdentifier
        :param object_type: The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**.
        :type object_type: ObjectTypeApiName
        :param primary_key: The primary key of the object from which the links originate. To look up the expected primary key for your object type, use the `Get object type` endpoint or the **Ontology Manager**.
        :type primary_key: PropertyValueEscapedString
        :param link_type: The API name of the link that exists between the object and the requested objects. To find the API name for your link type, check the **Ontology Manager**.
        :type link_type: LinkTypeApiName
        :param linked_object_primary_key: The primary key of the requested linked object. To look up the expected primary key for your object type, use the `Get object type` endpoint (passing the linked object type) or the **Ontology Manager**.
        :type linked_object_primary_key: PropertyValueEscapedString
        :param artifact_repository: The repository associated with a marketplace installation.
        :type artifact_repository: Optional[ArtifactRepositoryRid]
        :param exclude_rid: A flag to exclude the retrieval of the `__rid` property.  Setting this to true may improve performance of this endpoint for object types in OSV2.
        :type exclude_rid: Optional[bool]
        :param package_name: The package name of the generated SDK.
        :type package_name: Optional[SdkPackageName]
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
                resource_path="/v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/links/{linkType}/{linkedObjectPrimaryKey}",
                query_params={
                    "artifactRepository": artifact_repository,
                    "excludeRid": exclude_rid,
                    "packageName": package_name,
                    "select": select,
                },
                path_params={
                    "ontology": ontology,
                    "objectType": object_type,
                    "primaryKey": primary_key,
                    "linkType": link_type,
                    "linkedObjectPrimaryKey": linked_object_primary_key,
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
    def list_linked_objects(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        object_type: ontologies_models.ObjectTypeApiName,
        primary_key: ontologies_models.PropertyValueEscapedString,
        link_type: ontologies_models.LinkTypeApiName,
        *,
        artifact_repository: typing.Optional[ontologies_models.ArtifactRepositoryRid] = None,
        exclude_rid: typing.Optional[bool] = None,
        order_by: typing.Optional[ontologies_models.OrderBy] = None,
        package_name: typing.Optional[ontologies_models.SdkPackageName] = None,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        select: typing.Optional[typing.List[ontologies_models.SelectedPropertyApiName]] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> core.AsyncResourceIterator[ontologies_models.OntologyObjectV2]:
        """
        Lists the linked objects for a specific object and the given link type.

        Note that this endpoint does not guarantee consistency. Changes to the data could result in missing or
        repeated objects in the response pages.

        For Object Storage V1 backed objects, this endpoint returns a maximum of 10,000 objects. After 10,000 objects have been returned and if more objects
        are available, attempting to load another page will result in an `ObjectsExceededLimit` error being returned. There is no limit on Object Storage V2 backed objects.

        Each page may be smaller or larger than the requested page size. However, it
        is guaranteed that if there are more results available, at least one result will be present
        in the response.

        Note that null value properties will not be returned.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

        :param ontology: The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.
        :type ontology: OntologyIdentifier
        :param object_type: The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**.
        :type object_type: ObjectTypeApiName
        :param primary_key: The primary key of the object from which the links originate. To look up the expected primary key for your object type, use the `Get object type` endpoint or the **Ontology Manager**.
        :type primary_key: PropertyValueEscapedString
        :param link_type: The API name of the link that exists between the object and the requested objects. To find the API name for your link type, check the **Ontology Manager**.
        :type link_type: LinkTypeApiName
        :param artifact_repository: The repository associated with a marketplace installation.
        :type artifact_repository: Optional[ArtifactRepositoryRid]
        :param exclude_rid: A flag to exclude the retrieval of the `__rid` property.  Setting this to true may improve performance of this endpoint for object types in OSV2.
        :type exclude_rid: Optional[bool]
        :param order_by:
        :type order_by: Optional[OrderBy]
        :param package_name: The package name of the generated SDK.
        :type package_name: Optional[SdkPackageName]
        :param page_size: The desired size of the page to be returned. Defaults to 1,000. See [page sizes](https://palantir.com/docs/foundry/api/general/overview/paging/#page-sizes) for details.
        :type page_size: Optional[PageSize]
        :param page_token:
        :type page_token: Optional[PageToken]
        :param select: The properties of the object type that should be included in the response. Omit this parameter to get all the properties.
        :type select: Optional[List[SelectedPropertyApiName]]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.AsyncResourceIterator[ontologies_models.OntologyObjectV2]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/links/{linkType}",
                query_params={
                    "artifactRepository": artifact_repository,
                    "excludeRid": exclude_rid,
                    "orderBy": order_by,
                    "packageName": package_name,
                    "pageSize": page_size,
                    "pageToken": page_token,
                    "select": select,
                },
                path_params={
                    "ontology": ontology,
                    "objectType": object_type,
                    "primaryKey": primary_key,
                    "linkType": link_type,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ontologies_models.ListLinkedObjectsResponseV2,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode", "ITERATOR"),
            ),
        )


class _AsyncLinkedObjectClientRaw:
    def __init__(self, client: AsyncLinkedObjectClient) -> None:
        def get_linked_object(_: ontologies_models.OntologyObjectV2): ...
        def list_linked_objects(_: ontologies_models.ListLinkedObjectsResponseV2): ...

        self.get_linked_object = core.async_with_raw_response(
            get_linked_object, client.get_linked_object
        )
        self.list_linked_objects = core.async_with_raw_response(
            list_linked_objects, client.list_linked_objects
        )


class _AsyncLinkedObjectClientStreaming:
    def __init__(self, client: AsyncLinkedObjectClient) -> None:
        def get_linked_object(_: ontologies_models.OntologyObjectV2): ...
        def list_linked_objects(_: ontologies_models.ListLinkedObjectsResponseV2): ...

        self.get_linked_object = core.async_with_streaming_response(
            get_linked_object, client.get_linked_object
        )
        self.list_linked_objects = core.async_with_streaming_response(
            list_linked_objects, client.list_linked_objects
        )
