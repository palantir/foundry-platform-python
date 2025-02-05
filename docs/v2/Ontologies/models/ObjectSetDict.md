# ObjectSetDict

Represents the definition of an `ObjectSet` in the ontology.

This is a discriminator type and does not contain any fields. Instead, it is a union
of of the models listed below.

This discriminator class uses the `type` field to differentiate between classes.

| Class | Value
| ------------ | -------------
ObjectSetSearchAroundTypeDict | searchAround
ObjectSetStaticTypeDict | static
ObjectSetIntersectionTypeDict | intersect
ObjectSetWithPropertiesTypeDict | withProperties
ObjectSetSubtractTypeDict | subtract
ObjectSetNearestNeighborsTypeDict | nearestNeighbors
ObjectSetUnionTypeDict | union
ObjectSetAsTypeTypeDict | asType
ObjectSetMethodInputTypeDict | methodInput
ObjectSetReferenceTypeDict | reference
ObjectSetFilterTypeDict | filter
ObjectSetInterfaceBaseTypeDict | interfaceBase
ObjectSetAsBaseObjectTypesTypeDict | asBaseObjectTypes
ObjectSetBaseTypeDict | base


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
