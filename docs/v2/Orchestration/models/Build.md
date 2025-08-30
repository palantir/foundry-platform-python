# Build

Build

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**rid** | BuildRid | Yes | The RID of a Build. |
**branch_name** | BranchName | Yes | The branch that the build is running on. |
**created_time** | CreatedTime | Yes | The timestamp that the build was created. |
**created_by** | CreatedBy | Yes | The user who created the build. |
**fallback_branches** | FallbackBranches | Yes |  |
**job_rids** | List[JobRid] | Yes |  |
**retry_count** | RetryCount | Yes |  |
**retry_backoff_duration** | RetryBackoffDuration | Yes |  |
**abort_on_failure** | AbortOnFailure | Yes |  |
**status** | BuildStatus | Yes |  |
**schedule_rid** | Optional[ScheduleRid] | No | Schedule RID of the Schedule that triggered this build. If a user triggered the build, Schedule RID will be empty. |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
