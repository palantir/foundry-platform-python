# GetObjectTypeFullMetadataBatchResponse

GetObjectTypeFullMetadataBatchResponse

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**data** | List[ObjectTypeFullMetadata] | Yes | The requested object types, in the order they were requested. Object types that were not found are omitted, so this may contain fewer entries than were requested.  Each object type's `linkTypes` is only populated when the request specifies `includeLinkTypes=true`, and is ordered by link type API name. It may also be empty if the object type has no outgoing link types, or if the requesting token cannot see the object types on the other side of them.  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
