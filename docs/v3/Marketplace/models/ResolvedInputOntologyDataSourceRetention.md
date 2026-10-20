# ResolvedInputOntologyDataSourceRetention

Retention thresholds for a direct Ontology data source in an edge environment.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**target_size_bytes** | Long | Yes | The size in bytes to retain after retention runs. Encoded as a decimal-integer string; must be between 0 and 9007199254740991, inclusive. |
**trigger_size_bytes** | Long | Yes | The size in bytes that triggers retention. Encoded as a decimal-integer string; must be between 0 and 9007199254740991, inclusive. |
**type** | Literal["ontologyDataSourceRetention"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v3-link) [[Back to API list]](../../../../README.md#apis-v3-link) [[Back to README]](../../../../README.md)
