# PipelineBuilderLiteral

A typed pipeline parameter literal. Arrays and maps contain tagged literal JSON with the same variants and value formats, recursively. A null literal uses the `empty` variant rather than a JSON null value.

This is a discriminator type and does not contain any fields. Instead, it is a union
of of the models listed below.

This discriminator class uses the `type` field to differentiate between classes.

| Class | Value
| ------------ | -------------
PipelineBuilderLiteralArray | array
PipelineBuilderLiteralBinary | binary
PipelineBuilderLiteralBoolean | boolean
PipelineBuilderLiteralDate | date
PipelineBuilderLiteralDatetime | datetime
PipelineBuilderLiteralDecimal | decimal
PipelineBuilderLiteralDouble | double
PipelineBuilderLiteralEmpty | empty
PipelineBuilderLiteralInteger | integer
PipelineBuilderLiteralLong | long
PipelineBuilderLiteralMap | map
PipelineBuilderLiteralString | string


[[Back to Model list]](../../../../README.md#models-v3-link) [[Back to API list]](../../../../README.md#apis-v3-link) [[Back to README]](../../../../README.md)
