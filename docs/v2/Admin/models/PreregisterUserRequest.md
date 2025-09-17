# PreregisterUserRequest

PreregisterUserRequest

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**username** | UserUsername | Yes | The new user's username. This must match one of the provider's supported username patterns. |
**organization** | OrganizationRid | Yes | The RID of the user's primary Organization. This may be changed when the user logs in for the first time depending on any configured Organization assignment rules.  |
**given_name** | Optional[str] | No |  |
**family_name** | Optional[str] | No |  |
**email** | Optional[str] | No |  |
**attributes** | Optional[Dict[AttributeName, AttributeValues]] | No |  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
