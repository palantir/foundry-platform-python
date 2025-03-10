# QueryDataType

A union of all the types supported by Ontology Query parameters or outputs.


This is a discriminator type and does not contain any fields. Instead, it is a union
of of the models listed below.

This discriminator class uses the `type` field to differentiate between classes.

| Class | Value
| ------------ | -------------
core_models.DateType | date
QueryStructType | struct
QuerySetType | set
core_models.StringType | string
EntrySetType | entrySet
core_models.DoubleType | double
core_models.IntegerType | integer
ThreeDimensionalAggregation | threeDimensionalAggregation
QueryUnionType | union
core_models.FloatType | float
core_models.LongType | long
core_models.BooleanType | boolean
core_models.UnsupportedType | unsupported
core_models.AttachmentType | attachment
core_models.NullType | null
QueryArrayType | array
OntologyObjectSetType | objectSet
TwoDimensionalAggregation | twoDimensionalAggregation
OntologyObjectType | object
core_models.TimestampType | timestamp


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
