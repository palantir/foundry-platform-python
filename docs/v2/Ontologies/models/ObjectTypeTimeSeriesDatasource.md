# ObjectTypeTimeSeriesDatasource

An object type datasource backed by a time series sync, providing values for time-dependent properties.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**time_series_sync_rid** | TimeseriesSyncRid | Yes |  |
**properties** | List[PropertyApiName] | Yes | The set of properties that are bound to the time series.  |
**type** | Literal["timeSeries"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
