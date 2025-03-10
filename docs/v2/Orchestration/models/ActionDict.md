# ActionDict

Action

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**target** | BuildTargetDict | Yes |  |
**branchName** | datasets_models.BranchName | Yes | The target branch the schedule should run on. |
**fallbackBranches** | FallbackBranches | Yes |  |
**forceBuild** | ForceBuild | Yes |  |
**retryCount** | typing_extensions.NotRequired[RetryCount] | No |  |
**retryBackoffDuration** | typing_extensions.NotRequired[RetryBackoffDurationDict] | No |  |
**abortOnFailure** | AbortOnFailure | Yes |  |
**notificationsEnabled** | NotificationsEnabled | Yes |  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
