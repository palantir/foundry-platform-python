# OntologyFullMetadata

OntologyFullMetadata

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**ontology** | OntologyV2 | Yes |  |
**object_types** | Dict[ObjectTypeApiName, ObjectTypeFullMetadata] | Yes |  |
**action_types** | Dict[ActionTypeApiName, ActionTypeV2] | Yes |  |
**action_types_full_metadata** | Dict[ActionTypeApiName, ActionTypeFullMetadata] | Yes | The full metadata for the loaded action types. This is only populated if the request opted in to it by setting `includeActionTypeFullMetadata` to `true`. The `actionTypes` field is always populated, regardless of this flag.  |
**query_types** | Dict[VersionedQueryTypeApiName, QueryTypeV2] | Yes |  |
**interface_types** | Dict[InterfaceTypeApiName, InterfaceType] | Yes |  |
**shared_property_types** | Dict[SharedPropertyTypeApiName, SharedPropertyType] | Yes |  |
**branch** | Optional[BranchMetadata] | No |  |
**value_types** | Dict[ValueTypeApiName, OntologyValueType] | Yes |  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
