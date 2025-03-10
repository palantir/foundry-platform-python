# OntologyDataType

A union of all the primitive types used by Palantir's Ontology-based products.


This is a discriminator type and does not contain any fields. Instead, it is a union
of of the models listed below.

This discriminator class uses the `type` field to differentiate between classes.

| Class | Value
| ------------ | -------------
core_models.DateType | date
OntologyStructType | struct
OntologySetType | set
core_models.StringType | string
core_models.ByteType | byte
core_models.DoubleType | double
core_models.IntegerType | integer
core_models.FloatType | float
core_models.AnyType | any
core_models.LongType | long
core_models.BooleanType | boolean
core_models.CipherTextType | cipherText
core_models.MarkingType | marking
core_models.UnsupportedType | unsupported
OntologyArrayType | array
OntologyObjectSetType | objectSet
core_models.BinaryType | binary
core_models.ShortType | short
core_models.DecimalType | decimal
OntologyMapType | map
core_models.TimestampType | timestamp
OntologyObjectType | object


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
