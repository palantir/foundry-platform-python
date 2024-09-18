# QueryDataType

A union of all the types supported by Ontology Query parameters or outputs.


This is a discriminator type and does not contain any fields. Instead, it is a union
of of the models listed below.

This discriminator class uses the `type` field to differentiate between classes.

| Class | Value
| ------------ | -------------
DateType | date
QueryStructType | struct
QuerySetType | set
StringType | string
DoubleType | double
IntegerType | integer
ThreeDimensionalAggregation | threeDimensionalAggregation
QueryUnionType | union
FloatType | float
LongType | long
BooleanType | boolean
UnsupportedType | unsupported
AttachmentType | attachment
NullType | null
QueryArrayType | array
OntologyObjectSetType | objectSet
TwoDimensionalAggregation | twoDimensionalAggregation
OntologyObjectType | object
TimestampType | timestamp


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
