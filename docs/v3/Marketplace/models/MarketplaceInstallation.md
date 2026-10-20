# MarketplaceInstallation

A registered product installation and Compass resource. Its latest target version is absent until an installation job runs.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**description** | Optional[str] | No | The current description of the installation in Compass. Absent if no description is set. |
**display_name** | str | Yes | The current display name of the installation in Compass. |
**latest_target_version** | Optional[ProductVersion] | No | The product version targeted by the latest submitted installation job. This may differ from the currently installed version. Absent if no installation job has run. |
**marketplace_rid** | MarketplaceRid | Yes |  |
**namespace_rid** | NamespaceRid | Yes | The RID of the namespace that the installation currently belongs to in Compass. |
**ontology_rid** | Optional[OntologyRid] | No | The ontology where jobs for this installation create or update ontology resources. Omit if the product does not interact with the ontology. |
**parent_folder_rid** | FolderRid | Yes | The RID of the Compass project or folder that currently contains the installation. On creation, this is the destination where the installation is registered and its jobs create resources. |
**product_id** | ProductId | Yes |  |
**rid** | MarketplaceInstallationRid | Yes |  |


[[Back to Model list]](../../../../README.md#models-v3-link) [[Back to API list]](../../../../README.md#apis-v3-link) [[Back to README]](../../../../README.md)
