# JobDict

Job

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**rid** | JobRid | Yes | The RID of a Job. |
**buildRid** | BuildRid | Yes | The RID of the Build that the Job belongs to. |
**startedTime** | JobStartedTime | Yes | The time this job started waiting for the dependencies to be resolved. |
**finishedTime** | NotRequired[datetime] | No | The time this job was finished. |
**jobStatus** | JobStatus | Yes |  |
**outputs** | List[JobOutputDict] | Yes | Outputs of the Job. Only outputs with supported types are listed here; unsupported types are omitted. Currently supported types are Dataset and Media Set outputs.  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
