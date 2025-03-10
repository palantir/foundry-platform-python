# Build

Build

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**rid** | core_models.BuildRid | Yes | The RID of a Build. |
**branch_name** | datasets_models.BranchName | Yes | The branch that the build is running on. |
**created_time** | core_models.CreatedTime | Yes | The timestamp that the build was created. |
**created_by** | core_models.CreatedBy | Yes | The user who created the build. |
**fallback_branches** | FallbackBranches | Yes |  |
**retry_count** | RetryCount | Yes |  |
**retry_backoff_duration** | RetryBackoffDuration | Yes |  |
**abort_on_failure** | AbortOnFailure | Yes |  |
**status** | BuildStatus | Yes |  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
