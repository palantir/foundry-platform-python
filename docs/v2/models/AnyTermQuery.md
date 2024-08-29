# AnyTermQuery

Returns objects where the specified field contains any of the whitespace separated words in any 
order in the provided value. This query supports fuzzy matching.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**field** | FieldNameV1 | Yes |  |
**value** | StrictStr | Yes |  |
**fuzzy** | Optional[Fuzzy] | No |  |
**type** | Literal["anyTerm"] | Yes | None |


[[Back to Model list]](../../../README.md#models-v2-link) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to README]](../../../README.md)