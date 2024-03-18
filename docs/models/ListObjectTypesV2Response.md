# ListObjectTypesV2Response

ListObjectTypesV2Response

## Properties
Name | Type | Required | Description |
------------ | ------------- | ------------- | ------------- |
**next_page_token** | PageToken | No | The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and populate the next request's `pageToken` field with it.  |
**data** | List[ObjectTypeV2] | No | The list of object types in the current page. |


[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
