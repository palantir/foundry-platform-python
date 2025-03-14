# Schedule

Schedule

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**rid** | RID | Yes |  |
**display_name** | Optional[str] | No |  |
**description** | Optional[str] | No |  |
**current_version_rid** | RID | Yes | The RID of the current schedule version |
**created_time** | datetime | Yes |  |
**created_by** | str | Yes |  |
**updated_time** | datetime | Yes |  |
**updated_by** | UUID | Yes |  |
**paused** | bool | Yes |  |
**trigger** | Optional[Trigger] | No | The schedule trigger. If the requesting user does not have permission to see the trigger, this will be empty.  |
**action** | Action | Yes |  |
**scope_mode** | ScopeMode | Yes |  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
