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

import typing

import pydantic
import typing_extensions

from foundry import _core as core

AbortOnFailure = bool
"""
If any job in the build is unsuccessful, immediately finish the
build by cancelling all other jobs.
"""


class Action(pydantic.BaseModel):
    """Action"""

    target: BuildTarget
    branch_name: datasets_models.BranchName = pydantic.Field(alias=str("branchName"))  # type: ignore[literal-required]
    """The target branch the schedule should run on."""

    fallback_branches: FallbackBranches = pydantic.Field(alias=str("fallbackBranches"))  # type: ignore[literal-required]
    force_build: ForceBuild = pydantic.Field(alias=str("forceBuild"))  # type: ignore[literal-required]
    retry_count: typing.Optional[RetryCount] = pydantic.Field(alias=str("retryCount"), default=None)  # type: ignore[literal-required]
    retry_backoff_duration: typing.Optional[RetryBackoffDuration] = pydantic.Field(alias=str("retryBackoffDuration"), default=None)  # type: ignore[literal-required]
    abort_on_failure: AbortOnFailure = pydantic.Field(alias=str("abortOnFailure"))  # type: ignore[literal-required]
    notifications_enabled: NotificationsEnabled = pydantic.Field(alias=str("notificationsEnabled"))  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ActionDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(ActionDict, self.model_dump(by_alias=True, exclude_none=True))


class ActionDict(typing_extensions.TypedDict):
    """Action"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    target: BuildTargetDict
    branchName: datasets_models.BranchName
    """The target branch the schedule should run on."""

    fallbackBranches: FallbackBranches
    forceBuild: ForceBuild
    retryCount: typing_extensions.NotRequired[RetryCount]
    retryBackoffDuration: typing_extensions.NotRequired[RetryBackoffDurationDict]
    abortOnFailure: AbortOnFailure
    notificationsEnabled: NotificationsEnabled


class AndTrigger(pydantic.BaseModel):
    """Trigger after all of the given triggers emit an event."""

    triggers: typing.List[Trigger]
    type: typing.Literal["and"] = "and"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "AndTriggerDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(AndTriggerDict, self.model_dump(by_alias=True, exclude_none=True))


class AndTriggerDict(typing_extensions.TypedDict):
    """Trigger after all of the given triggers emit an event."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    triggers: typing.List[TriggerDict]
    type: typing.Literal["and"]


class Build(pydantic.BaseModel):
    """Build"""

    rid: core_models.BuildRid
    """The RID of a Build."""

    branch_name: datasets_models.BranchName = pydantic.Field(alias=str("branchName"))  # type: ignore[literal-required]
    """The branch that the build is running on."""

    created_time: core_models.CreatedTime = pydantic.Field(alias=str("createdTime"))  # type: ignore[literal-required]
    """The timestamp that the build was created."""

    created_by: core_models.CreatedBy = pydantic.Field(alias=str("createdBy"))  # type: ignore[literal-required]
    """The user who created the build."""

    fallback_branches: FallbackBranches = pydantic.Field(alias=str("fallbackBranches"))  # type: ignore[literal-required]
    retry_count: RetryCount = pydantic.Field(alias=str("retryCount"))  # type: ignore[literal-required]
    retry_backoff_duration: RetryBackoffDuration = pydantic.Field(alias=str("retryBackoffDuration"))  # type: ignore[literal-required]
    abort_on_failure: AbortOnFailure = pydantic.Field(alias=str("abortOnFailure"))  # type: ignore[literal-required]
    status: BuildStatus
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "BuildDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(BuildDict, self.model_dump(by_alias=True, exclude_none=True))


class BuildDict(typing_extensions.TypedDict):
    """Build"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    rid: core_models.BuildRid
    """The RID of a Build."""

    branchName: datasets_models.BranchName
    """The branch that the build is running on."""

    createdTime: core_models.CreatedTime
    """The timestamp that the build was created."""

    createdBy: core_models.CreatedBy
    """The user who created the build."""

    fallbackBranches: FallbackBranches
    retryCount: RetryCount
    retryBackoffDuration: RetryBackoffDurationDict
    abortOnFailure: AbortOnFailure
    status: BuildStatus


BuildStatus = typing.Literal["RUNNING", "SUCCEEDED", "FAILED", "CANCELED"]
"""The status of the build."""


BuildTarget = typing_extensions.Annotated[
    typing.Union["UpstreamTarget", "ManualTarget", "ConnectingTarget"],
    pydantic.Field(discriminator="type"),
]
"""The targets of the build."""


BuildTargetDict = typing_extensions.Annotated[
    typing.Union["UpstreamTargetDict", "ManualTargetDict", "ConnectingTargetDict"],
    pydantic.Field(discriminator="type"),
]
"""The targets of the build."""


BuildableRid = core.RID
"""
The Resource Identifier (RID) of a Resource that can be built. For example, this is a Dataset RID, Media Set
RID or Restricted View RID.
"""


class ConnectingTarget(pydantic.BaseModel):
    """
    All datasets between the input datasets (exclusive) and the
    target datasets (inclusive) except for the datasets to ignore.
    """

    input_rids: typing.List[BuildableRid] = pydantic.Field(alias=str("inputRids"))  # type: ignore[literal-required]
    """The upstream input datasets (exclusive)."""

    target_rids: typing.List[BuildableRid] = pydantic.Field(alias=str("targetRids"))  # type: ignore[literal-required]
    """The downstream target datasets (inclusive)."""

    ignored_rids: typing.List[BuildableRid] = pydantic.Field(alias=str("ignoredRids"))  # type: ignore[literal-required]
    """The datasets between the input datasets and target datasets to exclude."""

    type: typing.Literal["connecting"] = "connecting"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ConnectingTargetDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(ConnectingTargetDict, self.model_dump(by_alias=True, exclude_none=True))


class ConnectingTargetDict(typing_extensions.TypedDict):
    """
    All datasets between the input datasets (exclusive) and the
    target datasets (inclusive) except for the datasets to ignore.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    inputRids: typing.List[BuildableRid]
    """The upstream input datasets (exclusive)."""

    targetRids: typing.List[BuildableRid]
    """The downstream target datasets (inclusive)."""

    ignoredRids: typing.List[BuildableRid]
    """The datasets between the input datasets and target datasets to exclude."""

    type: typing.Literal["connecting"]


