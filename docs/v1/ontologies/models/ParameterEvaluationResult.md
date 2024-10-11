# ParameterEvaluationResult

Represents the validity of a parameter against the configured constraints.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**result** | ValidationResult | Yes |  |
**evaluated_constraints** | List[ParameterEvaluatedConstraint] | Yes |  |
**required** | pydantic.StrictBool | Yes | Represents whether the parameter is a required input to the action. |


[[Back to Model list]](../../../../README.md#models-v1-link) [[Back to API list]](../../../../README.md#apis-v1-link) [[Back to README]](../../../../README.md)
