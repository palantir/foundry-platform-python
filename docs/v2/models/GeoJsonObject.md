# GeoJsonObject

GeoJSon object

The coordinate reference system for all GeoJSON coordinates is a
geographic coordinate reference system, using the World Geodetic System
1984 (WGS 84) datum, with longitude and latitude units of decimal
degrees.
This is equivalent to the coordinate reference system identified by the
Open Geospatial Consortium (OGC) URN
An OPTIONAL third-position element SHALL be the height in meters above
or below the WGS 84 reference ellipsoid.
In the absence of elevation values, applications sensitive to height or
depth SHOULD interpret positions as being at local ground or sea level.


This is a discriminator type and does not contain any fields. Instead, it is a union
of of the models listed below.

This discriminator class uses the `type` field to differentiate between classes.

| Class | Value
| ------------ | -------------
[Feature](Feature.md) | Feature
[FeatureCollection](FeatureCollection.md) | FeatureCollection
[GeoPoint](GeoPoint.md) | Point
[MultiPoint](MultiPoint.md) | MultiPoint
[LineString](LineString.md) | LineString
[MultiLineString](MultiLineString.md) | MultiLineString
[Polygon](Polygon.md) | Polygon
[MultiPolygon](MultiPolygon.md) | MultiPolygon
[GeometryCollection](GeometryCollection.md) | GeometryCollection


[[Back to Model list]](../../../README.md#models-v2-link) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
