# CreateScheduleRequest

CreateScheduleRequest

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**display_name** | Optional[str] | No |  |
**description** | Optional[str] | No |  |
**action** | CreateScheduleRequestAction | Yes |  |
**trigger** | Optional[Trigger] | No | The schedule trigger. If the requesting user does not have permission to see the trigger, this will be empty.  |
**scope_mode** | Optional[CreateScheduleRequestScopeMode] | No |  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
