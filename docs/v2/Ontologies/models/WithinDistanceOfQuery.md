# WithinDistanceOfQuery

Returns objects where the specified field contains a point within the distance provided of the center point.
Allows you to specify a property to query on by a variety of means. Either `field` or `propertyIdentifier` 
must be supplied, but not both.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**field** | typing.Optional[PropertyApiName] | No |  |
**property_identifier** | typing.Optional[PropertyIdentifier] | No |  |
**value** | CenterPoint | Yes |  |
**type** | typing.Literal["withinDistanceOf"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
