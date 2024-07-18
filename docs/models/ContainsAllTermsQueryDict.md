# ContainsAllTermsQueryDict

Returns objects where the specified field contains all of the whitespace separated words in any
order in the provided value. This query supports fuzzy matching.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**field** | PropertyApiName | Yes |  |
**fuzzy** | NotRequired[FuzzyV2] | No |  |
**type** | Literal["containsAllTerms"] | Yes | None |
**value** | StrictStr | Yes |  |


[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