class CreateScheduleRequestAction(pydantic.BaseModel):
    """CreateScheduleRequestAction"""

    abort_on_failure: typing.Optional[AbortOnFailure] = pydantic.Field(alias=str("abortOnFailure"), default=None)  # type: ignore[literal-required]
    force_build: typing.Optional[ForceBuild] = pydantic.Field(alias=str("forceBuild"), default=None)  # type: ignore[literal-required]
    retry_backoff_duration: typing.Optional[RetryBackoffDuration] = pydantic.Field(alias=str("retryBackoffDuration"), default=None)  # type: ignore[literal-required]
    retry_count: typing.Optional[RetryCount] = pydantic.Field(alias=str("retryCount"), default=None)  # type: ignore[literal-required]
    fallback_branches: typing.Optional[FallbackBranches] = pydantic.Field(alias=str("fallbackBranches"), default=None)  # type: ignore[literal-required]
    branch_name: typing.Optional[datasets_models.BranchName] = pydantic.Field(alias=str("branchName"), default=None)  # type: ignore[literal-required]
    """The target branch the schedule should run on."""

    notifications_enabled: typing.Optional[NotificationsEnabled] = pydantic.Field(alias=str("notificationsEnabled"), default=None)  # type: ignore[literal-required]
    target: CreateScheduleRequestBuildTarget
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "CreateScheduleRequestActionDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            CreateScheduleRequestActionDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class CreateScheduleRequestActionDict(typing_extensions.TypedDict):
    """CreateScheduleRequestAction"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    abortOnFailure: typing_extensions.NotRequired[AbortOnFailure]
    forceBuild: typing_extensions.NotRequired[ForceBuild]
    retryBackoffDuration: typing_extensions.NotRequired[RetryBackoffDurationDict]
    retryCount: typing_extensions.NotRequired[RetryCount]
    fallbackBranches: typing_extensions.NotRequired[FallbackBranches]
    branchName: typing_extensions.NotRequired[datasets_models.BranchName]
    """The target branch the schedule should run on."""

    notificationsEnabled: typing_extensions.NotRequired[NotificationsEnabled]
    target: CreateScheduleRequestBuildTargetDict


CreateScheduleRequestBuildTarget = typing_extensions.Annotated[
    typing.Union[
        "CreateScheduleRequestUpstreamTarget",
        "CreateScheduleRequestManualTarget",
        "CreateScheduleRequestConnectingTarget",
    ],
    pydantic.Field(discriminator="type"),
]
"""The targets of the build."""


CreateScheduleRequestBuildTargetDict = typing_extensions.Annotated[
    typing.Union[
        "CreateScheduleRequestUpstreamTargetDict",
        "CreateScheduleRequestManualTargetDict",
        "CreateScheduleRequestConnectingTargetDict",
    ],
    pydantic.Field(discriminator="type"),
]
"""The targets of the build."""


class CreateScheduleRequestConnectingTarget(pydantic.BaseModel):
    """CreateScheduleRequestConnectingTarget"""

    ignored_rids: typing.Optional[typing.List[BuildableRid]] = pydantic.Field(alias=str("ignoredRids"), default=None)  # type: ignore[literal-required]
    """The datasets between the input datasets and target datasets to exclude."""

    target_rids: typing.List[BuildableRid] = pydantic.Field(alias=str("targetRids"))  # type: ignore[literal-required]
    """The downstream target datasets (inclusive)."""

    input_rids: typing.List[BuildableRid] = pydantic.Field(alias=str("inputRids"))  # type: ignore[literal-required]
    """The upstream input datasets (exclusive)."""

    type: typing.Literal["connecting"] = "connecting"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "CreateScheduleRequestConnectingTargetDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            CreateScheduleRequestConnectingTargetDict,
            self.model_dump(by_alias=True, exclude_none=True),
        )


class CreateScheduleRequestConnectingTargetDict(typing_extensions.TypedDict):
    """CreateScheduleRequestConnectingTarget"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    ignoredRids: typing_extensions.NotRequired[typing.List[BuildableRid]]
    """The datasets between the input datasets and target datasets to exclude."""

    targetRids: typing.List[BuildableRid]
    """The downstream target datasets (inclusive)."""

    inputRids: typing.List[BuildableRid]
    """The upstream input datasets (exclusive)."""

    type: typing.Literal["connecting"]


class CreateScheduleRequestManualTarget(pydantic.BaseModel):
    """CreateScheduleRequestManualTarget"""

    target_rids: typing.List[BuildableRid] = pydantic.Field(alias=str("targetRids"))  # type: ignore[literal-required]
    type: typing.Literal["manual"] = "manual"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "CreateScheduleRequestManualTargetDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            CreateScheduleRequestManualTargetDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class CreateScheduleRequestManualTargetDict(typing_extensions.TypedDict):
    """CreateScheduleRequestManualTarget"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    targetRids: typing.List[BuildableRid]
    type: typing.Literal["manual"]


class CreateScheduleRequestProjectScope(pydantic.BaseModel):
    """CreateScheduleRequestProjectScope"""

    project_rids: typing.List[filesystem_models.ProjectRid] = pydantic.Field(alias=str("projectRids"))  # type: ignore[literal-required]
    type: typing.Literal["project"] = "project"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "CreateScheduleRequestProjectScopeDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            CreateScheduleRequestProjectScopeDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class CreateScheduleRequestProjectScopeDict(typing_extensions.TypedDict):
    """CreateScheduleRequestProjectScope"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    projectRids: typing.List[filesystem_models.ProjectRid]
    type: typing.Literal["project"]


CreateScheduleRequestScopeMode = typing_extensions.Annotated[
    typing.Union["CreateScheduleRequestProjectScope", "CreateScheduleRequestUserScope"],
    pydantic.Field(discriminator="type"),
]
"""The boundaries for the schedule build."""


CreateScheduleRequestScopeModeDict = typing_extensions.Annotated[
    typing.Union["CreateScheduleRequestProjectScopeDict", "CreateScheduleRequestUserScopeDict"],
    pydantic.Field(discriminator="type"),
]
"""The boundaries for the schedule build."""


class CreateScheduleRequestUpstreamTarget(pydantic.BaseModel):
    """CreateScheduleRequestUpstreamTarget"""

    ignored_rids: typing.Optional[typing.List[BuildableRid]] = pydantic.Field(alias=str("ignoredRids"), default=None)  # type: ignore[literal-required]
    """The datasets to ignore when calculating the final set of dataset to build."""

    target_rids: typing.List[BuildableRid] = pydantic.Field(alias=str("targetRids"))  # type: ignore[literal-required]
    """The target datasets."""

    type: typing.Literal["upstream"] = "upstream"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "CreateScheduleRequestUpstreamTargetDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            CreateScheduleRequestUpstreamTargetDict,
            self.model_dump(by_alias=True, exclude_none=True),
        )


