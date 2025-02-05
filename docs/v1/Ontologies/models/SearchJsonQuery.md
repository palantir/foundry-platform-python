# SearchJsonQuery

SearchJsonQuery

This is a discriminator type and does not contain any fields. Instead, it is a union
of of the models listed below.

This discriminator class uses the `type` field to differentiate between classes.

| Class | Value
| ------------ | -------------
OrQuery | or
PrefixQuery | prefix
LtQuery | lt
AllTermsQuery | allTerms
EqualsQuery | eq
GtQuery | gt
ContainsQuery | contains
NotQuery | not
PhraseQuery | phrase
AndQuery | and
IsNullQuery | isNull
GteQuery | gte
AnyTermQuery | anyTerm
LteQuery | lte


[[Back to Model list]](../../../../README.md#models-v1-link) [[Back to API list]](../../../../README.md#apis-v1-link) [[Back to README]](../../../../README.md)
