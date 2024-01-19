# OntologyDataType

A union of all the primitive types used by Palantir's Ontology-based products.

This is a discriminator class and does not contain any additional fields. Instead, it
is a union of of the classes listed below.

This discriminator class uses the `type` field to differentiate between classes.

Class | Value
------------ | -------------
[AnyType](AnyType.md) | any
[OntologyArrayType](OntologyArrayType.md) | array
[BinaryType](BinaryType.md) | binary
[BooleanType](BooleanType.md) | boolean
[ByteType](ByteType.md) | byte
[DateType](DateType.md) | date
[DecimalType](DecimalType.md) | decimal
[DoubleType](DoubleType.md) | double
[FloatType](FloatType.md) | float
[IntegerType](IntegerType.md) | integer
[LongType](LongType.md) | long
[OntologyMapType](OntologyMapType.md) | map
[OntologyObjectType](OntologyObjectType.md) | object
[OntologyObjectSetType](OntologyObjectSetType.md) | objectSet
[OntologySetType](OntologySetType.md) | set
[ShortType](ShortType.md) | short
[StringType](StringType.md) | string
[OntologyStructType](OntologyStructType.md) | struct
[TimestampType](TimestampType.md) | timestamp
[UnsupportedType](UnsupportedType.md) | unsupported

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
