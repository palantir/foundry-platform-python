# SearchJsonQuery

SearchJsonQuery

This is a discriminator type and does not contain any fields. Instead, it is a union
of of the models listed below.

This discriminator class uses the `type` field to differentiate between classes.

| Class | Value
| ------------ | -------------
[LtQuery](LtQuery.md) | lt
[GtQuery](GtQuery.md) | gt
[LteQuery](LteQuery.md) | lte
[GteQuery](GteQuery.md) | gte
[EqualsQuery](EqualsQuery.md) | eq
[IsNullQuery](IsNullQuery.md) | isNull
[ContainsQuery](ContainsQuery.md) | contains
[AndQuery](AndQuery.md) | and
[OrQuery](OrQuery.md) | or
[NotQuery](NotQuery.md) | not
[PrefixQuery](PrefixQuery.md) | prefix
[PhraseQuery](PhraseQuery.md) | phrase
[AnyTermQuery](AnyTermQuery.md) | anyTerm
[AllTermsQuery](AllTermsQuery.md) | allTerms


[[Back to Model list]](../../../README.md#models-v1-link) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to README]](../../../README.md)
