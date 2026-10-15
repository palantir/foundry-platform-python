# ObjectSetEntities

The concrete object types referenced while evaluating the complete object set, including object types
implementing referenced interfaces and types used by link traversals or derived properties.
These types are identified by API name and may not have objects in the returned page.
Entity information can change and should be refreshed when reloading the set.
This field is only returned on the first page when entity information is available.
An omitted field indicates unavailable dependency information.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**object_type_api_names** | List[ObjectTypeApiName] | Yes |  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
