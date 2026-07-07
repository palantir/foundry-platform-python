# ObjectTypeTableDatasource

An object type datasource backed by a Foundry table.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**table_rid** | TableRid | Yes |  |
**branch** | Optional[DatasourceBranchId] | No |  |
**property_mapping** | Dict[PropertyApiName, PropertyTypeMappingInfo] | Yes | A mapping from property API name to a description of how that property is bound to the table. Properties whose mapping info cannot be modeled are omitted.  |
**type** | Literal["table"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
