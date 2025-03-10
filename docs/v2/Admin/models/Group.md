# Group

Group

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**id** | core_models.PrincipalId | Yes |  |
**name** | GroupName | Yes | The name of the Group. |
**description** | typing.Optional[str] | No | A description of the Group. |
**realm** | core_models.Realm | Yes |  |
**organizations** | typing.List[core_models.OrganizationRid] | Yes | The RIDs of the Organizations whose members can see this group. At least one Organization RID must be listed.  |
**attributes** | typing.Dict[AttributeName, AttributeValues] | Yes | A map of the Group's attributes. Attributes prefixed with "multipass:" are reserved for internal use by Foundry and are subject to change. |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
