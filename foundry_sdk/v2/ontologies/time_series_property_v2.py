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


class TimeSeriesPropertyV2Client:
    """
    The API client for the TimeSeriesPropertyV2 Resource.

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

        self.with_streaming_response = _TimeSeriesPropertyV2ClientStreaming(self)
        self.with_raw_response = _TimeSeriesPropertyV2ClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get_first_point(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        object_type: ontologies_models.ObjectTypeApiName,
        primary_key: ontologies_models.PropertyValueEscapedString,
        property: ontologies_models.PropertyApiName,
        *,
        artifact_repository: typing.Optional[ontologies_models.ArtifactRepositoryRid] = None,
        package_name: typing.Optional[ontologies_models.SdkPackageName] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Optional[ontologies_models.TimeSeriesPoint]:
        """
        Get the first point of a time series property.

        Third-party applications using this endpoint via OAuth2 must request the
        following operation scopes: `api:ontologies-read`.

        :param ontology: The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.
        :type ontology: OntologyIdentifier
        :param object_type: The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**.
        :type object_type: ObjectTypeApiName
        :param primary_key: The primary key of the object with the time series property.
        :type primary_key: PropertyValueEscapedString
        :param property: The API name of the time series property. To find the API name for your time series property, check the **Ontology Manager** or use the **Get object type** endpoint.
        :type property: PropertyApiName
        :param artifact_repository: The repository associated with a marketplace installation.
        :type artifact_repository: Optional[ArtifactRepositoryRid]
        :param package_name: The package name of the generated SDK.
        :type package_name: Optional[SdkPackageName]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Optional[ontologies_models.TimeSeriesPoint]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/timeseries/{property}/firstPoint",
                query_params={
                    "artifactRepository": artifact_repository,
                    "packageName": package_name,
                },
                path_params={
                    "ontology": ontology,
                    "objectType": object_type,
                    "primaryKey": primary_key,
                    "property": property,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=typing.Optional[ontologies_models.TimeSeriesPoint],
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get_last_point(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        object_type: ontologies_models.ObjectTypeApiName,
        primary_key: ontologies_models.PropertyValueEscapedString,
        property: ontologies_models.PropertyApiName,
        *,
        artifact_repository: typing.Optional[ontologies_models.ArtifactRepositoryRid] = None,
        package_name: typing.Optional[ontologies_models.SdkPackageName] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Optional[ontologies_models.TimeSeriesPoint]:
        """
        Get the last point of a time series property.

        Third-party applications using this endpoint via OAuth2 must request the
        following operation scopes: `api:ontologies-read`.

        :param ontology: The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.
        :type ontology: OntologyIdentifier
        :param object_type: The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**.
        :type object_type: ObjectTypeApiName
        :param primary_key: The primary key of the object with the time series property.
        :type primary_key: PropertyValueEscapedString
        :param property: The API name of the time series property. To find the API name for your time series property, check the **Ontology Manager** or use the **Get object type** endpoint.
        :type property: PropertyApiName
        :param artifact_repository: The repository associated with a marketplace installation.
        :type artifact_repository: Optional[ArtifactRepositoryRid]
        :param package_name: The package name of the generated SDK.
        :type package_name: Optional[SdkPackageName]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Optional[ontologies_models.TimeSeriesPoint]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/timeseries/{property}/lastPoint",
                query_params={
                    "artifactRepository": artifact_repository,
                    "packageName": package_name,
                },
                path_params={
                    "ontology": ontology,
                    "objectType": object_type,
                    "primaryKey": primary_key,
                    "property": property,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=typing.Optional[ontologies_models.TimeSeriesPoint],
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def stream_points(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        object_type: ontologies_models.ObjectTypeApiName,
        primary_key: ontologies_models.PropertyValueEscapedString,
        property: ontologies_models.PropertyApiName,
        *,
        aggregate: typing.Optional[ontologies_models.AggregateTimeSeries] = None,
        artifact_repository: typing.Optional[ontologies_models.ArtifactRepositoryRid] = None,
        format: typing.Optional[ontologies_models.StreamingOutputFormat] = None,
        package_name: typing.Optional[ontologies_models.SdkPackageName] = None,
        range: typing.Optional[ontologies_models.TimeRange] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> bytes:
        """
        Stream all of the points of a time series property.

        Third-party applications using this endpoint via OAuth2 must request the
        following operation scopes: `api:ontologies-read`.

        :param ontology: The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.
        :type ontology: OntologyIdentifier
        :param object_type: The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**.
        :type object_type: ObjectTypeApiName
        :param primary_key: The primary key of the object with the time series property.
        :type primary_key: PropertyValueEscapedString
        :param property: The API name of the time series property. To find the API name for your time series property, check the **Ontology Manager** or use the **Get object type** endpoint.
        :type property: PropertyApiName
        :param aggregate:
        :type aggregate: Optional[AggregateTimeSeries]
        :param artifact_repository: The repository associated with a marketplace installation.
        :type artifact_repository: Optional[ArtifactRepositoryRid]
        :param format: The output format to serialize the output binary stream in. Default is JSON. ARROW is more efficient than JSON at streaming a large sized response.
        :type format: Optional[StreamingOutputFormat]
        :param package_name: The package name of the generated SDK.
        :type package_name: Optional[SdkPackageName]
        :param range:
        :type range: Optional[TimeRange]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: bytes
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/timeseries/{property}/streamPoints",
                query_params={
                    "artifactRepository": artifact_repository,
                    "format": format,
                    "packageName": package_name,
                },
                path_params={
                    "ontology": ontology,
                    "objectType": object_type,
                    "primaryKey": primary_key,
                    "property": property,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "*/*",
                },
                body={
                    "range": range,
                    "aggregate": aggregate,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "range": typing.Optional[ontologies_models.TimeRange],
                        "aggregate": typing.Optional[ontologies_models.AggregateTimeSeries],
                    },
                ),
                response_type=bytes,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _TimeSeriesPropertyV2ClientRaw:
    def __init__(self, client: TimeSeriesPropertyV2Client) -> None:
        def get_first_point(_: typing.Optional[ontologies_models.TimeSeriesPoint]): ...
        def get_last_point(_: typing.Optional[ontologies_models.TimeSeriesPoint]): ...
        def stream_points(_: bytes): ...

        self.get_first_point = core.with_raw_response(get_first_point, client.get_first_point)
        self.get_last_point = core.with_raw_response(get_last_point, client.get_last_point)
        self.stream_points = core.with_raw_response(stream_points, client.stream_points)


class _TimeSeriesPropertyV2ClientStreaming:
    def __init__(self, client: TimeSeriesPropertyV2Client) -> None:
        def get_first_point(_: typing.Optional[ontologies_models.TimeSeriesPoint]): ...
        def get_last_point(_: typing.Optional[ontologies_models.TimeSeriesPoint]): ...
        def stream_points(_: bytes): ...

        self.get_first_point = core.with_streaming_response(get_first_point, client.get_first_point)
        self.get_last_point = core.with_streaming_response(get_last_point, client.get_last_point)
        self.stream_points = core.with_streaming_response(stream_points, client.stream_points)


class AsyncTimeSeriesPropertyV2Client:
    """
    The API client for the TimeSeriesPropertyV2 Resource.

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

        self.with_streaming_response = _AsyncTimeSeriesPropertyV2ClientStreaming(self)
        self.with_raw_response = _AsyncTimeSeriesPropertyV2ClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get_first_point(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        object_type: ontologies_models.ObjectTypeApiName,
        primary_key: ontologies_models.PropertyValueEscapedString,
        property: ontologies_models.PropertyApiName,
        *,
        artifact_repository: typing.Optional[ontologies_models.ArtifactRepositoryRid] = None,
        package_name: typing.Optional[ontologies_models.SdkPackageName] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[typing.Optional[ontologies_models.TimeSeriesPoint]]:
        """
        Get the first point of a time series property.

        Third-party applications using this endpoint via OAuth2 must request the
        following operation scopes: `api:ontologies-read`.

        :param ontology: The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.
        :type ontology: OntologyIdentifier
        :param object_type: The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**.
        :type object_type: ObjectTypeApiName
        :param primary_key: The primary key of the object with the time series property.
        :type primary_key: PropertyValueEscapedString
        :param property: The API name of the time series property. To find the API name for your time series property, check the **Ontology Manager** or use the **Get object type** endpoint.
        :type property: PropertyApiName
        :param artifact_repository: The repository associated with a marketplace installation.
        :type artifact_repository: Optional[ArtifactRepositoryRid]
        :param package_name: The package name of the generated SDK.
        :type package_name: Optional[SdkPackageName]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[typing.Optional[ontologies_models.TimeSeriesPoint]]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/timeseries/{property}/firstPoint",
                query_params={
                    "artifactRepository": artifact_repository,
                    "packageName": package_name,
                },
                path_params={
                    "ontology": ontology,
                    "objectType": object_type,
                    "primaryKey": primary_key,
                    "property": property,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=typing.Optional[ontologies_models.TimeSeriesPoint],
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get_last_point(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        object_type: ontologies_models.ObjectTypeApiName,
        primary_key: ontologies_models.PropertyValueEscapedString,
        property: ontologies_models.PropertyApiName,
        *,
        artifact_repository: typing.Optional[ontologies_models.ArtifactRepositoryRid] = None,
        package_name: typing.Optional[ontologies_models.SdkPackageName] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[typing.Optional[ontologies_models.TimeSeriesPoint]]:
        """
        Get the last point of a time series property.

        Third-party applications using this endpoint via OAuth2 must request the
        following operation scopes: `api:ontologies-read`.

        :param ontology: The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.
        :type ontology: OntologyIdentifier
        :param object_type: The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**.
        :type object_type: ObjectTypeApiName
        :param primary_key: The primary key of the object with the time series property.
        :type primary_key: PropertyValueEscapedString
        :param property: The API name of the time series property. To find the API name for your time series property, check the **Ontology Manager** or use the **Get object type** endpoint.
        :type property: PropertyApiName
        :param artifact_repository: The repository associated with a marketplace installation.
        :type artifact_repository: Optional[ArtifactRepositoryRid]
        :param package_name: The package name of the generated SDK.
        :type package_name: Optional[SdkPackageName]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[typing.Optional[ontologies_models.TimeSeriesPoint]]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/timeseries/{property}/lastPoint",
                query_params={
                    "artifactRepository": artifact_repository,
                    "packageName": package_name,
                },
                path_params={
                    "ontology": ontology,
                    "objectType": object_type,
                    "primaryKey": primary_key,
                    "property": property,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=typing.Optional[ontologies_models.TimeSeriesPoint],
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def stream_points(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        object_type: ontologies_models.ObjectTypeApiName,
        primary_key: ontologies_models.PropertyValueEscapedString,
        property: ontologies_models.PropertyApiName,
        *,
        aggregate: typing.Optional[ontologies_models.AggregateTimeSeries] = None,
        artifact_repository: typing.Optional[ontologies_models.ArtifactRepositoryRid] = None,
        format: typing.Optional[ontologies_models.StreamingOutputFormat] = None,
        package_name: typing.Optional[ontologies_models.SdkPackageName] = None,
        range: typing.Optional[ontologies_models.TimeRange] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[bytes]:
        """
        Stream all of the points of a time series property.

        Third-party applications using this endpoint via OAuth2 must request the
        following operation scopes: `api:ontologies-read`.

        :param ontology: The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.
        :type ontology: OntologyIdentifier
        :param object_type: The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**.
        :type object_type: ObjectTypeApiName
        :param primary_key: The primary key of the object with the time series property.
        :type primary_key: PropertyValueEscapedString
        :param property: The API name of the time series property. To find the API name for your time series property, check the **Ontology Manager** or use the **Get object type** endpoint.
        :type property: PropertyApiName
        :param aggregate:
        :type aggregate: Optional[AggregateTimeSeries]
        :param artifact_repository: The repository associated with a marketplace installation.
        :type artifact_repository: Optional[ArtifactRepositoryRid]
        :param format: The output format to serialize the output binary stream in. Default is JSON. ARROW is more efficient than JSON at streaming a large sized response.
        :type format: Optional[StreamingOutputFormat]
        :param package_name: The package name of the generated SDK.
        :type package_name: Optional[SdkPackageName]
        :param range:
        :type range: Optional[TimeRange]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[bytes]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/timeseries/{property}/streamPoints",
                query_params={
                    "artifactRepository": artifact_repository,
                    "format": format,
                    "packageName": package_name,
                },
                path_params={
                    "ontology": ontology,
                    "objectType": object_type,
                    "primaryKey": primary_key,
                    "property": property,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "*/*",
                },
                body={
                    "range": range,
                    "aggregate": aggregate,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "range": typing.Optional[ontologies_models.TimeRange],
                        "aggregate": typing.Optional[ontologies_models.AggregateTimeSeries],
                    },
                ),
                response_type=bytes,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _AsyncTimeSeriesPropertyV2ClientRaw:
    def __init__(self, client: AsyncTimeSeriesPropertyV2Client) -> None:
        def get_first_point(_: typing.Optional[ontologies_models.TimeSeriesPoint]): ...
        def get_last_point(_: typing.Optional[ontologies_models.TimeSeriesPoint]): ...
        def stream_points(_: bytes): ...

        self.get_first_point = core.async_with_raw_response(get_first_point, client.get_first_point)
        self.get_last_point = core.async_with_raw_response(get_last_point, client.get_last_point)
        self.stream_points = core.async_with_raw_response(stream_points, client.stream_points)


class _AsyncTimeSeriesPropertyV2ClientStreaming:
    def __init__(self, client: AsyncTimeSeriesPropertyV2Client) -> None:
        def get_first_point(_: typing.Optional[ontologies_models.TimeSeriesPoint]): ...
        def get_last_point(_: typing.Optional[ontologies_models.TimeSeriesPoint]): ...
        def stream_points(_: bytes): ...

        self.get_first_point = core.async_with_streaming_response(
            get_first_point, client.get_first_point
        )
        self.get_last_point = core.async_with_streaming_response(
            get_last_point, client.get_last_point
        )
        self.stream_points = core.async_with_streaming_response(stream_points, client.stream_points)
