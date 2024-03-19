# ListFilesResponse

A page of Files and an optional page token that can be used to retrieve the next page.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**next_page_token** | PageToken | No | The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and populate the next request's `pageToken` field with it.  |
**data** | List[File] | No | None |


[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
