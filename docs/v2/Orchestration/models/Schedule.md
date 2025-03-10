# Schedule

Schedule

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**rid** | ScheduleRid | Yes |  |
**display_name** | typing.Optional[str] | No |  |
**description** | typing.Optional[str] | No |  |
**current_version_rid** | ScheduleVersionRid | Yes | The RID of the current schedule version |
**created_time** | core_models.CreatedTime | Yes |  |
**created_by** | core_models.CreatedBy | Yes |  |
**updated_time** | core_models.UpdatedTime | Yes |  |
**updated_by** | core_models.UpdatedBy | Yes |  |
**paused** | SchedulePaused | Yes |  |
**trigger** | typing.Optional[Trigger] | No | The schedule trigger. If the requesting user does not have permission to see the trigger, this will be empty.  |
**action** | Action | Yes |  |
**scope_mode** | ScopeMode | Yes |  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
