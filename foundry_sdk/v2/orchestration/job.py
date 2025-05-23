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

import annotated_types
import pydantic
import typing_extensions

from foundry_sdk import _core as core
from foundry_sdk import _errors as errors
from foundry_sdk.v2.core import models as core_models
from foundry_sdk.v2.orchestration import errors as orchestration_errors
from foundry_sdk.v2.orchestration import models as orchestration_models


class JobClient:
    """
    The API client for the Job Resource.

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

        self.with_streaming_response = _JobClientStreaming(self)
        self.with_raw_response = _JobClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        job_rid: core_models.JobRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> orchestration_models.Job:
        """
        Get the Job with the specified rid.
        :param job_rid: The RID of a Job.
        :type job_rid: JobRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: orchestration_models.Job

        :raises JobNotFound: The given Job could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/orchestration/jobs/{jobRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "jobRid": job_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=orchestration_models.Job,
                request_timeout=request_timeout,
                throwable_errors={
                    "JobNotFound": orchestration_errors.JobNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get_batch(
        self,
        body: typing_extensions.Annotated[
            typing.List[orchestration_models.GetJobsBatchRequestElement],
            annotated_types.Len(min_length=1, max_length=500),
        ],
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> orchestration_models.GetJobsBatchResponse:
        """
        Execute multiple get requests on Job.

        The maximum batch size for this endpoint is 500.
        :param body: Body of the request
        :type body: List[GetJobsBatchRequestElement]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: orchestration_models.GetJobsBatchResponse
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/orchestration/jobs/getBatch",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body=body,
                body_type=typing_extensions.Annotated[
                    typing.List[orchestration_models.GetJobsBatchRequestElement],
                    annotated_types.Len(min_length=1, max_length=500),
                ],
                response_type=orchestration_models.GetJobsBatchResponse,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _JobClientRaw:
    def __init__(self, client: JobClient) -> None:
        def get(_: orchestration_models.Job): ...
        def get_batch(_: orchestration_models.GetJobsBatchResponse): ...

        self.get = core.with_raw_response(get, client.get)
        self.get_batch = core.with_raw_response(get_batch, client.get_batch)


class _JobClientStreaming:
    def __init__(self, client: JobClient) -> None:
        def get(_: orchestration_models.Job): ...
        def get_batch(_: orchestration_models.GetJobsBatchResponse): ...

        self.get = core.with_streaming_response(get, client.get)
        self.get_batch = core.with_streaming_response(get_batch, client.get_batch)


class AsyncJobClient:
    """
    The API client for the Job Resource.

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

        self.with_streaming_response = _AsyncJobClientStreaming(self)
        self.with_raw_response = _AsyncJobClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        job_rid: core_models.JobRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[orchestration_models.Job]:
        """
        Get the Job with the specified rid.
        :param job_rid: The RID of a Job.
        :type job_rid: JobRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[orchestration_models.Job]

        :raises JobNotFound: The given Job could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/orchestration/jobs/{jobRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "jobRid": job_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=orchestration_models.Job,
                request_timeout=request_timeout,
                throwable_errors={
                    "JobNotFound": orchestration_errors.JobNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get_batch(
        self,
        body: typing_extensions.Annotated[
            typing.List[orchestration_models.GetJobsBatchRequestElement],
            annotated_types.Len(min_length=1, max_length=500),
        ],
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[orchestration_models.GetJobsBatchResponse]:
        """
        Execute multiple get requests on Job.

        The maximum batch size for this endpoint is 500.
        :param body: Body of the request
        :type body: List[GetJobsBatchRequestElement]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[orchestration_models.GetJobsBatchResponse]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/orchestration/jobs/getBatch",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body=body,
                body_type=typing_extensions.Annotated[
                    typing.List[orchestration_models.GetJobsBatchRequestElement],
                    annotated_types.Len(min_length=1, max_length=500),
                ],
                response_type=orchestration_models.GetJobsBatchResponse,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _AsyncJobClientRaw:
    def __init__(self, client: AsyncJobClient) -> None:
        def get(_: orchestration_models.Job): ...
        def get_batch(_: orchestration_models.GetJobsBatchResponse): ...

        self.get = core.async_with_raw_response(get, client.get)
        self.get_batch = core.async_with_raw_response(get_batch, client.get_batch)


class _AsyncJobClientStreaming:
    def __init__(self, client: AsyncJobClient) -> None:
        def get(_: orchestration_models.Job): ...
        def get_batch(_: orchestration_models.GetJobsBatchResponse): ...

        self.get = core.async_with_streaming_response(get, client.get)
        self.get_batch = core.async_with_streaming_response(get_batch, client.get_batch)
