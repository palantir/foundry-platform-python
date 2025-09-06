# LinkTypeSideV2

`foreignKeyPropertyApiName` is the API name of the foreign key on this object type. If absent, the link is
either a m2m link or the linked object has the foreign key and this object type has the primary key.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**api_name** | LinkTypeApiName | Yes |  |
**display_name** | DisplayName | Yes |  |
**status** | ReleaseStatus | Yes |  |
**object_type_api_name** | ObjectTypeApiName | Yes |  |
**cardinality** | LinkTypeSideCardinality | Yes |  |
**foreign_key_property_api_name** | Optional[PropertyApiName] | No |  |
**link_type_rid** | LinkTypeRid | Yes |  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
