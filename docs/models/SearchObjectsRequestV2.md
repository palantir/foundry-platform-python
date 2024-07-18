# SearchObjectsRequestV2

SearchObjectsRequestV2

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**exclude_rid** | Optional[StrictBool] | No | A flag to exclude the retrieval of the `__rid` property. Setting this to true may improve performance of this endpoint for object types in OSV2.  |
**order_by** | Optional[SearchOrderByV2] | No |  |
**page_size** | Optional[PageSize] | No |  |
**page_token** | Optional[PageToken] | No |  |
**select** | List[PropertyApiName] | Yes | The API names of the object type properties to include in the response.  |
**where** | Optional[SearchJsonQueryV2] | No |  |


[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
