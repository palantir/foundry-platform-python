# UserDict

User

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**id** | PrincipalId | Yes |  |
**username** | UserUsername | Yes |  |
**givenName** | NotRequired[StrictStr] | No |  |
**familyName** | NotRequired[StrictStr] | No |  |
**email** | NotRequired[StrictStr] | No | The email at which to contact a User. Multiple users may have the same email address. |
**realm** | Realm | Yes |  |
**organization** | OrganizationRid | Yes |  |
**attributes** | Dict[AttributeName, AttributeValues] | Yes | A map of the User's attributes. Attributes prefixed with "multipass:" are reserved for internal use by Foundry and are subject to change. Additional attributes may be configured by Foundry administrators in  Control Panel and populated by the User's SSO provider upon login.  |


[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
