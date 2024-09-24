# QueryDataTypeDict

A union of all the types supported by Query parameters or outputs.


This is a discriminator type and does not contain any fields. Instead, it is a union
of of the models listed below.

This discriminator class uses the `type` field to differentiate between classes.

| Class | Value
| ------------ | -------------
DateTypeDict | date
QueryStructTypeDict | struct
QuerySetTypeDict | set
StringTypeDict | string
DoubleTypeDict | double
IntegerTypeDict | integer
ThreeDimensionalAggregationDict | threeDimensionalAggregation
QueryUnionTypeDict | union
FloatTypeDict | float
LongTypeDict | long
BooleanTypeDict | boolean
UnsupportedTypeDict | unsupported
AttachmentTypeDict | attachment
NullTypeDict | null
QueryArrayTypeDict | array
TwoDimensionalAggregationDict | twoDimensionalAggregation
TimestampTypeDict | timestamp


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
