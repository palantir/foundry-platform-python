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

from typing import Any
from typing import Dict
from typing import Optional

import pydantic
from typing_extensions import Annotated
from typing_extensions import TypedDict

from foundry._core import ApiClient
from foundry._core import Auth
from foundry._core import RequestInfo
from foundry._errors import handle_unexpected
from foundry.v2.core.models._preview_mode import PreviewMode
from foundry.v2.orchestration.models._create_schedule_request_action_dict import (
    CreateScheduleRequestActionDict,
)  # NOQA
from foundry.v2.orchestration.models._create_schedule_request_scope_mode_dict import (
    CreateScheduleRequestScopeModeDict,
)  # NOQA
from foundry.v2.orchestration.models._replace_schedule_request_action_dict import (
    ReplaceScheduleRequestActionDict,
)  # NOQA
from foundry.v2.orchestration.models._replace_schedule_request_scope_mode_dict import (
    ReplaceScheduleRequestScopeModeDict,
)  # NOQA
from foundry.v2.orchestration.models._schedule import Schedule
from foundry.v2.orchestration.models._schedule_rid import ScheduleRid
from foundry.v2.orchestration.models._schedule_run import ScheduleRun
from foundry.v2.orchestration.models._trigger_dict import TriggerDict


class ScheduleClient:
    def __init__(self, auth: Auth, hostname: str) -> None:
        self._api_client = ApiClient(auth=auth, hostname=hostname)

    @pydantic.validate_call
    @handle_unexpected
    def create(
        self,
        *,
        action: CreateScheduleRequestActionDict,
        description: Optional[pydantic.StrictStr] = None,
        display_name: Optional[pydantic.StrictStr] = None,
        preview: Optional[PreviewMode] = None,
        scope_mode: Optional[CreateScheduleRequestScopeModeDict] = None,
        trigger: Optional[TriggerDict] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> Schedule:
        """
        Creates a new Schedule.
        :param action:
        :type action: CreateScheduleRequestActionDict
        :param description:
        :type description: Optional[pydantic.StrictStr]
        :param display_name:
        :type display_name: Optional[pydantic.StrictStr]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param scope_mode:
        :type scope_mode: Optional[CreateScheduleRequestScopeModeDict]
        :param trigger: The schedule trigger. If the requesting user does not have permission to see the trigger, this will be empty.
        :type trigger: Optional[TriggerDict]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: Schedule
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
                        "displayName": Optional[pydantic.StrictStr],
                        "description": Optional[pydantic.StrictStr],
                        "action": CreateScheduleRequestActionDict,
                        "trigger": Optional[TriggerDict],
                        "scopeMode": Optional[CreateScheduleRequestScopeModeDict],
                    },
                ),
                response_type=Schedule,
                request_timeout=request_timeout,
            ),
        )

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
            ),
        )

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
            ),
        )

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
            ),
        )

    @pydantic.validate_call
    @handle_unexpected
    def replace(
        self,
        schedule_rid: ScheduleRid,
        *,
        action: ReplaceScheduleRequestActionDict,
        description: Optional[pydantic.StrictStr] = None,
        display_name: Optional[pydantic.StrictStr] = None,
        preview: Optional[PreviewMode] = None,
        scope_mode: Optional[ReplaceScheduleRequestScopeModeDict] = None,
        trigger: Optional[TriggerDict] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> Schedule:
        """
        Replace the Schedule with the specified rid.
        :param schedule_rid: scheduleRid
        :type schedule_rid: ScheduleRid
        :param action:
        :type action: ReplaceScheduleRequestActionDict
        :param description:
        :type description: Optional[pydantic.StrictStr]
        :param display_name:
        :type display_name: Optional[pydantic.StrictStr]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param scope_mode:
        :type scope_mode: Optional[ReplaceScheduleRequestScopeModeDict]
        :param trigger: The schedule trigger. If the requesting user does not have permission to see the trigger, this will be empty.
        :type trigger: Optional[TriggerDict]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: Schedule
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
                        "displayName": Optional[pydantic.StrictStr],
                        "description": Optional[pydantic.StrictStr],
                        "action": ReplaceScheduleRequestActionDict,
                        "trigger": Optional[TriggerDict],
                        "scopeMode": Optional[ReplaceScheduleRequestScopeModeDict],
                    },
                ),
                response_type=Schedule,
                request_timeout=request_timeout,
            ),
        )

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
            ),
        )

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
            ),
        )
