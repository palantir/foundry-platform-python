# ScheduleDict

Schedule

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**rid** | ScheduleRid | Yes |  |
**displayName** | NotRequired[StrictStr] | No |  |
**description** | NotRequired[StrictStr] | No |  |
**versionRid** | ScheduleVersionRid | Yes | The RID of the current schedule version |
**createdTime** | CreatedTime | Yes |  |
**createdBy** | CreatedBy | Yes |  |
**updatedTime** | UpdatedTime | Yes |  |
**updatedBy** | UpdatedBy | Yes |  |
**paused** | SchedulePaused | Yes |  |
**trigger** | NotRequired[TriggerDict] | No | The schedule trigger. If the requesting user does not have permission to see the trigger, this will be empty.  |
**action** | ActionDict | Yes |  |
**scopeMode** | ScopeModeDict | Yes |  |


[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)