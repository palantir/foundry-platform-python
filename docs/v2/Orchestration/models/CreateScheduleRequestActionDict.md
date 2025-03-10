# CreateScheduleRequestActionDict

CreateScheduleRequestAction

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**abortOnFailure** | typing_extensions.NotRequired[AbortOnFailure] | No |  |
**forceBuild** | typing_extensions.NotRequired[ForceBuild] | No |  |
**retryBackoffDuration** | typing_extensions.NotRequired[RetryBackoffDurationDict] | No |  |
**retryCount** | typing_extensions.NotRequired[RetryCount] | No |  |
**fallbackBranches** | typing_extensions.NotRequired[FallbackBranches] | No |  |
**branchName** | typing_extensions.NotRequired[BranchName] | No | The target branch the schedule should run on. |
**notificationsEnabled** | typing_extensions.NotRequired[NotificationsEnabled] | No |  |
**target** | CreateScheduleRequestBuildTargetDict | Yes |  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
