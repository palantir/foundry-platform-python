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


class ExperimentArtifactTableClient:
    """
    The API client for the ExperimentArtifactTable Resource.

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

        self.with_streaming_response = _ExperimentArtifactTableClientStreaming(self)
        self.with_raw_response = _ExperimentArtifactTableClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def json(
        self,
        model_rid: models_models.ModelRid,
        experiment_rid: models_models.ExperimentRid,
        experiment_artifact_table_name: models_models.ExperimentArtifactName,
        *,
        offset: typing.Optional[int] = None,
        page_size: typing.Optional[core_models.PageSize] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> bytes:
        """
        Read table data from an experiment artifact as a streamed binary response containing JSON.
        The response body is a JSON array of row objects, where each object maps column names to values.
        Results are paginated by row count with a default page size of 10 and a maximum of 100.

        :param model_rid:
        :type model_rid: ModelRid
        :param experiment_rid:
        :type experiment_rid: ExperimentRid
        :param experiment_artifact_table_name:
        :type experiment_artifact_table_name: ExperimentArtifactName
        :param offset: Number of rows to skip from the beginning. Defaults to 0.
        :type offset: Optional[int]
        :param page_size: Maximum number of rows to return. Default is 10, maximum is 100.
        :type page_size: Optional[PageSize]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: bytes

        :raises JsonExperimentArtifactTablePermissionDenied: Could not json the ExperimentArtifactTable.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/models/{modelRid}/experiments/{experimentRid}/artifactTables/{experimentArtifactTableName}/json",
                query_params={
                    "offset": offset,
                    "pageSize": page_size,
                    "preview": preview,
                },
                path_params={
                    "modelRid": model_rid,
                    "experimentRid": experiment_rid,
                    "experimentArtifactTableName": experiment_artifact_table_name,
                },
                header_params={
                    "Accept": "application/octet-stream",
                },
                body=None,
                response_type=bytes,
                request_timeout=request_timeout,
                throwable_errors={
                    "JsonExperimentArtifactTablePermissionDenied": models_errors.JsonExperimentArtifactTablePermissionDenied,
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
        experiment_artifact_table_name: models_models.ExperimentArtifactName,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> core.TableResponse:
        """
        Read raw table data from experiment artifacts in Parquet format.

        :param model_rid:
        :type model_rid: ModelRid
        :param experiment_rid:
        :type experiment_rid: ExperimentRid
        :param experiment_artifact_table_name:
        :type experiment_artifact_table_name: ExperimentArtifactName
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.TableResponse


        :raises ParquetExperimentArtifactTablePermissionDenied: Could not parquet the ExperimentArtifactTable.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/models/{modelRid}/experiments/{experimentRid}/artifactTables/{experimentArtifactTableName}/parquet",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "modelRid": model_rid,
                    "experimentRid": experiment_rid,
                    "experimentArtifactTableName": experiment_artifact_table_name,
                },
                header_params={
                    "Accept": "application/octet-stream",
                },
                body=None,
                response_type=bytes,
                request_timeout=request_timeout,
                throwable_errors={
                    "ParquetExperimentArtifactTablePermissionDenied": models_errors.ParquetExperimentArtifactTablePermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode", "PARQUET_TABLE"),
            ),
        )


class _ExperimentArtifactTableClientRaw:
    def __init__(self, client: ExperimentArtifactTableClient) -> None:
        def json(_: bytes): ...
        def parquet(_: bytes): ...

        self.json = core.with_raw_response(json, client.json)
        self.parquet = core.with_raw_response(parquet, client.parquet)


class _ExperimentArtifactTableClientStreaming:
    def __init__(self, client: ExperimentArtifactTableClient) -> None:
        def json(_: bytes): ...
        def parquet(_: bytes): ...

        self.json = core.with_streaming_response(json, client.json)
        self.parquet = core.with_streaming_response(parquet, client.parquet)


class AsyncExperimentArtifactTableClient:
    """
    The API client for the ExperimentArtifactTable Resource.

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

        self.with_streaming_response = _AsyncExperimentArtifactTableClientStreaming(self)
        self.with_raw_response = _AsyncExperimentArtifactTableClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def json(
        self,
        model_rid: models_models.ModelRid,
        experiment_rid: models_models.ExperimentRid,
        experiment_artifact_table_name: models_models.ExperimentArtifactName,
        *,
        offset: typing.Optional[int] = None,
        page_size: typing.Optional[core_models.PageSize] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[bytes]:
        """
        Read table data from an experiment artifact as a streamed binary response containing JSON.
        The response body is a JSON array of row objects, where each object maps column names to values.
        Results are paginated by row count with a default page size of 10 and a maximum of 100.

        :param model_rid:
        :type model_rid: ModelRid
        :param experiment_rid:
        :type experiment_rid: ExperimentRid
        :param experiment_artifact_table_name:
        :type experiment_artifact_table_name: ExperimentArtifactName
        :param offset: Number of rows to skip from the beginning. Defaults to 0.
        :type offset: Optional[int]
        :param page_size: Maximum number of rows to return. Default is 10, maximum is 100.
        :type page_size: Optional[PageSize]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[bytes]

        :raises JsonExperimentArtifactTablePermissionDenied: Could not json the ExperimentArtifactTable.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/models/{modelRid}/experiments/{experimentRid}/artifactTables/{experimentArtifactTableName}/json",
                query_params={
                    "offset": offset,
                    "pageSize": page_size,
                    "preview": preview,
                },
                path_params={
                    "modelRid": model_rid,
                    "experimentRid": experiment_rid,
                    "experimentArtifactTableName": experiment_artifact_table_name,
                },
                header_params={
                    "Accept": "application/octet-stream",
                },
                body=None,
                response_type=bytes,
                request_timeout=request_timeout,
                throwable_errors={
                    "JsonExperimentArtifactTablePermissionDenied": models_errors.JsonExperimentArtifactTablePermissionDenied,
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
        experiment_artifact_table_name: models_models.ExperimentArtifactName,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[core.TableResponse]:
        """
                Read raw table data from experiment artifacts in Parquet format.

                :param model_rid:
                :type model_rid: ModelRid
                :param experiment_rid:
                :type experiment_rid: ExperimentRid
                :param experiment_artifact_table_name:
                :type experiment_artifact_table_name: ExperimentArtifactName
                :param preview: Enables the use of preview functionality.
                :type preview: Optional[PreviewMode]
                :param request_timeout: timeout setting for this request in seconds.
                :type request_timeout: Optional[int]
                :return: Returns the result object.
                :rtype: typing.Awaitable[core.TableResponse
        ]

                :raises ParquetExperimentArtifactTablePermissionDenied: Could not parquet the ExperimentArtifactTable.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/models/{modelRid}/experiments/{experimentRid}/artifactTables/{experimentArtifactTableName}/parquet",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "modelRid": model_rid,
                    "experimentRid": experiment_rid,
                    "experimentArtifactTableName": experiment_artifact_table_name,
                },
                header_params={
                    "Accept": "application/octet-stream",
                },
                body=None,
                response_type=bytes,
                request_timeout=request_timeout,
                throwable_errors={
                    "ParquetExperimentArtifactTablePermissionDenied": models_errors.ParquetExperimentArtifactTablePermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode", "PARQUET_TABLE"),
            ),
        )


class _AsyncExperimentArtifactTableClientRaw:
    def __init__(self, client: AsyncExperimentArtifactTableClient) -> None:
        def json(_: bytes): ...
        def parquet(_: bytes): ...

        self.json = core.async_with_raw_response(json, client.json)
        self.parquet = core.async_with_raw_response(parquet, client.parquet)


class _AsyncExperimentArtifactTableClientStreaming:
    def __init__(self, client: AsyncExperimentArtifactTableClient) -> None:
        def json(_: bytes): ...
        def parquet(_: bytes): ...

        self.json = core.async_with_streaming_response(json, client.json)
        self.parquet = core.async_with_streaming_response(parquet, client.parquet)
