# BuildDict

Build

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**rid** | BuildRid | Yes | The RID of a Build. |
**branchName** | BranchName | Yes | The branch that the build is running on. |
**createdTime** | CreatedTime | Yes | The timestamp that the build was created. |
**createdBy** | CreatedBy | Yes | The user who created the build. |
**fallbackBranches** | FallbackBranches | Yes |  |
**jobRids** | List[JobRid] | Yes |  |
**retryCount** | RetryCount | Yes |  |
**retryBackoffDuration** | DurationDict | Yes |  |
**abortOnFailure** | AbortOnFailure | Yes |  |
**status** | BuildStatus | Yes |  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
