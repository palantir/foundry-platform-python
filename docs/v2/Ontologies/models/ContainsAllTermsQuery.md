# ContainsAllTermsQuery

Returns objects where the specified field contains all of the whitespace separated words in any
order in the provided value. This query supports fuzzy matching. Allows you to specify a property to query on 
by a variety of means. Either `field` or `propertyIdentifier` must be supplied, but not both.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**field** | typing.Optional[PropertyApiName] | No |  |
**property_identifier** | typing.Optional[PropertyIdentifier] | No |  |
**value** | str | Yes |  |
**fuzzy** | typing.Optional[FuzzyV2] | No |  |
**type** | typing.Literal["containsAllTerms"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
