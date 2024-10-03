# ObjectSetDict

Represents the definition of an `ObjectSet` in the `Ontology`.

This is a discriminator type and does not contain any fields. Instead, it is a union
of of the models listed below.

This discriminator class uses the `type` field to differentiate between classes.

| Class | Value
| ------------ | -------------
ObjectSetReferenceTypeDict | reference
ObjectSetFilterTypeDict | filter
ObjectSetSearchAroundTypeDict | searchAround
ObjectSetInterfaceBaseTypeDict | interfaceBase
ObjectSetStaticTypeDict | static
ObjectSetIntersectionTypeDict | intersect
ObjectSetAsBaseObjectTypesTypeDict | asBaseObjectTypes
ObjectSetSubtractTypeDict | subtract
ObjectSetUnionTypeDict | union
ObjectSetAsTypeTypeDict | asType
ObjectSetBaseTypeDict | base


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
