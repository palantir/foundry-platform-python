# AnyTermQueryDict

Returns objects where the specified field contains any of the whitespace separated words in any 
order in the provided value. This query supports fuzzy matching.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**field** | FieldNameV1 | Yes |  |
**value** | StrictStr | Yes |  |
**fuzzy** | NotRequired[Fuzzy] | No |  |
**type** | Literal["anyTerm"] | Yes | None |


[[Back to Model list]](../../../README.md#models-v1-link) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to README]](../../../README.md)
