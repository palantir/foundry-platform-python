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

from foundry_sdk import _core as core
from foundry_sdk.v2.core import models as core_models
from foundry_sdk.v2.datasets import models as datasets_models
from foundry_sdk.v2.filesystem import models as filesystem_models

AbortOnFailure = bool
"""
If any job in the build is unsuccessful, immediately finish the
build by cancelling all other jobs.
"""


class Action(core.ModelBase):
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


class AffectedResourcesResponse(core.ModelBase):
    """AffectedResourcesResponse"""

    datasets: typing.List[BuildableRid]


class AndTrigger(core.ModelBase):
    """Trigger after all of the given triggers emit an event."""

    triggers: typing.List[Trigger]
    type: typing.Literal["and"] = "and"


class Build(core.ModelBase):
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
    job_rids: typing.List[core_models.JobRid] = pydantic.Field(alias=str("jobRids"))  # type: ignore[literal-required]
    retry_count: RetryCount = pydantic.Field(alias=str("retryCount"))  # type: ignore[literal-required]
    retry_backoff_duration: RetryBackoffDuration = pydantic.Field(alias=str("retryBackoffDuration"))  # type: ignore[literal-required]
    abort_on_failure: AbortOnFailure = pydantic.Field(alias=str("abortOnFailure"))  # type: ignore[literal-required]
    status: BuildStatus
    schedule_rid: typing.Optional[core_models.ScheduleRid] = pydantic.Field(alias=str("scheduleRid"), default=None)  # type: ignore[literal-required]
    """Schedule RID of the Schedule that triggered this build. If a user triggered the build, Schedule RID will be empty."""


BuildStatus = typing.Literal["RUNNING", "SUCCEEDED", "FAILED", "CANCELED"]
"""The status of the build."""


BuildTarget = typing_extensions.Annotated[
    typing.Union["UpstreamTarget", "ManualTarget", "ConnectingTarget"],
    pydantic.Field(discriminator="type"),
]
"""The targets of the build."""


BuildableRid = core.RID
"""
The Resource Identifier (RID) of a Resource that can be built. For example, this is a Dataset RID, Media Set
RID or Restricted View RID.
"""


class ConnectingTarget(core.ModelBase):
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


class CreateScheduleRequestAction(core.ModelBase):
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


CreateScheduleRequestBuildTarget = typing_extensions.Annotated[
    typing.Union[
        "CreateScheduleRequestUpstreamTarget",
        "CreateScheduleRequestManualTarget",
        "CreateScheduleRequestConnectingTarget",
    ],
    pydantic.Field(discriminator="type"),
]
"""The targets of the build."""


class CreateScheduleRequestConnectingTarget(core.ModelBase):
    """CreateScheduleRequestConnectingTarget"""

    ignored_rids: typing.Optional[typing.List[BuildableRid]] = pydantic.Field(alias=str("ignoredRids"), default=None)  # type: ignore[literal-required]
    """The datasets between the input datasets and target datasets to exclude."""

    target_rids: typing.List[BuildableRid] = pydantic.Field(alias=str("targetRids"))  # type: ignore[literal-required]
    """The downstream target datasets (inclusive)."""

    input_rids: typing.List[BuildableRid] = pydantic.Field(alias=str("inputRids"))  # type: ignore[literal-required]
    """The upstream input datasets (exclusive)."""

    type: typing.Literal["connecting"] = "connecting"


class CreateScheduleRequestManualTarget(core.ModelBase):
    """CreateScheduleRequestManualTarget"""

    target_rids: typing.List[BuildableRid] = pydantic.Field(alias=str("targetRids"))  # type: ignore[literal-required]
    type: typing.Literal["manual"] = "manual"


class CreateScheduleRequestProjectScope(core.ModelBase):
    """CreateScheduleRequestProjectScope"""

    project_rids: typing.List[filesystem_models.ProjectRid] = pydantic.Field(alias=str("projectRids"))  # type: ignore[literal-required]
    type: typing.Literal["project"] = "project"


