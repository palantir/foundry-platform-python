# CreateScheduleRequestActionDict

CreateScheduleRequestAction

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**abortOnFailure** | NotRequired[AbortOnFailure] | No |  |
**forceBuild** | NotRequired[ForceBuild] | No |  |
**retryBackoffDuration** | NotRequired[DurationDict] | No |  |
**retryCount** | NotRequired[RetryCount] | No |  |
**fallbackBranches** | NotRequired[FallbackBranches] | No |  |
**branchName** | NotRequired[BranchName] | No | The target branch the schedule should run on. |
**notificationsEnabled** | NotRequired[NotificationsEnabled] | No |  |
**target** | CreateScheduleRequestBuildTargetDict | Yes |  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
