# Job

Job

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**rid** | JobRid | Yes | The RID of a Job. |
**build_rid** | BuildRid | Yes | The RID of the Build that the Job belongs to. |
**started_time** | JobStartedTime | Yes | The time this job started waiting for the dependencies to be resolved. |
**latest_attempt_start_time** | Optional[datetime] | No | The time this job's latest attempt started running. This field may be empty or outdated if the job failed to start. |
**finished_time** | Optional[datetime] | No | The time this job was finished. |
**job_status** | JobStatus | Yes |  |
**outputs** | List[JobOutput] | Yes | Outputs of the Job. Only outputs with supported types are listed here; unsupported types are omitted. Currently supported types are Dataset and Media Set outputs.  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
