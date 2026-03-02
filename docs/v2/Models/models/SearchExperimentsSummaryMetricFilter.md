# SearchExperimentsSummaryMetricFilter

Filter that atomically binds a series name and aggregation type to a value comparison,
ensuring all conditions are evaluated on the same summary metric.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**series_name** | SeriesName | Yes | The name of the series this metric belongs to. |
**aggregation** | SummaryMetricAggregation | Yes | The aggregation type (MIN, MAX, LAST). |
**operator** | SearchExperimentsNumericFilterOperator | Yes | The comparison operator (EQ, GT, or LT). |
**value** | Any | Yes | The value to compare against. |
**type** | Literal["summaryMetricFilter"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
