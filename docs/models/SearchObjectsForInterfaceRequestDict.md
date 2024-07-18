# SearchObjectsForInterfaceRequestDict

SearchObjectsForInterfaceRequest

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**augmentedProperties** | Dict[ObjectTypeApiName, List[PropertyApiName]] | Yes | A map from object type API name to a list of property type API names. For each returned object, if the  object’s object type is a key in the map, then we augment the response for that object type with the list  of properties specified in the value.  |
**augmentedSharedPropertyTypes** | Dict[InterfaceTypeApiName, List[SharedPropertyTypeApiName]] | Yes | A map from interface type API name to a list of shared property type API names. For each returned object, if the object implements an interface that is a key in the map, then we augment the response for that object  type with the list of properties specified in the value.  |
**orderBy** | NotRequired[SearchOrderByV2Dict] | No |  |
**otherInterfaceTypes** | List[InterfaceTypeApiName] | Yes | A list of interface type API names. Object types must implement all the mentioned interfaces in order to be  included in the response.  |
**pageSize** | NotRequired[PageSize] | No |  |
**pageToken** | NotRequired[PageToken] | No |  |
**selectedObjectTypes** | List[ObjectTypeApiName] | Yes | A list of object type API names that should be included in the response. If non-empty, object types that are not mentioned will not be included in the response even if they implement the specified interface. Omit the  parameter to include all object types.  |
**selectedSharedPropertyTypes** | List[SharedPropertyTypeApiName] | Yes | A list of shared property type API names of the interface type that should be included in the response.  Omit this parameter to include all properties of the interface type in the response.  |
**where** | NotRequired[SearchJsonQueryV2Dict] | No |  |


[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
