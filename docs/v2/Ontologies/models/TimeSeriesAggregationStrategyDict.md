# TimeSeriesAggregationStrategyDict

CUMULATIVE aggregates all points up to the current point.
ROLLING aggregates all points in a rolling window whose size is either the specified number of points or
time duration.
PERIODIC aggregates all points in specified time windows.


This is a discriminator type and does not contain any fields. Instead, it is a union
of of the models listed below.

This discriminator class uses the `type` field to differentiate between classes.

| Class | Value
| ------------ | -------------
TimeSeriesRollingAggregateDict | rolling
TimeSeriesPeriodicAggregateDict | periodic
TimeSeriesCumulativeAggregateDict | cumulative


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
