# OntologyDataTypeDict

A union of all the primitive types used by Palantir's Ontology-based products.


This is a discriminator type and does not contain any fields. Instead, it is a union
of of the models listed below.

This discriminator class uses the `type` field to differentiate between classes.

| Class | Value
| ------------ | -------------
core_models.DateTypeDict | date
OntologyStructTypeDict | struct
OntologySetTypeDict | set
core_models.StringTypeDict | string
core_models.ByteTypeDict | byte
core_models.DoubleTypeDict | double
core_models.IntegerTypeDict | integer
core_models.FloatTypeDict | float
core_models.AnyTypeDict | any
core_models.LongTypeDict | long
core_models.BooleanTypeDict | boolean
core_models.CipherTextTypeDict | cipherText
core_models.MarkingTypeDict | marking
core_models.UnsupportedTypeDict | unsupported
OntologyArrayTypeDict | array
OntologyObjectSetTypeDict | objectSet
core_models.BinaryTypeDict | binary
core_models.ShortTypeDict | short
core_models.DecimalTypeDict | decimal
OntologyMapTypeDict | map
core_models.TimestampTypeDict | timestamp
OntologyObjectTypeDict | object


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
