# ParameterConstraintValue

The source of a constraint bound value: either a literal or a reference to another parameter that is
resolved when the action is validated or applied.


This is a discriminator type and does not contain any fields. Instead, it is a union
of of the models listed below.

This discriminator class uses the `type` field to differentiate between classes.

| Class | Value
| ------------ | -------------
StaticConstraintValue | static
ParameterLengthConstraintValue | parameterLength
ParameterValueConstraintValue | parameterValue


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
