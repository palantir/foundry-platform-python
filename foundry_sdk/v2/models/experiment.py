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
from functools import cached_property

import pydantic
import typing_extensions

from foundry_sdk import _core as core
from foundry_sdk import _errors as errors
from foundry_sdk.v2.core import models as core_models
from foundry_sdk.v2.models import errors as models_errors
from foundry_sdk.v2.models import models as models_models


class ExperimentClient:
    """
    The API client for the Experiment Resource.

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

        self.with_streaming_response = _ExperimentClientStreaming(self)
        self.with_raw_response = _ExperimentClientRaw(self)

    @cached_property
    def Series(self):
        from foundry_sdk.v2.models.experiment_series import ExperimentSeriesClient

        return ExperimentSeriesClient(
            auth=self._auth,
            hostname=self._hostname,
            config=self._config,
        )

    @cached_property
    def ArtifactTable(self):
        from foundry_sdk.v2.models.experiment_artifact_table import (
            ExperimentArtifactTableClient,
        )  # NOQA

        return ExperimentArtifactTableClient(
            auth=self._auth,
            hostname=self._hostname,
            config=self._config,
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        model_rid: models_models.ModelRid,
        experiment_rid: models_models.ExperimentRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> models_models.Experiment:
        """
        Retrieve a single experiment with all metadata, parameters, series metadata, and summary metrics.

        :param model_rid:
        :type model_rid: ModelRid
        :param experiment_rid:
        :type experiment_rid: ExperimentRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: models_models.Experiment

        :raises ExperimentNotFound: The given Experiment could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/models/{modelRid}/experiments/{experimentRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "modelRid": model_rid,
                    "experimentRid": experiment_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=models_models.Experiment,
                request_timeout=request_timeout,
                throwable_errors={
                    "ExperimentNotFound": models_errors.ExperimentNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def search(
        self,
        model_rid: models_models.ModelRid,
        *,
        order_by: typing.Optional[models_models.SearchExperimentsOrderBy] = None,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        where: typing.Optional[models_models.SearchExperimentsFilter] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> models_models.SearchExperimentsResponse:
        """
        Search experiments using complex nested queries on experiment metadata, parameters, series,
        and summary metrics. Supports AND/OR/NOT combinations and various predicates.
        Returns a maximum of 100 results per page.

        :param model_rid:
        :type model_rid: ModelRid
        :param order_by: The field to sort by. Default is to sort by relevance.
        :type order_by: Optional[SearchExperimentsOrderBy]
        :param page_size: The maximum number of results to return. Default 50, maximum of 100.
        :type page_size: Optional[PageSize]
        :param page_token: PageToken to identify the next page to retrieve. Leave empty for the first request.
        :type page_token: Optional[PageToken]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param where: Optional search filter for filtering experiments. If not provided, all experiments for the model are returned.
        :type where: Optional[SearchExperimentsFilter]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: models_models.SearchExperimentsResponse

        :raises SearchExperimentsPermissionDenied: Could not search the Experiment.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/models/{modelRid}/experiments/search",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "modelRid": model_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body=models_models.SearchExperimentsRequest(
                    where=where,
                    order_by=order_by,
                    page_size=page_size,
                    page_token=page_token,
                ),
                response_type=models_models.SearchExperimentsResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "SearchExperimentsPermissionDenied": models_errors.SearchExperimentsPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _ExperimentClientRaw:
    def __init__(self, client: ExperimentClient) -> None:
        def get(_: models_models.Experiment): ...
        def search(_: models_models.SearchExperimentsResponse): ...

        self.get = core.with_raw_response(get, client.get)
        self.search = core.with_raw_response(search, client.search)


class _ExperimentClientStreaming:
    def __init__(self, client: ExperimentClient) -> None:
        def get(_: models_models.Experiment): ...
        def search(_: models_models.SearchExperimentsResponse): ...

        self.get = core.with_streaming_response(get, client.get)
        self.search = core.with_streaming_response(search, client.search)


class AsyncExperimentClient:
    """
    The API client for the Experiment Resource.

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

        self.with_streaming_response = _AsyncExperimentClientStreaming(self)
        self.with_raw_response = _AsyncExperimentClientRaw(self)

    @cached_property
    def Series(self):
        from foundry_sdk.v2.models.experiment_series import AsyncExperimentSeriesClient

        return AsyncExperimentSeriesClient(
            auth=self._auth,
            hostname=self._hostname,
            config=self._config,
        )

    @cached_property
    def ArtifactTable(self):
        from foundry_sdk.v2.models.experiment_artifact_table import (
            AsyncExperimentArtifactTableClient,
        )  # NOQA

        return AsyncExperimentArtifactTableClient(
            auth=self._auth,
            hostname=self._hostname,
            config=self._config,
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        model_rid: models_models.ModelRid,
        experiment_rid: models_models.ExperimentRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[models_models.Experiment]:
        """
        Retrieve a single experiment with all metadata, parameters, series metadata, and summary metrics.

        :param model_rid:
        :type model_rid: ModelRid
        :param experiment_rid:
        :type experiment_rid: ExperimentRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[models_models.Experiment]

        :raises ExperimentNotFound: The given Experiment could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/models/{modelRid}/experiments/{experimentRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "modelRid": model_rid,
                    "experimentRid": experiment_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=models_models.Experiment,
                request_timeout=request_timeout,
                throwable_errors={
                    "ExperimentNotFound": models_errors.ExperimentNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def search(
        self,
        model_rid: models_models.ModelRid,
        *,
        order_by: typing.Optional[models_models.SearchExperimentsOrderBy] = None,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        where: typing.Optional[models_models.SearchExperimentsFilter] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[models_models.SearchExperimentsResponse]:
        """
        Search experiments using complex nested queries on experiment metadata, parameters, series,
        and summary metrics. Supports AND/OR/NOT combinations and various predicates.
        Returns a maximum of 100 results per page.

        :param model_rid:
        :type model_rid: ModelRid
        :param order_by: The field to sort by. Default is to sort by relevance.
        :type order_by: Optional[SearchExperimentsOrderBy]
        :param page_size: The maximum number of results to return. Default 50, maximum of 100.
        :type page_size: Optional[PageSize]
        :param page_token: PageToken to identify the next page to retrieve. Leave empty for the first request.
        :type page_token: Optional[PageToken]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param where: Optional search filter for filtering experiments. If not provided, all experiments for the model are returned.
        :type where: Optional[SearchExperimentsFilter]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[models_models.SearchExperimentsResponse]

        :raises SearchExperimentsPermissionDenied: Could not search the Experiment.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/models/{modelRid}/experiments/search",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "modelRid": model_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body=models_models.SearchExperimentsRequest(
                    where=where,
                    order_by=order_by,
                    page_size=page_size,
                    page_token=page_token,
                ),
                response_type=models_models.SearchExperimentsResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "SearchExperimentsPermissionDenied": models_errors.SearchExperimentsPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _AsyncExperimentClientRaw:
    def __init__(self, client: AsyncExperimentClient) -> None:
        def get(_: models_models.Experiment): ...
        def search(_: models_models.SearchExperimentsResponse): ...

        self.get = core.async_with_raw_response(get, client.get)
        self.search = core.async_with_raw_response(search, client.search)


class _AsyncExperimentClientStreaming:
    def __init__(self, client: AsyncExperimentClient) -> None:
        def get(_: models_models.Experiment): ...
        def search(_: models_models.SearchExperimentsResponse): ...

        self.get = core.async_with_streaming_response(get, client.get)
        self.search = core.async_with_streaming_response(search, client.search)
