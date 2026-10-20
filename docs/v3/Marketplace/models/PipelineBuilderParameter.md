# PipelineBuilderParameter

A literal, regular expression, or enum value matching the parameter requested by the product.

This is a discriminator type and does not contain any fields. Instead, it is a union
of of the models listed below.

This discriminator class uses the `type` field to differentiate between classes.

| Class | Value
| ------------ | -------------
PipelineBuilderParameterEnum | enum
PipelineBuilderParameterLiteral | literal
PipelineBuilderParameterRegex | regex


[[Back to Model list]](../../../../README.md#models-v3-link) [[Back to API list]](../../../../README.md#apis-v3-link) [[Back to README]](../../../../README.md)
