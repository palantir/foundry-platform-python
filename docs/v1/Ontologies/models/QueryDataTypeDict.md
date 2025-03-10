# QueryDataTypeDict

A union of all the types supported by Ontology Query parameters or outputs.


This is a discriminator type and does not contain any fields. Instead, it is a union
of of the models listed below.

This discriminator class uses the `type` field to differentiate between classes.

| Class | Value
| ------------ | -------------
core_models.DateTypeDict | date
QueryStructTypeDict | struct
QuerySetTypeDict | set
core_models.StringTypeDict | string
EntrySetTypeDict | entrySet
core_models.DoubleTypeDict | double
core_models.IntegerTypeDict | integer
ThreeDimensionalAggregationDict | threeDimensionalAggregation
QueryUnionTypeDict | union
core_models.FloatTypeDict | float
core_models.LongTypeDict | long
core_models.BooleanTypeDict | boolean
core_models.UnsupportedTypeDict | unsupported
core_models.AttachmentTypeDict | attachment
core_models.NullTypeDict | null
QueryArrayTypeDict | array
OntologyObjectSetTypeDict | objectSet
TwoDimensionalAggregationDict | twoDimensionalAggregation
OntologyObjectTypeDict | object
core_models.TimestampTypeDict | timestamp


[[Back to Model list]](../../../../README.md#models-v1-link) [[Back to API list]](../../../../README.md#apis-v1-link) [[Back to README]](../../../../README.md)
