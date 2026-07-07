# ObjectTypeEditsOnlyDatasource

An object type datasource that is not backed by any external Foundry resource. All properties on the object type
can only be populated via Actions. Other datasources have edit only *properties*, which are permissioned to the
backing tabular datasource. This datasource has no backing tabular datasource and is a true edit only object
type. Note that this datasource type is incompatible with any other datasource and all the properties on the
object type are backed by it.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**type** | Literal["editsOnly"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
