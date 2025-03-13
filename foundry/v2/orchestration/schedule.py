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
import warnings

import pydantic
import typing_extensions

from foundry import _core as core
from foundry import _errors as errors
from foundry.v2.core import models as core_models
from foundry.v2.orchestration import errors as orchestration_errors
from foundry.v2.orchestration import models as orchestration_models


class ScheduleClient:
    """
    The API client for the Schedule Resource.

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
        self.with_streaming_response = _ScheduleClientStreaming(
            auth=auth, hostname=hostname, config=config
        )
        self.with_raw_response = _ScheduleClientRaw(auth=auth, hostname=hostname, config=config)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def create(
        self,
        *,
        action: typing.Union[
            orchestration_models.CreateScheduleRequestAction,
            orchestration_models.CreateScheduleRequestActionDict,
        ],
        description: typing.Optional[str] = None,
        display_name: typing.Optional[str] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        scope_mode: typing.Optional[
            typing.Union[
                orchestration_models.CreateScheduleRequestScopeMode,
                orchestration_models.CreateScheduleRequestScopeModeDict,
            ]
        ] = None,
        trigger: typing.Optional[
            typing.Union[orchestration_models.Trigger, orchestration_models.TriggerDict]
        ] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> orchestration_models.Schedule:
        """
        Creates a new Schedule.
        :param action:
        :type action: Union[CreateScheduleRequestAction, CreateScheduleRequestActionDict]
        :param description:
        :type description: Optional[str]
        :param display_name:
        :type display_name: Optional[str]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param scope_mode:
        :type scope_mode: Optional[Union[CreateScheduleRequestScopeMode, CreateScheduleRequestScopeModeDict]]
        :param trigger: The schedule trigger. If the requesting user does not have permission to see the trigger, this will be empty.
        :type trigger: Optional[Union[Trigger, TriggerDict]]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: orchestration_models.Schedule

        :raises CreateSchedulePermissionDenied: Could not create the Schedule.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "displayName": typing.Optional[str],
                        "description": typing.Optional[str],
                        "action": typing.Union[
                            orchestration_models.CreateScheduleRequestAction,
                            orchestration_models.CreateScheduleRequestActionDict,
                        ],
                        "trigger": typing.Optional[
                            typing.Union[
                                orchestration_models.Trigger, orchestration_models.TriggerDict
                            ]
                        ],
                        "scopeMode": typing.Optional[
                            typing.Union[
                                orchestration_models.CreateScheduleRequestScopeMode,
                                orchestration_models.CreateScheduleRequestScopeModeDict,
                            ]
                        ],
                    },
                ),
                response_type=orchestration_models.Schedule,
                request_timeout=request_timeout,
                throwable_errors={
                    "CreateSchedulePermissionDenied": orchestration_errors.CreateSchedulePermissionDenied,
                },
            ),
        ).decode()

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def delete(
        self,
        schedule_rid: orchestration_models.ScheduleRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> None:
        """
        Delete the Schedule with the specified rid.
        :param schedule_rid:
        :type schedule_rid: ScheduleRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: None

        :raises DeleteSchedulePermissionDenied: Could not delete the Schedule.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        schedule_rid: orchestration_models.ScheduleRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> orchestration_models.Schedule:
        """
        Get the Schedule with the specified rid.
        :param schedule_rid:
        :type schedule_rid: ScheduleRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: orchestration_models.Schedule

        :raises ScheduleNotFound: The given Schedule could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                response_type=orchestration_models.Schedule,
                request_timeout=request_timeout,
                throwable_errors={
                    "ScheduleNotFound": orchestration_errors.ScheduleNotFound,
                },
            ),
        ).decode()

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def pause(
        self,
        schedule_rid: orchestration_models.ScheduleRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> None:
        """

        :param schedule_rid:
        :type schedule_rid: ScheduleRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: None

        :raises PauseSchedulePermissionDenied: Could not pause the Schedule.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def replace(
        self,
        schedule_rid: orchestration_models.ScheduleRid,
        *,
        action: typing.Union[
            orchestration_models.ReplaceScheduleRequestAction,
            orchestration_models.ReplaceScheduleRequestActionDict,
        ],
        description: typing.Optional[str] = None,
        display_name: typing.Optional[str] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        scope_mode: typing.Optional[
            typing.Union[
                orchestration_models.ReplaceScheduleRequestScopeMode,
                orchestration_models.ReplaceScheduleRequestScopeModeDict,
            ]
        ] = None,
        trigger: typing.Optional[
            typing.Union[orchestration_models.Trigger, orchestration_models.TriggerDict]
        ] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> orchestration_models.Schedule:
        """
        Replace the Schedule with the specified rid.
        :param schedule_rid:
        :type schedule_rid: ScheduleRid
        :param action:
        :type action: Union[ReplaceScheduleRequestAction, ReplaceScheduleRequestActionDict]
        :param description:
        :type description: Optional[str]
        :param display_name:
        :type display_name: Optional[str]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param scope_mode:
        :type scope_mode: Optional[Union[ReplaceScheduleRequestScopeMode, ReplaceScheduleRequestScopeModeDict]]
        :param trigger: The schedule trigger. If the requesting user does not have permission to see the trigger, this will be empty.
        :type trigger: Optional[Union[Trigger, TriggerDict]]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: orchestration_models.Schedule

        :raises ReplaceSchedulePermissionDenied: Could not replace the Schedule.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "displayName": typing.Optional[str],
                        "description": typing.Optional[str],
                        "action": typing.Union[
                            orchestration_models.ReplaceScheduleRequestAction,
                            orchestration_models.ReplaceScheduleRequestActionDict,
                        ],
                        "trigger": typing.Optional[
                            typing.Union[
                                orchestration_models.Trigger, orchestration_models.TriggerDict
                            ]
                        ],
                        "scopeMode": typing.Optional[
                            typing.Union[
                                orchestration_models.ReplaceScheduleRequestScopeMode,
                                orchestration_models.ReplaceScheduleRequestScopeModeDict,
                            ]
                        ],
                    },
                ),
                response_type=orchestration_models.Schedule,
                request_timeout=request_timeout,
                throwable_errors={
                    "ReplaceSchedulePermissionDenied": orchestration_errors.ReplaceSchedulePermissionDenied,
                },
            ),
        ).decode()

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def run(
        self,
        schedule_rid: orchestration_models.ScheduleRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> orchestration_models.ScheduleRun:
        """

        :param schedule_rid:
        :type schedule_rid: ScheduleRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: orchestration_models.ScheduleRun

        :raises RunSchedulePermissionDenied: Could not run the Schedule.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                response_type=orchestration_models.ScheduleRun,
                request_timeout=request_timeout,
                throwable_errors={
                    "RunSchedulePermissionDenied": orchestration_errors.RunSchedulePermissionDenied,
                },
            ),
        ).decode()

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def runs(
        self,
        schedule_rid: orchestration_models.ScheduleRid,
        *,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ResourceIterator[orchestration_models.ScheduleRun]:
        """
        Get the most recent runs of a Schedule. If no page size is provided, a page size of 100 will be used.

        :param schedule_rid:
        :type schedule_rid: ScheduleRid
        :param page_size: The page size to use for the endpoint.
        :type page_size: Optional[PageSize]
        :param page_token: The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
        :type page_token: Optional[PageToken]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ResourceIterator[orchestration_models.ScheduleRun]
        """

        return self._api_client.iterate_api(
            core.RequestInfo(
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
                response_type=orchestration_models.ListRunsOfScheduleResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def runs_page(
        self,
        schedule_rid: orchestration_models.ScheduleRid,
        *,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> orchestration_models.ListRunsOfScheduleResponse:
        """
        Get the most recent runs of a Schedule. If no page size is provided, a page size of 100 will be used.

        :param schedule_rid:
        :type schedule_rid: ScheduleRid
        :param page_size: The page size to use for the endpoint.
        :type page_size: Optional[PageSize]
        :param page_token: The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
        :type page_token: Optional[PageToken]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: orchestration_models.ListRunsOfScheduleResponse
        """

        warnings.warn(
            "The client.orchestration.Schedule.runs_page(...) method has been deprecated. Please use client.orchestration.Schedule.runs(...) instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        return self._api_client.call_api(
            core.RequestInfo(
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
                response_type=orchestration_models.ListRunsOfScheduleResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        ).decode()

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def unpause(
        self,
        schedule_rid: orchestration_models.ScheduleRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> None:
        """

        :param schedule_rid:
        :type schedule_rid: ScheduleRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: None

        :raises UnpauseSchedulePermissionDenied: Could not unpause the Schedule.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
    def create(
        self,
        *,
        action: typing.Union[
            orchestration_models.CreateScheduleRequestAction,
            orchestration_models.CreateScheduleRequestActionDict,
        ],
        description: typing.Optional[str] = None,
        display_name: typing.Optional[str] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        scope_mode: typing.Optional[
            typing.Union[
                orchestration_models.CreateScheduleRequestScopeMode,
                orchestration_models.CreateScheduleRequestScopeModeDict,
            ]
        ] = None,
        trigger: typing.Optional[
            typing.Union[orchestration_models.Trigger, orchestration_models.TriggerDict]
        ] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[orchestration_models.Schedule]:
        """
        Creates a new Schedule.
        :param action:
        :type action: Union[CreateScheduleRequestAction, CreateScheduleRequestActionDict]
        :param description:
        :type description: Optional[str]
        :param display_name:
        :type display_name: Optional[str]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param scope_mode:
        :type scope_mode: Optional[Union[CreateScheduleRequestScopeMode, CreateScheduleRequestScopeModeDict]]
        :param trigger: The schedule trigger. If the requesting user does not have permission to see the trigger, this will be empty.
        :type trigger: Optional[Union[Trigger, TriggerDict]]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[orchestration_models.Schedule]

        :raises CreateSchedulePermissionDenied: Could not create the Schedule.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "displayName": typing.Optional[str],
                        "description": typing.Optional[str],
                        "action": typing.Union[
                            orchestration_models.CreateScheduleRequestAction,
                            orchestration_models.CreateScheduleRequestActionDict,
                        ],
                        "trigger": typing.Optional[
                            typing.Union[
                                orchestration_models.Trigger, orchestration_models.TriggerDict
                            ]
                        ],
                        "scopeMode": typing.Optional[
                            typing.Union[
                                orchestration_models.CreateScheduleRequestScopeMode,
                                orchestration_models.CreateScheduleRequestScopeModeDict,
                            ]
                        ],
                    },
                ),
                response_type=orchestration_models.Schedule,
                request_timeout=request_timeout,
                throwable_errors={
                    "CreateSchedulePermissionDenied": orchestration_errors.CreateSchedulePermissionDenied,
                },
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def delete(
        self,
        schedule_rid: orchestration_models.ScheduleRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[None]:
        """
        Delete the Schedule with the specified rid.
        :param schedule_rid:
        :type schedule_rid: ScheduleRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[None]

        :raises DeleteSchedulePermissionDenied: Could not delete the Schedule.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        schedule_rid: orchestration_models.ScheduleRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[orchestration_models.Schedule]:
        """
        Get the Schedule with the specified rid.
        :param schedule_rid:
        :type schedule_rid: ScheduleRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[orchestration_models.Schedule]

        :raises ScheduleNotFound: The given Schedule could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                response_type=orchestration_models.Schedule,
                request_timeout=request_timeout,
                throwable_errors={
                    "ScheduleNotFound": orchestration_errors.ScheduleNotFound,
                },
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def pause(
        self,
        schedule_rid: orchestration_models.ScheduleRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[None]:
        """

        :param schedule_rid:
        :type schedule_rid: ScheduleRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[None]

        :raises PauseSchedulePermissionDenied: Could not pause the Schedule.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def replace(
        self,
        schedule_rid: orchestration_models.ScheduleRid,
        *,
        action: typing.Union[
            orchestration_models.ReplaceScheduleRequestAction,
            orchestration_models.ReplaceScheduleRequestActionDict,
        ],
        description: typing.Optional[str] = None,
        display_name: typing.Optional[str] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        scope_mode: typing.Optional[
            typing.Union[
                orchestration_models.ReplaceScheduleRequestScopeMode,
                orchestration_models.ReplaceScheduleRequestScopeModeDict,
            ]
        ] = None,
        trigger: typing.Optional[
            typing.Union[orchestration_models.Trigger, orchestration_models.TriggerDict]
        ] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[orchestration_models.Schedule]:
        """
        Replace the Schedule with the specified rid.
        :param schedule_rid:
        :type schedule_rid: ScheduleRid
        :param action:
        :type action: Union[ReplaceScheduleRequestAction, ReplaceScheduleRequestActionDict]
        :param description:
        :type description: Optional[str]
        :param display_name:
        :type display_name: Optional[str]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param scope_mode:
        :type scope_mode: Optional[Union[ReplaceScheduleRequestScopeMode, ReplaceScheduleRequestScopeModeDict]]
        :param trigger: The schedule trigger. If the requesting user does not have permission to see the trigger, this will be empty.
        :type trigger: Optional[Union[Trigger, TriggerDict]]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[orchestration_models.Schedule]

        :raises ReplaceSchedulePermissionDenied: Could not replace the Schedule.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "displayName": typing.Optional[str],
                        "description": typing.Optional[str],
                        "action": typing.Union[
                            orchestration_models.ReplaceScheduleRequestAction,
                            orchestration_models.ReplaceScheduleRequestActionDict,
                        ],
                        "trigger": typing.Optional[
                            typing.Union[
                                orchestration_models.Trigger, orchestration_models.TriggerDict
                            ]
                        ],
                        "scopeMode": typing.Optional[
                            typing.Union[
                                orchestration_models.ReplaceScheduleRequestScopeMode,
                                orchestration_models.ReplaceScheduleRequestScopeModeDict,
                            ]
                        ],
                    },
                ),
                response_type=orchestration_models.Schedule,
                request_timeout=request_timeout,
                throwable_errors={
                    "ReplaceSchedulePermissionDenied": orchestration_errors.ReplaceSchedulePermissionDenied,
                },
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def run(
        self,
        schedule_rid: orchestration_models.ScheduleRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[orchestration_models.ScheduleRun]:
        """

        :param schedule_rid:
        :type schedule_rid: ScheduleRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[orchestration_models.ScheduleRun]

        :raises RunSchedulePermissionDenied: Could not run the Schedule.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                response_type=orchestration_models.ScheduleRun,
                request_timeout=request_timeout,
                throwable_errors={
                    "RunSchedulePermissionDenied": orchestration_errors.RunSchedulePermissionDenied,
                },
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def runs(
        self,
        schedule_rid: orchestration_models.ScheduleRid,
        *,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[orchestration_models.ListRunsOfScheduleResponse]:
        """
        Get the most recent runs of a Schedule. If no page size is provided, a page size of 100 will be used.

        :param schedule_rid:
        :type schedule_rid: ScheduleRid
        :param page_size: The page size to use for the endpoint.
        :type page_size: Optional[PageSize]
        :param page_token: The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
        :type page_token: Optional[PageToken]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[orchestration_models.ListRunsOfScheduleResponse]
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                response_type=orchestration_models.ListRunsOfScheduleResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def runs_page(
        self,
        schedule_rid: orchestration_models.ScheduleRid,
        *,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[orchestration_models.ListRunsOfScheduleResponse]:
        """
        Get the most recent runs of a Schedule. If no page size is provided, a page size of 100 will be used.

        :param schedule_rid:
        :type schedule_rid: ScheduleRid
        :param page_size: The page size to use for the endpoint.
        :type page_size: Optional[PageSize]
        :param page_token: The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
        :type page_token: Optional[PageToken]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[orchestration_models.ListRunsOfScheduleResponse]
        """

        warnings.warn(
            "The client.orchestration.Schedule.runs_page(...) method has been deprecated. Please use client.orchestration.Schedule.runs(...) instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        return self._api_client.call_api(
            core.RequestInfo(
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
                response_type=orchestration_models.ListRunsOfScheduleResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def unpause(
        self,
        schedule_rid: orchestration_models.ScheduleRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[None]:
        """

        :param schedule_rid:
        :type schedule_rid: ScheduleRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[None]

        :raises UnpauseSchedulePermissionDenied: Could not unpause the Schedule.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
    def create(
        self,
        *,
        action: typing.Union[
            orchestration_models.CreateScheduleRequestAction,
            orchestration_models.CreateScheduleRequestActionDict,
        ],
        description: typing.Optional[str] = None,
        display_name: typing.Optional[str] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        scope_mode: typing.Optional[
            typing.Union[
                orchestration_models.CreateScheduleRequestScopeMode,
                orchestration_models.CreateScheduleRequestScopeModeDict,
            ]
        ] = None,
        trigger: typing.Optional[
            typing.Union[orchestration_models.Trigger, orchestration_models.TriggerDict]
        ] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[orchestration_models.Schedule]:
        """
        Creates a new Schedule.
        :param action:
        :type action: Union[CreateScheduleRequestAction, CreateScheduleRequestActionDict]
        :param description:
        :type description: Optional[str]
        :param display_name:
        :type display_name: Optional[str]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param scope_mode:
        :type scope_mode: Optional[Union[CreateScheduleRequestScopeMode, CreateScheduleRequestScopeModeDict]]
        :param trigger: The schedule trigger. If the requesting user does not have permission to see the trigger, this will be empty.
        :type trigger: Optional[Union[Trigger, TriggerDict]]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[orchestration_models.Schedule]

        :raises CreateSchedulePermissionDenied: Could not create the Schedule.
        """

        return self._api_client.stream_api(
            core.RequestInfo(
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
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "displayName": typing.Optional[str],
                        "description": typing.Optional[str],
                        "action": typing.Union[
                            orchestration_models.CreateScheduleRequestAction,
                            orchestration_models.CreateScheduleRequestActionDict,
                        ],
                        "trigger": typing.Optional[
                            typing.Union[
                                orchestration_models.Trigger, orchestration_models.TriggerDict
                            ]
                        ],
                        "scopeMode": typing.Optional[
                            typing.Union[
                                orchestration_models.CreateScheduleRequestScopeMode,
                                orchestration_models.CreateScheduleRequestScopeModeDict,
                            ]
                        ],
                    },
                ),
                response_type=orchestration_models.Schedule,
                request_timeout=request_timeout,
                throwable_errors={
                    "CreateSchedulePermissionDenied": orchestration_errors.CreateSchedulePermissionDenied,
                },
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def delete(
        self,
        schedule_rid: orchestration_models.ScheduleRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[None]:
        """
        Delete the Schedule with the specified rid.
        :param schedule_rid:
        :type schedule_rid: ScheduleRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[None]

        :raises DeleteSchedulePermissionDenied: Could not delete the Schedule.
        """

        return self._api_client.stream_api(
            core.RequestInfo(
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

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        schedule_rid: orchestration_models.ScheduleRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[orchestration_models.Schedule]:
        """
        Get the Schedule with the specified rid.
        :param schedule_rid:
        :type schedule_rid: ScheduleRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[orchestration_models.Schedule]

        :raises ScheduleNotFound: The given Schedule could not be found.
        """

        return self._api_client.stream_api(
            core.RequestInfo(
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
                response_type=orchestration_models.Schedule,
                request_timeout=request_timeout,
                throwable_errors={
                    "ScheduleNotFound": orchestration_errors.ScheduleNotFound,
                },
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def pause(
        self,
        schedule_rid: orchestration_models.ScheduleRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[None]:
        """

        :param schedule_rid:
        :type schedule_rid: ScheduleRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[None]

        :raises PauseSchedulePermissionDenied: Could not pause the Schedule.
        """

        return self._api_client.stream_api(
            core.RequestInfo(
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

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def replace(
        self,
        schedule_rid: orchestration_models.ScheduleRid,
        *,
        action: typing.Union[
            orchestration_models.ReplaceScheduleRequestAction,
            orchestration_models.ReplaceScheduleRequestActionDict,
        ],
        description: typing.Optional[str] = None,
        display_name: typing.Optional[str] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        scope_mode: typing.Optional[
            typing.Union[
                orchestration_models.ReplaceScheduleRequestScopeMode,
                orchestration_models.ReplaceScheduleRequestScopeModeDict,
            ]
        ] = None,
        trigger: typing.Optional[
            typing.Union[orchestration_models.Trigger, orchestration_models.TriggerDict]
        ] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[orchestration_models.Schedule]:
        """
        Replace the Schedule with the specified rid.
        :param schedule_rid:
        :type schedule_rid: ScheduleRid
        :param action:
        :type action: Union[ReplaceScheduleRequestAction, ReplaceScheduleRequestActionDict]
        :param description:
        :type description: Optional[str]
        :param display_name:
        :type display_name: Optional[str]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param scope_mode:
        :type scope_mode: Optional[Union[ReplaceScheduleRequestScopeMode, ReplaceScheduleRequestScopeModeDict]]
        :param trigger: The schedule trigger. If the requesting user does not have permission to see the trigger, this will be empty.
        :type trigger: Optional[Union[Trigger, TriggerDict]]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[orchestration_models.Schedule]

        :raises ReplaceSchedulePermissionDenied: Could not replace the Schedule.
        """

        return self._api_client.stream_api(
            core.RequestInfo(
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
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "displayName": typing.Optional[str],
                        "description": typing.Optional[str],
                        "action": typing.Union[
                            orchestration_models.ReplaceScheduleRequestAction,
                            orchestration_models.ReplaceScheduleRequestActionDict,
                        ],
                        "trigger": typing.Optional[
                            typing.Union[
                                orchestration_models.Trigger, orchestration_models.TriggerDict
                            ]
                        ],
                        "scopeMode": typing.Optional[
                            typing.Union[
                                orchestration_models.ReplaceScheduleRequestScopeMode,
                                orchestration_models.ReplaceScheduleRequestScopeModeDict,
                            ]
                        ],
                    },
                ),
                response_type=orchestration_models.Schedule,
                request_timeout=request_timeout,
                throwable_errors={
                    "ReplaceSchedulePermissionDenied": orchestration_errors.ReplaceSchedulePermissionDenied,
                },
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def run(
        self,
        schedule_rid: orchestration_models.ScheduleRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[orchestration_models.ScheduleRun]:
        """

        :param schedule_rid:
        :type schedule_rid: ScheduleRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[orchestration_models.ScheduleRun]

        :raises RunSchedulePermissionDenied: Could not run the Schedule.
        """

        return self._api_client.stream_api(
            core.RequestInfo(
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
                response_type=orchestration_models.ScheduleRun,
                request_timeout=request_timeout,
                throwable_errors={
                    "RunSchedulePermissionDenied": orchestration_errors.RunSchedulePermissionDenied,
                },
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def runs(
        self,
        schedule_rid: orchestration_models.ScheduleRid,
        *,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[orchestration_models.ListRunsOfScheduleResponse]:
        """
        Get the most recent runs of a Schedule. If no page size is provided, a page size of 100 will be used.

        :param schedule_rid:
        :type schedule_rid: ScheduleRid
        :param page_size: The page size to use for the endpoint.
        :type page_size: Optional[PageSize]
        :param page_token: The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
        :type page_token: Optional[PageToken]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[orchestration_models.ListRunsOfScheduleResponse]
        """

        return self._api_client.stream_api(
            core.RequestInfo(
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
                response_type=orchestration_models.ListRunsOfScheduleResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def runs_page(
        self,
        schedule_rid: orchestration_models.ScheduleRid,
        *,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[orchestration_models.ListRunsOfScheduleResponse]:
        """
        Get the most recent runs of a Schedule. If no page size is provided, a page size of 100 will be used.

        :param schedule_rid:
        :type schedule_rid: ScheduleRid
        :param page_size: The page size to use for the endpoint.
        :type page_size: Optional[PageSize]
        :param page_token: The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
        :type page_token: Optional[PageToken]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[orchestration_models.ListRunsOfScheduleResponse]
        """

        warnings.warn(
            "The client.orchestration.Schedule.runs_page(...) method has been deprecated. Please use client.orchestration.Schedule.runs(...) instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        return self._api_client.stream_api(
            core.RequestInfo(
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
                response_type=orchestration_models.ListRunsOfScheduleResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def unpause(
        self,
        schedule_rid: orchestration_models.ScheduleRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[None]:
        """

        :param schedule_rid:
        :type schedule_rid: ScheduleRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[None]

        :raises UnpauseSchedulePermissionDenied: Could not unpause the Schedule.
        """

        return self._api_client.stream_api(
            core.RequestInfo(
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
