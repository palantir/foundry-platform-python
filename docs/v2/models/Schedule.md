# Schedule

Schedule

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**rid** | ScheduleRid | Yes |  |
**display_name** | Optional[StrictStr] | No |  |
**description** | Optional[StrictStr] | No |  |
**version_rid** | ScheduleVersionRid | Yes | The RID of the current schedule version |
**created_time** | CreatedTime | Yes |  |
**created_by** | CreatedBy | Yes |  |
**updated_time** | UpdatedTime | Yes |  |
**updated_by** | UpdatedBy | Yes |  |
**paused** | SchedulePaused | Yes |  |
**trigger** | Optional[Trigger] | No | The schedule trigger. If the requesting user does not have permission to see the trigger, this will be empty.  |
**action** | Action | Yes |  |
**scope_mode** | ScopeMode | Yes |  |


[[Back to Model list]](../../../README.md#models-v2-link) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
