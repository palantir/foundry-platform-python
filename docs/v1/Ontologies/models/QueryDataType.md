# QueryDataType

A union of all the types supported by Ontology Query parameters or outputs.


This is a discriminator type and does not contain any fields. Instead, it is a union
of of the models listed below.

This discriminator class uses the `type` field to differentiate between classes.

| Class | Value
| ------------ | -------------
DateType | date
OntologyInterfaceObjectType | interfaceObject
QueryStructType | struct
QuerySetType | set
VoidType | void
StringType | string
EntrySetType | entrySet
DoubleType | double
IntegerType | integer
ThreeDimensionalAggregation | threeDimensionalAggregation
QueryUnionType | union
FloatType | float
LongType | long
BooleanType | boolean
UnsupportedType | unsupported
AttachmentType | attachment
MediaReferenceType | mediaReference
NullType | null
QueryArrayType | array
OntologyObjectSetType | objectSet
TwoDimensionalAggregation | twoDimensionalAggregation
OntologyInterfaceObjectSetType | interfaceObjectSet
OntologyObjectType | object
TimestampType | timestamp


[[Back to Model list]](../../../../README.md#models-v1-link) [[Back to API list]](../../../../README.md#apis-v1-link) [[Back to README]](../../../../README.md)
