# BuildDict

Build

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**rid** | core_models.BuildRid | Yes | The RID of a Build. |
**branchName** | datasets_models.BranchName | Yes | The branch that the build is running on. |
**createdTime** | core_models.CreatedTime | Yes | The timestamp that the build was created. |
**createdBy** | core_models.CreatedBy | Yes | The user who created the build. |
**fallbackBranches** | FallbackBranches | Yes |  |
**retryCount** | RetryCount | Yes |  |
**retryBackoffDuration** | RetryBackoffDurationDict | Yes |  |
**abortOnFailure** | AbortOnFailure | Yes |  |
**status** | BuildStatus | Yes |  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
