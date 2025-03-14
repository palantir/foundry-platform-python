# Build

Build

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**rid** | RID | Yes | The RID of a Build. |
**branch_name** | str | Yes | The branch that the build is running on. |
**created_time** | datetime | Yes | The timestamp that the build was created. |
**created_by** | str | Yes | The user who created the build. |
**fallback_branches** | FallbackBranches | Yes |  |
**job_rids** | List[JobRid] | Yes |  |
**retry_count** | int | Yes |  |
**retry_backoff_duration** | Duration | Yes |  |
**abort_on_failure** | bool | Yes |  |
**status** | BuildStatus | Yes |  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
