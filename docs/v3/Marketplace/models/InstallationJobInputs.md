# InstallationJobInputs

Input values and explicitly unset inputs for a target installation. Inputs absent from both fields may be fulfilled by defaults, automatic mapping, or recommendations. Use `discoverInputs` to inspect available sources.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**explicitly_unset** | List[InputApiName] | Yes | Names deliberately left unfulfilled. An unset suppresses automatic fulfillment. Names must not also occur in `values`. An unset child does not require an explicitly supplied parent. |
**values** | Dict[InputApiName, InputValue] | Yes | Manually supplied values keyed by qualified input API name. A child with a value requires its parent to have a value in this map, recursively through the ancestor chain. |


[[Back to Model list]](../../../../README.md#models-v3-link) [[Back to API list]](../../../../README.md#apis-v3-link) [[Back to README]](../../../../README.md)
