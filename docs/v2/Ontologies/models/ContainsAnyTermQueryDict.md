# ContainsAnyTermQueryDict

Returns objects where the specified field contains any of the whitespace separated words in any 
order in the provided value. This query supports fuzzy matching. Allows you to specify a property to query on
by a variety of means. Either `field` or `propertyIdentifier` must be supplied, but not both.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**field** | NotRequired[PropertyApiName] | No |  |
**propertyIdentifier** | NotRequired[PropertyIdentifierDict] | No |  |
**value** | str | Yes |  |
**fuzzy** | NotRequired[FuzzyV2] | No |  |
**type** | Literal["containsAnyTerm"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
