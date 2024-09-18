# OntologyDataType

A union of all the primitive types used by Palantir's Ontology-based products.


This is a discriminator type and does not contain any fields. Instead, it is a union
of of the models listed below.

This discriminator class uses the `type` field to differentiate between classes.

| Class | Value
| ------------ | -------------
DateType | date
OntologyStructType | struct
OntologySetType | set
StringType | string
ByteType | byte
DoubleType | double
IntegerType | integer
FloatType | float
AnyType | any
LongType | long
BooleanType | boolean
MarkingType | marking
UnsupportedType | unsupported
OntologyArrayType | array
OntologyObjectSetType | objectSet
BinaryType | binary
ShortType | short
DecimalType | decimal
OntologyMapType | map
TimestampType | timestamp
OntologyObjectType | object


[[Back to Model list]](../../../../README.md#models-v1-link) [[Back to API list]](../../../../README.md#apis-v1-link) [[Back to README]](../../../../README.md)
