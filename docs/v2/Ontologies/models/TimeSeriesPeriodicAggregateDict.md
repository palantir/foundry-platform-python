# TimeSeriesPeriodicAggregateDict

Aggregates values over discrete, periodic windows for a given time series.

A periodic window divides the time series into windows of fixed durations.
For each window, an aggregate function is applied to the points within that window. The result is a time series
with values representing the aggregate for each window. Windows with no data points are not included
in the output.

Periodic aggregation is useful for downsampling a continuous stream of data to larger granularities such as
hourly, daily, monthly.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**windowSize** | PreciseDurationDict | Yes |  |
**alignmentTimestamp** | datetime | Yes |  |
**windowType** | TimeSeriesWindowType | Yes |  |
**type** | Literal["periodic"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
