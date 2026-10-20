# CurrentInstallationInput

A fulfilled input of the installation, including how its current value was supplied.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**source** | InputSource | Yes | The mechanism that supplied the current value. |
**value** | InputValue | Yes | The current value. Its representation may differ from the one originally supplied. Credentials contain only secret names, with no secret values, and cannot be used as input to another installation job. |


[[Back to Model list]](../../../../README.md#models-v3-link) [[Back to API list]](../../../../README.md#apis-v3-link) [[Back to README]](../../../../README.md)
