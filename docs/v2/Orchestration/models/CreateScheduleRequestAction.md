# CreateScheduleRequestAction

CreateScheduleRequestAction

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**abort_on_failure** | typing.Optional[AbortOnFailure] | No |  |
**force_build** | typing.Optional[ForceBuild] | No |  |
**retry_backoff_duration** | typing.Optional[RetryBackoffDuration] | No |  |
**retry_count** | typing.Optional[RetryCount] | No |  |
**fallback_branches** | typing.Optional[FallbackBranches] | No |  |
**branch_name** | typing.Optional[datasets_models.BranchName] | No | The target branch the schedule should run on. |
**notifications_enabled** | typing.Optional[NotificationsEnabled] | No |  |
**target** | CreateScheduleRequestBuildTarget | Yes |  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
