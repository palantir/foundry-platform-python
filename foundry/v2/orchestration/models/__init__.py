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


from foundry.v2.orchestration.models._abort_on_failure import AbortOnFailure
from foundry.v2.orchestration.models._action import Action
from foundry.v2.orchestration.models._action_dict import ActionDict
from foundry.v2.orchestration.models._and_trigger import AndTrigger
from foundry.v2.orchestration.models._and_trigger_dict import AndTriggerDict
from foundry.v2.orchestration.models._build import Build
from foundry.v2.orchestration.models._build_dict import BuildDict
from foundry.v2.orchestration.models._build_rid import BuildRid
from foundry.v2.orchestration.models._build_status import BuildStatus
from foundry.v2.orchestration.models._build_target import BuildTarget
from foundry.v2.orchestration.models._build_target_dict import BuildTargetDict
from foundry.v2.orchestration.models._buildable_rid import BuildableRid
from foundry.v2.orchestration.models._connecting_target import ConnectingTarget
from foundry.v2.orchestration.models._connecting_target_dict import ConnectingTargetDict
from foundry.v2.orchestration.models._create_schedule_request_action_build_target_connecting_target_dict import (
    CreateScheduleRequestActionBuildTargetConnectingTargetDict,
)  # NOQA
from foundry.v2.orchestration.models._create_schedule_request_action_build_target_dict import (
    CreateScheduleRequestActionBuildTargetDict,
)  # NOQA
from foundry.v2.orchestration.models._create_schedule_request_action_build_target_manual_target_dict import (
    CreateScheduleRequestActionBuildTargetManualTargetDict,
)  # NOQA
from foundry.v2.orchestration.models._create_schedule_request_action_build_target_upstream_target_dict import (
    CreateScheduleRequestActionBuildTargetUpstreamTargetDict,
)  # NOQA
from foundry.v2.orchestration.models._create_schedule_request_action_dict import (
    CreateScheduleRequestActionDict,
)  # NOQA
from foundry.v2.orchestration.models._create_schedule_request_scope_mode_dict import (
    CreateScheduleRequestScopeModeDict,
)  # NOQA
from foundry.v2.orchestration.models._create_schedule_request_scope_mode_project_scope_dict import (
    CreateScheduleRequestScopeModeProjectScopeDict,
)  # NOQA
from foundry.v2.orchestration.models._create_schedule_request_scope_mode_user_scope_dict import (
    CreateScheduleRequestScopeModeUserScopeDict,
)  # NOQA
from foundry.v2.orchestration.models._cron_expression import CronExpression
from foundry.v2.orchestration.models._dataset_updated_trigger import DatasetUpdatedTrigger  # NOQA
from foundry.v2.orchestration.models._dataset_updated_trigger_dict import (
    DatasetUpdatedTriggerDict,
)  # NOQA
from foundry.v2.orchestration.models._fallback_branches import FallbackBranches
from foundry.v2.orchestration.models._force_build import ForceBuild
from foundry.v2.orchestration.models._job_succeeded_trigger import JobSucceededTrigger
from foundry.v2.orchestration.models._job_succeeded_trigger_dict import (
    JobSucceededTriggerDict,
)  # NOQA
from foundry.v2.orchestration.models._manual_target import ManualTarget
from foundry.v2.orchestration.models._manual_target_dict import ManualTargetDict
from foundry.v2.orchestration.models._media_set_updated_trigger import (
    MediaSetUpdatedTrigger,
)  # NOQA
from foundry.v2.orchestration.models._media_set_updated_trigger_dict import (
    MediaSetUpdatedTriggerDict,
)  # NOQA
from foundry.v2.orchestration.models._new_logic_trigger import NewLogicTrigger
from foundry.v2.orchestration.models._new_logic_trigger_dict import NewLogicTriggerDict
from foundry.v2.orchestration.models._notifications_enabled import NotificationsEnabled
from foundry.v2.orchestration.models._or_trigger import OrTrigger
from foundry.v2.orchestration.models._or_trigger_dict import OrTriggerDict
from foundry.v2.orchestration.models._project_scope import ProjectScope
from foundry.v2.orchestration.models._project_scope_dict import ProjectScopeDict
from foundry.v2.orchestration.models._replace_schedule_request_action_build_target_connecting_target_dict import (
    ReplaceScheduleRequestActionBuildTargetConnectingTargetDict,
)  # NOQA
from foundry.v2.orchestration.models._replace_schedule_request_action_build_target_dict import (
    ReplaceScheduleRequestActionBuildTargetDict,
)  # NOQA
from foundry.v2.orchestration.models._replace_schedule_request_action_build_target_manual_target_dict import (
    ReplaceScheduleRequestActionBuildTargetManualTargetDict,
)  # NOQA
from foundry.v2.orchestration.models._replace_schedule_request_action_build_target_upstream_target_dict import (
    ReplaceScheduleRequestActionBuildTargetUpstreamTargetDict,
)  # NOQA
from foundry.v2.orchestration.models._replace_schedule_request_action_dict import (
    ReplaceScheduleRequestActionDict,
)  # NOQA
from foundry.v2.orchestration.models._replace_schedule_request_scope_mode_dict import (
    ReplaceScheduleRequestScopeModeDict,
)  # NOQA
from foundry.v2.orchestration.models._replace_schedule_request_scope_mode_project_scope_dict import (
    ReplaceScheduleRequestScopeModeProjectScopeDict,
)  # NOQA
from foundry.v2.orchestration.models._replace_schedule_request_scope_mode_user_scope_dict import (
    ReplaceScheduleRequestScopeModeUserScopeDict,
)  # NOQA
from foundry.v2.orchestration.models._retry_backoff_duration import RetryBackoffDuration
from foundry.v2.orchestration.models._retry_backoff_duration_dict import (
    RetryBackoffDurationDict,
)  # NOQA
from foundry.v2.orchestration.models._retry_count import RetryCount
from foundry.v2.orchestration.models._schedule import Schedule
from foundry.v2.orchestration.models._schedule_dict import ScheduleDict
from foundry.v2.orchestration.models._schedule_paused import SchedulePaused
from foundry.v2.orchestration.models._schedule_rid import ScheduleRid
from foundry.v2.orchestration.models._schedule_run import ScheduleRun
from foundry.v2.orchestration.models._schedule_run_dict import ScheduleRunDict
from foundry.v2.orchestration.models._schedule_run_error import ScheduleRunError
from foundry.v2.orchestration.models._schedule_run_error_dict import ScheduleRunErrorDict  # NOQA
from foundry.v2.orchestration.models._schedule_run_error_name import ScheduleRunErrorName  # NOQA
from foundry.v2.orchestration.models._schedule_run_ignored import ScheduleRunIgnored
from foundry.v2.orchestration.models._schedule_run_ignored_dict import (
    ScheduleRunIgnoredDict,
)  # NOQA
from foundry.v2.orchestration.models._schedule_run_result import ScheduleRunResult
from foundry.v2.orchestration.models._schedule_run_result_dict import ScheduleRunResultDict  # NOQA
from foundry.v2.orchestration.models._schedule_run_rid import ScheduleRunRid
from foundry.v2.orchestration.models._schedule_run_submitted import ScheduleRunSubmitted
from foundry.v2.orchestration.models._schedule_run_submitted_dict import (
    ScheduleRunSubmittedDict,
)  # NOQA
from foundry.v2.orchestration.models._schedule_succeeded_trigger import (
    ScheduleSucceededTrigger,
)  # NOQA
from foundry.v2.orchestration.models._schedule_succeeded_trigger_dict import (
    ScheduleSucceededTriggerDict,
)  # NOQA
from foundry.v2.orchestration.models._schedule_version_rid import ScheduleVersionRid
from foundry.v2.orchestration.models._scope_mode import ScopeMode
from foundry.v2.orchestration.models._scope_mode_dict import ScopeModeDict
from foundry.v2.orchestration.models._time_trigger import TimeTrigger
from foundry.v2.orchestration.models._time_trigger_dict import TimeTriggerDict
from foundry.v2.orchestration.models._trigger import Trigger
from foundry.v2.orchestration.models._trigger_dict import TriggerDict
from foundry.v2.orchestration.models._upstream_target import UpstreamTarget
from foundry.v2.orchestration.models._upstream_target_dict import UpstreamTargetDict
from foundry.v2.orchestration.models._user_scope import UserScope
from foundry.v2.orchestration.models._user_scope_dict import UserScopeDict

