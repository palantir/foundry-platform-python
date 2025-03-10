# ScheduleVersionDict

ScheduleVersion

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**rid** | ScheduleVersionRid | Yes | The RID of a schedule version |
**scheduleRid** | ScheduleRid | Yes |  |
**createdTime** | core_models.CreatedTime | Yes | The time the schedule version was created |
**createdBy** | core_models.CreatedBy | Yes | The Foundry user who created the schedule version |
**trigger** | typing_extensions.NotRequired[TriggerDict] | No |  |
**action** | ActionDict | Yes |  |
**scopeMode** | ScopeModeDict | Yes |  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