class CreateScheduleRequestUpstreamTargetDict(typing_extensions.TypedDict):
    """CreateScheduleRequestUpstreamTarget"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    ignoredRids: typing_extensions.NotRequired[typing.List[BuildableRid]]
    """The datasets to ignore when calculating the final set of dataset to build."""

    targetRids: typing.List[BuildableRid]
    """The target datasets."""

    type: typing.Literal["upstream"]


class CreateScheduleRequestUserScope(pydantic.BaseModel):
    """CreateScheduleRequestUserScope"""

    type: typing.Literal["user"] = "user"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "CreateScheduleRequestUserScopeDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            CreateScheduleRequestUserScopeDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class CreateScheduleRequestUserScopeDict(typing_extensions.TypedDict):
    """CreateScheduleRequestUserScope"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    type: typing.Literal["user"]


CronExpression = str
"""
A standard CRON expression with minute, hour, day, month
and day of week.
"""


class DatasetUpdatedTrigger(pydantic.BaseModel):
    """
    Trigger whenever a new transaction is committed to the
    dataset on the target branch.
    """

    dataset_rid: datasets_models.DatasetRid = pydantic.Field(alias=str("datasetRid"))  # type: ignore[literal-required]
    branch_name: datasets_models.BranchName = pydantic.Field(alias=str("branchName"))  # type: ignore[literal-required]
    type: typing.Literal["datasetUpdated"] = "datasetUpdated"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "DatasetUpdatedTriggerDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            DatasetUpdatedTriggerDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class DatasetUpdatedTriggerDict(typing_extensions.TypedDict):
    """
    Trigger whenever a new transaction is committed to the
    dataset on the target branch.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    datasetRid: datasets_models.DatasetRid
    branchName: datasets_models.BranchName
    type: typing.Literal["datasetUpdated"]


FallbackBranches = typing.List["datasets_models.BranchName"]
"""
The branches to retrieve JobSpecs from if no JobSpec is found on the
target branch.
"""


ForceBuild = bool
"""Whether to ignore staleness information when running the build."""


class GetBuildsBatchRequestElement(pydantic.BaseModel):
    """GetBuildsBatchRequestElement"""

    build_rid: core_models.BuildRid = pydantic.Field(alias=str("buildRid"))  # type: ignore[literal-required]
    """The RID of a Build."""

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "GetBuildsBatchRequestElementDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            GetBuildsBatchRequestElementDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class GetBuildsBatchRequestElementDict(typing_extensions.TypedDict):
    """GetBuildsBatchRequestElement"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    buildRid: core_models.BuildRid
    """The RID of a Build."""


class GetBuildsBatchResponse(pydantic.BaseModel):
    """GetBuildsBatchResponse"""

    data: typing.Dict[core_models.BuildRid, Build]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "GetBuildsBatchResponseDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            GetBuildsBatchResponseDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class GetBuildsBatchResponseDict(typing_extensions.TypedDict):
    """GetBuildsBatchResponse"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    data: typing.Dict[core_models.BuildRid, BuildDict]


class Job(pydantic.BaseModel):
    """Job"""

    rid: core_models.JobRid
    """The RID of a Job."""

    build_rid: core_models.BuildRid = pydantic.Field(alias=str("buildRid"))  # type: ignore[literal-required]
    """The RID of the Build that the Job belongs to."""

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "JobDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(JobDict, self.model_dump(by_alias=True, exclude_none=True))


class JobDict(typing_extensions.TypedDict):
    """Job"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    rid: core_models.JobRid
    """The RID of a Job."""

    buildRid: core_models.BuildRid
    """The RID of the Build that the Job belongs to."""


class JobSucceededTrigger(pydantic.BaseModel):
    """
    Trigger whenever a job succeeds on the dataset and on the target
    branch.
    """

    dataset_rid: datasets_models.DatasetRid = pydantic.Field(alias=str("datasetRid"))  # type: ignore[literal-required]
    branch_name: datasets_models.BranchName = pydantic.Field(alias=str("branchName"))  # type: ignore[literal-required]
    type: typing.Literal["jobSucceeded"] = "jobSucceeded"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "JobSucceededTriggerDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            JobSucceededTriggerDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class JobSucceededTriggerDict(typing_extensions.TypedDict):
    """
    Trigger whenever a job succeeds on the dataset and on the target
    branch.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    datasetRid: datasets_models.DatasetRid
    branchName: datasets_models.BranchName
    type: typing.Literal["jobSucceeded"]


class ListRunsOfScheduleResponse(pydantic.BaseModel):
    """ListRunsOfScheduleResponse"""

    data: typing.List[ScheduleRun]
    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ListRunsOfScheduleResponseDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            ListRunsOfScheduleResponseDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class ListRunsOfScheduleResponseDict(typing_extensions.TypedDict):
    """ListRunsOfScheduleResponse"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    data: typing.List[ScheduleRunDict]
    nextPageToken: typing_extensions.NotRequired[core_models.PageToken]


class ManualTarget(pydantic.BaseModel):
    """Manually specify all datasets to build."""

    target_rids: typing.List[BuildableRid] = pydantic.Field(alias=str("targetRids"))  # type: ignore[literal-required]
    type: typing.Literal["manual"] = "manual"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ManualTargetDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(ManualTargetDict, self.model_dump(by_alias=True, exclude_none=True))


class ManualTargetDict(typing_extensions.TypedDict):
    """Manually specify all datasets to build."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    targetRids: typing.List[BuildableRid]
    type: typing.Literal["manual"]


class MediaSetUpdatedTrigger(pydantic.BaseModel):
    """
    Trigger whenever an update is made to a media set on the target
    branch. For transactional media sets, this happens when a transaction
    is committed. For non-transactional media sets, this event happens
    eventually (but not necessary immediately) after an update.
    """

    media_set_rid: core_models.MediaSetRid = pydantic.Field(alias=str("mediaSetRid"))  # type: ignore[literal-required]
    branch_name: datasets_models.BranchName = pydantic.Field(alias=str("branchName"))  # type: ignore[literal-required]
    type: typing.Literal["mediaSetUpdated"] = "mediaSetUpdated"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "MediaSetUpdatedTriggerDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            MediaSetUpdatedTriggerDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class MediaSetUpdatedTriggerDict(typing_extensions.TypedDict):
    """
    Trigger whenever an update is made to a media set on the target
    branch. For transactional media sets, this happens when a transaction
    is committed. For non-transactional media sets, this event happens
    eventually (but not necessary immediately) after an update.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    mediaSetRid: core_models.MediaSetRid
    branchName: datasets_models.BranchName
    type: typing.Literal["mediaSetUpdated"]


