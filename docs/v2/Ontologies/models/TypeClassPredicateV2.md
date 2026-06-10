# TypeClassPredicateV2

A predicate for matching type classes. Matches a type class when `kind`, and `name` if provided, match the
corresponding attribute of the type class. If `name` is empty, only `kind` is required to match. You can
search for both parameter type classes and action type type classes.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**kind** | str | Yes | Exact match predicate for the `kind` attribute of a type class. |
**name** | Optional[str] | No | Exact match predicate for the `name` attribute of a type class. |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
