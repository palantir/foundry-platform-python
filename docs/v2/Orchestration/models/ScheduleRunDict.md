# ScheduleRunDict

ScheduleRun

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**rid** | RID | Yes | The RID of a schedule run |
**scheduleRid** | RID | Yes |  |
**scheduleVersionRid** | RID | Yes |  |
**createdTime** | datetime | Yes | The time at which the schedule run was created. |
**createdBy** | NotRequired[CreatedBy] | No | The Foundry user who manually invoked this schedule run. Automatic trigger runs have this field set to empty.  |
**result** | NotRequired[ScheduleRunResultDict] | No | The result of triggering the schedule. If empty, it means the service is still working on triggering the schedule.  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
