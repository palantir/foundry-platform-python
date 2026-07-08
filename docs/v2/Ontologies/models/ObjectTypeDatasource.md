# ObjectTypeDatasource

A datasource that supplies property values for an object type. Each object type can have one or more
datasources; together they back all of the object type's properties. The `definition` carries the RID of the
backing Foundry resource (for example, the dataset RID for a dataset-backed object type), enabling callers to
navigate from an object type to its backing data.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**rid** | DatasourceRid | Yes |  |
**definition** | ObjectTypeDatasourceDefinition | Yes |  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
