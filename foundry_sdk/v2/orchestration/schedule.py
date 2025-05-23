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
from foundry_sdk.v2.orchestration import errors as orchestration_errors
from foundry_sdk.v2.orchestration import models as orchestration_models


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

        self.with_streaming_response = _ScheduleClientStreaming(self)
        self.with_raw_response = _ScheduleClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def create(
        self,
        *,
        action: orchestration_models.CreateScheduleRequestAction,
        description: typing.Optional[str] = None,
        display_name: typing.Optional[str] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        scope_mode: typing.Optional[orchestration_models.CreateScheduleRequestScopeMode] = None,
        trigger: typing.Optional[orchestration_models.Trigger] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> orchestration_models.Schedule:
        """
        Creates a new Schedule.
        :param action:
        :type action: CreateScheduleRequestAction
        :param description:
        :type description: Optional[str]
        :param display_name:
        :type display_name: Optional[str]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param scope_mode:
        :type scope_mode: Optional[CreateScheduleRequestScopeMode]
        :param trigger: The schedule trigger. If the requesting user does not have permission to see the trigger, this will be empty.
        :type trigger: Optional[Trigger]
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
                        "action": orchestration_models.CreateScheduleRequestAction,
                        "trigger": typing.Optional[orchestration_models.Trigger],
                        "scopeMode": typing.Optional[
                            orchestration_models.CreateScheduleRequestScopeMode
                        ],
                    },
                ),
                response_type=orchestration_models.Schedule,
                request_timeout=request_timeout,
                throwable_errors={
                    "CreateSchedulePermissionDenied": orchestration_errors.CreateSchedulePermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def delete(
        self,
        schedule_rid: core_models.ScheduleRid,
        *,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> None:
        """
        Delete the Schedule with the specified rid.
        :param schedule_rid:
        :type schedule_rid: ScheduleRid
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
                query_params={},
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
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        schedule_rid: core_models.ScheduleRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
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
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def pause(
        self,
        schedule_rid: core_models.ScheduleRid,
        *,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> None:
        """

        :param schedule_rid:
        :type schedule_rid: ScheduleRid
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
                query_params={},
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
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def replace(
        self,
        schedule_rid: core_models.ScheduleRid,
        *,
        action: orchestration_models.ReplaceScheduleRequestAction,
        description: typing.Optional[str] = None,
        display_name: typing.Optional[str] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        scope_mode: typing.Optional[orchestration_models.ReplaceScheduleRequestScopeMode] = None,
        trigger: typing.Optional[orchestration_models.Trigger] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> orchestration_models.Schedule:
        """
        Replace the Schedule with the specified rid.
        :param schedule_rid:
        :type schedule_rid: ScheduleRid
        :param action:
        :type action: ReplaceScheduleRequestAction
        :param description:
        :type description: Optional[str]
        :param display_name:
        :type display_name: Optional[str]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param scope_mode:
        :type scope_mode: Optional[ReplaceScheduleRequestScopeMode]
        :param trigger: The schedule trigger. If the requesting user does not have permission to see the trigger, this will be empty.
        :type trigger: Optional[Trigger]
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
                        "action": orchestration_models.ReplaceScheduleRequestAction,
                        "trigger": typing.Optional[orchestration_models.Trigger],
                        "scopeMode": typing.Optional[
                            orchestration_models.ReplaceScheduleRequestScopeMode
                        ],
                    },
                ),
                response_type=orchestration_models.Schedule,
                request_timeout=request_timeout,
                throwable_errors={
                    "ReplaceSchedulePermissionDenied": orchestration_errors.ReplaceSchedulePermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def run(
        self,
        schedule_rid: core_models.ScheduleRid,
        *,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> orchestration_models.ScheduleRun:
        """

        :param schedule_rid:
        :type schedule_rid: ScheduleRid
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
                query_params={},
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
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def runs(
        self,
        schedule_rid: core_models.ScheduleRid,
        *,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> core.ResourceIterator[orchestration_models.ScheduleRun]:
        """
        Get the most recent runs of a Schedule. If no page size is provided, a page size of 100 will be used.

        :param schedule_rid:
        :type schedule_rid: ScheduleRid
        :param page_size: The page size to use for the endpoint.
        :type page_size: Optional[PageSize]
        :param page_token: The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
        :type page_token: Optional[PageToken]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ResourceIterator[orchestration_models.ScheduleRun]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/orchestration/schedules/{scheduleRid}/runs",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
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
                response_mode=_sdk_internal.get("response_mode", "ITERATOR"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def unpause(
        self,
        schedule_rid: core_models.ScheduleRid,
        *,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> None:
        """

        :param schedule_rid:
        :type schedule_rid: ScheduleRid
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
                query_params={},
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
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _ScheduleClientRaw:
    def __init__(self, client: ScheduleClient) -> None:
        def create(_: orchestration_models.Schedule): ...
        def delete(_: None): ...
        def get(_: orchestration_models.Schedule): ...
        def pause(_: None): ...
        def replace(_: orchestration_models.Schedule): ...
        def run(_: orchestration_models.ScheduleRun): ...
        def runs(_: orchestration_models.ListRunsOfScheduleResponse): ...
        def unpause(_: None): ...

        self.create = core.with_raw_response(create, client.create)
        self.delete = core.with_raw_response(delete, client.delete)
        self.get = core.with_raw_response(get, client.get)
        self.pause = core.with_raw_response(pause, client.pause)
        self.replace = core.with_raw_response(replace, client.replace)
        self.run = core.with_raw_response(run, client.run)
        self.runs = core.with_raw_response(runs, client.runs)
        self.unpause = core.with_raw_response(unpause, client.unpause)


class _ScheduleClientStreaming:
    def __init__(self, client: ScheduleClient) -> None:
        def create(_: orchestration_models.Schedule): ...
        def get(_: orchestration_models.Schedule): ...
        def replace(_: orchestration_models.Schedule): ...
        def run(_: orchestration_models.ScheduleRun): ...
        def runs(_: orchestration_models.ListRunsOfScheduleResponse): ...

        self.create = core.with_streaming_response(create, client.create)
        self.get = core.with_streaming_response(get, client.get)
        self.replace = core.with_streaming_response(replace, client.replace)
        self.run = core.with_streaming_response(run, client.run)
        self.runs = core.with_streaming_response(runs, client.runs)


class AsyncScheduleClient:
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
        self._api_client = core.AsyncApiClient(auth=auth, hostname=hostname, config=config)

        self.with_streaming_response = _AsyncScheduleClientStreaming(self)
        self.with_raw_response = _AsyncScheduleClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def create(
        self,
        *,
        action: orchestration_models.CreateScheduleRequestAction,
        description: typing.Optional[str] = None,
        display_name: typing.Optional[str] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        scope_mode: typing.Optional[orchestration_models.CreateScheduleRequestScopeMode] = None,
        trigger: typing.Optional[orchestration_models.Trigger] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[orchestration_models.Schedule]:
        """
        Creates a new Schedule.
        :param action:
        :type action: CreateScheduleRequestAction
        :param description:
        :type description: Optional[str]
        :param display_name:
        :type display_name: Optional[str]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param scope_mode:
        :type scope_mode: Optional[CreateScheduleRequestScopeMode]
        :param trigger: The schedule trigger. If the requesting user does not have permission to see the trigger, this will be empty.
        :type trigger: Optional[Trigger]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[orchestration_models.Schedule]

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
                        "action": orchestration_models.CreateScheduleRequestAction,
                        "trigger": typing.Optional[orchestration_models.Trigger],
                        "scopeMode": typing.Optional[
                            orchestration_models.CreateScheduleRequestScopeMode
                        ],
                    },
                ),
                response_type=orchestration_models.Schedule,
                request_timeout=request_timeout,
                throwable_errors={
                    "CreateSchedulePermissionDenied": orchestration_errors.CreateSchedulePermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def delete(
        self,
        schedule_rid: core_models.ScheduleRid,
        *,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[None]:
        """
        Delete the Schedule with the specified rid.
        :param schedule_rid:
        :type schedule_rid: ScheduleRid
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[None]

        :raises DeleteSchedulePermissionDenied: Could not delete the Schedule.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="DELETE",
                resource_path="/v2/orchestration/schedules/{scheduleRid}",
                query_params={},
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
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        schedule_rid: core_models.ScheduleRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[orchestration_models.Schedule]:
        """
        Get the Schedule with the specified rid.
        :param schedule_rid:
        :type schedule_rid: ScheduleRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[orchestration_models.Schedule]

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
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def pause(
        self,
        schedule_rid: core_models.ScheduleRid,
        *,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[None]:
        """

        :param schedule_rid:
        :type schedule_rid: ScheduleRid
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[None]

        :raises PauseSchedulePermissionDenied: Could not pause the Schedule.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/orchestration/schedules/{scheduleRid}/pause",
                query_params={},
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
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def replace(
        self,
        schedule_rid: core_models.ScheduleRid,
        *,
        action: orchestration_models.ReplaceScheduleRequestAction,
        description: typing.Optional[str] = None,
        display_name: typing.Optional[str] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        scope_mode: typing.Optional[orchestration_models.ReplaceScheduleRequestScopeMode] = None,
        trigger: typing.Optional[orchestration_models.Trigger] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[orchestration_models.Schedule]:
        """
        Replace the Schedule with the specified rid.
        :param schedule_rid:
        :type schedule_rid: ScheduleRid
        :param action:
        :type action: ReplaceScheduleRequestAction
        :param description:
        :type description: Optional[str]
        :param display_name:
        :type display_name: Optional[str]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param scope_mode:
        :type scope_mode: Optional[ReplaceScheduleRequestScopeMode]
        :param trigger: The schedule trigger. If the requesting user does not have permission to see the trigger, this will be empty.
        :type trigger: Optional[Trigger]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[orchestration_models.Schedule]

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
                        "action": orchestration_models.ReplaceScheduleRequestAction,
                        "trigger": typing.Optional[orchestration_models.Trigger],
                        "scopeMode": typing.Optional[
                            orchestration_models.ReplaceScheduleRequestScopeMode
                        ],
                    },
                ),
                response_type=orchestration_models.Schedule,
                request_timeout=request_timeout,
                throwable_errors={
                    "ReplaceSchedulePermissionDenied": orchestration_errors.ReplaceSchedulePermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def run(
        self,
        schedule_rid: core_models.ScheduleRid,
        *,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[orchestration_models.ScheduleRun]:
        """

        :param schedule_rid:
        :type schedule_rid: ScheduleRid
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[orchestration_models.ScheduleRun]

        :raises RunSchedulePermissionDenied: Could not run the Schedule.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/orchestration/schedules/{scheduleRid}/run",
                query_params={},
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
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def runs(
        self,
        schedule_rid: core_models.ScheduleRid,
        *,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> core.AsyncResourceIterator[orchestration_models.ScheduleRun]:
        """
        Get the most recent runs of a Schedule. If no page size is provided, a page size of 100 will be used.

        :param schedule_rid:
        :type schedule_rid: ScheduleRid
        :param page_size: The page size to use for the endpoint.
        :type page_size: Optional[PageSize]
        :param page_token: The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
        :type page_token: Optional[PageToken]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.AsyncResourceIterator[orchestration_models.ScheduleRun]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/orchestration/schedules/{scheduleRid}/runs",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
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
                response_mode=_sdk_internal.get("response_mode", "ITERATOR"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def unpause(
        self,
        schedule_rid: core_models.ScheduleRid,
        *,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[None]:
        """

        :param schedule_rid:
        :type schedule_rid: ScheduleRid
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[None]

        :raises UnpauseSchedulePermissionDenied: Could not unpause the Schedule.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/orchestration/schedules/{scheduleRid}/unpause",
                query_params={},
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
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _AsyncScheduleClientRaw:
    def __init__(self, client: AsyncScheduleClient) -> None:
        def create(_: orchestration_models.Schedule): ...
        def delete(_: None): ...
        def get(_: orchestration_models.Schedule): ...
        def pause(_: None): ...
        def replace(_: orchestration_models.Schedule): ...
        def run(_: orchestration_models.ScheduleRun): ...
        def runs(_: orchestration_models.ListRunsOfScheduleResponse): ...
        def unpause(_: None): ...

        self.create = core.async_with_raw_response(create, client.create)
        self.delete = core.async_with_raw_response(delete, client.delete)
        self.get = core.async_with_raw_response(get, client.get)
        self.pause = core.async_with_raw_response(pause, client.pause)
        self.replace = core.async_with_raw_response(replace, client.replace)
        self.run = core.async_with_raw_response(run, client.run)
        self.runs = core.async_with_raw_response(runs, client.runs)
        self.unpause = core.async_with_raw_response(unpause, client.unpause)


class _AsyncScheduleClientStreaming:
    def __init__(self, client: AsyncScheduleClient) -> None:
        def create(_: orchestration_models.Schedule): ...
        def get(_: orchestration_models.Schedule): ...
        def replace(_: orchestration_models.Schedule): ...
        def run(_: orchestration_models.ScheduleRun): ...
        def runs(_: orchestration_models.ListRunsOfScheduleResponse): ...

        self.create = core.async_with_streaming_response(create, client.create)
        self.get = core.async_with_streaming_response(get, client.get)
        self.replace = core.async_with_streaming_response(replace, client.replace)
        self.run = core.async_with_streaming_response(run, client.run)
        self.runs = core.async_with_streaming_response(runs, client.runs)
