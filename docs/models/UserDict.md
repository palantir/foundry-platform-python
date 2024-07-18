# UserDict

User

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**attributes** | Dict[AttributeName, AttributeValues] | Yes | A map of the User's attributes. Attributes prefixed with "multipass:" are reserved for internal use by Foundry and are subject to change. Additional attributes may be configured by Foundry administrators in  Control Panel and populated by the User's SSO provider upon login.  |
**email** | NotRequired[StrictStr] | No | The email at which to contact a User. Multiple users may have the same email address. |
**familyName** | NotRequired[StrictStr] | No |  |
**givenName** | NotRequired[StrictStr] | No |  |
**id** | PrincipalId | Yes |  |
**organization** | NotRequired[OrganizationRid] | No |  |
**realm** | Realm | Yes |  |
**username** | UserUsername | Yes |  |


[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
