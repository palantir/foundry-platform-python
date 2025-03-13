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
from foundry.v2.ontologies import models as ontologies_models


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
        self.with_streaming_response = _TimeSeriesPropertyV2ClientStreaming(
            auth=auth, hostname=hostname, config=config
        )
        self.with_raw_response = _TimeSeriesPropertyV2ClientRaw(
            auth=auth, hostname=hostname, config=config
        )

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
            ),
        ).decode()

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
            ),
        ).decode()

    @typing_extensions.overload
    @typing_extensions.deprecated(
        "Using the `stream` parameter is deprecated. Please use the `with_streaming_response` instead."
    )
    def stream_points(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        object_type: ontologies_models.ObjectTypeApiName,
        primary_key: ontologies_models.PropertyValueEscapedString,
        property: ontologies_models.PropertyApiName,
        *,
        stream: typing.Literal[True],
        aggregate: typing.Optional[
            typing.Union[
                ontologies_models.AggregateTimeSeries, ontologies_models.AggregateTimeSeriesDict
            ]
        ] = None,
        artifact_repository: typing.Optional[ontologies_models.ArtifactRepositoryRid] = None,
        format: typing.Optional[ontologies_models.StreamingOutputFormat] = None,
        package_name: typing.Optional[ontologies_models.SdkPackageName] = None,
        range: typing.Optional[
            typing.Union[ontologies_models.TimeRange, ontologies_models.TimeRangeDict]
        ] = None,
        chunk_size: typing.Optional[int] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.BinaryStream:
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
        :type aggregate: Optional[Union[AggregateTimeSeries, AggregateTimeSeriesDict]]
        :param artifact_repository: The repository associated with a marketplace installation.
        :type artifact_repository: Optional[ArtifactRepositoryRid]
        :param format: The output format to serialize the output binary stream in. Default is JSON. ARROW is more efficient than JSON at streaming a large sized response.
        :type format: Optional[StreamingOutputFormat]
        :param package_name: The package name of the generated SDK.
        :type package_name: Optional[SdkPackageName]
        :param range:
        :type range: Optional[Union[TimeRange, TimeRangeDict]]
        :param stream: Whether to stream back the binary data in an iterator. This avoids reading the entire content of the response into memory at once.
        :type stream: bool
        :param chunk_size: The number of bytes that should be read into memory for each chunk. If set to None, the data will become available as it arrives in whatever size is sent from the host.
        :type chunk_size: Optional[int]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.BinaryStream
        """
        ...

    @typing_extensions.overload
    def stream_points(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        object_type: ontologies_models.ObjectTypeApiName,
        primary_key: ontologies_models.PropertyValueEscapedString,
        property: ontologies_models.PropertyApiName,
        *,
        aggregate: typing.Optional[
            typing.Union[
                ontologies_models.AggregateTimeSeries, ontologies_models.AggregateTimeSeriesDict
            ]
        ] = None,
        artifact_repository: typing.Optional[ontologies_models.ArtifactRepositoryRid] = None,
        format: typing.Optional[ontologies_models.StreamingOutputFormat] = None,
        package_name: typing.Optional[ontologies_models.SdkPackageName] = None,
        range: typing.Optional[
            typing.Union[ontologies_models.TimeRange, ontologies_models.TimeRangeDict]
        ] = None,
        stream: typing.Literal[False] = False,
        request_timeout: typing.Optional[core.Timeout] = None,
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
        :type aggregate: Optional[Union[AggregateTimeSeries, AggregateTimeSeriesDict]]
        :param artifact_repository: The repository associated with a marketplace installation.
        :type artifact_repository: Optional[ArtifactRepositoryRid]
        :param format: The output format to serialize the output binary stream in. Default is JSON. ARROW is more efficient than JSON at streaming a large sized response.
        :type format: Optional[StreamingOutputFormat]
        :param package_name: The package name of the generated SDK.
        :type package_name: Optional[SdkPackageName]
        :param range:
        :type range: Optional[Union[TimeRange, TimeRangeDict]]
        :param stream: Whether to stream back the binary data in an iterator. This avoids reading the entire content of the response into memory at once.
        :type stream: bool
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: bytes
        """
        ...

    @typing_extensions.overload
    @typing_extensions.deprecated(
        "Using the `stream` parameter is deprecated. Please use the `with_streaming_response` instead."
    )
    def stream_points(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        object_type: ontologies_models.ObjectTypeApiName,
        primary_key: ontologies_models.PropertyValueEscapedString,
        property: ontologies_models.PropertyApiName,
        *,
        stream: bool,
        aggregate: typing.Optional[
            typing.Union[
                ontologies_models.AggregateTimeSeries, ontologies_models.AggregateTimeSeriesDict
            ]
        ] = None,
        artifact_repository: typing.Optional[ontologies_models.ArtifactRepositoryRid] = None,
        format: typing.Optional[ontologies_models.StreamingOutputFormat] = None,
        package_name: typing.Optional[ontologies_models.SdkPackageName] = None,
        range: typing.Optional[
            typing.Union[ontologies_models.TimeRange, ontologies_models.TimeRangeDict]
        ] = None,
        chunk_size: typing.Optional[int] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> typing.Union[bytes, core.BinaryStream]:
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
        :type aggregate: Optional[Union[AggregateTimeSeries, AggregateTimeSeriesDict]]
        :param artifact_repository: The repository associated with a marketplace installation.
        :type artifact_repository: Optional[ArtifactRepositoryRid]
        :param format: The output format to serialize the output binary stream in. Default is JSON. ARROW is more efficient than JSON at streaming a large sized response.
        :type format: Optional[StreamingOutputFormat]
        :param package_name: The package name of the generated SDK.
        :type package_name: Optional[SdkPackageName]
        :param range:
        :type range: Optional[Union[TimeRange, TimeRangeDict]]
        :param stream: Whether to stream back the binary data in an iterator. This avoids reading the entire content of the response into memory at once.
        :type stream: bool
        :param chunk_size: The number of bytes that should be read into memory for each chunk. If set to None, the data will become available as it arrives in whatever size is sent from the host.
        :type chunk_size: Optional[int]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Union[bytes, core.BinaryStream]
        """
        ...

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
        aggregate: typing.Optional[
            typing.Union[
                ontologies_models.AggregateTimeSeries, ontologies_models.AggregateTimeSeriesDict
            ]
        ] = None,
        artifact_repository: typing.Optional[ontologies_models.ArtifactRepositoryRid] = None,
        format: typing.Optional[ontologies_models.StreamingOutputFormat] = None,
        package_name: typing.Optional[ontologies_models.SdkPackageName] = None,
        range: typing.Optional[
            typing.Union[ontologies_models.TimeRange, ontologies_models.TimeRangeDict]
        ] = None,
        stream: bool = False,
        chunk_size: typing.Optional[int] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> typing.Union[bytes, core.BinaryStream]:
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
        :type aggregate: Optional[Union[AggregateTimeSeries, AggregateTimeSeriesDict]]
        :param artifact_repository: The repository associated with a marketplace installation.
        :type artifact_repository: Optional[ArtifactRepositoryRid]
        :param format: The output format to serialize the output binary stream in. Default is JSON. ARROW is more efficient than JSON at streaming a large sized response.
        :type format: Optional[StreamingOutputFormat]
        :param package_name: The package name of the generated SDK.
        :type package_name: Optional[SdkPackageName]
        :param range:
        :type range: Optional[Union[TimeRange, TimeRangeDict]]
        :param stream: Whether to stream back the binary data in an iterator. This avoids reading the entire content of the response into memory at once.
        :type stream: bool
        :param chunk_size: The number of bytes that should be read into memory for each chunk. If set to None, the data will become available as it arrives in whatever size is sent from the host.
        :type chunk_size: Optional[int]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Union[bytes, core.BinaryStream]
        """

        if stream:
            warnings.warn(
                f"client.ontologies.TimeSeriesPropertyV2.stream_points(..., stream=True, chunk_size={chunk_size}) is deprecated. Please use:\n\nwith client.ontologies.TimeSeriesPropertyV2.with_streaming_response.stream_points(...) as response:\n    response.iter_bytes(chunk_size={chunk_size})\n",
                DeprecationWarning,
                stacklevel=2,
            )

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
                        "range": typing.Optional[
                            typing.Union[
                                ontologies_models.TimeRange, ontologies_models.TimeRangeDict
                            ]
                        ],
                        "aggregate": typing.Optional[
                            typing.Union[
                                ontologies_models.AggregateTimeSeries,
                                ontologies_models.AggregateTimeSeriesDict,
                            ]
                        ],
                    },
                ),
                response_type=bytes,
                stream=stream,
                chunk_size=chunk_size,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        ).decode()