class NewLogicTrigger(pydantic.BaseModel):
    """
    Trigger whenever a new JobSpec is put on the dataset and on
    that branch.
    """

    branch_name: datasets_models.BranchName = pydantic.Field(alias=str("branchName"))  # type: ignore[literal-required]
    dataset_rid: datasets_models.DatasetRid = pydantic.Field(alias=str("datasetRid"))  # type: ignore[literal-required]
    type: typing.Literal["newLogic"] = "newLogic"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "NewLogicTriggerDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(NewLogicTriggerDict, self.model_dump(by_alias=True, exclude_none=True))


class NewLogicTriggerDict(typing_extensions.TypedDict):
    """
    Trigger whenever a new JobSpec is put on the dataset and on
    that branch.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    branchName: datasets_models.BranchName
    datasetRid: datasets_models.DatasetRid
    type: typing.Literal["newLogic"]


NotificationsEnabled = bool
"""
Whether to receive a notification at the end of the build.
The notification will be sent to the user that has performed the request.
"""


class OrTrigger(pydantic.BaseModel):
    """Trigger whenever any of the given triggers emit an event."""

    triggers: typing.List[Trigger]
    type: typing.Literal["or"] = "or"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "OrTriggerDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(OrTriggerDict, self.model_dump(by_alias=True, exclude_none=True))


class OrTriggerDict(typing_extensions.TypedDict):
    """Trigger whenever any of the given triggers emit an event."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    triggers: typing.List[TriggerDict]
    type: typing.Literal["or"]


class ProjectScope(pydantic.BaseModel):
    """The schedule will only build resources in the following projects."""

    project_rids: typing.List[filesystem_models.ProjectRid] = pydantic.Field(alias=str("projectRids"))  # type: ignore[literal-required]
    type: typing.Literal["project"] = "project"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ProjectScopeDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(ProjectScopeDict, self.model_dump(by_alias=True, exclude_none=True))


class ProjectScopeDict(typing_extensions.TypedDict):
    """The schedule will only build resources in the following projects."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    projectRids: typing.List[filesystem_models.ProjectRid]
    type: typing.Literal["project"]


class ReplaceScheduleRequestAction(pydantic.BaseModel):
    """ReplaceScheduleRequestAction"""

    abort_on_failure: typing.Optional[AbortOnFailure] = pydantic.Field(alias=str("abortOnFailure"), default=None)  # type: ignore[literal-required]
    force_build: typing.Optional[ForceBuild] = pydantic.Field(alias=str("forceBuild"), default=None)  # type: ignore[literal-required]
    retry_backoff_duration: typing.Optional[RetryBackoffDuration] = pydantic.Field(alias=str("retryBackoffDuration"), default=None)  # type: ignore[literal-required]
    retry_count: typing.Optional[RetryCount] = pydantic.Field(alias=str("retryCount"), default=None)  # type: ignore[literal-required]
    fallback_branches: typing.Optional[FallbackBranches] = pydantic.Field(alias=str("fallbackBranches"), default=None)  # type: ignore[literal-required]
    branch_name: typing.Optional[datasets_models.BranchName] = pydantic.Field(alias=str("branchName"), default=None)  # type: ignore[literal-required]
    """The target branch the schedule should run on."""

    notifications_enabled: typing.Optional[NotificationsEnabled] = pydantic.Field(alias=str("notificationsEnabled"), default=None)  # type: ignore[literal-required]
    target: ReplaceScheduleRequestBuildTarget
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ReplaceScheduleRequestActionDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            ReplaceScheduleRequestActionDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class ReplaceScheduleRequestActionDict(typing_extensions.TypedDict):
    """ReplaceScheduleRequestAction"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    abortOnFailure: typing_extensions.NotRequired[AbortOnFailure]
    forceBuild: typing_extensions.NotRequired[ForceBuild]
    retryBackoffDuration: typing_extensions.NotRequired[RetryBackoffDurationDict]
    retryCount: typing_extensions.NotRequired[RetryCount]
    fallbackBranches: typing_extensions.NotRequired[FallbackBranches]
    branchName: typing_extensions.NotRequired[datasets_models.BranchName]
    """The target branch the schedule should run on."""

    notificationsEnabled: typing_extensions.NotRequired[NotificationsEnabled]
    target: ReplaceScheduleRequestBuildTargetDict


ReplaceScheduleRequestBuildTarget = typing_extensions.Annotated[
    typing.Union[
        "ReplaceScheduleRequestUpstreamTarget",
        "ReplaceScheduleRequestManualTarget",
        "ReplaceScheduleRequestConnectingTarget",
    ],
    pydantic.Field(discriminator="type"),
]
"""The targets of the build."""


ReplaceScheduleRequestBuildTargetDict = typing_extensions.Annotated[
    typing.Union[
        "ReplaceScheduleRequestUpstreamTargetDict",
        "ReplaceScheduleRequestManualTargetDict",
        "ReplaceScheduleRequestConnectingTargetDict",
    ],
    pydantic.Field(discriminator="type"),
]
"""The targets of the build."""


class ReplaceScheduleRequestConnectingTarget(pydantic.BaseModel):
    """ReplaceScheduleRequestConnectingTarget"""

    ignored_rids: typing.Optional[typing.List[BuildableRid]] = pydantic.Field(alias=str("ignoredRids"), default=None)  # type: ignore[literal-required]
    """The datasets between the input datasets and target datasets to exclude."""

    target_rids: typing.List[BuildableRid] = pydantic.Field(alias=str("targetRids"))  # type: ignore[literal-required]
    """The downstream target datasets (inclusive)."""

    input_rids: typing.List[BuildableRid] = pydantic.Field(alias=str("inputRids"))  # type: ignore[literal-required]
    """The upstream input datasets (exclusive)."""

    type: typing.Literal["connecting"] = "connecting"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ReplaceScheduleRequestConnectingTargetDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            ReplaceScheduleRequestConnectingTargetDict,
            self.model_dump(by_alias=True, exclude_none=True),
        )


class ReplaceScheduleRequestConnectingTargetDict(typing_extensions.TypedDict):
    """ReplaceScheduleRequestConnectingTarget"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    ignoredRids: typing_extensions.NotRequired[typing.List[BuildableRid]]
    """The datasets between the input datasets and target datasets to exclude."""

    targetRids: typing.List[BuildableRid]
    """The downstream target datasets (inclusive)."""

    inputRids: typing.List[BuildableRid]
    """The upstream input datasets (exclusive)."""

    type: typing.Literal["connecting"]


class ReplaceScheduleRequestManualTarget(pydantic.BaseModel):
    """ReplaceScheduleRequestManualTarget"""

    target_rids: typing.List[BuildableRid] = pydantic.Field(alias=str("targetRids"))  # type: ignore[literal-required]
    type: typing.Literal["manual"] = "manual"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ReplaceScheduleRequestManualTargetDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            ReplaceScheduleRequestManualTargetDict,
            self.model_dump(by_alias=True, exclude_none=True),
        )


class ReplaceScheduleRequestManualTargetDict(typing_extensions.TypedDict):
    """ReplaceScheduleRequestManualTarget"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    targetRids: typing.List[BuildableRid]
    type: typing.Literal["manual"]


