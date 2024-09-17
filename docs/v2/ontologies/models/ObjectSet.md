# ObjectSet

Represents the definition of an `ObjectSet` in the `Ontology`.

This is a discriminator type and does not contain any fields. Instead, it is a union
of of the models listed below.

This discriminator class uses the `type` field to differentiate between classes.

| Class | Value
| ------------ | -------------
ObjectSetReferenceType | reference
ObjectSetFilterType | filter
ObjectSetSearchAroundType | searchAround
ObjectSetStaticType | static
ObjectSetIntersectionType | intersect
ObjectSetSubtractType | subtract
ObjectSetUnionType | union
ObjectSetBaseType | base


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
