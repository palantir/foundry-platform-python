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


from __future__ import annotations

from functools import cached_property
from typing import Any
from typing import Dict
from typing import Optional

import pydantic
from typing_extensions import Annotated

from foundry._core import ApiClient
from foundry._core import ApiResponse
from foundry._core import Auth
from foundry._core import Config
from foundry._core import RequestInfo
from foundry._core import StreamingContextManager
from foundry._core.utils import maybe_ignore_preview
from foundry._errors import handle_unexpected
from foundry.v2.core.models._preview_mode import PreviewMode
from foundry.v2.orchestration import errors as orchestration_errors
from foundry.v2.orchestration.models._schedule import Schedule
from foundry.v2.orchestration.models._schedule_version import ScheduleVersion
from foundry.v2.orchestration.models._schedule_version_rid import ScheduleVersionRid


class ScheduleVersionClient:
    """
    The API client for the ScheduleVersion Resource.

    :param auth: Your auth configuration.
    :param hostname: Your Foundry hostname (for example, "myfoundry.palantirfoundry.com"). This can also include your API gateway service URI.
    :param config: Optionally specify the configuration for the HTTP session.
    """

    def __init__(
        self,
        auth: Auth,
        hostname: str,
        config: Optional[Config] = None,
    ):
        self._auth = auth
        self._hostname = hostname
        self._config = config
        self._api_client = ApiClient(auth=auth, hostname=hostname, config=config)
        self.with_streaming_response = _ScheduleVersionClientStreaming(
            auth=auth, hostname=hostname, config=config
        )
        self.with_raw_response = _ScheduleVersionClientRaw(
            auth=auth, hostname=hostname, config=config
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def get(
        self,
        schedule_version_rid: ScheduleVersionRid,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ScheduleVersion:
        """
        Get the ScheduleVersion with the specified rid.
        :param schedule_version_rid: scheduleVersionRid
        :type schedule_version_rid: ScheduleVersionRid
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ScheduleVersion

        :raises ScheduleVersionNotFound: The given ScheduleVersion could not be found.
        """

        return self._api_client.call_api(
            RequestInfo(
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
                response_type=ScheduleVersion,
                request_timeout=request_timeout,
                throwable_errors={
                    "ScheduleVersionNotFound": orchestration_errors.ScheduleVersionNotFound,
                },
            ),
        ).decode()

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def schedule(
        self,
        schedule_version_rid: ScheduleVersionRid,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> Optional[Schedule]:
        """

        :param schedule_version_rid: scheduleVersionRid
        :type schedule_version_rid: ScheduleVersionRid
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: Optional[Schedule]
        """

        return self._api_client.call_api(
            RequestInfo(
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
                response_type=Optional[Schedule],
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
        auth: Auth,
        hostname: str,
        config: Optional[Config] = None,
    ):
        self._auth = auth
        self._hostname = hostname
        self._config = config
        self._api_client = ApiClient(auth=auth, hostname=hostname, config=config)

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def get(
        self,
        schedule_version_rid: ScheduleVersionRid,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[ScheduleVersion]:
        """
        Get the ScheduleVersion with the specified rid.
        :param schedule_version_rid: scheduleVersionRid
        :type schedule_version_rid: ScheduleVersionRid
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[ScheduleVersion]

        :raises ScheduleVersionNotFound: The given ScheduleVersion could not be found.
        """

        return self._api_client.call_api(
            RequestInfo(
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
                response_type=ScheduleVersion,
                request_timeout=request_timeout,
                throwable_errors={
                    "ScheduleVersionNotFound": orchestration_errors.ScheduleVersionNotFound,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def schedule(
        self,
        schedule_version_rid: ScheduleVersionRid,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[Optional[Schedule]]:
        """

        :param schedule_version_rid: scheduleVersionRid
        :type schedule_version_rid: ScheduleVersionRid
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[Optional[Schedule]]
        """

        return self._api_client.call_api(
            RequestInfo(
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
                response_type=Optional[Schedule],
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
        auth: Auth,
        hostname: str,
        config: Optional[Config] = None,
    ):
        self._auth = auth
        self._hostname = hostname
        self._config = config
        self._api_client = ApiClient(auth=auth, hostname=hostname, config=config)

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def get(
        self,
        schedule_version_rid: ScheduleVersionRid,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[ScheduleVersion]:
        """
        Get the ScheduleVersion with the specified rid.
        :param schedule_version_rid: scheduleVersionRid
        :type schedule_version_rid: ScheduleVersionRid
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[ScheduleVersion]

        :raises ScheduleVersionNotFound: The given ScheduleVersion could not be found.
        """

        return self._api_client.stream_api(
            RequestInfo(
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
                response_type=ScheduleVersion,
                request_timeout=request_timeout,
                throwable_errors={
                    "ScheduleVersionNotFound": orchestration_errors.ScheduleVersionNotFound,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def schedule(
        self,
        schedule_version_rid: ScheduleVersionRid,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[Optional[Schedule]]:
        """

        :param schedule_version_rid: scheduleVersionRid
        :type schedule_version_rid: ScheduleVersionRid
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[Optional[Schedule]]
        """

        return self._api_client.stream_api(
            RequestInfo(
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
                response_type=Optional[Schedule],
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )
