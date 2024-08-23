# SearchJsonQueryDict

SearchJsonQuery

This is a discriminator type and does not contain any fields. Instead, it is a union
of of the models listed below.

This discriminator class uses the `type` field to differentiate between classes.

| Class | Value
| ------------ | -------------
[LtQueryDict](LtQueryDict.md) | lt
[GtQueryDict](GtQueryDict.md) | gt
[LteQueryDict](LteQueryDict.md) | lte
[GteQueryDict](GteQueryDict.md) | gte
[EqualsQueryDict](EqualsQueryDict.md) | eq
[IsNullQueryDict](IsNullQueryDict.md) | isNull
[ContainsQueryDict](ContainsQueryDict.md) | contains
[AndQueryDict](AndQueryDict.md) | and
[OrQueryDict](OrQueryDict.md) | or
[NotQueryDict](NotQueryDict.md) | not
[PrefixQueryDict](PrefixQueryDict.md) | prefix
[PhraseQueryDict](PhraseQueryDict.md) | phrase
[AnyTermQueryDict](AnyTermQueryDict.md) | anyTerm
[AllTermsQueryDict](AllTermsQueryDict.md) | allTerms


[[Back to Model list]](../../../README.md#models-v2-link) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to README]](../../../README.md)
