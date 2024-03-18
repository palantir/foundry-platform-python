# SearchObjectsRequest

SearchObjectsRequest

## Properties
Name | Type | Required | Description |
------------ | ------------- | ------------- | ------------- |
**query** | SearchJsonQueryRequest | Yes | SearchJsonQueryRequest |
**order_by** | SearchOrderByRequest | No | Specifies the ordering of search results by a field and an ordering direction. |
**page_size** | PageSize | No | The page size to use for the endpoint. |
**page_token** | PageToken | No | The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and populate the next request's `pageToken` field with it.  |
**fields** | List[PropertyApiName] | No | The API names of the object type properties to include in the response.  |


[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
