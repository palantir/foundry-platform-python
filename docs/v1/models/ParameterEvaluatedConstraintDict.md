# ParameterEvaluatedConstraintDict

A constraint that an action parameter value must satisfy in order to be considered valid.
Constraints can be configured on action parameters in the **Ontology Manager**. 
Applicable constraints are determined dynamically based on parameter inputs. 
Parameter values are evaluated against the final set of constraints.

The type of the constraint.
| Type                  | Description                                                                                                                                                                                                                     |
|-----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `arraySize`           | The parameter expects an array of values and the size of the array must fall within the defined range.                                                                                                                          |
| `groupMember`         | The parameter value must be the user id of a member belonging to at least one of the groups defined by the constraint.                                                                                                          |
| `objectPropertyValue` | The parameter value must be a property value of an object found within an object set.                                                                                                                                           |
| `objectQueryResult`   | The parameter value must be the primary key of an object found within an object set.                                                                                                                                            |
| `oneOf`               | The parameter has a manually predefined set of options.                                                                                                                                                                         |
| `range`               | The parameter value must be within the defined range.                                                                                                                                                                           |
| `stringLength`        | The parameter value must have a length within the defined range.                                                                                                                                                                |
| `stringRegexMatch`    | The parameter value must match a predefined regular expression.                                                                                                                                                                 |
| `unevaluable`         | The parameter cannot be evaluated because it depends on another parameter or object set that can't be evaluated. This can happen when a parameter's allowed values are defined by another parameter that is missing or invalid. |


This is a discriminator type and does not contain any fields. Instead, it is a union
of of the models listed below.

This discriminator class uses the `type` field to differentiate between classes.

| Class | Value
| ------------ | -------------
[ArraySizeConstraintDict](ArraySizeConstraintDict.md) | arraySize
[GroupMemberConstraintDict](GroupMemberConstraintDict.md) | groupMember
[ObjectPropertyValueConstraintDict](ObjectPropertyValueConstraintDict.md) | objectPropertyValue
[ObjectQueryResultConstraintDict](ObjectQueryResultConstraintDict.md) | objectQueryResult
[OneOfConstraintDict](OneOfConstraintDict.md) | oneOf
[RangeConstraintDict](RangeConstraintDict.md) | range
[StringLengthConstraintDict](StringLengthConstraintDict.md) | stringLength
[StringRegexMatchConstraintDict](StringRegexMatchConstraintDict.md) | stringRegexMatch
[UnevaluableConstraintDict](UnevaluableConstraintDict.md) | unevaluable


[[Back to Model list]](../../../README.md#models-v1-link) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
