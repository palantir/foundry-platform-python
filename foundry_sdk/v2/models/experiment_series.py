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
from foundry_sdk.v2.models import errors as models_errors
from foundry_sdk.v2.models import models as models_models


class ExperimentSeriesClient:
    """
    The API client for the ExperimentSeries Resource.

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

        self.with_streaming_response = _ExperimentSeriesClientStreaming(self)
        self.with_raw_response = _ExperimentSeriesClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def json(
        self,
        model_rid: models_models.ModelRid,
        experiment_rid: models_models.ExperimentRid,
        experiment_series_name: models_models.SeriesName,
        *,
        offset: typing.Optional[int] = None,
        page_size: typing.Optional[core_models.PageSize] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> models_models.Series:
        """
        Retrieve raw time-series data for a single series in JSON format.
        Results are paginated with a default page size of 200 and a maximum of 1000.

        :param model_rid:
        :type model_rid: ModelRid
        :param experiment_rid:
        :type experiment_rid: ExperimentRid
        :param experiment_series_name:
        :type experiment_series_name: SeriesName
        :param offset: Number of values to skip from the beginning. Defaults to 0.
        :type offset: Optional[int]
        :param page_size: Maximum number of values to return per page. Default is 200, maximum is 1000.
        :type page_size: Optional[PageSize]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: models_models.Series

        :raises JsonExperimentSeriesPermissionDenied: Could not json the ExperimentSeries.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/models/{modelRid}/experiments/{experimentRid}/series/{experimentSeriesName}/json",
                query_params={
                    "offset": offset,
                    "pageSize": page_size,
                    "preview": preview,
                },
                path_params={
                    "modelRid": model_rid,
                    "experimentRid": experiment_rid,
                    "experimentSeriesName": experiment_series_name,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=models_models.Series,
                request_timeout=request_timeout,
                throwable_errors={
                    "JsonExperimentSeriesPermissionDenied": models_errors.JsonExperimentSeriesPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def parquet(
        self,
        model_rid: models_models.ModelRid,
        experiment_rid: models_models.ExperimentRid,
        experiment_series_name: models_models.SeriesName,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> core.TableResponse:
        """
        Retrieve raw time-series data for a single series as a streamed binary response in Apache Parquet format.

        :param model_rid:
        :type model_rid: ModelRid
        :param experiment_rid:
        :type experiment_rid: ExperimentRid
        :param experiment_series_name:
        :type experiment_series_name: SeriesName
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.TableResponse


        :raises ParquetExperimentSeriesPermissionDenied: Could not parquet the ExperimentSeries.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/models/{modelRid}/experiments/{experimentRid}/series/{experimentSeriesName}/parquet",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "modelRid": model_rid,
                    "experimentRid": experiment_rid,
                    "experimentSeriesName": experiment_series_name,
                },
                header_params={
                    "Accept": "application/octet-stream",
                },
                body=None,
                response_type=bytes,
                request_timeout=request_timeout,
                throwable_errors={
                    "ParquetExperimentSeriesPermissionDenied": models_errors.ParquetExperimentSeriesPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode", "PARQUET_TABLE"),
            ),
        )


class _ExperimentSeriesClientRaw:
    def __init__(self, client: ExperimentSeriesClient) -> None:
        def json(_: models_models.Series): ...
        def parquet(_: bytes): ...

        self.json = core.with_raw_response(json, client.json)
        self.parquet = core.with_raw_response(parquet, client.parquet)


class _ExperimentSeriesClientStreaming:
    def __init__(self, client: ExperimentSeriesClient) -> None:
        def json(_: models_models.Series): ...
        def parquet(_: bytes): ...

        self.json = core.with_streaming_response(json, client.json)
        self.parquet = core.with_streaming_response(parquet, client.parquet)


class AsyncExperimentSeriesClient:
    """
    The API client for the ExperimentSeries Resource.

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

        self.with_streaming_response = _AsyncExperimentSeriesClientStreaming(self)
        self.with_raw_response = _AsyncExperimentSeriesClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def json(
        self,
        model_rid: models_models.ModelRid,
        experiment_rid: models_models.ExperimentRid,
        experiment_series_name: models_models.SeriesName,
        *,
        offset: typing.Optional[int] = None,
        page_size: typing.Optional[core_models.PageSize] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[models_models.Series]:
        """
        Retrieve raw time-series data for a single series in JSON format.
        Results are paginated with a default page size of 200 and a maximum of 1000.

        :param model_rid:
        :type model_rid: ModelRid
        :param experiment_rid:
        :type experiment_rid: ExperimentRid
        :param experiment_series_name:
        :type experiment_series_name: SeriesName
        :param offset: Number of values to skip from the beginning. Defaults to 0.
        :type offset: Optional[int]
        :param page_size: Maximum number of values to return per page. Default is 200, maximum is 1000.
        :type page_size: Optional[PageSize]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[models_models.Series]

        :raises JsonExperimentSeriesPermissionDenied: Could not json the ExperimentSeries.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/models/{modelRid}/experiments/{experimentRid}/series/{experimentSeriesName}/json",
                query_params={
                    "offset": offset,
                    "pageSize": page_size,
                    "preview": preview,
                },
                path_params={
                    "modelRid": model_rid,
                    "experimentRid": experiment_rid,
                    "experimentSeriesName": experiment_series_name,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=models_models.Series,
                request_timeout=request_timeout,
                throwable_errors={
                    "JsonExperimentSeriesPermissionDenied": models_errors.JsonExperimentSeriesPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def parquet(
        self,
        model_rid: models_models.ModelRid,
        experiment_rid: models_models.ExperimentRid,
        experiment_series_name: models_models.SeriesName,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[core.TableResponse]:
        """
                Retrieve raw time-series data for a single series as a streamed binary response in Apache Parquet format.

                :param model_rid:
                :type model_rid: ModelRid
                :param experiment_rid:
                :type experiment_rid: ExperimentRid
                :param experiment_series_name:
                :type experiment_series_name: SeriesName
                :param preview: Enables the use of preview functionality.
                :type preview: Optional[PreviewMode]
                :param request_timeout: timeout setting for this request in seconds.
                :type request_timeout: Optional[int]
                :return: Returns the result object.
                :rtype: typing.Awaitable[core.TableResponse
        ]

                :raises ParquetExperimentSeriesPermissionDenied: Could not parquet the ExperimentSeries.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/models/{modelRid}/experiments/{experimentRid}/series/{experimentSeriesName}/parquet",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "modelRid": model_rid,
                    "experimentRid": experiment_rid,
                    "experimentSeriesName": experiment_series_name,
                },
                header_params={
                    "Accept": "application/octet-stream",
                },
                body=None,
                response_type=bytes,
                request_timeout=request_timeout,
                throwable_errors={
                    "ParquetExperimentSeriesPermissionDenied": models_errors.ParquetExperimentSeriesPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode", "PARQUET_TABLE"),
            ),
        )


class _AsyncExperimentSeriesClientRaw:
    def __init__(self, client: AsyncExperimentSeriesClient) -> None:
        def json(_: models_models.Series): ...
        def parquet(_: bytes): ...

        self.json = core.async_with_raw_response(json, client.json)
        self.parquet = core.async_with_raw_response(parquet, client.parquet)


class _AsyncExperimentSeriesClientStreaming:
    def __init__(self, client: AsyncExperimentSeriesClient) -> None:
        def json(_: models_models.Series): ...
        def parquet(_: bytes): ...

        self.json = core.async_with_streaming_response(json, client.json)
        self.parquet = core.async_with_streaming_response(parquet, client.parquet)
