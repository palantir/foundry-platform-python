# SearchJsonQueryDict

SearchJsonQuery

This is a discriminator type and does not contain any fields. Instead, it is a union
of of the models listed below.

This discriminator class uses the `type` field to differentiate between classes.

| Class | Value
| ------------ | -------------
OrQueryDict | or
PrefixQueryDict | prefix
LtQueryDict | lt
AllTermsQueryDict | allTerms
EqualsQueryDict | eq
GtQueryDict | gt
ContainsQueryDict | contains
NotQueryDict | not
PhraseQueryDict | phrase
AndQueryDict | and
IsNullQueryDict | isNull
GteQueryDict | gte
AnyTermQueryDict | anyTerm
LteQueryDict | lte


[[Back to Model list]](../../../../README.md#models-v1-link) [[Back to API list]](../../../../README.md#apis-v1-link) [[Back to README]](../../../../README.md)
