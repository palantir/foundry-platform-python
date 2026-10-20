# DiscoverInstallationJobInputsResponse

DiscoverInstallationJobInputsResponse

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**errors** | List[InstallationError] | Yes | Errors encountered during input resolution. Errors for inputs excluded by `sourceFilter` are omitted. |
**inputs** | Dict[MarketplaceInstallationRid, DiscoveredInstallationInputs] | Yes | All matching input requirements for each requested installation after source filtering, without pagination. An installation's input map is empty if no inputs match. |


[[Back to Model list]](../../../../README.md#models-v3-link) [[Back to API list]](../../../../README.md#apis-v3-link) [[Back to README]](../../../../README.md)
