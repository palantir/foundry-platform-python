# GeoShapeV2Query

Returns objects where the specified field satisfies the provided geometry query with the given spatial operator.
Supports both envelope (bounding box) and GeoJSON geometries for filtering geopoint or geoshape properties.
Either `field` or `propertyIdentifier` can be supplied, but not both.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**field** | Optional[PropertyApiName] | No |  |
**property_identifier** | Optional[PropertyIdentifier] | No |  |
**geometry** | GeoShapeV2Geometry | Yes |  |
**spatial_filter_mode** | SpatialFilterMode | Yes |  |
**type** | Literal["geoShapeV2"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
