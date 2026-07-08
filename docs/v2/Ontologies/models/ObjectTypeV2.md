# ObjectTypeV2

Represents an object type in the Ontology.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**api_name** | ObjectTypeApiName | Yes |  |
**display_name** | DisplayName | Yes |  |
**status** | ReleaseStatus | Yes |  |
**description** | Optional[str] | No | The description of the object type. |
**plural_display_name** | str | Yes | The plural display name of the object type. |
**icon** | Icon | Yes |  |
**primary_key** | PropertyApiName | Yes |  |
**properties** | Dict[PropertyApiName, PropertyV2] | Yes | A map of the properties of the object type. |
**rid** | ObjectTypeRid | Yes |  |
**title_property** | PropertyApiName | Yes |  |
**visibility** | Optional[ObjectTypeVisibility] | No |  |
**aliases** | Optional[List[str]] | No | Alternative names (synonyms) for the object type, usable as search terms. This field is only populated on the get-by-RID read paths (e.g. `getObjectTypeV2`); it is always empty on the `listObjectTypesV2` endpoint.  |
**datasources** | List[ObjectTypeDatasource] | Yes | The datasources backing this object type which the user has access to see. Only populated when the request specifies `includeDatasources=true`. This list may be empty if the user doesn't have access to any datasources.  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
