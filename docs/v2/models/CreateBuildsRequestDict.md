# CreateBuildsRequestDict

CreateBuildsRequest

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**target** | BuildTargetDict | Yes | The targets of the schedule. |
**branchName** | NotRequired[BranchName] | No | The target branch the build should run on. |
**fallbackBranches** | FallbackBranches | Yes |  |
**forceBuild** | NotRequired[ForceBuild] | No |  |
**retryCount** | NotRequired[RetryCount] | No | The number of retry attempts for failed jobs. |
**retryBackoffDuration** | NotRequired[RetryBackoffDurationDict] | No |  |
**abortOnFailure** | NotRequired[AbortOnFailure] | No |  |
**notificationsEnabled** | NotRequired[NotificationsEnabled] | No |  |


[[Back to Model list]](../../../README.md#models-v2-link) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to README]](../../../README.md)
