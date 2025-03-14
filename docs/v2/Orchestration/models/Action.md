# Action

Action

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**target** | BuildTarget | Yes |  |
**branch_name** | str | Yes | The target branch the schedule should run on. |
**fallback_branches** | FallbackBranches | Yes |  |
**force_build** | bool | Yes |  |
**retry_count** | Optional[RetryCount] | No |  |
**retry_backoff_duration** | Optional[RetryBackoffDuration] | No |  |
**abort_on_failure** | bool | Yes |  |
**notifications_enabled** | bool | Yes |  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
