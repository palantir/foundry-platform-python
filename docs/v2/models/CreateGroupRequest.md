# CreateGroupRequest

CreateGroupRequest

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**name** | GroupName | Yes | The name of the Group. |
**organizations** | List[OrganizationRid] | Yes | The RIDs of the Organizations whose members can see this group. At least one Organization RID must be listed.  |
**description** | Optional[StrictStr] | No | A description of the Group. |
**attributes** | Dict[AttributeName, AttributeValues] | Yes | A map of the Group's attributes. Attributes prefixed with "multipass:" are reserved for internal use by Foundry and are subject to change. |


[[Back to Model list]](../../../README.md#models-v2-link) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to README]](../../../README.md)