CreateScheduleRequestScopeMode = typing_extensions.Annotated[
    typing.Union[CreateScheduleRequestProjectScope, "CreateScheduleRequestUserScope"],
    pydantic.Field(discriminator="type"),
]
"""The boundaries for the schedule build."""


class CreateScheduleRequestUpstreamTarget(core.ModelBase):
    """CreateScheduleRequestUpstreamTarget"""

    ignored_rids: typing.Optional[typing.List[BuildableRid]] = pydantic.Field(alias=str("ignoredRids"), default=None)  # type: ignore[literal-required]
    """The datasets to ignore when calculating the final set of dataset to build."""

    target_rids: typing.List[BuildableRid] = pydantic.Field(alias=str("targetRids"))  # type: ignore[literal-required]
    """The target datasets."""

    type: typing.Literal["upstream"] = "upstream"


class CreateScheduleRequestUserScope(core.ModelBase):
    """CreateScheduleRequestUserScope"""

    type: typing.Literal["user"] = "user"


CronExpression = str
"""
A standard CRON expression with minute, hour, day, month
and day of week.
"""


class DatasetJobOutput(core.ModelBase):
    """DatasetJobOutput"""

    dataset_rid: datasets_models.DatasetRid = pydantic.Field(alias=str("datasetRid"))  # type: ignore[literal-required]
    output_transaction_rid: typing.Optional[datasets_models.TransactionRid] = pydantic.Field(alias=str("outputTransactionRid"), default=None)  # type: ignore[literal-required]
    type: typing.Literal["datasetJobOutput"] = "datasetJobOutput"


class DatasetUpdatedTrigger(core.ModelBase):
    """
    Trigger whenever a new transaction is committed to the
    dataset on the target branch.
    """

    dataset_rid: datasets_models.DatasetRid = pydantic.Field(alias=str("datasetRid"))  # type: ignore[literal-required]
    branch_name: datasets_models.BranchName = pydantic.Field(alias=str("branchName"))  # type: ignore[literal-required]
    type: typing.Literal["datasetUpdated"] = "datasetUpdated"


FallbackBranches = typing.List[datasets_models.BranchName]
"""
The branches to retrieve JobSpecs from if no JobSpec is found on the
target branch.
"""


ForceBuild = bool
"""Whether to ignore staleness information when running the build."""


class GetBuildsBatchRequestElement(core.ModelBase):
    """GetBuildsBatchRequestElement"""

    build_rid: core_models.BuildRid = pydantic.Field(alias=str("buildRid"))  # type: ignore[literal-required]
    """The RID of a Build."""


class GetBuildsBatchResponse(core.ModelBase):
    """GetBuildsBatchResponse"""

    data: typing.Dict[core_models.BuildRid, Build]


class GetJobsBatchRequestElement(core.ModelBase):
    """GetJobsBatchRequestElement"""

    job_rid: core_models.JobRid = pydantic.Field(alias=str("jobRid"))  # type: ignore[literal-required]
    """The RID of a Job."""


class GetJobsBatchResponse(core.ModelBase):
    """GetJobsBatchResponse"""

    data: typing.Dict[core_models.JobRid, Job]


class GetSchedulesBatchRequestElement(core.ModelBase):
    """GetSchedulesBatchRequestElement"""

    schedule_rid: core_models.ScheduleRid = pydantic.Field(alias=str("scheduleRid"))  # type: ignore[literal-required]


class GetSchedulesBatchResponse(core.ModelBase):
    """GetSchedulesBatchResponse"""

    data: typing.Dict[core_models.ScheduleRid, Schedule]


