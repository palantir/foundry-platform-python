# BuildDict

Build

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**rid** | RID | Yes | The RID of a Build. |
**branchName** | str | Yes | The branch that the build is running on. |
**createdTime** | datetime | Yes | The timestamp that the build was created. |
**createdBy** | str | Yes | The user who created the build. |
**fallbackBranches** | FallbackBranches | Yes |  |
**jobRids** | List[JobRid] | Yes |  |
**retryCount** | int | Yes |  |
**retryBackoffDuration** | DurationDict | Yes |  |
**abortOnFailure** | bool | Yes |  |
**status** | BuildStatus | Yes |  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
