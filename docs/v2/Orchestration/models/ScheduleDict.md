# ScheduleDict

Schedule

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**rid** | ScheduleRid | Yes |  |
**displayName** | typing_extensions.NotRequired[str] | No |  |
**description** | typing_extensions.NotRequired[str] | No |  |
**currentVersionRid** | ScheduleVersionRid | Yes | The RID of the current schedule version |
**createdTime** | core_models.CreatedTime | Yes |  |
**createdBy** | core_models.CreatedBy | Yes |  |
**updatedTime** | core_models.UpdatedTime | Yes |  |
**updatedBy** | core_models.UpdatedBy | Yes |  |
**paused** | SchedulePaused | Yes |  |
**trigger** | typing_extensions.NotRequired[TriggerDict] | No | The schedule trigger. If the requesting user does not have permission to see the trigger, this will be empty.  |
**action** | ActionDict | Yes |  |
**scopeMode** | ScopeModeDict | Yes |  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
