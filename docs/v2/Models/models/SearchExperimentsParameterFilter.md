# SearchExperimentsParameterFilter

Filter that atomically binds a parameter name to a value comparison,
ensuring both conditions are evaluated on the same parameter.
Supported combinations:
- EQ: boolean, double, integer, or datetime value
- GT/LT: double, integer, or datetime value
- CONTAINS: string value (substring match on the parameter's string value)


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**parameter_name** | ParameterName | Yes | The exact name of the parameter to filter on. |
**operator** | SearchExperimentsParameterFilterOperator | Yes | The comparison operator to apply. |
**value** | Any | Yes | The value to compare against. |
**type** | Literal["parameterFilter"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
