# ObjectSetDict

Represents the definition of an `ObjectSet` in the `Ontology`.

This is a discriminator type and does not contain any fields. Instead, it is a union
of of the models listed below.

This discriminator class uses the `type` field to differentiate between classes.

| Class | Value
| ------------ | -------------
[ObjectSetBaseTypeDict](ObjectSetBaseTypeDict.md) | base
[ObjectSetStaticTypeDict](ObjectSetStaticTypeDict.md) | static
[ObjectSetReferenceTypeDict](ObjectSetReferenceTypeDict.md) | reference
[ObjectSetFilterTypeDict](ObjectSetFilterTypeDict.md) | filter
[ObjectSetUnionTypeDict](ObjectSetUnionTypeDict.md) | union
[ObjectSetIntersectionTypeDict](ObjectSetIntersectionTypeDict.md) | intersect
[ObjectSetSubtractTypeDict](ObjectSetSubtractTypeDict.md) | subtract
[ObjectSetSearchAroundTypeDict](ObjectSetSearchAroundTypeDict.md) | searchAround


[[Back to Model list]](../../../README.md#models-v1-link) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to README]](../../../README.md)