__all__ = [
    "AbortOnFailure",
    "Action",
    "ActionDict",
    "AndTrigger",
    "AndTriggerDict",
    "Build",
    "BuildDict",
    "BuildRid",
    "BuildStatus",
    "BuildTarget",
    "BuildTargetDict",
    "BuildableRid",
    "ConnectingTarget",
    "ConnectingTargetDict",
    "CreateScheduleRequestActionBuildTargetConnectingTargetDict",
    "CreateScheduleRequestActionBuildTargetDict",
    "CreateScheduleRequestActionBuildTargetManualTargetDict",
    "CreateScheduleRequestActionBuildTargetUpstreamTargetDict",
    "CreateScheduleRequestActionDict",
    "CreateScheduleRequestScopeModeDict",
    "CreateScheduleRequestScopeModeProjectScopeDict",
    "CreateScheduleRequestScopeModeUserScopeDict",
    "CronExpression",
    "DatasetUpdatedTrigger",
    "DatasetUpdatedTriggerDict",
    "FallbackBranches",
    "ForceBuild",
    "JobSucceededTrigger",
    "JobSucceededTriggerDict",
    "ManualTarget",
    "ManualTargetDict",
    "MediaSetUpdatedTrigger",
    "MediaSetUpdatedTriggerDict",
    "NewLogicTrigger",
    "NewLogicTriggerDict",
    "NotificationsEnabled",
    "OrTrigger",
    "OrTriggerDict",
    "ProjectScope",
    "ProjectScopeDict",
    "ReplaceScheduleRequestActionBuildTargetConnectingTargetDict",
    "ReplaceScheduleRequestActionBuildTargetDict",
    "ReplaceScheduleRequestActionBuildTargetManualTargetDict",
    "ReplaceScheduleRequestActionBuildTargetUpstreamTargetDict",
    "ReplaceScheduleRequestActionDict",
    "ReplaceScheduleRequestScopeModeDict",
    "ReplaceScheduleRequestScopeModeProjectScopeDict",
    "ReplaceScheduleRequestScopeModeUserScopeDict",
    "RetryBackoffDuration",
    "RetryBackoffDurationDict",
    "RetryCount",
    "Schedule",
    "ScheduleDict",
    "SchedulePaused",
    "ScheduleRid",
    "ScheduleRun",
    "ScheduleRunDict",
    "ScheduleRunError",
    "ScheduleRunErrorDict",
    "ScheduleRunErrorName",
    "ScheduleRunIgnored",
    "ScheduleRunIgnoredDict",
    "ScheduleRunResult",
    "ScheduleRunResultDict",
    "ScheduleRunRid",
    "ScheduleRunSubmitted",
    "ScheduleRunSubmittedDict",
    "ScheduleSucceededTrigger",
    "ScheduleSucceededTriggerDict",
    "ScheduleVersionRid",
    "ScopeMode",
    "ScopeModeDict",
    "TimeTrigger",
    "TimeTriggerDict",
    "Trigger",
    "TriggerDict",
    "UpstreamTarget",
    "UpstreamTargetDict",
    "UserScope",
    "UserScopeDict",
]
