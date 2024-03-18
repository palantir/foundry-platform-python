# SearchJsonQueryRequest

SearchJsonQueryRequest

This is a discriminator type and does not contain any fields. Instead, it is a union
of of the models listed below.

This discriminator class uses the `type` field to differentiate between classes.

Class | Value
------------ | -------------
[LtQueryRequest](LtQueryRequest.md) | lt
[GtQueryRequest](GtQueryRequest.md) | gt
[LteQueryRequest](LteQueryRequest.md) | lte
[GteQueryRequest](GteQueryRequest.md) | gte
[EqualsQueryRequest](EqualsQueryRequest.md) | eq
[IsNullQueryRequest](IsNullQueryRequest.md) | isNull
[ContainsQueryRequest](ContainsQueryRequest.md) | contains
[AndQueryRequest](AndQueryRequest.md) | and
[OrQueryRequest](OrQueryRequest.md) | or
[NotQueryRequest](NotQueryRequest.md) | not
[PrefixQueryRequest](PrefixQueryRequest.md) | prefix
[PhraseQueryRequest](PhraseQueryRequest.md) | phrase
[AnyTermQueryRequest](AnyTermQueryRequest.md) | anyTerm
[AllTermsQueryRequest](AllTermsQueryRequest.md) | allTerms


[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
