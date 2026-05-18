# SearchExperimentsRequest

SearchExperimentsRequest

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**where** | Optional[SearchExperimentsFilter] | No | Optional search filter for filtering experiments. If not provided, all experiments for the model are returned. |
**order_by** | Optional[SearchExperimentsOrderBy] | No | The field to sort by. Default is to sort by relevance. |
**page_size** | Optional[PageSize] | No | The maximum number of results to return. Default 50, maximum of 100. |
**page_token** | Optional[PageToken] | No | PageToken to identify the next page to retrieve. Leave empty for the first request. |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