class _TimeSeriesPropertyV2ClientRaw:
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
    ) -> core.ApiResponse[typing.Optional[ontologies_models.TimeSeriesPoint]]:
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
        :rtype: core.ApiResponse[typing.Optional[ontologies_models.TimeSeriesPoint]]
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
    ) -> core.ApiResponse[typing.Optional[ontologies_models.TimeSeriesPoint]]:
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
        :rtype: core.ApiResponse[typing.Optional[ontologies_models.TimeSeriesPoint]]
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
        aggregate: typing.Optional[
            typing.Union[
                ontologies_models.AggregateTimeSeries, ontologies_models.AggregateTimeSeriesDict
            ]
        ] = None,
        artifact_repository: typing.Optional[ontologies_models.ArtifactRepositoryRid] = None,
        format: typing.Optional[ontologies_models.StreamingOutputFormat] = None,
        package_name: typing.Optional[ontologies_models.SdkPackageName] = None,
        range: typing.Optional[
            typing.Union[ontologies_models.TimeRange, ontologies_models.TimeRangeDict]
        ] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[bytes]:
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
        :type aggregate: Optional[Union[AggregateTimeSeries, AggregateTimeSeriesDict]]
        :param artifact_repository: The repository associated with a marketplace installation.
        :type artifact_repository: Optional[ArtifactRepositoryRid]
        :param format: The output format to serialize the output binary stream in. Default is JSON. ARROW is more efficient than JSON at streaming a large sized response.
        :type format: Optional[StreamingOutputFormat]
        :param package_name: The package name of the generated SDK.
        :type package_name: Optional[SdkPackageName]
        :param range:
        :type range: Optional[Union[TimeRange, TimeRangeDict]]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[bytes]
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
                        "range": typing.Optional[
                            typing.Union[
                                ontologies_models.TimeRange, ontologies_models.TimeRangeDict
                            ]
                        ],
                        "aggregate": typing.Optional[
                            typing.Union[
                                ontologies_models.AggregateTimeSeries,
                                ontologies_models.AggregateTimeSeriesDict,
                            ]
                        ],
                    },
                ),
                response_type=bytes,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )


