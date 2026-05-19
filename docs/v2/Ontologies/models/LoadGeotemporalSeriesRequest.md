# LoadGeotemporalSeriesRequest

The request body for loading entries from a geotemporal series reference property.

A geotemporal series represents time-indexed geographic observations for an object, such as the location history
of a vehicle or aircraft. Each entry in the response is a map of property names to values, following the same
structure as `OntologyObjectV2`.

The `range` field is required and restricts results to a specific time window. Both `startTime` and `endTime`
are required on `range`. The `additionalProperties` field controls which additional properties appear in each
returned entry. Results are paginated; use `pageToken` from a previous response to retrieve additional pages.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**range** | AbsoluteTimeRange | Yes |  |
**additional_properties** | List[SelectedPropertyApiName] | Yes | The additional property API names to include in each entry. The "time" and "position" properties are always included and do not need to be specified here. Use this to request additional geotemporal series metadata properties such as "speed" or "heading". Properties that are not available for the underlying geotemporal integration will be omitted from the response entries.  |
**page_token** | Optional[PageToken] | No |  |
**page_size** | Optional[PageSize] | No |  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
