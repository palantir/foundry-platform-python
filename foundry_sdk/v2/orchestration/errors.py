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
from dataclasses import dataclass

import typing_extensions

from foundry_sdk import _core as core
from foundry_sdk import _errors as errors
from foundry_sdk.v2.core import models as core_models
from foundry_sdk.v2.orchestration import models as orchestration_models


class BuildInputsNotFoundParameters(typing_extensions.TypedDict):
    """The given build inputs could be found."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    resourceRids: typing.List[core.RID]


@dataclass
class BuildInputsNotFound(errors.NotFoundError):
    name: typing.Literal["BuildInputsNotFound"]
    parameters: BuildInputsNotFoundParameters
    error_instance_id: str


class BuildInputsPermissionDeniedParameters(typing_extensions.TypedDict):
    """The provided token does not have permission to use the given resources as inputs to the build."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    resourceRids: typing.List[core.RID]


@dataclass
class BuildInputsPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["BuildInputsPermissionDenied"]
    parameters: BuildInputsPermissionDeniedParameters
    error_instance_id: str


class BuildNotFoundParameters(typing_extensions.TypedDict):
    """The given Build could not be found."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    buildRid: core_models.BuildRid
    """The RID of a Build."""


@dataclass
class BuildNotFound(errors.NotFoundError):
    name: typing.Literal["BuildNotFound"]
    parameters: BuildNotFoundParameters
    error_instance_id: str


class BuildTargetsMissingJobSpecsParameters(typing_extensions.TypedDict):
    """The action targets are missing job specs"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    resourceRids: typing.List[core.RID]


@dataclass
class BuildTargetsMissingJobSpecs(errors.BadRequestError):
    name: typing.Literal["BuildTargetsMissingJobSpecs"]
    parameters: BuildTargetsMissingJobSpecsParameters
    error_instance_id: str


class BuildTargetsNotFoundParameters(typing_extensions.TypedDict):
    """The given build targets could not be found."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    resourceRids: typing.List[core.RID]


@dataclass
class BuildTargetsNotFound(errors.NotFoundError):
    name: typing.Literal["BuildTargetsNotFound"]
    parameters: BuildTargetsNotFoundParameters
    error_instance_id: str


class BuildTargetsPermissionDeniedParameters(typing_extensions.TypedDict):
    """The provided token does not have permission to build the given resources."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    resourceRids: typing.List[core.RID]


@dataclass
class BuildTargetsPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["BuildTargetsPermissionDenied"]
    parameters: BuildTargetsPermissionDeniedParameters
    error_instance_id: str


class BuildTargetsResolutionErrorParameters(typing_extensions.TypedDict):
    """Unable to resolve the given target to a set of targets to build."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class BuildTargetsResolutionError(errors.BadRequestError):
    name: typing.Literal["BuildTargetsResolutionError"]
    parameters: BuildTargetsResolutionErrorParameters
    error_instance_id: str


class BuildTargetsUpToDateParameters(typing_extensions.TypedDict):
    """
    The build targets are up to date and no Build was created. To rebuild the targets regardless,
    use the force build option when creating the Build.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class BuildTargetsUpToDate(errors.BadRequestError):
    name: typing.Literal["BuildTargetsUpToDate"]
    parameters: BuildTargetsUpToDateParameters
    error_instance_id: str


class CancelBuildPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not cancel the Build."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    buildRid: core_models.BuildRid
    """The RID of a Build."""


@dataclass
class CancelBuildPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["CancelBuildPermissionDenied"]
    parameters: CancelBuildPermissionDeniedParameters
    error_instance_id: str


class CreateBuildPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not create the Build."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class CreateBuildPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["CreateBuildPermissionDenied"]
    parameters: CreateBuildPermissionDeniedParameters
    error_instance_id: str


class CreateSchedulePermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not create the Schedule."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class CreateSchedulePermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["CreateSchedulePermissionDenied"]
    parameters: CreateSchedulePermissionDeniedParameters
    error_instance_id: str


class DeleteSchedulePermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not delete the Schedule."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    scheduleRid: core_models.ScheduleRid


