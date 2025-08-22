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


class TimeSeriesValueBankPropertyClient:
    """
    The API client for the TimeSeriesValueBankProperty Resource.

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

        self.with_streaming_response = _TimeSeriesValueBankPropertyClientStreaming(self)
        self.with_raw_response = _TimeSeriesValueBankPropertyClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get_latest_value(
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
    ) -> typing.Optional[ontologies_models.TimeseriesEntry]:
        """
        Get the latest value of a property backed by a timeseries. If a specific geotime series integration has both a history and a live integration, we will give precedence to the live integration.

        :param ontology:
        :type ontology: OntologyIdentifier
        :param object_type: The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**.
        :type object_type: ObjectTypeApiName
        :param primary_key: The primary key of the object with the timeseries property.
        :type primary_key: PropertyValueEscapedString
        :param property_name: The API name of the timeseries property. To find the API name for your property value bank property, check the **Ontology Manager** or use the **Get object type** endpoint.
        :type property_name: PropertyApiName
        :param sdk_package_rid: The package rid of the generated SDK.
        :type sdk_package_rid: Optional[SdkPackageRid]
        :param sdk_version: The version of the generated SDK.
        :type sdk_version: Optional[SdkVersion]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Optional[ontologies_models.TimeseriesEntry]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/timeseries/{propertyName}/latestValue",
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
                body_type=None,
                response_type=typing.Optional[ontologies_models.TimeseriesEntry],
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def stream_values(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        object_type: ontologies_models.ObjectTypeApiName,
        primary_key: ontologies_models.PropertyValueEscapedString,
        property: ontologies_models.PropertyApiName,
        *,
        range: typing.Optional[ontologies_models.TimeRange] = None,
        sdk_package_rid: typing.Optional[ontologies_models.SdkPackageRid] = None,
        sdk_version: typing.Optional[ontologies_models.SdkVersion] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> bytes:
        """
        Stream all of the points of a time series property (this includes geotime series references).

        :param ontology:
        :type ontology: OntologyIdentifier
        :param object_type: The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**.
        :type object_type: ObjectTypeApiName
        :param primary_key: The primary key of the object with the time series property.
        :type primary_key: PropertyValueEscapedString
        :param property: The API name of the time series backed property. To find the API name, check the **Ontology Manager** or use the **Get object type** endpoint.
        :type property: PropertyApiName
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
                resource_path="/v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/timeseries/{property}/streamValues",
                query_params={
                    "sdkPackageRid": sdk_package_rid,
                    "sdkVersion": sdk_version,
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
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "range": typing.Optional[ontologies_models.TimeRange],
                    },
                ),
                response_type=bytes,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _TimeSeriesValueBankPropertyClientRaw:
    def __init__(self, client: TimeSeriesValueBankPropertyClient) -> None:
        def get_latest_value(_: typing.Optional[ontologies_models.TimeseriesEntry]): ...
        def stream_values(_: bytes): ...

        self.get_latest_value = core.with_raw_response(get_latest_value, client.get_latest_value)
        self.stream_values = core.with_raw_response(stream_values, client.stream_values)


class _TimeSeriesValueBankPropertyClientStreaming:
    def __init__(self, client: TimeSeriesValueBankPropertyClient) -> None:
        def get_latest_value(_: typing.Optional[ontologies_models.TimeseriesEntry]): ...
        def stream_values(_: bytes): ...

        self.get_latest_value = core.with_streaming_response(
            get_latest_value, client.get_latest_value
        )
        self.stream_values = core.with_streaming_response(stream_values, client.stream_values)


class AsyncTimeSeriesValueBankPropertyClient:
    """
    The API client for the TimeSeriesValueBankProperty Resource.

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

        self.with_streaming_response = _AsyncTimeSeriesValueBankPropertyClientStreaming(self)
        self.with_raw_response = _AsyncTimeSeriesValueBankPropertyClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get_latest_value(
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
    ) -> typing.Awaitable[typing.Optional[ontologies_models.TimeseriesEntry]]:
        """
        Get the latest value of a property backed by a timeseries. If a specific geotime series integration has both a history and a live integration, we will give precedence to the live integration.

        :param ontology:
        :type ontology: OntologyIdentifier
        :param object_type: The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**.
        :type object_type: ObjectTypeApiName
        :param primary_key: The primary key of the object with the timeseries property.
        :type primary_key: PropertyValueEscapedString
        :param property_name: The API name of the timeseries property. To find the API name for your property value bank property, check the **Ontology Manager** or use the **Get object type** endpoint.
        :type property_name: PropertyApiName
        :param sdk_package_rid: The package rid of the generated SDK.
        :type sdk_package_rid: Optional[SdkPackageRid]
        :param sdk_version: The version of the generated SDK.
        :type sdk_version: Optional[SdkVersion]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[typing.Optional[ontologies_models.TimeseriesEntry]]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/timeseries/{propertyName}/latestValue",
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
                body_type=None,
                response_type=typing.Optional[ontologies_models.TimeseriesEntry],
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def stream_values(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        object_type: ontologies_models.ObjectTypeApiName,
        primary_key: ontologies_models.PropertyValueEscapedString,
        property: ontologies_models.PropertyApiName,
        *,
        range: typing.Optional[ontologies_models.TimeRange] = None,
        sdk_package_rid: typing.Optional[ontologies_models.SdkPackageRid] = None,
        sdk_version: typing.Optional[ontologies_models.SdkVersion] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[bytes]:
        """
        Stream all of the points of a time series property (this includes geotime series references).

        :param ontology:
        :type ontology: OntologyIdentifier
        :param object_type: The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**.
        :type object_type: ObjectTypeApiName
        :param primary_key: The primary key of the object with the time series property.
        :type primary_key: PropertyValueEscapedString
        :param property: The API name of the time series backed property. To find the API name, check the **Ontology Manager** or use the **Get object type** endpoint.
        :type property: PropertyApiName
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
                resource_path="/v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/timeseries/{property}/streamValues",
                query_params={
                    "sdkPackageRid": sdk_package_rid,
                    "sdkVersion": sdk_version,
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
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "range": typing.Optional[ontologies_models.TimeRange],
                    },
                ),
                response_type=bytes,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _AsyncTimeSeriesValueBankPropertyClientRaw:
    def __init__(self, client: AsyncTimeSeriesValueBankPropertyClient) -> None:
        def get_latest_value(_: typing.Optional[ontologies_models.TimeseriesEntry]): ...
        def stream_values(_: bytes): ...

        self.get_latest_value = core.async_with_raw_response(
            get_latest_value, client.get_latest_value
        )
        self.stream_values = core.async_with_raw_response(stream_values, client.stream_values)


class _AsyncTimeSeriesValueBankPropertyClientStreaming:
    def __init__(self, client: AsyncTimeSeriesValueBankPropertyClient) -> None:
        def get_latest_value(_: typing.Optional[ontologies_models.TimeseriesEntry]): ...
        def stream_values(_: bytes): ...

        self.get_latest_value = core.async_with_streaming_response(
            get_latest_value, client.get_latest_value
        )
        self.stream_values = core.async_with_streaming_response(stream_values, client.stream_values)
