# Geometry

Abstract type for all GeoJSon object except Feature and FeatureCollection

This is a discriminator class and does not contain any additional fields. Instead, it
is a union of of the classes listed below.

This discriminator class uses the `type` field to differentiate between classes.

Class | Value
------------ | -------------
[GeometryCollection](GeometryCollection.md) | GeometryCollection
[LineString](LineString.md) | LineString
[MultiLineString](MultiLineString.md) | MultiLineString
[MultiPoint](MultiPoint.md) | MultiPoint
[MultiPolygon](MultiPolygon.md) | MultiPolygon
[GeoPoint](GeoPoint.md) | Point
[Polygon](Polygon.md) | Polygon

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
