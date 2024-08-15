# GeometryCollectionDict

GeoJSon geometry collection

GeometryCollections composed of a single part or a number of parts of a
single type SHOULD be avoided when that single part or a single object
of multipart type (MultiPoint, MultiLineString, or MultiPolygon) could
be used instead.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**geometries** | List[GeometryDict] | Yes |  |
**bbox** | NotRequired[BBox] | No |  |
**type** | Literal["GeometryCollection"] | Yes | None |


[[Back to Model list]](../../../README.md#models-v1-link) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
