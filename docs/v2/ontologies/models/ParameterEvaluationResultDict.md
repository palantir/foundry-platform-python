# ParameterEvaluationResultDict

Represents the validity of a parameter against the configured constraints.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**result** | ValidationResult | Yes |  |
**evaluatedConstraints** | List[ParameterEvaluatedConstraintDict] | Yes |  |
**required** | pydantic.StrictBool | Yes | Represents whether the parameter is a required input to the action. |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
