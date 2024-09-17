# OntologyDataTypeDict

A union of all the primitive types used by Palantir's Ontology-based products.


This is a discriminator type and does not contain any fields. Instead, it is a union
of of the models listed below.

This discriminator class uses the `type` field to differentiate between classes.

| Class | Value
| ------------ | -------------
DateTypeDict | date
OntologyStructTypeDict | struct
OntologySetTypeDict | set
StringTypeDict | string
ByteTypeDict | byte
DoubleTypeDict | double
IntegerTypeDict | integer
FloatTypeDict | float
AnyTypeDict | any
LongTypeDict | long
BooleanTypeDict | boolean
MarkingTypeDict | marking
UnsupportedTypeDict | unsupported
OntologyArrayTypeDict | array
OntologyObjectSetTypeDict | objectSet
BinaryTypeDict | binary
ShortTypeDict | short
DecimalTypeDict | decimal
OntologyMapTypeDict | map
TimestampTypeDict | timestamp
OntologyObjectTypeDict | object


[[Back to Model list]](../../../../README.md#models-v1-link) [[Back to API list]](../../../../README.md#apis-v1-link) [[Back to README]](../../../../README.md)