class Job(core.ModelBase):
    """Job"""

    rid: core_models.JobRid
    """The RID of a Job."""

    build_rid: core_models.BuildRid = pydantic.Field(alias=str("buildRid"))  # type: ignore[literal-required]
    """The RID of the Build that the Job belongs to."""

    started_time: JobStartedTime = pydantic.Field(alias=str("startedTime"))  # type: ignore[literal-required]
    """The time this job started waiting for the dependencies to be resolved."""

    finished_time: typing.Optional[core.AwareDatetime] = pydantic.Field(alias=str("finishedTime"), default=None)  # type: ignore[literal-required]
    """The time this job was finished."""

    job_status: JobStatus = pydantic.Field(alias=str("jobStatus"))  # type: ignore[literal-required]
    outputs: typing.List[JobOutput]
    """
    Outputs of the Job. Only outputs with supported types are listed here; unsupported types are omitted.
    Currently supported types are Dataset and Media Set outputs.
    """


JobOutput = typing_extensions.Annotated[
    typing.Union[DatasetJobOutput, "TransactionalMediaSetJobOutput"],
    pydantic.Field(discriminator="type"),
]
"""Other types of Job Outputs exist in Foundry. Currently, only Dataset and Media Set are supported by the API."""


JobStartedTime = core.AwareDatetime
"""The time this job started waiting for the dependencies to be resolved."""


JobStatus = typing.Literal["WAITING", "RUNNING", "SUCCEEDED", "FAILED", "CANCELED", "DID_NOT_RUN"]
"""The status of the job."""


class JobSucceededTrigger(core.ModelBase):
    """
    Trigger whenever a job succeeds on the dataset and on the target
    branch.
    """

    dataset_rid: datasets_models.DatasetRid = pydantic.Field(alias=str("datasetRid"))  # type: ignore[literal-required]
    branch_name: datasets_models.BranchName = pydantic.Field(alias=str("branchName"))  # type: ignore[literal-required]
    type: typing.Literal["jobSucceeded"] = "jobSucceeded"


class ListJobsOfBuildResponse(core.ModelBase):
    """ListJobsOfBuildResponse"""

    data: typing.List[Job]
    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]


class ListRunsOfScheduleResponse(core.ModelBase):
    """ListRunsOfScheduleResponse"""

    data: typing.List[ScheduleRun]
    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]


class ManualTarget(core.ModelBase):
    """Manually specify all datasets to build."""

    target_rids: typing.List[BuildableRid] = pydantic.Field(alias=str("targetRids"))  # type: ignore[literal-required]
    type: typing.Literal["manual"] = "manual"


class ManualTrigger(core.ModelBase):
    """Only trigger the Schedule manually. If placed in an AND or OR condition, this Trigger will be ignored."""

    type: typing.Literal["manual"] = "manual"


class MediaSetUpdatedTrigger(core.ModelBase):
    """
    Trigger whenever an update is made to a media set on the target
    branch. For transactional media sets, this happens when a transaction
    is committed. For non-transactional media sets, this event happens
    eventually (but not necessary immediately) after an update.
    """

    media_set_rid: core_models.MediaSetRid = pydantic.Field(alias=str("mediaSetRid"))  # type: ignore[literal-required]
    branch_name: datasets_models.BranchName = pydantic.Field(alias=str("branchName"))  # type: ignore[literal-required]
    type: typing.Literal["mediaSetUpdated"] = "mediaSetUpdated"


class NewLogicTrigger(core.ModelBase):
    """
    Trigger whenever a new JobSpec is put on the dataset and on
    that branch.
    """

    branch_name: datasets_models.BranchName = pydantic.Field(alias=str("branchName"))  # type: ignore[literal-required]
    dataset_rid: datasets_models.DatasetRid = pydantic.Field(alias=str("datasetRid"))  # type: ignore[literal-required]
    type: typing.Literal["newLogic"] = "newLogic"


NotificationsEnabled = bool
"""
Whether to receive a notification at the end of the build.
The notification will be sent to the user that has most recently edited the schedule.
No notification will be sent if the schedule has `scopeMode` set to `ProjectScope`.
"""


class OrTrigger(core.ModelBase):
    """Trigger whenever any of the given triggers emit an event."""

    triggers: typing.List[Trigger]
    type: typing.Literal["or"] = "or"


