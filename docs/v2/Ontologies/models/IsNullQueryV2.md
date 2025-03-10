# IsNullQueryV2

Returns objects based on the existence of the specified field. Allows you to specify a property to query on
by a variety of means. Either `field` or `propertyIdentifier` must be supplied, but not both.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**field** | typing.Optional[PropertyApiName] | No |  |
**property_identifier** | typing.Optional[PropertyIdentifier] | No |  |
**value** | bool | Yes |  |
**type** | typing.Literal["isNull"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