@dataclass
class DeleteSchedulePermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["DeleteSchedulePermissionDenied"]
    parameters: DeleteSchedulePermissionDeniedParameters
    error_instance_id: str


class GetAffectedResourcesSchedulePermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not getAffectedResources the Schedule."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    scheduleRid: core_models.ScheduleRid


@dataclass
class GetAffectedResourcesSchedulePermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["GetAffectedResourcesSchedulePermissionDenied"]
    parameters: GetAffectedResourcesSchedulePermissionDeniedParameters
    error_instance_id: str


class InvalidAndTriggerParameters(typing_extensions.TypedDict):
    """The AND trigger should have at least one value."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class InvalidAndTrigger(errors.BadRequestError):
    name: typing.Literal["InvalidAndTrigger"]
    parameters: InvalidAndTriggerParameters
    error_instance_id: str


class InvalidMediaSetTriggerParameters(typing_extensions.TypedDict):
    """The given MediaSet rid is invalid."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    mediaSetRid: core_models.MediaSetRid


@dataclass
class InvalidMediaSetTrigger(errors.BadRequestError):
    name: typing.Literal["InvalidMediaSetTrigger"]
    parameters: InvalidMediaSetTriggerParameters
    error_instance_id: str


class InvalidOrTriggerParameters(typing_extensions.TypedDict):
    """The OR trigger should have at least one value."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class InvalidOrTrigger(errors.BadRequestError):
    name: typing.Literal["InvalidOrTrigger"]
    parameters: InvalidOrTriggerParameters
    error_instance_id: str


class InvalidScheduleDescriptionParameters(typing_extensions.TypedDict):
    """The schedule description is too long."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class InvalidScheduleDescription(errors.BadRequestError):
    name: typing.Literal["InvalidScheduleDescription"]
    parameters: InvalidScheduleDescriptionParameters
    error_instance_id: str


class InvalidScheduleNameParameters(typing_extensions.TypedDict):
    """The schedule name is too long"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class InvalidScheduleName(errors.BadRequestError):
    name: typing.Literal["InvalidScheduleName"]
    parameters: InvalidScheduleNameParameters
    error_instance_id: str


class InvalidTimeTriggerParameters(typing_extensions.TypedDict):
    """The schedule trigger cron expression is invalid."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    cronExpression: orchestration_models.CronExpression


@dataclass
class InvalidTimeTrigger(errors.BadRequestError):
    name: typing.Literal["InvalidTimeTrigger"]
    parameters: InvalidTimeTriggerParameters
    error_instance_id: str


class JobNotFoundParameters(typing_extensions.TypedDict):
    """The given Job could not be found."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    jobRid: core_models.JobRid
    """The RID of a Job."""


@dataclass
class JobNotFound(errors.NotFoundError):
    name: typing.Literal["JobNotFound"]
    parameters: JobNotFoundParameters
    error_instance_id: str


class MissingBuildTargetsParameters(typing_extensions.TypedDict):
    """The build target must contains at least one dataset target"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class MissingBuildTargets(errors.BadRequestError):
    name: typing.Literal["MissingBuildTargets"]
    parameters: MissingBuildTargetsParameters
    error_instance_id: str


class MissingConnectingBuildInputsParameters(typing_extensions.TypedDict):
    """The connecting build target must contains at least one input dataset target"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class MissingConnectingBuildInputs(errors.BadRequestError):
    name: typing.Literal["MissingConnectingBuildInputs"]
    parameters: MissingConnectingBuildInputsParameters
    error_instance_id: str


class MissingTriggerParameters(typing_extensions.TypedDict):
    """You must pass in a trigger when creating or updating a schedule"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class MissingTrigger(errors.BadRequestError):
    name: typing.Literal["MissingTrigger"]
    parameters: MissingTriggerParameters
    error_instance_id: str


class PauseSchedulePermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not pause the Schedule."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    scheduleRid: core_models.ScheduleRid


@dataclass
class PauseSchedulePermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["PauseSchedulePermissionDenied"]
    parameters: PauseSchedulePermissionDeniedParameters
    error_instance_id: str


class ReplaceSchedulePermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not replace the Schedule."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    scheduleRid: core_models.ScheduleRid


@dataclass
class ReplaceSchedulePermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["ReplaceSchedulePermissionDenied"]
    parameters: ReplaceSchedulePermissionDeniedParameters
    error_instance_id: str


class RunSchedulePermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not run the Schedule."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    scheduleRid: core_models.ScheduleRid


@dataclass
class RunSchedulePermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["RunSchedulePermissionDenied"]
    parameters: RunSchedulePermissionDeniedParameters
    error_instance_id: str


class ScheduleAlreadyRunningParameters(typing_extensions.TypedDict):
    """The target schedule is currently running."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    scheduleRid: core_models.ScheduleRid


@dataclass
class ScheduleAlreadyRunning(errors.ConflictError):
    name: typing.Literal["ScheduleAlreadyRunning"]
    parameters: ScheduleAlreadyRunningParameters
    error_instance_id: str


class ScheduleNotFoundParameters(typing_extensions.TypedDict):
    """The given Schedule could not be found."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    scheduleRid: core_models.ScheduleRid


@dataclass
class ScheduleNotFound(errors.NotFoundError):
    name: typing.Literal["ScheduleNotFound"]
    parameters: ScheduleNotFoundParameters
    error_instance_id: str


class ScheduleTriggerResourcesNotFoundParameters(typing_extensions.TypedDict):
    """The given resources in the schedule trigger could not be found."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    resourceRids: typing.List[core.RID]


@dataclass
class ScheduleTriggerResourcesNotFound(errors.NotFoundError):
    name: typing.Literal["ScheduleTriggerResourcesNotFound"]
    parameters: ScheduleTriggerResourcesNotFoundParameters
    error_instance_id: str


class ScheduleTriggerResourcesPermissionDeniedParameters(typing_extensions.TypedDict):
    """The provided token does not have permission to use the given resources as a schedule trigger."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    resourceRids: typing.List[core.RID]


@dataclass
class ScheduleTriggerResourcesPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["ScheduleTriggerResourcesPermissionDenied"]
    parameters: ScheduleTriggerResourcesPermissionDeniedParameters
    error_instance_id: str


class ScheduleVersionNotFoundParameters(typing_extensions.TypedDict):
    """The given ScheduleVersion could not be found."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    scheduleVersionRid: orchestration_models.ScheduleVersionRid
    """The RID of a schedule version"""


@dataclass
class ScheduleVersionNotFound(errors.NotFoundError):
    name: typing.Literal["ScheduleVersionNotFound"]
    parameters: ScheduleVersionNotFoundParameters
    error_instance_id: str


class SearchBuildsPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not search the Build."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class SearchBuildsPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["SearchBuildsPermissionDenied"]
    parameters: SearchBuildsPermissionDeniedParameters
    error_instance_id: str


class TargetNotSupportedParameters(typing_extensions.TypedDict):
    """
    The schedule target is not supported. The schedule target must be either a connecting target, upstream
    target or list of single dataset targets.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    scheduleRid: core_models.ScheduleRid


@dataclass
class TargetNotSupported(errors.BadRequestError):
    name: typing.Literal["TargetNotSupported"]
    parameters: TargetNotSupportedParameters
    error_instance_id: str


class UnpauseSchedulePermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not unpause the Schedule."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    scheduleRid: core_models.ScheduleRid


@dataclass
class UnpauseSchedulePermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["UnpauseSchedulePermissionDenied"]
    parameters: UnpauseSchedulePermissionDeniedParameters
    error_instance_id: str


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
    "GetAffectedResourcesSchedulePermissionDenied",
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
    "ScheduleAlreadyRunning",
    "ScheduleNotFound",
    "ScheduleTriggerResourcesNotFound",
    "ScheduleTriggerResourcesPermissionDenied",
    "ScheduleVersionNotFound",
    "SearchBuildsPermissionDenied",
    "TargetNotSupported",
    "UnpauseSchedulePermissionDenied",
]
