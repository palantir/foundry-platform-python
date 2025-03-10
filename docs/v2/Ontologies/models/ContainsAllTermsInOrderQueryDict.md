# ContainsAllTermsInOrderQueryDict

Returns objects where the specified field contains all of the terms in the order provided,
but they do have to be adjacent to each other. Allows you to specify a property to query on
by a variety of means. Either `field` or `propertyIdentifier` must be supplied, but not both.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**field** | typing_extensions.NotRequired[PropertyApiName] | No |  |
**propertyIdentifier** | typing_extensions.NotRequired[PropertyIdentifierDict] | No |  |
**value** | str | Yes |  |
**type** | Literal["containsAllTermsInOrder"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
