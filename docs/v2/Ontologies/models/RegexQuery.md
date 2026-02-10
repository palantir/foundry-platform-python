# RegexQuery

Returns objects where the specified field matches the regex pattern provided. This applies to the non-analyzed
form of text fields and supports standard regex syntax of dot (.), star(*) and question mark(?).
Either `field` or `propertyIdentifier` can be supplied, but not both.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**field** | Optional[PropertyApiName] | No |  |
**property_identifier** | Optional[PropertyIdentifier] | No |  |
**value** | str | Yes |  |
**type** | Literal["regex"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
