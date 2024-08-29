# GeometryDict

Abstract type for all GeoJSon object except Feature and FeatureCollection

This is a discriminator type and does not contain any fields. Instead, it is a union
of of the models listed below.

This discriminator class uses the `type` field to differentiate between classes.

| Class | Value
| ------------ | -------------
[GeoPointDict](GeoPointDict.md) | Point
[MultiPointDict](MultiPointDict.md) | MultiPoint
[LineStringDict](LineStringDict.md) | LineString
[MultiLineStringDict](MultiLineStringDict.md) | MultiLineString
[PolygonDict](PolygonDict.md) | Polygon
[MultiPolygonDict](MultiPolygonDict.md) | MultiPolygon
[GeometryCollectionDict](GeometryCollectionDict.md) | GeometryCollection


[[Back to Model list]](../../../README.md#models-v1-link) [[Back to API list]](../../../README.md#apis-v1-link) [[Back to README]](../../../README.md)