class _TimeSeriesPropertyV2ClientStreaming:
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
    ) -> core.StreamingContextManager[typing.Optional[ontologies_models.TimeSeriesPoint]]:
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
        :rtype: core.StreamingContextManager[typing.Optional[ontologies_models.TimeSeriesPoint]]
        """

        return self._api_client.stream_api(
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
    ) -> core.StreamingContextManager[typing.Optional[ontologies_models.TimeSeriesPoint]]:
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
        :rtype: core.StreamingContextManager[typing.Optional[ontologies_models.TimeSeriesPoint]]
        """

        return self._api_client.stream_api(
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
        aggregate: typing.Optional[
            typing.Union[
                ontologies_models.AggregateTimeSeries, ontologies_models.AggregateTimeSeriesDict
            ]
        ] = None,
        artifact_repository: typing.Optional[ontologies_models.ArtifactRepositoryRid] = None,
        format: typing.Optional[ontologies_models.StreamingOutputFormat] = None,
        package_name: typing.Optional[ontologies_models.SdkPackageName] = None,
        range: typing.Optional[
            typing.Union[ontologies_models.TimeRange, ontologies_models.TimeRangeDict]
        ] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[bytes]:
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
        :type aggregate: Optional[Union[AggregateTimeSeries, AggregateTimeSeriesDict]]
        :param artifact_repository: The repository associated with a marketplace installation.
        :type artifact_repository: Optional[ArtifactRepositoryRid]
        :param format: The output format to serialize the output binary stream in. Default is JSON. ARROW is more efficient than JSON at streaming a large sized response.
        :type format: Optional[StreamingOutputFormat]
        :param package_name: The package name of the generated SDK.
        :type package_name: Optional[SdkPackageName]
        :param range:
        :type range: Optional[Union[TimeRange, TimeRangeDict]]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[bytes]
        """

        return self._api_client.stream_api(
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
                        "range": typing.Optional[
                            typing.Union[
                                ontologies_models.TimeRange, ontologies_models.TimeRangeDict
                            ]
                        ],
                        "aggregate": typing.Optional[
                            typing.Union[
                                ontologies_models.AggregateTimeSeries,
                                ontologies_models.AggregateTimeSeriesDict,
                            ]
                        ],
                    },
                ),
                response_type=bytes,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )
