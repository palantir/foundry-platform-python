# ParseClassificationsRequest

ParseClassificationsRequest

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**classification_strings** | List[str] | Yes | The classification strings to parse, e.g. 'S//NF'. Requests must contain between 1 and 1000 entries. Duplicate entries count toward this limit but are parsed once. An empty list returns a `MissingBatchRequest` error, and more than 1000 entries returns a `BatchRequestSizeExceededLimit` error.  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
