# LoadObjectSetRequestV2

Represents the API POST body when loading an `ObjectSet`.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**exclude_rid** | Optional[StrictBool] | No | A flag to exclude the retrieval of the `__rid` property. Setting this to true may improve performance of this endpoint for object types in OSV2.  |
**object_set** | ObjectSet | Yes |  |
**order_by** | Optional[SearchOrderByV2] | No |  |
**page_size** | Optional[PageSize] | No |  |
**page_token** | Optional[PageToken] | No |  |
**select** | List[SelectedPropertyApiName] | Yes |  |


[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