class ProjectScope(core.ModelBase):
    """The schedule will only build resources in the following projects."""

    project_rids: typing.List[filesystem_models.ProjectRid] = pydantic.Field(alias=str("projectRids"))  # type: ignore[literal-required]
    type: typing.Literal["project"] = "project"


class ReplaceScheduleRequestAction(core.ModelBase):
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


ReplaceScheduleRequestBuildTarget = typing_extensions.Annotated[
    typing.Union[
        "ReplaceScheduleRequestUpstreamTarget",
        "ReplaceScheduleRequestManualTarget",
        "ReplaceScheduleRequestConnectingTarget",
    ],
    pydantic.Field(discriminator="type"),
]
"""The targets of the build."""


class ReplaceScheduleRequestConnectingTarget(core.ModelBase):
    """ReplaceScheduleRequestConnectingTarget"""

    ignored_rids: typing.Optional[typing.List[BuildableRid]] = pydantic.Field(alias=str("ignoredRids"), default=None)  # type: ignore[literal-required]
    """The datasets between the input datasets and target datasets to exclude."""

    target_rids: typing.List[BuildableRid] = pydantic.Field(alias=str("targetRids"))  # type: ignore[literal-required]
    """The downstream target datasets (inclusive)."""

    input_rids: typing.List[BuildableRid] = pydantic.Field(alias=str("inputRids"))  # type: ignore[literal-required]
    """The upstream input datasets (exclusive)."""

    type: typing.Literal["connecting"] = "connecting"


class ReplaceScheduleRequestManualTarget(core.ModelBase):
    """ReplaceScheduleRequestManualTarget"""

    target_rids: typing.List[BuildableRid] = pydantic.Field(alias=str("targetRids"))  # type: ignore[literal-required]
    type: typing.Literal["manual"] = "manual"


class ReplaceScheduleRequestProjectScope(core.ModelBase):
    """ReplaceScheduleRequestProjectScope"""

    project_rids: typing.List[filesystem_models.ProjectRid] = pydantic.Field(alias=str("projectRids"))  # type: ignore[literal-required]
    type: typing.Literal["project"] = "project"


ReplaceScheduleRequestScopeMode = typing_extensions.Annotated[
    typing.Union[ReplaceScheduleRequestProjectScope, "ReplaceScheduleRequestUserScope"],
    pydantic.Field(discriminator="type"),
]
"""The boundaries for the schedule build."""


class ReplaceScheduleRequestUpstreamTarget(core.ModelBase):
    """ReplaceScheduleRequestUpstreamTarget"""

    ignored_rids: typing.Optional[typing.List[BuildableRid]] = pydantic.Field(alias=str("ignoredRids"), default=None)  # type: ignore[literal-required]
    """The datasets to ignore when calculating the final set of dataset to build."""

    target_rids: typing.List[BuildableRid] = pydantic.Field(alias=str("targetRids"))  # type: ignore[literal-required]
    """The target datasets."""

    type: typing.Literal["upstream"] = "upstream"


class ReplaceScheduleRequestUserScope(core.ModelBase):
    """ReplaceScheduleRequestUserScope"""

    type: typing.Literal["user"] = "user"


RetryCount = int
"""
The number of retry attempts for failed Jobs within the Build. A Job's failure is not considered final until
all retries have been attempted or an error occurs indicating that retries cannot be performed. Be aware,
not all types of failures can be retried.
"""


class Schedule(core.ModelBase):
    """Schedule"""

    rid: core_models.ScheduleRid
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


SchedulePaused = bool
"""SchedulePaused"""


class ScheduleRun(core.ModelBase):
    """ScheduleRun"""

    rid: ScheduleRunRid
    """The RID of a schedule run"""

    schedule_rid: core_models.ScheduleRid = pydantic.Field(alias=str("scheduleRid"))  # type: ignore[literal-required]
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


class ScheduleRunError(core.ModelBase):
    """An error occurred attempting to run the schedule."""

    error_name: ScheduleRunErrorName = pydantic.Field(alias=str("errorName"))  # type: ignore[literal-required]
    description: str
    type: typing.Literal["error"] = "error"


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


