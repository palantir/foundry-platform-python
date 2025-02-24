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

import warnings
from functools import cached_property
from typing import Any
from typing import Dict
from typing import Optional
from typing import Union

import pydantic
from typing_extensions import Annotated
from typing_extensions import TypedDict

from foundry._core import ApiClient
from foundry._core import ApiResponse
from foundry._core import Auth
from foundry._core import Config
from foundry._core import RequestInfo
from foundry._core import ResourceIterator
from foundry._core import StreamingContextManager
from foundry._core.utils import maybe_ignore_preview
from foundry._errors import handle_unexpected
from foundry.v2.core.models._page_size import PageSize
from foundry.v2.core.models._page_token import PageToken
from foundry.v2.core.models._preview_mode import PreviewMode
from foundry.v2.orchestration import errors as orchestration_errors
from foundry.v2.orchestration.models._create_schedule_request_action import (
    CreateScheduleRequestAction,
)  # NOQA
from foundry.v2.orchestration.models._create_schedule_request_action_dict import (
    CreateScheduleRequestActionDict,
)  # NOQA
from foundry.v2.orchestration.models._create_schedule_request_scope_mode import (
    CreateScheduleRequestScopeMode,
)  # NOQA
from foundry.v2.orchestration.models._create_schedule_request_scope_mode_dict import (
    CreateScheduleRequestScopeModeDict,
)  # NOQA
from foundry.v2.orchestration.models._list_runs_of_schedule_response import (
    ListRunsOfScheduleResponse,
)  # NOQA
from foundry.v2.orchestration.models._replace_schedule_request_action import (
    ReplaceScheduleRequestAction,
)  # NOQA
from foundry.v2.orchestration.models._replace_schedule_request_action_dict import (
    ReplaceScheduleRequestActionDict,
)  # NOQA
from foundry.v2.orchestration.models._replace_schedule_request_scope_mode import (
    ReplaceScheduleRequestScopeMode,
)  # NOQA
from foundry.v2.orchestration.models._replace_schedule_request_scope_mode_dict import (
    ReplaceScheduleRequestScopeModeDict,
)  # NOQA
from foundry.v2.orchestration.models._schedule import Schedule
from foundry.v2.orchestration.models._schedule_rid import ScheduleRid
from foundry.v2.orchestration.models._schedule_run import ScheduleRun
from foundry.v2.orchestration.models._trigger import Trigger
from foundry.v2.orchestration.models._trigger_dict import TriggerDict


