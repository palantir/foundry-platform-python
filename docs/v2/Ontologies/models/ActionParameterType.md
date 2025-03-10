# ActionParameterType

A union of all the types supported by Ontology Action parameters.


This is a discriminator type and does not contain any fields. Instead, it is a union
of of the models listed below.

This discriminator class uses the `type` field to differentiate between classes.

| Class | Value
| ------------ | -------------
core_models.DateType | date
OntologyInterfaceObjectType | interfaceObject
OntologyStructType | struct
core_models.StringType | string
core_models.DoubleType | double
core_models.IntegerType | integer
core_models.LongType | long
OntologyObjectTypeReferenceType | objectType
core_models.BooleanType | boolean
core_models.MarkingType | marking
core_models.AttachmentType | attachment
core_models.MediaReferenceType | mediaReference
ActionParameterArrayType | array
OntologyObjectSetType | objectSet
OntologyObjectType | object
core_models.TimestampType | timestamp


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
