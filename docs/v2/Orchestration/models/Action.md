# Action

Action

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**target** | BuildTarget | Yes |  |
**branch_name** | datasets_models.BranchName | Yes | The target branch the schedule should run on. |
**fallback_branches** | FallbackBranches | Yes |  |
**force_build** | ForceBuild | Yes |  |
**retry_count** | typing.Optional[RetryCount] | No |  |
**retry_backoff_duration** | typing.Optional[RetryBackoffDuration] | No |  |
**abort_on_failure** | AbortOnFailure | Yes |  |
**notifications_enabled** | NotificationsEnabled | Yes |  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
