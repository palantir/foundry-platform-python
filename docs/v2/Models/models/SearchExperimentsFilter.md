# SearchExperimentsFilter

Filter for searching experiments using operator-based composition.
Supports equality, text matching, boolean combination operators, and compound filters
that atomically bind a name to a value comparison.

Example filters:
- Simple status: {"eq": {"field": "STATUS", "value": "RUNNING"}}
- Branch match: {"eq": {"field": "BRANCH", "value": "master"}}
- Parameter filter: {"parameterFilter": {"parameterName": "learning_rate", "operator": "GT", "value": 0.01}}
- Combined: {"and": {"filters": [
    {"eq": {"field": "STATUS", "value": "SUCCEEDED"}},
    {"parameterFilter": {"parameterName": "learning_rate", "operator": "GT", "value": 0.5}}
  ]}}


This is a discriminator type and does not contain any fields. Instead, it is a union
of of the models listed below.

This discriminator class uses the `type` field to differentiate between classes.

| Class | Value
| ------------ | -------------
SearchExperimentsSeriesFilter | seriesFilter
SearchExperimentsContainsFilter | contains
SearchExperimentsNotFilter | not
SearchExperimentsOrFilter | or
SearchExperimentsAndFilter | and
SearchExperimentsParameterFilter | parameterFilter
SearchExperimentsSummaryMetricFilter | summaryMetricFilter
SearchExperimentsEqualsFilter | eq
SearchExperimentsStartsWithFilter | startsWith


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