class ScheduleClient:
    """
    The API client for the Schedule Resource.

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
        self.with_streaming_response = _ScheduleClientStreaming(
            auth=auth, hostname=hostname, config=config
        )
        self.with_raw_response = _ScheduleClientRaw(auth=auth, hostname=hostname, config=config)

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def create(
        self,
        *,
        action: Union[CreateScheduleRequestAction, CreateScheduleRequestActionDict],
        description: Optional[str] = None,
        display_name: Optional[str] = None,
        preview: Optional[PreviewMode] = None,
        scope_mode: Optional[
            Union[CreateScheduleRequestScopeMode, CreateScheduleRequestScopeModeDict]
        ] = None,
        trigger: Optional[Union[Trigger, TriggerDict]] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> Schedule:
        """
        Creates a new Schedule.
        :param action:
        :type action: Union[CreateScheduleRequestAction, CreateScheduleRequestActionDict]
        :param description:
        :type description: Optional[str]
        :param display_name:
        :type display_name: Optional[str]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param scope_mode:
        :type scope_mode: Optional[Union[CreateScheduleRequestScopeMode, CreateScheduleRequestScopeModeDict]]
        :param trigger: The schedule trigger. If the requesting user does not have permission to see the trigger, this will be empty.
        :type trigger: Optional[Union[Trigger, TriggerDict]]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: Schedule

        :raises CreateSchedulePermissionDenied: Could not create the Schedule.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/orchestration/schedules",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "displayName": display_name,
                    "description": description,
                    "action": action,
                    "trigger": trigger,
                    "scopeMode": scope_mode,
                },
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "displayName": Optional[str],
                        "description": Optional[str],
                        "action": Union[
                            CreateScheduleRequestAction, CreateScheduleRequestActionDict
                        ],
                        "trigger": Optional[Union[Trigger, TriggerDict]],
                        "scopeMode": Optional[
                            Union[
                                CreateScheduleRequestScopeMode, CreateScheduleRequestScopeModeDict
                            ]
                        ],
                    },
                ),
                response_type=Schedule,
                request_timeout=request_timeout,
                throwable_errors={
                    "CreateSchedulePermissionDenied": orchestration_errors.CreateSchedulePermissionDenied,
                },
            ),
        ).decode()

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def delete(
        self,
        schedule_rid: ScheduleRid,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> None:
        """
        Delete the Schedule with the specified rid.
        :param schedule_rid: scheduleRid
        :type schedule_rid: ScheduleRid
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: None

        :raises DeleteSchedulePermissionDenied: Could not delete the Schedule.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="DELETE",
                resource_path="/v2/orchestration/schedules/{scheduleRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "scheduleRid": schedule_rid,
                },
                header_params={},
                body=None,
                body_type=None,
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "DeleteSchedulePermissionDenied": orchestration_errors.DeleteSchedulePermissionDenied,
                },
            ),
        ).decode()

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def get(
        self,
        schedule_rid: ScheduleRid,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> Schedule:
        """
        Get the Schedule with the specified rid.
        :param schedule_rid: scheduleRid
        :type schedule_rid: ScheduleRid
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: Schedule

        :raises ScheduleNotFound: The given Schedule could not be found.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/orchestration/schedules/{scheduleRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "scheduleRid": schedule_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=Schedule,
                request_timeout=request_timeout,
                throwable_errors={
                    "ScheduleNotFound": orchestration_errors.ScheduleNotFound,
                },
            ),
        ).decode()

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def pause(
        self,
        schedule_rid: ScheduleRid,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> None:
        """

        :param schedule_rid: scheduleRid
        :type schedule_rid: ScheduleRid
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: None

        :raises PauseSchedulePermissionDenied: Could not pause the Schedule.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/orchestration/schedules/{scheduleRid}/pause",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "scheduleRid": schedule_rid,
                },
                header_params={},
                body=None,
                body_type=None,
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "PauseSchedulePermissionDenied": orchestration_errors.PauseSchedulePermissionDenied,
                },
            ),
        ).decode()

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def replace(
        self,
        schedule_rid: ScheduleRid,
        *,
        action: Union[ReplaceScheduleRequestAction, ReplaceScheduleRequestActionDict],
        description: Optional[str] = None,
        display_name: Optional[str] = None,
        preview: Optional[PreviewMode] = None,
        scope_mode: Optional[
            Union[ReplaceScheduleRequestScopeMode, ReplaceScheduleRequestScopeModeDict]
        ] = None,
        trigger: Optional[Union[Trigger, TriggerDict]] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> Schedule:
        """
        Replace the Schedule with the specified rid.
        :param schedule_rid: scheduleRid
        :type schedule_rid: ScheduleRid
        :param action:
        :type action: Union[ReplaceScheduleRequestAction, ReplaceScheduleRequestActionDict]
        :param description:
        :type description: Optional[str]
        :param display_name:
        :type display_name: Optional[str]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param scope_mode:
        :type scope_mode: Optional[Union[ReplaceScheduleRequestScopeMode, ReplaceScheduleRequestScopeModeDict]]
        :param trigger: The schedule trigger. If the requesting user does not have permission to see the trigger, this will be empty.
        :type trigger: Optional[Union[Trigger, TriggerDict]]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: Schedule

        :raises ReplaceSchedulePermissionDenied: Could not replace the Schedule.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="PUT",
                resource_path="/v2/orchestration/schedules/{scheduleRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "scheduleRid": schedule_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "displayName": display_name,
                    "description": description,
                    "action": action,
                    "trigger": trigger,
                    "scopeMode": scope_mode,
                },
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "displayName": Optional[str],
                        "description": Optional[str],
                        "action": Union[
                            ReplaceScheduleRequestAction, ReplaceScheduleRequestActionDict
                        ],
                        "trigger": Optional[Union[Trigger, TriggerDict]],
                        "scopeMode": Optional[
                            Union[
                                ReplaceScheduleRequestScopeMode, ReplaceScheduleRequestScopeModeDict
                            ]
                        ],
                    },
                ),
                response_type=Schedule,
                request_timeout=request_timeout,
                throwable_errors={
                    "ReplaceSchedulePermissionDenied": orchestration_errors.ReplaceSchedulePermissionDenied,
                },
            ),
        ).decode()

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def run(
        self,
        schedule_rid: ScheduleRid,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ScheduleRun:
        """

        :param schedule_rid: scheduleRid
        :type schedule_rid: ScheduleRid
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ScheduleRun

        :raises RunSchedulePermissionDenied: Could not run the Schedule.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/orchestration/schedules/{scheduleRid}/run",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "scheduleRid": schedule_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ScheduleRun,
                request_timeout=request_timeout,
                throwable_errors={
                    "RunSchedulePermissionDenied": orchestration_errors.RunSchedulePermissionDenied,
                },
            ),
        ).decode()

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def runs(
        self,
        schedule_rid: ScheduleRid,
        *,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ResourceIterator[ScheduleRun]:
        """
        Get the most recent runs of a Schedule. If no page size is provided, a page size of 100 will be used.

        :param schedule_rid: scheduleRid
        :type schedule_rid: ScheduleRid
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param page_token: pageToken
        :type page_token: Optional[PageToken]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ResourceIterator[ScheduleRun]
        """

        return self._api_client.iterate_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/orchestration/schedules/{scheduleRid}/runs",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
                    "preview": preview,
                },
                path_params={
                    "scheduleRid": schedule_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ListRunsOfScheduleResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def runs_page(
        self,
        schedule_rid: ScheduleRid,
        *,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ListRunsOfScheduleResponse:
        """
        Get the most recent runs of a Schedule. If no page size is provided, a page size of 100 will be used.

        :param schedule_rid: scheduleRid
        :type schedule_rid: ScheduleRid
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param page_token: pageToken
        :type page_token: Optional[PageToken]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ListRunsOfScheduleResponse
        """

        warnings.warn(
            "The client.orchestration.Schedule.runs_page(...) method has been deprecated. Please use client.orchestration.Schedule.runs(...) instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/orchestration/schedules/{scheduleRid}/runs",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
                    "preview": preview,
                },
                path_params={
                    "scheduleRid": schedule_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ListRunsOfScheduleResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        ).decode()

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def unpause(
        self,
        schedule_rid: ScheduleRid,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> None:
        """

        :param schedule_rid: scheduleRid
        :type schedule_rid: ScheduleRid
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: None

        :raises UnpauseSchedulePermissionDenied: Could not unpause the Schedule.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/orchestration/schedules/{scheduleRid}/unpause",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "scheduleRid": schedule_rid,
                },
                header_params={},
                body=None,
                body_type=None,
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "UnpauseSchedulePermissionDenied": orchestration_errors.UnpauseSchedulePermissionDenied,
                },
            ),
        ).decode()


