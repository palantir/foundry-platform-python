# LoadObjectSetV2MultipleObjectTypesResponse

Represents the API response when loading an `ObjectSet`. An `interfaceToObjectTypeMappings` field is 
optionally returned if the type scope of the returned object set includes any interfaces. The "type scope"
of an object set refers to whether objects contain all their properties (object-type type scope) or just the
properties that implement interface properties (interface type scope). There can be multiple type scopes in a
single object set- some objects may have all their properties and some may only have interface properties.

The `interfaceToObjectTypeMappings` field contains mappings from `SharedPropertyTypeApiName`s on the interface(s) to 
`PropertyApiName` for properties on the object(s).


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**data** | List[OntologyObjectV2] | Yes | The list of objects in the current page. |
**next_page_token** | Optional[PageToken] | No |  |
**total_count** | TotalCount | Yes |  |
**interface_to_object_type_mappings** | Dict[InterfaceTypeApiName, InterfaceToObjectTypeMappings] | Yes |  |
**compute_usage** | Optional[ComputeSeconds] | No |  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
