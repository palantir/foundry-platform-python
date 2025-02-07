# ContainsQueryV2Dict

Returns objects where the specified array contains a value. Allows you to specify a property to query on by a 
variety of means. Either `field` or `propertyIdentifier` must be supplied, but not both.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**field** | NotRequired[PropertyApiName] | No |  |
**propertyIdentifier** | NotRequired[PropertyIdentifierDict] | No |  |
**value** | PropertyValue | Yes |  |
**type** | Literal["contains"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
