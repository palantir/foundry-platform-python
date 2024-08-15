# ActionDict

Action

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**target** | BuildTargetDict | Yes |  |
**branchName** | BranchName | Yes | The target branch the schedule should run on. |
**fallbackBranches** | FallbackBranches | Yes |  |
**forceBuild** | ForceBuild | Yes |  |
**retryCount** | NotRequired[RetryCount] | No |  |
**retryBackoffDuration** | NotRequired[RetryBackoffDurationDict] | No |  |
**abortOnFailure** | AbortOnFailure | Yes |  |
**notificationsEnabled** | NotificationsEnabled | Yes |  |


[[Back to Model list]](../../../README.md#models-v2-link) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
