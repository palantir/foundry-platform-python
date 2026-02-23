# SearchExperimentsSeriesFilter

Filter that atomically binds a series name to a metric comparison,
ensuring all conditions are evaluated on the same series.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**series_name** | SeriesName | Yes | The name of the series to filter on. |
**field** | SearchExperimentsSeriesFilterField | Yes | The series metric to compare. |
**operator** | SearchExperimentsFilterOperator | Yes | The comparison operator (EQ, GT, or LT). |
**value** | Any | Yes | The value to compare against. |
**type** | Literal["seriesFilter"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