class _ScheduleClientRaw:
    """
    The API client for the Schedule Resource.

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
    def create(
        self,
        *,
        action: Union[CreateScheduleRequestAction, CreateScheduleRequestActionDict],
        description: Optional[str] = None,
        display_name: Optional[str] = None,
        preview: Optional[PreviewMode] = None,
        scope_mode: Optional[
            Union[CreateScheduleRequestScopeMode, CreateScheduleRequestScopeModeDict]
        ] = None,
        trigger: Optional[Union[Trigger, TriggerDict]] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[Schedule]:
        """
        Creates a new Schedule.
        :param action:
        :type action: Union[CreateScheduleRequestAction, CreateScheduleRequestActionDict]
        :param description:
        :type description: Optional[str]
        :param display_name:
        :type display_name: Optional[str]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param scope_mode:
        :type scope_mode: Optional[Union[CreateScheduleRequestScopeMode, CreateScheduleRequestScopeModeDict]]
        :param trigger: The schedule trigger. If the requesting user does not have permission to see the trigger, this will be empty.
        :type trigger: Optional[Union[Trigger, TriggerDict]]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[Schedule]

        :raises CreateSchedulePermissionDenied: Could not create the Schedule.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/orchestration/schedules",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "displayName": display_name,
                    "description": description,
                    "action": action,
                    "trigger": trigger,
                    "scopeMode": scope_mode,
                },
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "displayName": Optional[str],
                        "description": Optional[str],
                        "action": Union[
                            CreateScheduleRequestAction, CreateScheduleRequestActionDict
                        ],
                        "trigger": Optional[Union[Trigger, TriggerDict]],
                        "scopeMode": Optional[
                            Union[
                                CreateScheduleRequestScopeMode, CreateScheduleRequestScopeModeDict
                            ]
                        ],
                    },
                ),
                response_type=Schedule,
                request_timeout=request_timeout,
                throwable_errors={
                    "CreateSchedulePermissionDenied": orchestration_errors.CreateSchedulePermissionDenied,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def delete(
        self,
        schedule_rid: ScheduleRid,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[None]:
        """
        Delete the Schedule with the specified rid.
        :param schedule_rid: scheduleRid
        :type schedule_rid: ScheduleRid
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[None]

        :raises DeleteSchedulePermissionDenied: Could not delete the Schedule.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="DELETE",
                resource_path="/v2/orchestration/schedules/{scheduleRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "scheduleRid": schedule_rid,
                },
                header_params={},
                body=None,
                body_type=None,
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "DeleteSchedulePermissionDenied": orchestration_errors.DeleteSchedulePermissionDenied,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def get(
        self,
        schedule_rid: ScheduleRid,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[Schedule]:
        """
        Get the Schedule with the specified rid.
        :param schedule_rid: scheduleRid
        :type schedule_rid: ScheduleRid
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[Schedule]

        :raises ScheduleNotFound: The given Schedule could not be found.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/orchestration/schedules/{scheduleRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "scheduleRid": schedule_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=Schedule,
                request_timeout=request_timeout,
                throwable_errors={
                    "ScheduleNotFound": orchestration_errors.ScheduleNotFound,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def pause(
        self,
        schedule_rid: ScheduleRid,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[None]:
        """

        :param schedule_rid: scheduleRid
        :type schedule_rid: ScheduleRid
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[None]

        :raises PauseSchedulePermissionDenied: Could not pause the Schedule.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/orchestration/schedules/{scheduleRid}/pause",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "scheduleRid": schedule_rid,
                },
                header_params={},
                body=None,
                body_type=None,
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "PauseSchedulePermissionDenied": orchestration_errors.PauseSchedulePermissionDenied,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def replace(
        self,
        schedule_rid: ScheduleRid,
        *,
        action: Union[ReplaceScheduleRequestAction, ReplaceScheduleRequestActionDict],
        description: Optional[str] = None,
        display_name: Optional[str] = None,
        preview: Optional[PreviewMode] = None,
        scope_mode: Optional[
            Union[ReplaceScheduleRequestScopeMode, ReplaceScheduleRequestScopeModeDict]
        ] = None,
        trigger: Optional[Union[Trigger, TriggerDict]] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[Schedule]:
        """
        Replace the Schedule with the specified rid.
        :param schedule_rid: scheduleRid
        :type schedule_rid: ScheduleRid
        :param action:
        :type action: Union[ReplaceScheduleRequestAction, ReplaceScheduleRequestActionDict]
        :param description:
        :type description: Optional[str]
        :param display_name:
        :type display_name: Optional[str]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param scope_mode:
        :type scope_mode: Optional[Union[ReplaceScheduleRequestScopeMode, ReplaceScheduleRequestScopeModeDict]]
        :param trigger: The schedule trigger. If the requesting user does not have permission to see the trigger, this will be empty.
        :type trigger: Optional[Union[Trigger, TriggerDict]]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[Schedule]

        :raises ReplaceSchedulePermissionDenied: Could not replace the Schedule.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="PUT",
                resource_path="/v2/orchestration/schedules/{scheduleRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "scheduleRid": schedule_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "displayName": display_name,
                    "description": description,
                    "action": action,
                    "trigger": trigger,
                    "scopeMode": scope_mode,
                },
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "displayName": Optional[str],
                        "description": Optional[str],
                        "action": Union[
                            ReplaceScheduleRequestAction, ReplaceScheduleRequestActionDict
                        ],
                        "trigger": Optional[Union[Trigger, TriggerDict]],
                        "scopeMode": Optional[
                            Union[
                                ReplaceScheduleRequestScopeMode, ReplaceScheduleRequestScopeModeDict
                            ]
                        ],
                    },
                ),
                response_type=Schedule,
                request_timeout=request_timeout,
                throwable_errors={
                    "ReplaceSchedulePermissionDenied": orchestration_errors.ReplaceSchedulePermissionDenied,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def run(
        self,
        schedule_rid: ScheduleRid,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[ScheduleRun]:
        """

        :param schedule_rid: scheduleRid
        :type schedule_rid: ScheduleRid
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[ScheduleRun]

        :raises RunSchedulePermissionDenied: Could not run the Schedule.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/orchestration/schedules/{scheduleRid}/run",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "scheduleRid": schedule_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ScheduleRun,
                request_timeout=request_timeout,
                throwable_errors={
                    "RunSchedulePermissionDenied": orchestration_errors.RunSchedulePermissionDenied,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def runs(
        self,
        schedule_rid: ScheduleRid,
        *,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[ListRunsOfScheduleResponse]:
        """
        Get the most recent runs of a Schedule. If no page size is provided, a page size of 100 will be used.

        :param schedule_rid: scheduleRid
        :type schedule_rid: ScheduleRid
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param page_token: pageToken
        :type page_token: Optional[PageToken]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[ListRunsOfScheduleResponse]
        """

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/orchestration/schedules/{scheduleRid}/runs",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
                    "preview": preview,
                },
                path_params={
                    "scheduleRid": schedule_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ListRunsOfScheduleResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def runs_page(
        self,
        schedule_rid: ScheduleRid,
        *,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[ListRunsOfScheduleResponse]:
        """
        Get the most recent runs of a Schedule. If no page size is provided, a page size of 100 will be used.

        :param schedule_rid: scheduleRid
        :type schedule_rid: ScheduleRid
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param page_token: pageToken
        :type page_token: Optional[PageToken]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[ListRunsOfScheduleResponse]
        """

        warnings.warn(
            "The client.orchestration.Schedule.runs_page(...) method has been deprecated. Please use client.orchestration.Schedule.runs(...) instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/orchestration/schedules/{scheduleRid}/runs",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
                    "preview": preview,
                },
                path_params={
                    "scheduleRid": schedule_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ListRunsOfScheduleResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def unpause(
        self,
        schedule_rid: ScheduleRid,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[None]:
        """

        :param schedule_rid: scheduleRid
        :type schedule_rid: ScheduleRid
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[None]

        :raises UnpauseSchedulePermissionDenied: Could not unpause the Schedule.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/orchestration/schedules/{scheduleRid}/unpause",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "scheduleRid": schedule_rid,
                },
                header_params={},
                body=None,
                body_type=None,
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "UnpauseSchedulePermissionDenied": orchestration_errors.UnpauseSchedulePermissionDenied,
                },
            ),
        )