class ScheduleRunIgnored(core.ModelBase):
    """The schedule is not running as all targets are up-to-date."""

    type: typing.Literal["ignored"] = "ignored"


ScheduleRunResult = typing_extensions.Annotated[
    typing.Union[ScheduleRunIgnored, "ScheduleRunSubmitted", ScheduleRunError],
    pydantic.Field(discriminator="type"),
]
"""
The result of attempting to trigger the schedule. The schedule run will either be submitted as a build,
ignored if all targets are up-to-date or error.
"""


ScheduleRunRid = core.RID
"""The RID of a schedule run"""


class ScheduleRunSubmitted(core.ModelBase):
    """The schedule has been successfully triggered."""

    build_rid: core_models.BuildRid = pydantic.Field(alias=str("buildRid"))  # type: ignore[literal-required]
    type: typing.Literal["submitted"] = "submitted"


class ScheduleSucceededTrigger(core.ModelBase):
    """
    Trigger whenever the specified schedule completes its action
    successfully.
    """

    schedule_rid: core_models.ScheduleRid = pydantic.Field(alias=str("scheduleRid"))  # type: ignore[literal-required]
    type: typing.Literal["scheduleSucceeded"] = "scheduleSucceeded"


class ScheduleVersion(core.ModelBase):
    """ScheduleVersion"""

    rid: ScheduleVersionRid
    """The RID of a schedule version"""

    schedule_rid: core_models.ScheduleRid = pydantic.Field(alias=str("scheduleRid"))  # type: ignore[literal-required]
    created_time: core_models.CreatedTime = pydantic.Field(alias=str("createdTime"))  # type: ignore[literal-required]
    """The time the schedule version was created"""

    created_by: core_models.CreatedBy = pydantic.Field(alias=str("createdBy"))  # type: ignore[literal-required]
    """The Foundry user who created the schedule version"""

    trigger: typing.Optional[Trigger] = None
    action: Action
    scope_mode: ScopeMode = pydantic.Field(alias=str("scopeMode"))  # type: ignore[literal-required]


ScheduleVersionRid = core.RID
"""The RID of a schedule version"""


ScopeMode = typing_extensions.Annotated[
    typing.Union[ProjectScope, "UserScope"], pydantic.Field(discriminator="type")
]
"""The boundaries for the schedule build."""


class SearchBuildsAndFilter(core.ModelBase):
    """Returns the Builds where every filter is satisfied."""

    items: typing.List[SearchBuildsFilter]
    type: typing.Literal["and"] = "and"


class SearchBuildsEqualsFilter(core.ModelBase):
    """SearchBuildsEqualsFilter"""

    field: SearchBuildsEqualsFilterField
    value: typing.Any
    type: typing.Literal["eq"] = "eq"


SearchBuildsEqualsFilterField = typing.Literal["CREATED_BY", "BRANCH_NAME", "STATUS", "RID"]
"""SearchBuildsEqualsFilterField"""


SearchBuildsFilter = typing_extensions.Annotated[
    typing.Union[
        "SearchBuildsNotFilter",
        "SearchBuildsOrFilter",
        SearchBuildsAndFilter,
        "SearchBuildsLtFilter",
        "SearchBuildsGteFilter",
        SearchBuildsEqualsFilter,
    ],
    pydantic.Field(discriminator="type"),
]
"""SearchBuildsFilter"""


class SearchBuildsGteFilter(core.ModelBase):
    """SearchBuildsGteFilter"""

    field: SearchBuildsGteFilterField
    value: typing.Any
    type: typing.Literal["gte"] = "gte"


SearchBuildsGteFilterField = typing.Literal["STARTED_TIME", "FINISHED_TIME"]
"""SearchBuildsGteFilterField"""


class SearchBuildsLtFilter(core.ModelBase):
    """SearchBuildsLtFilter"""

    field: SearchBuildsLtFilterField
    value: typing.Any
    type: typing.Literal["lt"] = "lt"


