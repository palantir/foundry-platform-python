# MarketplaceInstallationInputs

The current fulfilled inputs and inputs explicitly left unfulfilled by the last job of a registered Marketplace installation.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**explicitly_unset** | List[InputApiName] | Yes | Qualified API names explicitly left unfulfilled by the last job that modified the installation. Optional inputs that were neither fulfilled nor explicitly unset are absent from both fields. |
**inputs** | Dict[InputApiName, CurrentInstallationInput] | Yes | Fulfilled values keyed by qualified input API name. Optional inputs without a current value are absent. |


[[Back to Model list]](../../../../README.md#models-v3-link) [[Back to API list]](../../../../README.md#apis-v3-link) [[Back to README]](../../../../README.md)
