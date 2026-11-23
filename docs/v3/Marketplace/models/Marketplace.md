# Marketplace

A Marketplace store containing published products available for installation.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**description** | Optional[str] | No | The current description of the store. Absent if no description is set. |
**display_name** | str | Yes | The current display name of the store. |
**rid** | MarketplaceRid | Yes | The store RID used as `marketplaceRid` when registering a product installation. |
**store_type** | MarketplaceStoreType | Yes | Whether this is a local or remote store. Only local stores expose a filesystem parent. |


[[Back to Model list]](../../../../README.md#models-v3-link) [[Back to API list]](../../../../README.md#apis-v3-link) [[Back to README]](../../../../README.md)
