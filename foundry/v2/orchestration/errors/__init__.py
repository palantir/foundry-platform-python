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


from foundry.v2.orchestration.errors._build_inputs_not_found import BuildInputsNotFound
from foundry.v2.orchestration.errors._build_inputs_permission_denied import (
    BuildInputsPermissionDenied,
)  # NOQA
from foundry.v2.orchestration.errors._build_not_found import BuildNotFound
from foundry.v2.orchestration.errors._build_targets_missing_job_specs import (
    BuildTargetsMissingJobSpecs,
)  # NOQA
from foundry.v2.orchestration.errors._build_targets_not_found import BuildTargetsNotFound  # NOQA
from foundry.v2.orchestration.errors._build_targets_permission_denied import (
    BuildTargetsPermissionDenied,
)  # NOQA
from foundry.v2.orchestration.errors._build_targets_resolution_error import (
    BuildTargetsResolutionError,
)  # NOQA
from foundry.v2.orchestration.errors._build_targets_up_to_date import BuildTargetsUpToDate  # NOQA
from foundry.v2.orchestration.errors._cancel_build_permission_denied import (
    CancelBuildPermissionDenied,
)  # NOQA
from foundry.v2.orchestration.errors._create_build_permission_denied import (
    CreateBuildPermissionDenied,
)  # NOQA
from foundry.v2.orchestration.errors._create_schedule_permission_denied import (
    CreateSchedulePermissionDenied,
)  # NOQA
from foundry.v2.orchestration.errors._delete_schedule_permission_denied import (
    DeleteSchedulePermissionDenied,
)  # NOQA
from foundry.v2.orchestration.errors._invalid_and_trigger import InvalidAndTrigger
from foundry.v2.orchestration.errors._invalid_media_set_trigger import (
    InvalidMediaSetTrigger,
)  # NOQA
from foundry.v2.orchestration.errors._invalid_or_trigger import InvalidOrTrigger
from foundry.v2.orchestration.errors._invalid_schedule_description import (
    InvalidScheduleDescription,
)  # NOQA
from foundry.v2.orchestration.errors._invalid_schedule_name import InvalidScheduleName
from foundry.v2.orchestration.errors._invalid_time_trigger import InvalidTimeTrigger
from foundry.v2.orchestration.errors._job_not_found import JobNotFound
from foundry.v2.orchestration.errors._missing_build_targets import MissingBuildTargets
from foundry.v2.orchestration.errors._missing_connecting_build_inputs import (
    MissingConnectingBuildInputs,
)  # NOQA
from foundry.v2.orchestration.errors._missing_trigger import MissingTrigger
from foundry.v2.orchestration.errors._pause_schedule_permission_denied import (
    PauseSchedulePermissionDenied,
)  # NOQA
from foundry.v2.orchestration.errors._replace_schedule_permission_denied import (
    ReplaceSchedulePermissionDenied,
)  # NOQA
from foundry.v2.orchestration.errors._run_schedule_permission_denied import (
    RunSchedulePermissionDenied,
)  # NOQA
from foundry.v2.orchestration.errors._schedule_not_found import ScheduleNotFound
from foundry.v2.orchestration.errors._schedule_trigger_resources_not_found import (
    ScheduleTriggerResourcesNotFound,
)  # NOQA
from foundry.v2.orchestration.errors._schedule_trigger_resources_permission_denied import (
    ScheduleTriggerResourcesPermissionDenied,
)  # NOQA
from foundry.v2.orchestration.errors._schedule_version_not_found import (
    ScheduleVersionNotFound,
)  # NOQA
from foundry.v2.orchestration.errors._search_builds_permission_denied import (
    SearchBuildsPermissionDenied,
)  # NOQA
from foundry.v2.orchestration.errors._target_not_supported import TargetNotSupported
from foundry.v2.orchestration.errors._unpause_schedule_permission_denied import (
    UnpauseSchedulePermissionDenied,
)  # NOQA

__all__ = [
    "BuildInputsNotFound",
    "BuildInputsPermissionDenied",
    "BuildNotFound",
    "BuildTargetsMissingJobSpecs",
    "BuildTargetsNotFound",
    "BuildTargetsPermissionDenied",
    "BuildTargetsResolutionError",
    "BuildTargetsUpToDate",
    "CancelBuildPermissionDenied",
    "CreateBuildPermissionDenied",
    "CreateSchedulePermissionDenied",
    "DeleteSchedulePermissionDenied",
    "InvalidAndTrigger",
    "InvalidMediaSetTrigger",
    "InvalidOrTrigger",
    "InvalidScheduleDescription",
    "InvalidScheduleName",
    "InvalidTimeTrigger",
    "JobNotFound",
    "MissingBuildTargets",
    "MissingConnectingBuildInputs",
    "MissingTrigger",
    "PauseSchedulePermissionDenied",
    "ReplaceSchedulePermissionDenied",
    "RunSchedulePermissionDenied",
    "ScheduleNotFound",
    "ScheduleTriggerResourcesNotFound",
    "ScheduleTriggerResourcesPermissionDenied",
    "ScheduleVersionNotFound",
    "SearchBuildsPermissionDenied",
    "TargetNotSupported",
    "UnpauseSchedulePermissionDenied",
]
