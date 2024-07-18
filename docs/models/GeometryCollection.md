# GeometryCollection

GeoJSon geometry collection

GeometryCollections composed of a single part or a number of parts of a
single type SHOULD be avoided when that single part or a single object
of multipart type (MultiPoint, MultiLineString, or MultiPolygon) could
be used instead.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**bbox** | Optional[BBox] | No |  |
**geometries** | List[Geometry] | Yes |  |
**type** | Literal["GeometryCollection"] | Yes | None |


[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
