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

from foundry import _core as core
from foundry import _errors as errors
from foundry.v2.core import models as core_models
from foundry.v2.orchestration import errors as orchestration_errors
from foundry.v2.orchestration import models as orchestration_models


class ScheduleVersionClient:
    """
    The API client for the ScheduleVersion Resource.

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
        self.with_streaming_response = _ScheduleVersionClientStreaming(
            auth=auth, hostname=hostname, config=config
        )
        self.with_raw_response = _ScheduleVersionClientRaw(
            auth=auth, hostname=hostname, config=config
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        schedule_version_rid: orchestration_models.ScheduleVersionRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> orchestration_models.ScheduleVersion:
        """
        Get the ScheduleVersion with the specified rid.
        :param schedule_version_rid: The RID of a schedule version
        :type schedule_version_rid: ScheduleVersionRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: orchestration_models.ScheduleVersion

        :raises ScheduleVersionNotFound: The given ScheduleVersion could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/orchestration/scheduleVersions/{scheduleVersionRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "scheduleVersionRid": schedule_version_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=orchestration_models.ScheduleVersion,
                request_timeout=request_timeout,
                throwable_errors={
                    "ScheduleVersionNotFound": orchestration_errors.ScheduleVersionNotFound,
                },
            ),
        ).decode()

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def schedule(
        self,
        schedule_version_rid: orchestration_models.ScheduleVersionRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> typing.Optional[orchestration_models.Schedule]:
        """

        :param schedule_version_rid: The RID of a schedule version
        :type schedule_version_rid: ScheduleVersionRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Optional[orchestration_models.Schedule]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/orchestration/scheduleVersions/{scheduleVersionRid}/schedule",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "scheduleVersionRid": schedule_version_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=typing.Optional[orchestration_models.Schedule],
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        ).decode()


class _ScheduleVersionClientRaw:
    """
    The API client for the ScheduleVersion Resource.

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
    def get(
        self,
        schedule_version_rid: orchestration_models.ScheduleVersionRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[orchestration_models.ScheduleVersion]:
        """
        Get the ScheduleVersion with the specified rid.
        :param schedule_version_rid: The RID of a schedule version
        :type schedule_version_rid: ScheduleVersionRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[orchestration_models.ScheduleVersion]

        :raises ScheduleVersionNotFound: The given ScheduleVersion could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/orchestration/scheduleVersions/{scheduleVersionRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "scheduleVersionRid": schedule_version_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=orchestration_models.ScheduleVersion,
                request_timeout=request_timeout,
                throwable_errors={
                    "ScheduleVersionNotFound": orchestration_errors.ScheduleVersionNotFound,
                },
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def schedule(
        self,
        schedule_version_rid: orchestration_models.ScheduleVersionRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[typing.Optional[orchestration_models.Schedule]]:
        """

        :param schedule_version_rid: The RID of a schedule version
        :type schedule_version_rid: ScheduleVersionRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[typing.Optional[orchestration_models.Schedule]]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/orchestration/scheduleVersions/{scheduleVersionRid}/schedule",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "scheduleVersionRid": schedule_version_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=typing.Optional[orchestration_models.Schedule],
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )


class _ScheduleVersionClientStreaming:
    """
    The API client for the ScheduleVersion Resource.

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
    def get(
        self,
        schedule_version_rid: orchestration_models.ScheduleVersionRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[orchestration_models.ScheduleVersion]:
        """
        Get the ScheduleVersion with the specified rid.
        :param schedule_version_rid: The RID of a schedule version
        :type schedule_version_rid: ScheduleVersionRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[orchestration_models.ScheduleVersion]

        :raises ScheduleVersionNotFound: The given ScheduleVersion could not be found.
        """

        return self._api_client.stream_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/orchestration/scheduleVersions/{scheduleVersionRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "scheduleVersionRid": schedule_version_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=orchestration_models.ScheduleVersion,
                request_timeout=request_timeout,
                throwable_errors={
                    "ScheduleVersionNotFound": orchestration_errors.ScheduleVersionNotFound,
                },
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def schedule(
        self,
        schedule_version_rid: orchestration_models.ScheduleVersionRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[typing.Optional[orchestration_models.Schedule]]:
        """

        :param schedule_version_rid: The RID of a schedule version
        :type schedule_version_rid: ScheduleVersionRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[typing.Optional[orchestration_models.Schedule]]
        """

        return self._api_client.stream_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/orchestration/scheduleVersions/{scheduleVersionRid}/schedule",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "scheduleVersionRid": schedule_version_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=typing.Optional[orchestration_models.Schedule],
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )
