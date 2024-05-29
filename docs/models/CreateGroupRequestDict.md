# CreateGroupRequestDict

CreateGroupRequest

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**name** | GroupName | Yes |  |
**organizations** | List[OrganizationRid] | Yes |  |
**description** | NotRequired[StrictStr] | No |  |
**attributes** | Dict[AttributeName, AttributeValues] | Yes | A map of the Group's attributes. Attributes prefixed with "multipass:" are reserved for internal use by Foundry and are subject to change. |


[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)