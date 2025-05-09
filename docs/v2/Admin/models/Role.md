# Role

Role

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**id** | RoleId | Yes |  |
**display_name** | RoleDisplayName | Yes |  |
**description** | RoleDescription | Yes |  |
**operations** | List[str] | Yes | A list of permissions that this role has. |
**can_assigns** | List[RoleId] | Yes | A list of roles that this role inherits. |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