SearchBuildsLtFilterField = typing.Literal["STARTED_TIME", "FINISHED_TIME"]
"""SearchBuildsLtFilterField"""


class SearchBuildsNotFilter(core.ModelBase):
    """Returns the Builds where the filter is not satisfied."""

    value: SearchBuildsFilter
    type: typing.Literal["not"] = "not"


class SearchBuildsOrFilter(core.ModelBase):
    """Returns the Builds where at least one filter is satisfied."""

    items: typing.List[SearchBuildsFilter]
    type: typing.Literal["or"] = "or"


class SearchBuildsOrderBy(core.ModelBase):
    """SearchBuildsOrderBy"""

    fields: typing.List[SearchBuildsOrderByItem]


SearchBuildsOrderByField = typing.Literal["STARTED_TIME", "FINISHED_TIME"]
"""SearchBuildsOrderByField"""


class SearchBuildsOrderByItem(core.ModelBase):
    """SearchBuildsOrderByItem"""

    field: SearchBuildsOrderByField
    direction: core_models.OrderByDirection


class SearchBuildsResponse(core.ModelBase):
    """SearchBuildsResponse"""

    data: typing.List[Build]
    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]


class TableUpdatedTrigger(core.ModelBase):
    """
    Trigger whenever a new transaction is committed to the
    table on the target branch.
    """

    table_rid: core_models.TableRid = pydantic.Field(alias=str("tableRid"))  # type: ignore[literal-required]
    branch_name: datasets_models.BranchName = pydantic.Field(alias=str("branchName"))  # type: ignore[literal-required]
    type: typing.Literal["tableUpdated"] = "tableUpdated"


class TimeTrigger(core.ModelBase):
    """Trigger on a time based schedule."""

    cron_expression: CronExpression = pydantic.Field(alias=str("cronExpression"))  # type: ignore[literal-required]
    time_zone: core_models.ZoneId = pydantic.Field(alias=str("timeZone"))  # type: ignore[literal-required]
    type: typing.Literal["time"] = "time"


class TransactionalMediaSetJobOutput(core.ModelBase):
    """TransactionalMediaSetJobOutput"""

    media_set_rid: core_models.MediaSetRid = pydantic.Field(alias=str("mediaSetRid"))  # type: ignore[literal-required]
    transaction_id: typing.Optional[str] = pydantic.Field(alias=str("transactionId"), default=None)  # type: ignore[literal-required]
    type: typing.Literal["transactionalMediaSetJobOutput"] = "transactionalMediaSetJobOutput"


Trigger = typing_extensions.Annotated[
    typing.Union[
        JobSucceededTrigger,
        OrTrigger,
        NewLogicTrigger,
        TableUpdatedTrigger,
        AndTrigger,
        DatasetUpdatedTrigger,
        ScheduleSucceededTrigger,
        MediaSetUpdatedTrigger,
        TimeTrigger,
        ManualTrigger,
    ],
    pydantic.Field(discriminator="type"),
]
"""Trigger"""


class UpstreamTarget(core.ModelBase):
    """Target the specified datasets along with all upstream datasets except the ignored datasets."""

    target_rids: typing.List[BuildableRid] = pydantic.Field(alias=str("targetRids"))  # type: ignore[literal-required]
    """The target datasets."""

    ignored_rids: typing.List[BuildableRid] = pydantic.Field(alias=str("ignoredRids"))  # type: ignore[literal-required]
    """The datasets to ignore when calculating the final set of dataset to build."""

    type: typing.Literal["upstream"] = "upstream"


class UserScope(core.ModelBase):
    """
    When triggered, the schedule will build all resources that the
    associated user is permitted to build.
    """

    type: typing.Literal["user"] = "user"


RetryBackoffDuration = core_models.Duration
"""The duration to wait before retrying after a Job fails."""


