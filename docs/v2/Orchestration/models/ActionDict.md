# ActionDict

Action

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**target** | BuildTargetDict | Yes |  |
**branchName** | str | Yes | The target branch the schedule should run on. |
**fallbackBranches** | FallbackBranches | Yes |  |
**forceBuild** | bool | Yes |  |
**retryCount** | NotRequired[RetryCount] | No |  |
**retryBackoffDuration** | NotRequired[RetryBackoffDurationDict] | No |  |
**abortOnFailure** | bool | Yes |  |
**notificationsEnabled** | bool | Yes |  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
