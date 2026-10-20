# CreateMarketplaceInstallationRequest

CreateMarketplaceInstallationRequest

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**installation_suffix** | Optional[str] | No | An optional suffix appended to the product title to form the initial display name, for example "Product title - CI staging". If omitted, the display name uses the product title alone. |
**marketplace_rid** | MarketplaceRid | Yes |  |
**ontology_rid** | Optional[OntologyRid] | No | The ontology where jobs for this installation create or update ontology resources. Omit if the product does not interact with the ontology. |
**parent_folder_rid** | FolderRid | Yes | The RID of the Compass project or folder that currently contains the installation. On creation, this is the destination where the installation is registered and its jobs create resources. |
**product_id** | ProductId | Yes |  |
**target_version_hint** | Optional[ProductVersionSelector] | No | If provided:  - validations that are version specific (e.g. singleton validations) are executed assuming     the installation will later have a job run to transition it to this specific target version.  - the installation title is resolved from the product title at that version.  If not provided, the latest released version of the product is used to resolve information for the steps above. |


[[Back to Model list]](../../../../README.md#models-v3-link) [[Back to API list]](../../../../README.md#apis-v3-link) [[Back to README]](../../../../README.md)
