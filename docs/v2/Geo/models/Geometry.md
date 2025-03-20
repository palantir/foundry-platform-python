# Geometry

Abstract type for all GeoJSon object except Feature and FeatureCollection

This is a discriminator type and does not contain any fields. Instead, it is a union
of of the models listed below.

This discriminator class uses the `type` field to differentiate between classes.

| Class | Value
| ------------ | -------------
MultiPoint | MultiPoint
GeometryCollection | GeometryCollection
MultiLineString | MultiLineString
LineString | LineString
MultiPolygon | MultiPolygon
GeoPoint | Point
Polygon | Polygon


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
