# Feature

GeoJSon 'Feature' object

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**geometry** | Optional[Geometry] | No |  |
**properties** | Dict[FeaturePropertyKey, Any] | Yes | A `Feature` object has a member with the name "properties".  The value of the properties member is an object (any JSON object or a JSON null value).  |
**id** | Optional[Any] | No | If a `Feature` has a commonly used identifier, that identifier SHOULD be included as a member of the Feature object with the name "id", and the value of this member is either a JSON string or number.  |
**bbox** | Optional[BBox] | No |  |
**type** | Literal["Feature"] | Yes | None |


[[Back to Model list]](../../../README.md#models-v2-link) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
