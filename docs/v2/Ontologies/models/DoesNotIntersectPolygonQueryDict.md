# DoesNotIntersectPolygonQueryDict

Returns objects where the specified field does not intersect the polygon provided. Allows you to specify a 
property to query on by a variety of means. Either `field` or `propertyIdentifier` must be supplied, but not 
both.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**field** | NotRequired[PropertyApiName] | No |  |
**propertyIdentifier** | NotRequired[PropertyIdentifierDict] | No |  |
**value** | PolygonDict | Yes |  |
**type** | Literal["doesNotIntersectPolygon"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
