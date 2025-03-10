# ActionParameterTypeDict

A union of all the types supported by Ontology Action parameters.


This is a discriminator type and does not contain any fields. Instead, it is a union
of of the models listed below.

This discriminator class uses the `type` field to differentiate between classes.

| Class | Value
| ------------ | -------------
core_models.DateTypeDict | date
OntologyInterfaceObjectTypeDict | interfaceObject
OntologyStructTypeDict | struct
core_models.StringTypeDict | string
core_models.DoubleTypeDict | double
core_models.IntegerTypeDict | integer
core_models.LongTypeDict | long
OntologyObjectTypeReferenceTypeDict | objectType
core_models.BooleanTypeDict | boolean
core_models.MarkingTypeDict | marking
core_models.AttachmentTypeDict | attachment
core_models.MediaReferenceTypeDict | mediaReference
ActionParameterArrayTypeDict | array
OntologyObjectSetTypeDict | objectSet
OntologyObjectTypeDict | object
core_models.TimestampTypeDict | timestamp


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
