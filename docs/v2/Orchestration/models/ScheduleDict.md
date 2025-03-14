# ScheduleDict

Schedule

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**rid** | RID | Yes |  |
**displayName** | NotRequired[str] | No |  |
**description** | NotRequired[str] | No |  |
**currentVersionRid** | RID | Yes | The RID of the current schedule version |
**createdTime** | datetime | Yes |  |
**createdBy** | str | Yes |  |
**updatedTime** | datetime | Yes |  |
**updatedBy** | UUID | Yes |  |
**paused** | bool | Yes |  |
**trigger** | NotRequired[TriggerDict] | No | The schedule trigger. If the requesting user does not have permission to see the trigger, this will be empty.  |
**action** | ActionDict | Yes |  |
**scopeMode** | ScopeModeDict | Yes |  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
