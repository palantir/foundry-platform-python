# StreamingExecuteQueryRequest

StreamingExecuteQueryRequest

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**ontology** | Optional[OntologyIdentifier] | No | Optional ontology identifier (RID or API name). When provided, executes an ontology-scoped function. When omitted, executes a global function.  |
**parameters** | Dict[ParameterId, Optional[DataValue]] | Yes |  |
**version** | Optional[FunctionVersion] | No |  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
