# AnyTermQueryRequest

Returns objects where the specified field contains any of the whitespace separated words in any 
order in the provided value. This query supports fuzzy matching.


## Properties
Name | Type | Required | Description |
------------ | ------------- | ------------- | ------------- |
**field** | StrictStr | Yes | None |
**value** | StrictStr | Yes | None |
**fuzzy** | Fuzzy | No | Setting fuzzy to `true` allows approximate matching in search queries that support it. |
**type** | Literal["anyTerm"] | Yes | None |


[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
