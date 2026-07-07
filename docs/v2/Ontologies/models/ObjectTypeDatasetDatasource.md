# ObjectTypeDatasetDatasource

An object type datasource backed by a Foundry dataset.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**dataset_rid** | DatasetRid | Yes |  |
**branch** | Optional[DatasourceBranchId] | No |  |
**property_mapping** | Dict[PropertyApiName, PropertyTypeMappingInfo] | Yes | A mapping from property API name to a description of how that property is bound to the dataset. Properties whose mapping info cannot be modeled are omitted.  |
**type** | Literal["dataset"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
