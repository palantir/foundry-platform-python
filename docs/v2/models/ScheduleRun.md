# ScheduleRun

ScheduleRun

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**rid** | ScheduleRunRid | Yes | The RID of a schedule run |
**schedule_rid** | ScheduleRid | Yes |  |
**schedule_version_rid** | ScheduleVersionRid | Yes |  |
**created_time** | CreatedTime | Yes | The time at which the schedule run was created. |
**created_by** | Optional[CreatedBy] | No | The Foundry user who manually invoked this schedule run. Automatic trigger runs have this field set to empty.  |
**result** | Optional[ScheduleRunResult] | No | The result of triggering the schedule. If empty, it means the service is still working on triggering the schedule.  |


[[Back to Model list]](../../../README.md#models-v2-link) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to README]](../../../README.md)
