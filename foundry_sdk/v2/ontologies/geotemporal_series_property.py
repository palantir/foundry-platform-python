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


class GeotemporalSeriesPropertyClient:
    """
    The API client for the GeotemporalSeriesProperty Resource.

    :param auth: Your auth configuration.
    :param hostname: The hostname supplier for resolving base URLs.
    :param config: Optionally specify the configuration for the HTTP session.
    """

    def __init__(
        self,
        auth: core.Auth,
        hostname: typing.Union[str, core.HostnameSupplier],
        config: typing.Optional[core.Config] = None,
    ):
        self._auth = auth
        if isinstance(hostname, core.HostnameSupplier):
            self._hostname_supplier = hostname
        else:
            self._hostname_supplier = core.create_hostname_supplier(hostname, config)
        self._hostname = self._hostname_supplier.get_hostname()
        self._config = config
        self._api_client = core.ApiClient(
            auth=auth, hostname=self._hostname_supplier, config=config
        )

        self.with_streaming_response = _GeotemporalSeriesPropertyClientStreaming(self)
        self.with_raw_response = _GeotemporalSeriesPropertyClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def load_geotemporal_series_entries(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        object_type: ontologies_models.ObjectTypeApiName,
        primary_key: ontologies_models.PropertyValueEscapedString,
        property: ontologies_models.PropertyApiName,
        *,
        additional_properties: typing.List[ontologies_models.SelectedPropertyApiName],
        range: ontologies_models.AbsoluteTimeRange,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        sdk_package_rid: typing.Optional[ontologies_models.SdkPackageRid] = None,
        sdk_version: typing.Optional[ontologies_models.SdkVersion] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> ontologies_models.LoadGeotemporalSeriesResponse:
        """
        Load the geotemporal series entries for a given object's geotemporal series reference property within the
        specified time range.

        Each entry in the response is a map of property names to values, following the same structure as
        `OntologyObjectV2`. Use the `additionalProperties` field in the request to control which properties are included
        in each entry depending on the underlying geotemporal integration.

        Results are paginated. Use the `nextPageToken` from the response to retrieve subsequent pages.

        :::callout{theme=warning title=Warning}
          Geotemporal series integrations with only "dataset archive" enabled are not supported.
        :::

        :param ontology:
        :type ontology: OntologyIdentifier
        :param object_type: The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**.
        :type object_type: ObjectTypeApiName
        :param primary_key: The primary key of the object with the geotemporal series property.
        :type primary_key: PropertyValueEscapedString
        :param property: The API name of the geotemporal series property. To find the API name for your property, check the **Ontology Manager** or use the **Get object type** endpoint.
        :type property: PropertyApiName
        :param additional_properties: The additional property API names to include in each entry. The "time" and "position" properties are always included and do not need to be specified here. Use this to request additional geotemporal series metadata properties such as "speed" or "heading". Properties that are not available for the underlying geotemporal integration will be omitted from the response entries.
        :type additional_properties: List[SelectedPropertyApiName]
        :param range:
        :type range: AbsoluteTimeRange
        :param page_size:
        :type page_size: Optional[PageSize]
        :param page_token:
        :type page_token: Optional[PageToken]
        :param preview: A boolean flag that, when set to true, enables the use of beta features in preview mode.
        :type preview: Optional[PreviewMode]
        :param sdk_package_rid: The package RID of the generated SDK.
        :type sdk_package_rid: Optional[SdkPackageRid]
        :param sdk_version: The version of the generated SDK.
        :type sdk_version: Optional[SdkVersion]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ontologies_models.LoadGeotemporalSeriesResponse
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/geotemporalSeries/{property}/loadEntries",
                query_params={
                    "preview": preview,
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
                    "Accept": "application/json",
                },
                body=ontologies_models.LoadGeotemporalSeriesRequest(
                    range=range,
                    additional_properties=additional_properties,
                    page_token=page_token,
                    page_size=page_size,
                ),
                response_type=ontologies_models.LoadGeotemporalSeriesResponse,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _GeotemporalSeriesPropertyClientRaw:
    def __init__(self, client: GeotemporalSeriesPropertyClient) -> None:
        def load_geotemporal_series_entries(_: ontologies_models.LoadGeotemporalSeriesResponse): ...

        self.load_geotemporal_series_entries = core.with_raw_response(
            load_geotemporal_series_entries, client.load_geotemporal_series_entries
        )


class _GeotemporalSeriesPropertyClientStreaming:
    def __init__(self, client: GeotemporalSeriesPropertyClient) -> None:
        def load_geotemporal_series_entries(_: ontologies_models.LoadGeotemporalSeriesResponse): ...

        self.load_geotemporal_series_entries = core.with_streaming_response(
            load_geotemporal_series_entries, client.load_geotemporal_series_entries
        )


class AsyncGeotemporalSeriesPropertyClient:
    """
    The API client for the GeotemporalSeriesProperty Resource.

    :param auth: Your auth configuration.
    :param hostname: The hostname supplier for resolving base URLs.
    :param config: Optionally specify the configuration for the HTTP session.
    """

    def __init__(
        self,
        auth: core.Auth,
        hostname: typing.Union[str, core.HostnameSupplier],
        config: typing.Optional[core.Config] = None,
    ):
        self._auth = auth
        if isinstance(hostname, core.HostnameSupplier):
            self._hostname_supplier = hostname
        else:
            self._hostname_supplier = core.create_hostname_supplier(hostname, config)
        self._hostname = self._hostname_supplier.get_hostname()
        self._config = config
        self._api_client = core.AsyncApiClient(
            auth=auth, hostname=self._hostname_supplier, config=config
        )

        self.with_streaming_response = _AsyncGeotemporalSeriesPropertyClientStreaming(self)
        self.with_raw_response = _AsyncGeotemporalSeriesPropertyClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def load_geotemporal_series_entries(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        object_type: ontologies_models.ObjectTypeApiName,
        primary_key: ontologies_models.PropertyValueEscapedString,
        property: ontologies_models.PropertyApiName,
        *,
        additional_properties: typing.List[ontologies_models.SelectedPropertyApiName],
        range: ontologies_models.AbsoluteTimeRange,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        sdk_package_rid: typing.Optional[ontologies_models.SdkPackageRid] = None,
        sdk_version: typing.Optional[ontologies_models.SdkVersion] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[ontologies_models.LoadGeotemporalSeriesResponse]:
        """
        Load the geotemporal series entries for a given object's geotemporal series reference property within the
        specified time range.

        Each entry in the response is a map of property names to values, following the same structure as
        `OntologyObjectV2`. Use the `additionalProperties` field in the request to control which properties are included
        in each entry depending on the underlying geotemporal integration.

        Results are paginated. Use the `nextPageToken` from the response to retrieve subsequent pages.

        :::callout{theme=warning title=Warning}
          Geotemporal series integrations with only "dataset archive" enabled are not supported.
        :::

        :param ontology:
        :type ontology: OntologyIdentifier
        :param object_type: The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**.
        :type object_type: ObjectTypeApiName
        :param primary_key: The primary key of the object with the geotemporal series property.
        :type primary_key: PropertyValueEscapedString
        :param property: The API name of the geotemporal series property. To find the API name for your property, check the **Ontology Manager** or use the **Get object type** endpoint.
        :type property: PropertyApiName
        :param additional_properties: The additional property API names to include in each entry. The "time" and "position" properties are always included and do not need to be specified here. Use this to request additional geotemporal series metadata properties such as "speed" or "heading". Properties that are not available for the underlying geotemporal integration will be omitted from the response entries.
        :type additional_properties: List[SelectedPropertyApiName]
        :param range:
        :type range: AbsoluteTimeRange
        :param page_size:
        :type page_size: Optional[PageSize]
        :param page_token:
        :type page_token: Optional[PageToken]
        :param preview: A boolean flag that, when set to true, enables the use of beta features in preview mode.
        :type preview: Optional[PreviewMode]
        :param sdk_package_rid: The package RID of the generated SDK.
        :type sdk_package_rid: Optional[SdkPackageRid]
        :param sdk_version: The version of the generated SDK.
        :type sdk_version: Optional[SdkVersion]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[ontologies_models.LoadGeotemporalSeriesResponse]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/geotemporalSeries/{property}/loadEntries",
                query_params={
                    "preview": preview,
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
                    "Accept": "application/json",
                },
                body=ontologies_models.LoadGeotemporalSeriesRequest(
                    range=range,
                    additional_properties=additional_properties,
                    page_token=page_token,
                    page_size=page_size,
                ),
                response_type=ontologies_models.LoadGeotemporalSeriesResponse,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _AsyncGeotemporalSeriesPropertyClientRaw:
    def __init__(self, client: AsyncGeotemporalSeriesPropertyClient) -> None:
        def load_geotemporal_series_entries(_: ontologies_models.LoadGeotemporalSeriesResponse): ...

        self.load_geotemporal_series_entries = core.async_with_raw_response(
            load_geotemporal_series_entries, client.load_geotemporal_series_entries
        )


class _AsyncGeotemporalSeriesPropertyClientStreaming:
    def __init__(self, client: AsyncGeotemporalSeriesPropertyClient) -> None:
        def load_geotemporal_series_entries(_: ontologies_models.LoadGeotemporalSeriesResponse): ...

        self.load_geotemporal_series_entries = core.async_with_streaming_response(
            load_geotemporal_series_entries, client.load_geotemporal_series_entries
        )