class _ScheduleClientStreaming:
    """
    The API client for the Schedule Resource.

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
    def create(
        self,
        *,
        action: Union[CreateScheduleRequestAction, CreateScheduleRequestActionDict],
        description: Optional[str] = None,
        display_name: Optional[str] = None,
        preview: Optional[PreviewMode] = None,
        scope_mode: Optional[
            Union[CreateScheduleRequestScopeMode, CreateScheduleRequestScopeModeDict]
        ] = None,
        trigger: Optional[Union[Trigger, TriggerDict]] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[Schedule]:
        """
        Creates a new Schedule.
        :param action:
        :type action: Union[CreateScheduleRequestAction, CreateScheduleRequestActionDict]
        :param description:
        :type description: Optional[str]
        :param display_name:
        :type display_name: Optional[str]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param scope_mode:
        :type scope_mode: Optional[Union[CreateScheduleRequestScopeMode, CreateScheduleRequestScopeModeDict]]
        :param trigger: The schedule trigger. If the requesting user does not have permission to see the trigger, this will be empty.
        :type trigger: Optional[Union[Trigger, TriggerDict]]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[Schedule]

        :raises CreateSchedulePermissionDenied: Could not create the Schedule.
        """

        return self._api_client.stream_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/orchestration/schedules",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "displayName": display_name,
                    "description": description,
                    "action": action,
                    "trigger": trigger,
                    "scopeMode": scope_mode,
                },
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "displayName": Optional[str],
                        "description": Optional[str],
                        "action": Union[
                            CreateScheduleRequestAction, CreateScheduleRequestActionDict
                        ],
                        "trigger": Optional[Union[Trigger, TriggerDict]],
                        "scopeMode": Optional[
                            Union[
                                CreateScheduleRequestScopeMode, CreateScheduleRequestScopeModeDict
                            ]
                        ],
                    },
                ),
                response_type=Schedule,
                request_timeout=request_timeout,
                throwable_errors={
                    "CreateSchedulePermissionDenied": orchestration_errors.CreateSchedulePermissionDenied,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def delete(
        self,
        schedule_rid: ScheduleRid,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[None]:
        """
        Delete the Schedule with the specified rid.
        :param schedule_rid: scheduleRid
        :type schedule_rid: ScheduleRid
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[None]

        :raises DeleteSchedulePermissionDenied: Could not delete the Schedule.
        """

        return self._api_client.stream_api(
            RequestInfo(
                method="DELETE",
                resource_path="/v2/orchestration/schedules/{scheduleRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "scheduleRid": schedule_rid,
                },
                header_params={},
                body=None,
                body_type=None,
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "DeleteSchedulePermissionDenied": orchestration_errors.DeleteSchedulePermissionDenied,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def get(
        self,
        schedule_rid: ScheduleRid,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[Schedule]:
        """
        Get the Schedule with the specified rid.
        :param schedule_rid: scheduleRid
        :type schedule_rid: ScheduleRid
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[Schedule]

        :raises ScheduleNotFound: The given Schedule could not be found.
        """

        return self._api_client.stream_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/orchestration/schedules/{scheduleRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "scheduleRid": schedule_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=Schedule,
                request_timeout=request_timeout,
                throwable_errors={
                    "ScheduleNotFound": orchestration_errors.ScheduleNotFound,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def pause(
        self,
        schedule_rid: ScheduleRid,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[None]:
        """

        :param schedule_rid: scheduleRid
        :type schedule_rid: ScheduleRid
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[None]

        :raises PauseSchedulePermissionDenied: Could not pause the Schedule.
        """

        return self._api_client.stream_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/orchestration/schedules/{scheduleRid}/pause",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "scheduleRid": schedule_rid,
                },
                header_params={},
                body=None,
                body_type=None,
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "PauseSchedulePermissionDenied": orchestration_errors.PauseSchedulePermissionDenied,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def replace(
        self,
        schedule_rid: ScheduleRid,
        *,
        action: Union[ReplaceScheduleRequestAction, ReplaceScheduleRequestActionDict],
        description: Optional[str] = None,
        display_name: Optional[str] = None,
        preview: Optional[PreviewMode] = None,
        scope_mode: Optional[
            Union[ReplaceScheduleRequestScopeMode, ReplaceScheduleRequestScopeModeDict]
        ] = None,
        trigger: Optional[Union[Trigger, TriggerDict]] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[Schedule]:
        """
        Replace the Schedule with the specified rid.
        :param schedule_rid: scheduleRid
        :type schedule_rid: ScheduleRid
        :param action:
        :type action: Union[ReplaceScheduleRequestAction, ReplaceScheduleRequestActionDict]
        :param description:
        :type description: Optional[str]
        :param display_name:
        :type display_name: Optional[str]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param scope_mode:
        :type scope_mode: Optional[Union[ReplaceScheduleRequestScopeMode, ReplaceScheduleRequestScopeModeDict]]
        :param trigger: The schedule trigger. If the requesting user does not have permission to see the trigger, this will be empty.
        :type trigger: Optional[Union[Trigger, TriggerDict]]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[Schedule]

        :raises ReplaceSchedulePermissionDenied: Could not replace the Schedule.
        """

        return self._api_client.stream_api(
            RequestInfo(
                method="PUT",
                resource_path="/v2/orchestration/schedules/{scheduleRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "scheduleRid": schedule_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "displayName": display_name,
                    "description": description,
                    "action": action,
                    "trigger": trigger,
                    "scopeMode": scope_mode,
                },
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "displayName": Optional[str],
                        "description": Optional[str],
                        "action": Union[
                            ReplaceScheduleRequestAction, ReplaceScheduleRequestActionDict
                        ],
                        "trigger": Optional[Union[Trigger, TriggerDict]],
                        "scopeMode": Optional[
                            Union[
                                ReplaceScheduleRequestScopeMode, ReplaceScheduleRequestScopeModeDict
                            ]
                        ],
                    },
                ),
                response_type=Schedule,
                request_timeout=request_timeout,
                throwable_errors={
                    "ReplaceSchedulePermissionDenied": orchestration_errors.ReplaceSchedulePermissionDenied,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def run(
        self,
        schedule_rid: ScheduleRid,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[ScheduleRun]:
        """

        :param schedule_rid: scheduleRid
        :type schedule_rid: ScheduleRid
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[ScheduleRun]

        :raises RunSchedulePermissionDenied: Could not run the Schedule.
        """

        return self._api_client.stream_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/orchestration/schedules/{scheduleRid}/run",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "scheduleRid": schedule_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ScheduleRun,
                request_timeout=request_timeout,
                throwable_errors={
                    "RunSchedulePermissionDenied": orchestration_errors.RunSchedulePermissionDenied,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def runs(
        self,
        schedule_rid: ScheduleRid,
        *,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[ListRunsOfScheduleResponse]:
        """
        Get the most recent runs of a Schedule. If no page size is provided, a page size of 100 will be used.

        :param schedule_rid: scheduleRid
        :type schedule_rid: ScheduleRid
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param page_token: pageToken
        :type page_token: Optional[PageToken]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[ListRunsOfScheduleResponse]
        """

        return self._api_client.stream_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/orchestration/schedules/{scheduleRid}/runs",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
                    "preview": preview,
                },
                path_params={
                    "scheduleRid": schedule_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ListRunsOfScheduleResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def runs_page(
        self,
        schedule_rid: ScheduleRid,
        *,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[ListRunsOfScheduleResponse]:
        """
        Get the most recent runs of a Schedule. If no page size is provided, a page size of 100 will be used.

        :param schedule_rid: scheduleRid
        :type schedule_rid: ScheduleRid
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param page_token: pageToken
        :type page_token: Optional[PageToken]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[ListRunsOfScheduleResponse]
        """

        warnings.warn(
            "The client.orchestration.Schedule.runs_page(...) method has been deprecated. Please use client.orchestration.Schedule.runs(...) instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        return self._api_client.stream_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/orchestration/schedules/{scheduleRid}/runs",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
                    "preview": preview,
                },
                path_params={
                    "scheduleRid": schedule_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ListRunsOfScheduleResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def unpause(
        self,
        schedule_rid: ScheduleRid,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[None]:
        """

        :param schedule_rid: scheduleRid
        :type schedule_rid: ScheduleRid
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[None]

        :raises UnpauseSchedulePermissionDenied: Could not unpause the Schedule.
        """

        return self._api_client.stream_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/orchestration/schedules/{scheduleRid}/unpause",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "scheduleRid": schedule_rid,
                },
                header_params={},
                body=None,
                body_type=None,
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "UnpauseSchedulePermissionDenied": orchestration_errors.UnpauseSchedulePermissionDenied,
                },
            ),
        )
