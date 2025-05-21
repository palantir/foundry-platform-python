# Role

A set of permissions that can be assigned to a principal for a specific resource type.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**id** | RoleId | Yes |  |
**role_set_id** | RoleSetId | Yes |  |
**name** | str | Yes |  |
**description** | str | Yes |  |
**is_default** | bool | Yes | Default roles are provided by Palantir and cannot be edited or modified by administrators.  |
**type** | RoleContext | Yes | The type of resource that is valid for this role. |
**operations** | List[Operation] | Yes | The operations that a principal can perform with this role on the assigned resource.  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
