# ObjectSet

Represents the definition of an `ObjectSet` in the `Ontology`.

This is a discriminator type and does not contain any fields. Instead, it is a union
of of the models listed below.

This discriminator class uses the `type` field to differentiate between classes.

| Class | Value
| ------------ | -------------
[ObjectSetBaseType](ObjectSetBaseType.md) | base
[ObjectSetStaticType](ObjectSetStaticType.md) | static
[ObjectSetReferenceType](ObjectSetReferenceType.md) | reference
[ObjectSetFilterType](ObjectSetFilterType.md) | filter
[ObjectSetUnionType](ObjectSetUnionType.md) | union
[ObjectSetIntersectionType](ObjectSetIntersectionType.md) | intersect
[ObjectSetSubtractType](ObjectSetSubtractType.md) | subtract
[ObjectSetSearchAroundType](ObjectSetSearchAroundType.md) | searchAround


[[Back to Model list]](../../../README.md#models-v2-link) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to README]](../../../README.md)
