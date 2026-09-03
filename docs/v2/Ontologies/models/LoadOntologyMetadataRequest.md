# LoadOntologyMetadataRequest

The Ontology metadata (i.e., object, link, action, query, and interface types) to load.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**object_types** | List[ObjectTypeApiName] | Yes |  |
**link_types** | List[LinkTypeApiName] | Yes |  |
**action_types** | List[ActionTypeApiName] | Yes |  |
**query_types** | List[VersionedQueryTypeApiName] | Yes |  |
**interface_types** | List[InterfaceTypeApiName] | Yes |  |
**include_action_type_full_metadata** | Optional[bool] | No | When set to `true`, the `actionTypesFullMetadata` field of the response will be populated in addition to `actionTypes`.  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
