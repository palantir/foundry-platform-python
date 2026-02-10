# StructFieldEvaluatedConstraint

A constraint that an action struct parameter field value must satisfy in order to be considered valid.
Constraints can be configured on fields of struct parameters in the **Ontology Manager**. 
Applicable constraints are determined dynamically based on parameter inputs. 
Parameter values are evaluated against the final set of constraints.

The type of the constraint.
| Type                  | Description                                                                                                                                                                                                                     |
|-----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `oneOf`               | The struct parameter field has a manually predefined set of options.                                                                                                                                                            |
| `range`               | The struct parameter field value must be within the defined range.                                                                                                                                                              |
| `stringLength`        | The struct parameter field value must have a length within the defined range.                                                                                                                                                   |
| `stringRegexMatch`    | The struct parameter field value must match a predefined regular expression.                                                                                                                                                    |
| `objectQueryResult`   | The struct parameter field value must be the primary key of an object found within an object set.                                                                                                                               |


This is a discriminator type and does not contain any fields. Instead, it is a union
of of the models listed below.

This discriminator class uses the `type` field to differentiate between classes.

| Class | Value
| ------------ | -------------
OneOfConstraint | oneOf
RangeConstraint | range
ObjectQueryResultConstraint | objectQueryResult
StringLengthConstraint | stringLength
StringRegexMatchConstraint | stringRegexMatch


[[Back to Model list]](../../../../README.md#models-v1-link) [[Back to API list]](../../../../README.md#apis-v1-link) [[Back to README]](../../../../README.md)
