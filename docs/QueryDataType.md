# QueryDataType

A union of all the types supported by Ontology Query parameters or outputs.

This is a discriminator class and does not contain any additional fields. Instead, it
is a union of of the classes listed below.

This discriminator class uses the `type` field to differentiate between classes.

Class | Value
------------ | -------------
[QueryArrayType](QueryArrayType.md) | array
[AttachmentType](AttachmentType.md) | attachment
[BooleanType](BooleanType.md) | boolean
[DateType](DateType.md) | date
[DoubleType](DoubleType.md) | double
[FloatType](FloatType.md) | float
[IntegerType](IntegerType.md) | integer
[LongType](LongType.md) | long
[NullType](NullType.md) | null
[OntologyObjectType](OntologyObjectType.md) | object
[OntologyObjectSetType](OntologyObjectSetType.md) | objectSet
[QuerySetType](QuerySetType.md) | set
[StringType](StringType.md) | string
[QueryStructType](QueryStructType.md) | struct
[ThreeDimensionalAggregation](ThreeDimensionalAggregation.md) | threeDimensionalAggregation
[TimestampType](TimestampType.md) | timestamp
[TwoDimensionalAggregation](TwoDimensionalAggregation.md) | twoDimensionalAggregation
[QueryUnionType](QueryUnionType.md) | union
[UnsupportedType](UnsupportedType.md) | unsupported

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
