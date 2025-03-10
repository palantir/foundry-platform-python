# ScheduleVersion

ScheduleVersion

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**rid** | ScheduleVersionRid | Yes | The RID of a schedule version |
**schedule_rid** | ScheduleRid | Yes |  |
**created_time** | core_models.CreatedTime | Yes | The time the schedule version was created |
**created_by** | core_models.CreatedBy | Yes | The Foundry user who created the schedule version |
**trigger** | typing.Optional[Trigger] | No |  |
**action** | Action | Yes |  |
**scope_mode** | ScopeMode | Yes |  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
