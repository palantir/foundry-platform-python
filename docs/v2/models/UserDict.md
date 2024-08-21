# UserDict

User

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**id** | PrincipalId | Yes |  |
**username** | UserUsername | Yes | The Foundry username of the User. This is unique within the realm. |
**givenName** | NotRequired[StrictStr] | No | The given name of the User. |
**familyName** | NotRequired[StrictStr] | No | The family name (last name) of the User. |
**email** | NotRequired[StrictStr] | No | The email at which to contact a User. Multiple users may have the same email address. |
**realm** | Realm | Yes |  |
**organization** | NotRequired[OrganizationRid] | No | The RID of the user's primary Organization. This will be blank for third-party application service users. |
**attributes** | Dict[AttributeName, AttributeValues] | Yes | A map of the User's attributes. Attributes prefixed with "multipass:" are reserved for internal use by Foundry and are subject to change. Additional attributes may be configured by Foundry administrators in  Control Panel and populated by the User's SSO provider upon login.  |


[[Back to Model list]](../../../README.md#models-v2-link) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to README]](../../../README.md)
