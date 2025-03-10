# ContainsAllTermsInOrderPrefixLastTerm

Returns objects where the specified field contains all of the terms in the order provided, 
but they do have to be adjacent to each other.
The last term can be a partial prefix match. Allows you to specify a property to query on
by a variety of means. Either `field` or `propertyIdentifier` can be supplied, but not both.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**field** | typing.Optional[PropertyApiName] | No |  |
**property_identifier** | typing.Optional[PropertyIdentifier] | No |  |
**value** | str | Yes |  |
**type** | typing.Literal["containsAllTermsInOrderPrefixLastTerm"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
