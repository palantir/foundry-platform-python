# ParameterValue

A typed parameter value for SQL query execution.

This is a discriminator type and does not contain any fields. Instead, it is a union
of of the models listed below.

This discriminator class uses the `type` field to differentiate between classes.

| Class | Value
| ------------ | -------------
ParameterDateValue | date
ParameterStructValue | struct
ParameterStringValue | string
ParameterDoubleValue | double
ParameterIntegerValue | integer
ParameterFloatValue | float
ParameterListValue | list
ParameterAnyValue | any
ParameterLongValue | long
ParameterBooleanValue | boolean
ParameterNullValue | null
ParameterBinaryValue | binary
ParameterShortValue | short
ParameterDecimalValue | decimal
ParameterMapValue | map
ParameterTimestampValue | timestamp


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
