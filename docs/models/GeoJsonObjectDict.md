# GeoJsonObjectDict

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
[FeatureDict](FeatureDict.md) | Feature
[FeatureCollectionDict](FeatureCollectionDict.md) | FeatureCollection
[GeoPointDict](GeoPointDict.md) | Point
[MultiPointDict](MultiPointDict.md) | MultiPoint
[LineStringDict](LineStringDict.md) | LineString
[MultiLineStringDict](MultiLineStringDict.md) | MultiLineString
[PolygonDict](PolygonDict.md) | Polygon
[MultiPolygonDict](MultiPolygonDict.md) | MultiPolygon
[GeometryCollectionDict](GeometryCollectionDict.md) | GeometryCollection


[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)