core.resolve_forward_references(BuildTarget, globalns=globals(), localns=locals())
core.resolve_forward_references(
    CreateScheduleRequestBuildTarget, globalns=globals(), localns=locals()
)
core.resolve_forward_references(
    CreateScheduleRequestScopeMode, globalns=globals(), localns=locals()
)
core.resolve_forward_references(FallbackBranches, globalns=globals(), localns=locals())
core.resolve_forward_references(JobOutput, globalns=globals(), localns=locals())
core.resolve_forward_references(
    ReplaceScheduleRequestBuildTarget, globalns=globals(), localns=locals()
)
core.resolve_forward_references(
    ReplaceScheduleRequestScopeMode, globalns=globals(), localns=locals()
)
core.resolve_forward_references(ScheduleRunResult, globalns=globals(), localns=locals())
core.resolve_forward_references(ScopeMode, globalns=globals(), localns=locals())
core.resolve_forward_references(SearchBuildsFilter, globalns=globals(), localns=locals())
core.resolve_forward_references(Trigger, globalns=globals(), localns=locals())

__all__ = [
    "AbortOnFailure",
    "Action",
    "AffectedResourcesResponse",
    "AndTrigger",
    "Build",
    "BuildStatus",
    "BuildTarget",
    "BuildableRid",
    "ConnectingTarget",
    "CreateScheduleRequestAction",
    "CreateScheduleRequestBuildTarget",
    "CreateScheduleRequestConnectingTarget",
    "CreateScheduleRequestManualTarget",
    "CreateScheduleRequestProjectScope",
    "CreateScheduleRequestScopeMode",
    "CreateScheduleRequestUpstreamTarget",
    "CreateScheduleRequestUserScope",
    "CronExpression",
    "DatasetJobOutput",
    "DatasetUpdatedTrigger",
    "FallbackBranches",
    "ForceBuild",
    "GetBuildsBatchRequestElement",
    "GetBuildsBatchResponse",
    "GetJobsBatchRequestElement",
    "GetJobsBatchResponse",
    "GetSchedulesBatchRequestElement",
    "GetSchedulesBatchResponse",
    "Job",
    "JobOutput",
    "JobStartedTime",
    "JobStatus",
    "JobSucceededTrigger",
    "ListJobsOfBuildResponse",
    "ListRunsOfScheduleResponse",
    "ManualTarget",
    "ManualTrigger",
    "MediaSetUpdatedTrigger",
    "NewLogicTrigger",
    "NotificationsEnabled",
    "OrTrigger",
    "ProjectScope",
    "ReplaceScheduleRequestAction",
    "ReplaceScheduleRequestBuildTarget",
    "ReplaceScheduleRequestConnectingTarget",
    "ReplaceScheduleRequestManualTarget",
    "ReplaceScheduleRequestProjectScope",
    "ReplaceScheduleRequestScopeMode",
    "ReplaceScheduleRequestUpstreamTarget",
    "ReplaceScheduleRequestUserScope",
    "RetryBackoffDuration",
    "RetryCount",
    "Schedule",
    "SchedulePaused",
    "ScheduleRun",
    "ScheduleRunError",
    "ScheduleRunErrorName",
    "ScheduleRunIgnored",
    "ScheduleRunResult",
    "ScheduleRunRid",
    "ScheduleRunSubmitted",
    "ScheduleSucceededTrigger",
    "ScheduleVersion",
    "ScheduleVersionRid",
    "ScopeMode",
    "SearchBuildsAndFilter",
    "SearchBuildsEqualsFilter",
    "SearchBuildsEqualsFilterField",
    "SearchBuildsFilter",
    "SearchBuildsGteFilter",
    "SearchBuildsGteFilterField",
    "SearchBuildsLtFilter",
    "SearchBuildsLtFilterField",
    "SearchBuildsNotFilter",
    "SearchBuildsOrFilter",
    "SearchBuildsOrderBy",
    "SearchBuildsOrderByField",
    "SearchBuildsOrderByItem",
    "SearchBuildsResponse",
    "TableUpdatedTrigger",
    "TimeTrigger",
    "TransactionalMediaSetJobOutput",
    "Trigger",
    "UpstreamTarget",
    "UserScope",
]
