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
StringType | string
IntegerType | integer
ThreeDimensionalAggregation | threeDimensionalAggregation
FloatType | float
LongType | long
UnsupportedType | unsupported
AttachmentType | attachment
QueryArrayType | array
OntologyObjectSetType | objectSet
TwoDimensionalAggregation | twoDimensionalAggregation
QueryTypeReferenceType | typeReference
TimestampType | timestamp
QuerySetType | set
VoidType | void
EntrySetType | entrySet
DoubleType | double
QueryUnionType | union
BooleanType | boolean
MediaReferenceType | mediaReference
NullType | null
OntologyInterfaceObjectSetType | interfaceObjectSet
OntologyObjectType | object


[[Back to Model list]](../../../../README.md#models-v1-link) [[Back to API list]](../../../../README.md#apis-v1-link) [[Back to README]](../../../../README.md)
