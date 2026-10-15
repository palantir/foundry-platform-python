# Resource

A Foundry resource.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**additional_fields** | AdditionalFields | Yes | Optional properties. Only the additional fields explicitly requested by the caller are populated. |
**created_time** | Optional[CreatedTime] | No | The timestamp when the resource was created. This field may be absent for legacy resources. |
**created_user_id** | Optional[UserId] | No | The ID of the user that created the resource. This field may be absent for legacy resources. |
**display_name** | DisplayName | Yes | The display name of the resource. |
**resource_type** | ResourceType | Yes | The type of the resource. |
**rid** | ResourceRid | Yes |  |
**updated_time** | Optional[UpdatedTime] | No | The timestamp when the resource was last modified. This field may be absent for legacy resources. |
**updated_user_id** | Optional[UserId] | No | The ID of the user that last modified the resource. This field may be absent for legacy resources. |
**type** | Literal["value"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v3-link) [[Back to API list]](../../../../README.md#apis-v3-link) [[Back to README]](../../../../README.md)
