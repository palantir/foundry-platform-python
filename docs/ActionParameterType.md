# ActionParameterType

A union of all the types supported by Ontology Action parameters.

This is a discriminator class and does not contain any additional fields. Instead, it
is a union of of the classes listed below.

This discriminator class uses the `type` field to differentiate between classes.

Class | Value
------------ | -------------
[ActionParameterArrayType](ActionParameterArrayType.md) | array
[AttachmentType](AttachmentType.md) | attachment
[BooleanType](BooleanType.md) | boolean
[DateType](DateType.md) | date
[DoubleType](DoubleType.md) | double
[IntegerType](IntegerType.md) | integer
[LongType](LongType.md) | long
[OntologyObjectType](OntologyObjectType.md) | object
[OntologyObjectSetType](OntologyObjectSetType.md) | objectSet
[StringType](StringType.md) | string
[TimestampType](TimestampType.md) | timestamp

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
