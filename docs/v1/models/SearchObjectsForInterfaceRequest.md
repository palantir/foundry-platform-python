# SearchObjectsForInterfaceRequest

SearchObjectsForInterfaceRequest

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**where** | Optional[SearchJsonQueryV2] | No |  |
**order_by** | Optional[SearchOrderByV2] | No |  |
**augmented_properties** | Dict[ObjectTypeApiName, List[PropertyApiName]] | Yes | A map from object type API name to a list of property type API names. For each returned object, if the  object’s object type is a key in the map, then we augment the response for that object type with the list  of properties specified in the value.  |
**augmented_shared_property_types** | Dict[InterfaceTypeApiName, List[SharedPropertyTypeApiName]] | Yes | A map from interface type API name to a list of shared property type API names. For each returned object, if the object implements an interface that is a key in the map, then we augment the response for that object  type with the list of properties specified in the value.  |
**selected_shared_property_types** | List[SharedPropertyTypeApiName] | Yes | A list of shared property type API names of the interface type that should be included in the response.  Omit this parameter to include all properties of the interface type in the response.  |
**selected_object_types** | List[ObjectTypeApiName] | Yes | A list of object type API names that should be included in the response. If non-empty, object types that are not mentioned will not be included in the response even if they implement the specified interface. Omit the  parameter to include all object types.  |
**other_interface_types** | List[InterfaceTypeApiName] | Yes | A list of interface type API names. Object types must implement all the mentioned interfaces in order to be  included in the response.  |
**page_size** | Optional[PageSize] | No |  |
**page_token** | Optional[PageToken] | No |  |


[[Back to Model list]](../../../README.md#models-v1-link) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
