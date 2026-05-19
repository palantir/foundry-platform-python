# LoadGeotemporalSeriesResponse

The response when loading entries from a geotemporal series reference property.

Each entry in `data` is a map of property names to values containing the fields requested via
`additionalProperties` in the corresponding `LoadGeotemporalSeriesRequest`. If `nextPageToken` is present,
additional entries are available and can be retrieved by passing the token in a subsequent request.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**data** | List[GeotemporalSeriesEntry] | Yes |  |
**next_page_token** | Optional[PageToken] | No |  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