class ReplaceScheduleRequestProjectScope(pydantic.BaseModel):
    """ReplaceScheduleRequestProjectScope"""

    project_rids: typing.List[filesystem_models.ProjectRid] = pydantic.Field(alias=str("projectRids"))  # type: ignore[literal-required]
    type: typing.Literal["project"] = "project"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ReplaceScheduleRequestProjectScopeDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            ReplaceScheduleRequestProjectScopeDict,
            self.model_dump(by_alias=True, exclude_none=True),
        )


class ReplaceScheduleRequestProjectScopeDict(typing_extensions.TypedDict):
    """ReplaceScheduleRequestProjectScope"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    projectRids: typing.List[filesystem_models.ProjectRid]
    type: typing.Literal["project"]


ReplaceScheduleRequestScopeMode = typing_extensions.Annotated[
    typing.Union["ReplaceScheduleRequestProjectScope", "ReplaceScheduleRequestUserScope"],
    pydantic.Field(discriminator="type"),
]
"""The boundaries for the schedule build."""


ReplaceScheduleRequestScopeModeDict = typing_extensions.Annotated[
    typing.Union["ReplaceScheduleRequestProjectScopeDict", "ReplaceScheduleRequestUserScopeDict"],
    pydantic.Field(discriminator="type"),
]
"""The boundaries for the schedule build."""


class ReplaceScheduleRequestUpstreamTarget(pydantic.BaseModel):
    """ReplaceScheduleRequestUpstreamTarget"""

    ignored_rids: typing.Optional[typing.List[BuildableRid]] = pydantic.Field(alias=str("ignoredRids"), default=None)  # type: ignore[literal-required]
    """The datasets to ignore when calculating the final set of dataset to build."""

    target_rids: typing.List[BuildableRid] = pydantic.Field(alias=str("targetRids"))  # type: ignore[literal-required]
    """The target datasets."""

    type: typing.Literal["upstream"] = "upstream"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ReplaceScheduleRequestUpstreamTargetDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            ReplaceScheduleRequestUpstreamTargetDict,
            self.model_dump(by_alias=True, exclude_none=True),
        )


class ReplaceScheduleRequestUpstreamTargetDict(typing_extensions.TypedDict):
    """ReplaceScheduleRequestUpstreamTarget"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    ignoredRids: typing_extensions.NotRequired[typing.List[BuildableRid]]
    """The datasets to ignore when calculating the final set of dataset to build."""

    targetRids: typing.List[BuildableRid]
    """The target datasets."""

    type: typing.Literal["upstream"]


class ReplaceScheduleRequestUserScope(pydantic.BaseModel):
    """ReplaceScheduleRequestUserScope"""

    type: typing.Literal["user"] = "user"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ReplaceScheduleRequestUserScopeDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            ReplaceScheduleRequestUserScopeDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class ReplaceScheduleRequestUserScopeDict(typing_extensions.TypedDict):
    """ReplaceScheduleRequestUserScope"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    type: typing.Literal["user"]


class RetryBackoffDuration(pydantic.BaseModel):
    """The duration to wait before retrying after a Job fails."""

    value: int
    """The duration value."""

    unit: core_models.TimeUnit
    """The unit of duration."""

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "RetryBackoffDurationDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            RetryBackoffDurationDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class RetryBackoffDurationDict(typing_extensions.TypedDict):
    """The duration to wait before retrying after a Job fails."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    value: int
    """The duration value."""

    unit: core_models.TimeUnit
    """The unit of duration."""


RetryCount = int
"""
The number of retry attempts for failed Jobs within the Build. A Job's failure is not considered final until
all retries have been attempted or an error occurs indicating that retries cannot be performed. Be aware,
not all types of failures can be retried.
"""


class Schedule(pydantic.BaseModel):
    """Schedule"""

    rid: ScheduleRid
    display_name: typing.Optional[str] = pydantic.Field(alias=str("displayName"), default=None)  # type: ignore[literal-required]
    description: typing.Optional[str] = None
    current_version_rid: ScheduleVersionRid = pydantic.Field(alias=str("currentVersionRid"))  # type: ignore[literal-required]
    """The RID of the current schedule version"""

    created_time: core_models.CreatedTime = pydantic.Field(alias=str("createdTime"))  # type: ignore[literal-required]
    created_by: core_models.CreatedBy = pydantic.Field(alias=str("createdBy"))  # type: ignore[literal-required]
    updated_time: core_models.UpdatedTime = pydantic.Field(alias=str("updatedTime"))  # type: ignore[literal-required]
    updated_by: core_models.UpdatedBy = pydantic.Field(alias=str("updatedBy"))  # type: ignore[literal-required]
    paused: SchedulePaused
    trigger: typing.Optional[Trigger] = None
    """
    The schedule trigger. If the requesting user does not have
    permission to see the trigger, this will be empty.
    """

    action: Action
    scope_mode: ScopeMode = pydantic.Field(alias=str("scopeMode"))  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ScheduleDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(ScheduleDict, self.model_dump(by_alias=True, exclude_none=True))


