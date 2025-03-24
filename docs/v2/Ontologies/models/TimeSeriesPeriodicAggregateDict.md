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
**alignmentTimestamp** | NotRequired[datetime] | No | The timestamp used to align the result, such that ticks in the result time series will lie at integer multiples of the window duration from the alignment timestamp.  Default is the first epoch timestamp (January 1, 1970, 00:00:00 UTC) so that all aggregated points have timestamps at midnight UTC at the start of each window duration.  For example, for a weekly aggregate with alignment timestamp 5 January, 8:33PM,  each aggregated timestamp will lie on the 7 day intervals at 8:33PM starting at 5 January.  |
**windowType** | TimeSeriesWindowType | Yes |  |
**type** | Literal["periodic"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
