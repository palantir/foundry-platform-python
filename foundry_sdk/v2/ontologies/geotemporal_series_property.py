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


class GeotemporalSeriesPropertyClient:
    """
    The API client for the GeotemporalSeriesProperty Resource.

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

        self.with_streaming_response = _GeotemporalSeriesPropertyClientStreaming(self)
        self.with_raw_response = _GeotemporalSeriesPropertyClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get_geotemporal_series_latest_value(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        object_type: ontologies_models.ObjectTypeApiName,
        primary_key: ontologies_models.PropertyValueEscapedString,
        property_name: ontologies_models.PropertyApiName,
        *,
        sdk_package_rid: typing.Optional[ontologies_models.SdkPackageRid] = None,
        sdk_version: typing.Optional[ontologies_models.SdkVersion] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Optional[ontologies_models.GeotemporalSeriesEntry]:
        """
        Get the latest recorded location for a geotemporal series reference property.

        :param ontology:
        :type ontology: OntologyIdentifier
        :param object_type: The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**.
        :type object_type: ObjectTypeApiName
        :param primary_key: The primary key of the object with the geotemporal series property.
        :type primary_key: PropertyValueEscapedString
        :param property_name: The API name of the geotemporal series property. To find the API name for your property, check the **Ontology Manager** or use the **Get object type** endpoint.
        :type property_name: PropertyApiName
        :param sdk_package_rid: The package rid of the generated SDK.
        :type sdk_package_rid: Optional[SdkPackageRid]
        :param sdk_version: The version of the generated SDK.
        :type sdk_version: Optional[SdkVersion]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Optional[ontologies_models.GeotemporalSeriesEntry]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/geotemporalSeries/{propertyName}/latestValue",
                query_params={
                    "sdkPackageRid": sdk_package_rid,
                    "sdkVersion": sdk_version,
                },
                path_params={
                    "ontology": ontology,
                    "objectType": object_type,
                    "primaryKey": primary_key,
                    "propertyName": property_name,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=typing.Optional[ontologies_models.GeotemporalSeriesEntry],
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def stream_geotemporal_series_historic_values(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        object_type: ontologies_models.ObjectTypeApiName,
        primary_key: ontologies_models.PropertyValueEscapedString,
        property_name: ontologies_models.PropertyApiName,
        *,
        range: typing.Optional[ontologies_models.TimeRange] = None,
        sdk_package_rid: typing.Optional[ontologies_models.SdkPackageRid] = None,
        sdk_version: typing.Optional[ontologies_models.SdkVersion] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> bytes:
        """
        Stream historic points of a geotemporal series reference property.

        :param ontology:
        :type ontology: OntologyIdentifier
        :param object_type: The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**.
        :type object_type: ObjectTypeApiName
        :param primary_key: The primary key of the object with the geotemporal series property.
        :type primary_key: PropertyValueEscapedString
        :param property_name: The API name of the geotemporal series property. To find the API name for your property, check the **Ontology Manager** or use the **Get object type** endpoint.
        :type property_name: PropertyApiName
        :param range:
        :type range: Optional[TimeRange]
        :param sdk_package_rid: The package rid of the generated SDK.
        :type sdk_package_rid: Optional[SdkPackageRid]
        :param sdk_version: The version of the generated SDK.
        :type sdk_version: Optional[SdkVersion]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: bytes
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/geotemporalSeries/{propertyName}/streamHistoricValues",
                query_params={
                    "sdkPackageRid": sdk_package_rid,
                    "sdkVersion": sdk_version,
                },
                path_params={
                    "ontology": ontology,
                    "objectType": object_type,
                    "primaryKey": primary_key,
                    "propertyName": property_name,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "*/*",
                },
                body=ontologies_models.StreamGeotemporalSeriesValuesRequest(
                    range=range,
                ),
                response_type=bytes,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _GeotemporalSeriesPropertyClientRaw:
    def __init__(self, client: GeotemporalSeriesPropertyClient) -> None:
        def get_geotemporal_series_latest_value(
            _: typing.Optional[ontologies_models.GeotemporalSeriesEntry],
        ): ...
        def stream_geotemporal_series_historic_values(_: bytes): ...

        self.get_geotemporal_series_latest_value = core.with_raw_response(
            get_geotemporal_series_latest_value, client.get_geotemporal_series_latest_value
        )
        self.stream_geotemporal_series_historic_values = core.with_raw_response(
            stream_geotemporal_series_historic_values,
            client.stream_geotemporal_series_historic_values,
        )


class _GeotemporalSeriesPropertyClientStreaming:
    def __init__(self, client: GeotemporalSeriesPropertyClient) -> None:
        def get_geotemporal_series_latest_value(
            _: typing.Optional[ontologies_models.GeotemporalSeriesEntry],
        ): ...
        def stream_geotemporal_series_historic_values(_: bytes): ...

        self.get_geotemporal_series_latest_value = core.with_streaming_response(
            get_geotemporal_series_latest_value, client.get_geotemporal_series_latest_value
        )
        self.stream_geotemporal_series_historic_values = core.with_streaming_response(
            stream_geotemporal_series_historic_values,
            client.stream_geotemporal_series_historic_values,
        )


class AsyncGeotemporalSeriesPropertyClient:
    """
    The API client for the GeotemporalSeriesProperty Resource.

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

        self.with_streaming_response = _AsyncGeotemporalSeriesPropertyClientStreaming(self)
        self.with_raw_response = _AsyncGeotemporalSeriesPropertyClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get_geotemporal_series_latest_value(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        object_type: ontologies_models.ObjectTypeApiName,
        primary_key: ontologies_models.PropertyValueEscapedString,
        property_name: ontologies_models.PropertyApiName,
        *,
        sdk_package_rid: typing.Optional[ontologies_models.SdkPackageRid] = None,
        sdk_version: typing.Optional[ontologies_models.SdkVersion] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[typing.Optional[ontologies_models.GeotemporalSeriesEntry]]:
        """
        Get the latest recorded location for a geotemporal series reference property.

        :param ontology:
        :type ontology: OntologyIdentifier
        :param object_type: The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**.
        :type object_type: ObjectTypeApiName
        :param primary_key: The primary key of the object with the geotemporal series property.
        :type primary_key: PropertyValueEscapedString
        :param property_name: The API name of the geotemporal series property. To find the API name for your property, check the **Ontology Manager** or use the **Get object type** endpoint.
        :type property_name: PropertyApiName
        :param sdk_package_rid: The package rid of the generated SDK.
        :type sdk_package_rid: Optional[SdkPackageRid]
        :param sdk_version: The version of the generated SDK.
        :type sdk_version: Optional[SdkVersion]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[typing.Optional[ontologies_models.GeotemporalSeriesEntry]]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/geotemporalSeries/{propertyName}/latestValue",
                query_params={
                    "sdkPackageRid": sdk_package_rid,
                    "sdkVersion": sdk_version,
                },
                path_params={
                    "ontology": ontology,
                    "objectType": object_type,
                    "primaryKey": primary_key,
                    "propertyName": property_name,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=typing.Optional[ontologies_models.GeotemporalSeriesEntry],
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def stream_geotemporal_series_historic_values(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        object_type: ontologies_models.ObjectTypeApiName,
        primary_key: ontologies_models.PropertyValueEscapedString,
        property_name: ontologies_models.PropertyApiName,
        *,
        range: typing.Optional[ontologies_models.TimeRange] = None,
        sdk_package_rid: typing.Optional[ontologies_models.SdkPackageRid] = None,
        sdk_version: typing.Optional[ontologies_models.SdkVersion] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[bytes]:
        """
        Stream historic points of a geotemporal series reference property.

        :param ontology:
        :type ontology: OntologyIdentifier
        :param object_type: The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**.
        :type object_type: ObjectTypeApiName
        :param primary_key: The primary key of the object with the geotemporal series property.
        :type primary_key: PropertyValueEscapedString
        :param property_name: The API name of the geotemporal series property. To find the API name for your property, check the **Ontology Manager** or use the **Get object type** endpoint.
        :type property_name: PropertyApiName
        :param range:
        :type range: Optional[TimeRange]
        :param sdk_package_rid: The package rid of the generated SDK.
        :type sdk_package_rid: Optional[SdkPackageRid]
        :param sdk_version: The version of the generated SDK.
        :type sdk_version: Optional[SdkVersion]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[bytes]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/geotemporalSeries/{propertyName}/streamHistoricValues",
                query_params={
                    "sdkPackageRid": sdk_package_rid,
                    "sdkVersion": sdk_version,
                },
                path_params={
                    "ontology": ontology,
                    "objectType": object_type,
                    "primaryKey": primary_key,
                    "propertyName": property_name,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "*/*",
                },
                body=ontologies_models.StreamGeotemporalSeriesValuesRequest(
                    range=range,
                ),
                response_type=bytes,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _AsyncGeotemporalSeriesPropertyClientRaw:
    def __init__(self, client: AsyncGeotemporalSeriesPropertyClient) -> None:
        def get_geotemporal_series_latest_value(
            _: typing.Optional[ontologies_models.GeotemporalSeriesEntry],
        ): ...
        def stream_geotemporal_series_historic_values(_: bytes): ...

        self.get_geotemporal_series_latest_value = core.async_with_raw_response(
            get_geotemporal_series_latest_value, client.get_geotemporal_series_latest_value
        )
        self.stream_geotemporal_series_historic_values = core.async_with_raw_response(
            stream_geotemporal_series_historic_values,
            client.stream_geotemporal_series_historic_values,
        )


class _AsyncGeotemporalSeriesPropertyClientStreaming:
    def __init__(self, client: AsyncGeotemporalSeriesPropertyClient) -> None:
        def get_geotemporal_series_latest_value(
            _: typing.Optional[ontologies_models.GeotemporalSeriesEntry],
        ): ...
        def stream_geotemporal_series_historic_values(_: bytes): ...

        self.get_geotemporal_series_latest_value = core.async_with_streaming_response(
            get_geotemporal_series_latest_value, client.get_geotemporal_series_latest_value
        )
        self.stream_geotemporal_series_historic_values = core.async_with_streaming_response(
            stream_geotemporal_series_historic_values,
            client.stream_geotemporal_series_historic_values,
        )