class ScheduleDict(typing_extensions.TypedDict):
    """Schedule"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    rid: ScheduleRid
    displayName: typing_extensions.NotRequired[str]
    description: typing_extensions.NotRequired[str]
    currentVersionRid: ScheduleVersionRid
    """The RID of the current schedule version"""

    createdTime: core_models.CreatedTime
    createdBy: core_models.CreatedBy
    updatedTime: core_models.UpdatedTime
    updatedBy: core_models.UpdatedBy
    paused: SchedulePaused
    trigger: typing_extensions.NotRequired[TriggerDict]
    """
    The schedule trigger. If the requesting user does not have
    permission to see the trigger, this will be empty.
    """

    action: ActionDict
    scopeMode: ScopeModeDict


SchedulePaused = bool
"""SchedulePaused"""


ScheduleRid = core.RID
"""The Resource Identifier (RID) of a Schedule."""


class ScheduleRun(pydantic.BaseModel):
    """ScheduleRun"""

    rid: ScheduleRunRid
    """The RID of a schedule run"""

    schedule_rid: ScheduleRid = pydantic.Field(alias=str("scheduleRid"))  # type: ignore[literal-required]
    schedule_version_rid: ScheduleVersionRid = pydantic.Field(alias=str("scheduleVersionRid"))  # type: ignore[literal-required]
    created_time: core_models.CreatedTime = pydantic.Field(alias=str("createdTime"))  # type: ignore[literal-required]
    """The time at which the schedule run was created."""

    created_by: typing.Optional[core_models.CreatedBy] = pydantic.Field(alias=str("createdBy"), default=None)  # type: ignore[literal-required]
    """
    The Foundry user who manually invoked this schedule run. Automatic trigger runs have this field set to
    empty.
    """

    result: typing.Optional[ScheduleRunResult] = None
    """
    The result of triggering the schedule. If empty, it means the service
    is still working on triggering the schedule.
    """

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ScheduleRunDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(ScheduleRunDict, self.model_dump(by_alias=True, exclude_none=True))


class ScheduleRunDict(typing_extensions.TypedDict):
    """ScheduleRun"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    rid: ScheduleRunRid
    """The RID of a schedule run"""

    scheduleRid: ScheduleRid
    scheduleVersionRid: ScheduleVersionRid
    createdTime: core_models.CreatedTime
    """The time at which the schedule run was created."""

    createdBy: typing_extensions.NotRequired[core_models.CreatedBy]
    """
    The Foundry user who manually invoked this schedule run. Automatic trigger runs have this field set to
    empty.
    """

    result: typing_extensions.NotRequired[ScheduleRunResultDict]
    """
    The result of triggering the schedule. If empty, it means the service
    is still working on triggering the schedule.
    """


class ScheduleRunError(pydantic.BaseModel):
    """An error occurred attempting to run the schedule."""

    error_name: ScheduleRunErrorName = pydantic.Field(alias=str("errorName"))  # type: ignore[literal-required]
    description: str
    type: typing.Literal["error"] = "error"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ScheduleRunErrorDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(ScheduleRunErrorDict, self.model_dump(by_alias=True, exclude_none=True))


class ScheduleRunErrorDict(typing_extensions.TypedDict):
    """An error occurred attempting to run the schedule."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    errorName: ScheduleRunErrorName
    description: str
    type: typing.Literal["error"]


ScheduleRunErrorName = typing.Literal[
    "TargetResolutionFailure",
    "CyclicDependency",
    "IncompatibleTargets",
    "PermissionDenied",
    "JobSpecNotFound",
    "ScheduleOwnerNotFound",
    "Internal",
]
"""ScheduleRunErrorName"""


class ScheduleRunIgnored(pydantic.BaseModel):
    """The schedule is not running as all targets are up-to-date."""

    type: typing.Literal["ignored"] = "ignored"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ScheduleRunIgnoredDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            ScheduleRunIgnoredDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class ScheduleRunIgnoredDict(typing_extensions.TypedDict):
    """The schedule is not running as all targets are up-to-date."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    type: typing.Literal["ignored"]


ScheduleRunResult = typing_extensions.Annotated[
    typing.Union["ScheduleRunIgnored", "ScheduleRunSubmitted", "ScheduleRunError"],
    pydantic.Field(discriminator="type"),
]
"""
The result of attempting to trigger the schedule. The schedule run will either be submitted as a build,
ignored if all targets are up-to-date or error.
"""


ScheduleRunResultDict = typing_extensions.Annotated[
    typing.Union["ScheduleRunIgnoredDict", "ScheduleRunSubmittedDict", "ScheduleRunErrorDict"],
    pydantic.Field(discriminator="type"),
]
"""
The result of attempting to trigger the schedule. The schedule run will either be submitted as a build,
ignored if all targets are up-to-date or error.
"""


ScheduleRunRid = core.RID
"""The RID of a schedule run"""


class ScheduleRunSubmitted(pydantic.BaseModel):
    """The schedule has been successfully triggered."""

    build_rid: core_models.BuildRid = pydantic.Field(alias=str("buildRid"))  # type: ignore[literal-required]
    type: typing.Literal["submitted"] = "submitted"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ScheduleRunSubmittedDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            ScheduleRunSubmittedDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class ScheduleRunSubmittedDict(typing_extensions.TypedDict):
    """The schedule has been successfully triggered."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    buildRid: core_models.BuildRid
    type: typing.Literal["submitted"]


class ScheduleSucceededTrigger(pydantic.BaseModel):
    """
    Trigger whenever the specified schedule completes its action
    successfully.
    """

    schedule_rid: ScheduleRid = pydantic.Field(alias=str("scheduleRid"))  # type: ignore[literal-required]
    type: typing.Literal["scheduleSucceeded"] = "scheduleSucceeded"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ScheduleSucceededTriggerDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            ScheduleSucceededTriggerDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class ScheduleSucceededTriggerDict(typing_extensions.TypedDict):
    """
    Trigger whenever the specified schedule completes its action
    successfully.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    scheduleRid: ScheduleRid
    type: typing.Literal["scheduleSucceeded"]


class ScheduleVersion(pydantic.BaseModel):
    """ScheduleVersion"""

    rid: ScheduleVersionRid
    """The RID of a schedule version"""

    schedule_rid: ScheduleRid = pydantic.Field(alias=str("scheduleRid"))  # type: ignore[literal-required]
    created_time: core_models.CreatedTime = pydantic.Field(alias=str("createdTime"))  # type: ignore[literal-required]
    """The time the schedule version was created"""

    created_by: core_models.CreatedBy = pydantic.Field(alias=str("createdBy"))  # type: ignore[literal-required]
    """The Foundry user who created the schedule version"""

    trigger: typing.Optional[Trigger] = None
    action: Action
    scope_mode: ScopeMode = pydantic.Field(alias=str("scopeMode"))  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ScheduleVersionDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(ScheduleVersionDict, self.model_dump(by_alias=True, exclude_none=True))


class ScheduleVersionDict(typing_extensions.TypedDict):
    """ScheduleVersion"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    rid: ScheduleVersionRid
    """The RID of a schedule version"""

    scheduleRid: ScheduleRid
    createdTime: core_models.CreatedTime
    """The time the schedule version was created"""

    createdBy: core_models.CreatedBy
    """The Foundry user who created the schedule version"""

    trigger: typing_extensions.NotRequired[TriggerDict]
    action: ActionDict
    scopeMode: ScopeModeDict


ScheduleVersionRid = core.RID
"""The RID of a schedule version"""


ScopeMode = typing_extensions.Annotated[
    typing.Union["ProjectScope", "UserScope"], pydantic.Field(discriminator="type")
]
"""The boundaries for the schedule build."""


ScopeModeDict = typing_extensions.Annotated[
    typing.Union["ProjectScopeDict", "UserScopeDict"], pydantic.Field(discriminator="type")
]
"""The boundaries for the schedule build."""


class SearchBuildsAndFilter(pydantic.BaseModel):
    """Returns the Builds where every filter is satisfied."""

    items: typing.List[SearchBuildsFilter]
    type: typing.Literal["and"] = "and"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "SearchBuildsAndFilterDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            SearchBuildsAndFilterDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class SearchBuildsAndFilterDict(typing_extensions.TypedDict):
    """Returns the Builds where every filter is satisfied."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    items: typing.List[SearchBuildsFilterDict]
    type: typing.Literal["and"]


