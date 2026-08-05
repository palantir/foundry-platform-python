# SearchObjectsRequestV2

SearchObjectsRequestV2

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**where** | Optional[SearchJsonQueryV2] | No |  |
**order_by** | Optional[SearchOrderByV2] | No |  |
**page_size** | Optional[PageSize] | No |  |
**page_token** | Optional[PageToken] | No |  |
**select** | List[PropertyApiName] | Yes | The API names of the object type properties to include in the response.  |
**select_v2** | Optional[List[PropertyIdentifier]] | No | The identifiers of the properties to include in the response. Only selectV2 or select should be populated, but not both.  |
**default_load_level** | Optional[PropertyLoadLevel] | No |  |
**exclude_rid** | Optional[bool] | No | A flag to exclude the retrieval of the `__rid` property. Setting this to true may improve performance of this endpoint for object types in OSV2.  |
**snapshot** | Optional[bool] | No | A flag to use snapshot consistency when paging. Setting this to true will give you a consistent view from before you start paging through the results, ensuring you do not get duplicate or missing items. Setting this to false will let new results enter as you page, but you may encounter duplicate or missing items. This defaults to false if not specified, which means you will always get the latest results.  |
**reference_signing_options** | Optional[ReferenceSigningOptions] | No |  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
