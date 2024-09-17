# AllTermsQueryDict

Returns objects where the specified field contains all of the whitespace separated words in any
order in the provided value. This query supports fuzzy matching.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**field** | FieldNameV1 | Yes |  |
**value** | StrictStr | Yes |  |
**fuzzy** | NotRequired[Fuzzy] | No |  |
**type** | Literal["allTerms"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v1-link) [[Back to API list]](../../../../README.md#apis-v1-link) [[Back to README]](../../../../README.md)