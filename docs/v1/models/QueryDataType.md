# QueryDataType

A union of all the types supported by Ontology Query parameters or outputs.


This is a discriminator type and does not contain any fields. Instead, it is a union
of of the models listed below.

This discriminator class uses the `type` field to differentiate between classes.

| Class | Value
| ------------ | -------------
[QueryArrayType](QueryArrayType.md) | array
[AttachmentType](AttachmentType.md) | attachment
[BooleanType](BooleanType.md) | boolean
[DateType](DateType.md) | date
[DoubleType](DoubleType.md) | double
[FloatType](FloatType.md) | float
[IntegerType](IntegerType.md) | integer
[LongType](LongType.md) | long
[OntologyObjectSetType](OntologyObjectSetType.md) | objectSet
[OntologyObjectType](OntologyObjectType.md) | object
[QuerySetType](QuerySetType.md) | set
[StringType](StringType.md) | string
[QueryStructType](QueryStructType.md) | struct
[ThreeDimensionalAggregation](ThreeDimensionalAggregation.md) | threeDimensionalAggregation
[TimestampType](TimestampType.md) | timestamp
[TwoDimensionalAggregation](TwoDimensionalAggregation.md) | twoDimensionalAggregation
[QueryUnionType](QueryUnionType.md) | union
[NullType](NullType.md) | null
[UnsupportedType](UnsupportedType.md) | unsupported


[[Back to Model list]](../../../README.md#models-v1-link) [[Back to API list]](../../../README.md#apis-v1-link) [[Back to README]](../../../README.md)