class SearchBuildsEqualsFilter(pydantic.BaseModel):
    """SearchBuildsEqualsFilter"""

    field: SearchBuildsEqualsFilterField
    value: typing.Any
    type: typing.Literal["eq"] = "eq"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "SearchBuildsEqualsFilterDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            SearchBuildsEqualsFilterDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class SearchBuildsEqualsFilterDict(typing_extensions.TypedDict):
    """SearchBuildsEqualsFilter"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    field: SearchBuildsEqualsFilterField
    value: typing.Any
    type: typing.Literal["eq"]


SearchBuildsEqualsFilterField = typing.Literal["CREATED_BY", "BRANCH_NAME", "STATUS", "RID"]
"""SearchBuildsEqualsFilterField"""


SearchBuildsFilter = typing_extensions.Annotated[
    typing.Union[
        "SearchBuildsNotFilter",
        "SearchBuildsOrFilter",
        "SearchBuildsAndFilter",
        "SearchBuildsLtFilter",
        "SearchBuildsGteFilter",
        "SearchBuildsEqualsFilter",
    ],
    pydantic.Field(discriminator="type"),
]
"""SearchBuildsFilter"""


SearchBuildsFilterDict = typing_extensions.Annotated[
    typing.Union[
        "SearchBuildsNotFilterDict",
        "SearchBuildsOrFilterDict",
        "SearchBuildsAndFilterDict",
        "SearchBuildsLtFilterDict",
        "SearchBuildsGteFilterDict",
        "SearchBuildsEqualsFilterDict",
    ],
    pydantic.Field(discriminator="type"),
]
"""SearchBuildsFilter"""


class SearchBuildsGteFilter(pydantic.BaseModel):
    """SearchBuildsGteFilter"""

    field: SearchBuildsGteFilterField
    value: typing.Any
    type: typing.Literal["gte"] = "gte"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "SearchBuildsGteFilterDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            SearchBuildsGteFilterDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class SearchBuildsGteFilterDict(typing_extensions.TypedDict):
    """SearchBuildsGteFilter"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    field: SearchBuildsGteFilterField
    value: typing.Any
    type: typing.Literal["gte"]


SearchBuildsGteFilterField = typing.Literal["STARTED_TIME", "FINISHED_TIME"]
"""SearchBuildsGteFilterField"""


class SearchBuildsLtFilter(pydantic.BaseModel):
    """SearchBuildsLtFilter"""

    field: SearchBuildsLtFilterField
    value: typing.Any
    type: typing.Literal["lt"] = "lt"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "SearchBuildsLtFilterDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            SearchBuildsLtFilterDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class SearchBuildsLtFilterDict(typing_extensions.TypedDict):
    """SearchBuildsLtFilter"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    field: SearchBuildsLtFilterField
    value: typing.Any
    type: typing.Literal["lt"]


SearchBuildsLtFilterField = typing.Literal["STARTED_TIME", "FINISHED_TIME"]
"""SearchBuildsLtFilterField"""


class SearchBuildsNotFilter(pydantic.BaseModel):
    """Returns the Builds where the filter is not satisfied."""

    value: SearchBuildsFilter
    type: typing.Literal["not"] = "not"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "SearchBuildsNotFilterDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            SearchBuildsNotFilterDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class SearchBuildsNotFilterDict(typing_extensions.TypedDict):
    """Returns the Builds where the filter is not satisfied."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    value: SearchBuildsFilterDict
    type: typing.Literal["not"]


class SearchBuildsOrFilter(pydantic.BaseModel):
    """Returns the Builds where at least one filter is satisfied."""

    items: typing.List[SearchBuildsFilter]
    type: typing.Literal["or"] = "or"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "SearchBuildsOrFilterDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            SearchBuildsOrFilterDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class SearchBuildsOrFilterDict(typing_extensions.TypedDict):
    """Returns the Builds where at least one filter is satisfied."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    items: typing.List[SearchBuildsFilterDict]
    type: typing.Literal["or"]


class SearchBuildsOrderBy(pydantic.BaseModel):
    """SearchBuildsOrderBy"""

    fields: typing.List[SearchBuildsOrderByItem]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "SearchBuildsOrderByDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            SearchBuildsOrderByDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class SearchBuildsOrderByDict(typing_extensions.TypedDict):
    """SearchBuildsOrderBy"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    fields: typing.List[SearchBuildsOrderByItemDict]


SearchBuildsOrderByField = typing.Literal["STARTED_TIME", "FINISHED_TIME"]
"""SearchBuildsOrderByField"""


class SearchBuildsOrderByItem(pydantic.BaseModel):
    """SearchBuildsOrderByItem"""

    field: SearchBuildsOrderByField
    direction: core_models.OrderByDirection
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "SearchBuildsOrderByItemDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            SearchBuildsOrderByItemDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class SearchBuildsOrderByItemDict(typing_extensions.TypedDict):
    """SearchBuildsOrderByItem"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    field: SearchBuildsOrderByField
    direction: core_models.OrderByDirection


class SearchBuildsResponse(pydantic.BaseModel):
    """SearchBuildsResponse"""

    data: typing.List[Build]
    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "SearchBuildsResponseDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            SearchBuildsResponseDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class SearchBuildsResponseDict(typing_extensions.TypedDict):
    """SearchBuildsResponse"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    data: typing.List[BuildDict]
    nextPageToken: typing_extensions.NotRequired[core_models.PageToken]


class TimeTrigger(pydantic.BaseModel):
    """Trigger on a time based schedule."""

    cron_expression: CronExpression = pydantic.Field(alias=str("cronExpression"))  # type: ignore[literal-required]
    time_zone: core_models.ZoneId = pydantic.Field(alias=str("timeZone"))  # type: ignore[literal-required]
    type: typing.Literal["time"] = "time"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "TimeTriggerDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(TimeTriggerDict, self.model_dump(by_alias=True, exclude_none=True))


class TimeTriggerDict(typing_extensions.TypedDict):
    """Trigger on a time based schedule."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    cronExpression: CronExpression
    timeZone: core_models.ZoneId
    type: typing.Literal["time"]


Trigger = typing_extensions.Annotated[
    typing.Union[
        "JobSucceededTrigger",
        "OrTrigger",
        "NewLogicTrigger",
        "AndTrigger",
        "DatasetUpdatedTrigger",
        "ScheduleSucceededTrigger",
        "MediaSetUpdatedTrigger",
        "TimeTrigger",
    ],
    pydantic.Field(discriminator="type"),
]
"""Trigger"""


TriggerDict = typing_extensions.Annotated[
    typing.Union[
        "JobSucceededTriggerDict",
        "OrTriggerDict",
        "NewLogicTriggerDict",
        "AndTriggerDict",
        "DatasetUpdatedTriggerDict",
        "ScheduleSucceededTriggerDict",
        "MediaSetUpdatedTriggerDict",
        "TimeTriggerDict",
    ],
    pydantic.Field(discriminator="type"),
]
"""Trigger"""


class UpstreamTarget(pydantic.BaseModel):
    """Target the specified datasets along with all upstream datasets except the ignored datasets."""

    target_rids: typing.List[BuildableRid] = pydantic.Field(alias=str("targetRids"))  # type: ignore[literal-required]
    """The target datasets."""

    ignored_rids: typing.List[BuildableRid] = pydantic.Field(alias=str("ignoredRids"))  # type: ignore[literal-required]
    """The datasets to ignore when calculating the final set of dataset to build."""

    type: typing.Literal["upstream"] = "upstream"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "UpstreamTargetDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(UpstreamTargetDict, self.model_dump(by_alias=True, exclude_none=True))


class UpstreamTargetDict(typing_extensions.TypedDict):
    """Target the specified datasets along with all upstream datasets except the ignored datasets."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    targetRids: typing.List[BuildableRid]
    """The target datasets."""

    ignoredRids: typing.List[BuildableRid]
    """The datasets to ignore when calculating the final set of dataset to build."""

    type: typing.Literal["upstream"]


class UserScope(pydantic.BaseModel):
    """
    When triggered, the schedule will build all resources that the
    associated user is permitted to build.
    """

    type: typing.Literal["user"] = "user"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "UserScopeDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(UserScopeDict, self.model_dump(by_alias=True, exclude_none=True))


class UserScopeDict(typing_extensions.TypedDict):
    """
    When triggered, the schedule will build all resources that the
    associated user is permitted to build.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    type: typing.Literal["user"]


from foundry.v2.core import models as core_models  # noqa: E402
from foundry.v2.datasets import models as datasets_models  # noqa: E402
from foundry.v2.filesystem import models as filesystem_models  # noqa: E402

__all__ = [
    "AbortOnFailure",
    "Action",
    "ActionDict",
    "AndTrigger",
    "AndTriggerDict",
    "Build",
    "BuildDict",
    "BuildStatus",
    "BuildTarget",
    "BuildTargetDict",
    "BuildableRid",
    "ConnectingTarget",
    "ConnectingTargetDict",
    "CreateScheduleRequestAction",
    "CreateScheduleRequestActionDict",
    "CreateScheduleRequestBuildTarget",
    "CreateScheduleRequestBuildTargetDict",
    "CreateScheduleRequestConnectingTarget",
    "CreateScheduleRequestConnectingTargetDict",
    "CreateScheduleRequestManualTarget",
    "CreateScheduleRequestManualTargetDict",
    "CreateScheduleRequestProjectScope",
    "CreateScheduleRequestProjectScopeDict",
    "CreateScheduleRequestScopeMode",
    "CreateScheduleRequestScopeModeDict",
    "CreateScheduleRequestUpstreamTarget",
    "CreateScheduleRequestUpstreamTargetDict",
    "CreateScheduleRequestUserScope",
    "CreateScheduleRequestUserScopeDict",
    "CronExpression",
    "DatasetUpdatedTrigger",
    "DatasetUpdatedTriggerDict",
    "FallbackBranches",
    "ForceBuild",
    "GetBuildsBatchRequestElement",
    "GetBuildsBatchRequestElementDict",
    "GetBuildsBatchResponse",
    "GetBuildsBatchResponseDict",
    "Job",
    "JobDict",
    "JobSucceededTrigger",
    "JobSucceededTriggerDict",
    "ListRunsOfScheduleResponse",
    "ListRunsOfScheduleResponseDict",
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
    "ReplaceScheduleRequestAction",
    "ReplaceScheduleRequestActionDict",
    "ReplaceScheduleRequestBuildTarget",
    "ReplaceScheduleRequestBuildTargetDict",
    "ReplaceScheduleRequestConnectingTarget",
    "ReplaceScheduleRequestConnectingTargetDict",
    "ReplaceScheduleRequestManualTarget",
    "ReplaceScheduleRequestManualTargetDict",
    "ReplaceScheduleRequestProjectScope",
    "ReplaceScheduleRequestProjectScopeDict",
    "ReplaceScheduleRequestScopeMode",
    "ReplaceScheduleRequestScopeModeDict",
    "ReplaceScheduleRequestUpstreamTarget",
    "ReplaceScheduleRequestUpstreamTargetDict",
    "ReplaceScheduleRequestUserScope",
    "ReplaceScheduleRequestUserScopeDict",
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
    "ScheduleVersion",
    "ScheduleVersionDict",
    "ScheduleVersionRid",
    "ScopeMode",
    "ScopeModeDict",
    "SearchBuildsAndFilter",
    "SearchBuildsAndFilterDict",
    "SearchBuildsEqualsFilter",
    "SearchBuildsEqualsFilterDict",
    "SearchBuildsEqualsFilterField",
    "SearchBuildsFilter",
    "SearchBuildsFilterDict",
    "SearchBuildsGteFilter",
    "SearchBuildsGteFilterDict",
    "SearchBuildsGteFilterField",
    "SearchBuildsLtFilter",
    "SearchBuildsLtFilterDict",
    "SearchBuildsLtFilterField",
    "SearchBuildsNotFilter",
    "SearchBuildsNotFilterDict",
    "SearchBuildsOrFilter",
    "SearchBuildsOrFilterDict",
    "SearchBuildsOrderBy",
    "SearchBuildsOrderByDict",
    "SearchBuildsOrderByField",
    "SearchBuildsOrderByItem",
    "SearchBuildsOrderByItemDict",
    "SearchBuildsResponse",
    "SearchBuildsResponseDict",
    "TimeTrigger",
    "TimeTriggerDict",
    "Trigger",
    "TriggerDict",
    "UpstreamTarget",
    "UpstreamTargetDict",
    "UserScope",
    "UserScopeDict",
]
